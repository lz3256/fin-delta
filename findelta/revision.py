"""Apply explicit, source-audited train-only corrections without changing evaluation."""
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path

from .common import messages, read_jsonl, sha256, write_json, write_jsonl
from .data import context, export_sft
from .verify import NUMBER, close, execute, number, parse_prediction, score


def record_hash(row):
    return hashlib.sha256(json.dumps(row, sort_keys=True, ensure_ascii=False,
                                     separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def signed_cell_number(raw):
    """Narrow parser for audited numeric cells, including FinQA's -121 (121)."""
    tokens = [number(m.group()) for m in NUMBER.finditer(raw)]
    if not tokens or any(abs(x) != abs(tokens[0]) for x in tokens):
        raise ValueError("Cell is not one unambiguous numeric value")
    value = tokens[0]
    if raw.strip().startswith("(") and raw.strip().endswith(")") and value > 0:
        value = -value
    return value


def validate_cell_bindings(target, source, bindings):
    """Validate manually annotated cells, not infer financial semantics from text."""
    expected = {(i, j) for i, step in enumerate(target["steps"])
                for j, arg in enumerate(step["args"]) if isinstance(arg, dict)}
    seen = set()
    for binding in bindings:
        location = (binding["step"], binding["arg"])
        if location in seen or location not in expected:
            raise ValueError("Duplicate or extraneous cell annotation")
        seen.add(location)
        arg = target["steps"][location[0]]["args"][location[1]]
        row, col = binding["row"], binding["column"]
        if type(row) is not int or type(col) is not int or row < 0 or col < 0:
            raise ValueError("Invalid cell coordinates")
        if arg["source"] != f"table_{row}":
            raise ValueError("Operand source does not match original row")
        cell = source["table"][row][col]
        if cell != binding["original_cell"]:
            raise ValueError("Original source cell changed")
        value = signed_cell_number(cell)
        if binding["semantics"] == "magnitude":
            value = abs(value)
        elif binding["semantics"] != "signed":
            raise ValueError("Unknown sign semantics")
        if number(arg["value"]) != value:
            raise ValueError("Operand disagrees with signed original cell")
        if not binding.get("metric") or not binding.get("period") or not binding.get("unit"):
            raise ValueError("Explicit metric, period and unit annotation required")
    if seen != expected:
        raise ValueError("Every evidence operand requires a cell annotation")


def build_revision(parent, plan_dir, out):
    parent, plan_dir, out = map(Path, (parent, plan_dir, out))
    if out.exists():
        raise ValueError("Revision directory already exists; refusing overwrite")
    plan = json.loads((plan_dir / "plan.json").read_text())
    hashes = {s: sha256(parent / f"{s}.jsonl") for s in ["train", "dev", "test"]}
    if hashes != plan["parent_sha256"]:
        raise ValueError("Frozen parent cohort hash mismatch")
    for name, digest in plan["review_files_sha256"].items():
        if sha256(plan_dir / name) != digest:
            raise ValueError("Review file hash mismatch")
    rows = read_jsonl(parent / "train.jsonl")
    if not rows or any(r["split"] != "train" for r in rows):
        raise ValueError("Only training rows may be revised")
    byid = {r["id"]: r for r in rows}
    if len(byid) != len(rows):
        raise ValueError("Duplicate training IDs")
    decisions = read_jsonl(plan_dir / "decisions.jsonl")
    decisions_byid = {d["id"]: d for d in decisions}
    if len(decisions_byid) != len(decisions) or not set(decisions_byid) <= set(byid):
        raise ValueError("Duplicate or non-train review ID")
    sources = {r["id"]: r for r in read_jsonl(plan_dir / "source-records.jsonl")}
    revised, control, quarantine, changes = [], [], [], []
    for old in rows:
        d = decisions_byid.get(old["id"])
        new = copy.deepcopy(old)
        if d:
            if d["parent_record_sha256"] != record_hash(old):
                raise ValueError("Reviewed row changed")
            source = sources[old["id"]]
            if source["qa"]["question"] != old["question"] or context(source) != old["evidence"]:
                raise ValueError("Reviewed original source disagrees with parent input")
            if d.get("reviewer_type") != "ai_assistant" or not d.get("rationale"):
                raise ValueError("Missing explicit review provenance")
            action = d["action"]
            if action == "quarantine":
                quarantine.append({"original": old, "decision": d})
                continue
            if action == "repair":
                target = parse_prediction(copy.deepcopy(d["replacement_target"]))
                if target["abstain"]:
                    raise ValueError("This revision does not introduce abstention training")
                validate_cell_bindings(target, source, d["cell_bindings"])
                value, used = execute(target["steps"], old["evidence"])
                if not close(value, d["independent_answer"]) or not close(value, target["answer"]):
                    raise ValueError("Repair differs from independent calculation")
                if target == old["target"]:
                    raise ValueError("No-op repair")
                new["target"] = target
                new["gold_evidence_ids"] = sorted(used)
                new["audit"]["reviewed_revision"] = {"version": plan["version"],
                    "parent_record_sha256": record_hash(old), "reviewer_type": "ai_assistant",
                    "category": d["category"], "rationale": d["rationale"],
                    "answer_unit": d["answer_unit"]}
                # The prompt is unchanged, but the old completion token count is stale.
                new.pop("token_counts", None)
                changes.append({"id": old["id"], "before": old["target"], "after": target,
                                "category": d["category"], "rationale": d["rationale"]})
            elif action != "keep":
                raise ValueError("Unknown review action")
        if messages(new) != messages(old):
            raise ValueError("Target-only revision must preserve every input prompt")
        if not score(new, new["target"])["verified_correct"]:
            raise ValueError("Revised training target fails structural verification")
        revised.append(new)
        control.append(old)
    if not revised:
        raise ValueError("Empty revised dataset")
    if {s: sha256(parent / f"{s}.jsonl") for s in hashes} != hashes:
        raise ValueError("Parent cohort mutated during build")
    # Write only after all review and structural checks have passed.
    out.mkdir(parents=True)
    write_jsonl(out / "train.jsonl", revised)
    write_jsonl(out / "train-control.jsonl", control)
    write_jsonl(out / "quarantine.jsonl", quarantine)
    write_jsonl(out / "changes.jsonl", changes)
    for split in ["dev", "test"]:
        (out / f"{split}.jsonl").write_bytes((parent / f"{split}.jsonl").read_bytes())
    export_sft(out / "train.jsonl", out / "sft.jsonl")
    export_sft(out / "train-control.jsonl", out / "sft-control.jsonl")
    manifest = {"version": plan["version"], "parent_sha256": hashes,
        "plan_sha256": sha256(plan_dir / "plan.json"), "review_files_sha256": plan["review_files_sha256"],
        "counts": {"parent_train": len(rows), "train": len(revised), "matched_control": len(control),
                   "reviewed": len(decisions), "unreviewed_retained": len(rows)-len(decisions),
                   "repaired": len(changes), "quarantined": len(quarantine),
                   "reviewed_kept": sum(d["action"] == "keep" for d in decisions),
                   **{s: sum(bool(line.strip()) for line in (parent / f"{s}.jsonl").read_bytes().splitlines()) for s in ["dev", "test"]}},
        "sha256": {name: sha256(out / name) for name in ["train.jsonl", "train-control.jsonl", "sft.jsonl", "sft-control.jsonl", "dev.jsonl", "test.jsonl", "quarantine.jsonl", "changes.jsonl"]},
        "reviewer_type": "ai_assistant", "human_reviewed": 0,
        "quarantine_categories": dict(Counter(q["decision"]["category"] for q in quarantine)),
        "repair_categories": dict(Counter(c["category"] for c in changes)),
        "training_run_performed": False, "all_retained_prompts_identical": True,
        "holdouts_byte_identical": True,
        "scope": "Targeted corrections of previously reviewed train issues, NOT a full semantic audit; no universal unit normalization or input-table rewrite."}
    write_json(out / "manifest.json", manifest)
    return manifest
