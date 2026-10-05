import collections
import hashlib
import json
import random
import re
import urllib.request
from pathlib import Path

from .common import completion, messages, read_jsonl, sha256, write_json, write_jsonl
from .verify import CONSTANTS, close, evidence_numbers, execute, number

FINQA_REVISION = "0f16e2867befa6840783e58be38c9efb9229d742"
# Both share classes belong to the same issuer. Extend with audited aliases if data grows.
ISSUER_ALIASES = {"UA": "UAA"}
FINQA_HASHES = {
    "train": "49f237eb9779b569473b26b08048867d04635a7cc39ad6a7a5664c55bb428db6",
    "dev": "a847fb7e0d61a3125a1e2909852df6b89f1ee64d2c5ff1bf689e332214deee51",
    "test": "831dbfb2e785dbc227f895ce3f24046433467aec67b09db2bd6ac7692a8a30dc",
}


def download(out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    manifest = {"repository": "https://github.com/czyssrs/FinQA", "revision": FINQA_REVISION, "files": {}}
    for split, digest in FINQA_HASHES.items():
        path = out / f"{split}.json"
        url = f"https://raw.githubusercontent.com/czyssrs/FinQA/{FINQA_REVISION}/dataset/{split}.json"
        if not path.exists():
            req = urllib.request.Request(url, headers={"User-Agent": "FinDelta-research/0.1"})
            raw = urllib.request.urlopen(req, timeout=90).read()
            if hashlib.sha256(raw).hexdigest() != digest:
                raise ValueError(f"Source hash mismatch: {split}")
            path.write_bytes(raw)
        if sha256(path) != digest:
            raise ValueError(f"Existing file hash mismatch: {path}")
        manifest["files"][split] = {"url": url, "sha256": digest}
    license_url = f"https://raw.githubusercontent.com/czyssrs/FinQA/{FINQA_REVISION}/LICENSE"
    license_path = out / "LICENSE.FinQA"
    if not license_path.exists():
        license_path.write_bytes(urllib.request.urlopen(license_url, timeout=30).read())
    write_json(out / "source_manifest.json", manifest)
    return manifest


def context(record):
    # Only original fields. NEVER use qa.model_input, gold_inds, or retrieval results here.
    evidence = {f"text_{i}": text for i, text in enumerate(record["pre_text"] + record["post_text"])}
    table = record["table"]
    if table:
        evidence["table_0"] = " | ".join(table[0])
        for i, row in enumerate(table[1:], 1):
            evidence[f"table_{i}"] = " | ".join(
                f"{table[0][j] if j < len(table[0]) else 'column ' + str(j)}: {cell}"
                for j, cell in enumerate(row))
    return evidence


def convert(record, original_split):
    qa = record["qa"]
    evidence = context(record)
    raw_program = qa["program"].strip()
    parsed = re.findall(r"([a-z_]+)\(([^(),]+),\s*([^(),]+)\)", raw_program)
    remainder = re.sub(r"[a-z_]+\([^(),]+,\s*[^(),]+\)", "", raw_program)
    if not parsed or remainder.replace(",", "").strip():
        raise ValueError("program_parse")
    gold_ids = list(qa.get("gold_inds", {}))
    priority = [key for key in gold_ids if key in evidence] + [key for key in evidence if key not in gold_ids]
    nums = {key: evidence_numbers(text) for key, text in evidence.items()}
    steps = []
    for op, left, right in parsed:
        if op not in {"add", "subtract", "multiply", "divide"}:
            raise ValueError("unsupported_operation:" + op)
        args = []
        for raw in [left.strip(), right.strip()]:
            if raw in CONSTANTS or re.fullmatch(r"#\d+", raw):
                args.append(raw)
            else:
                val = number(raw)
                key = next((key for key in priority if val in nums[key]), None)
                if key is None:
                    raise ValueError("operand_not_found")
                args.append({"source": key, "value": raw})
        steps.append({"op": op, "args": args})
    result, used = execute(steps, evidence)
    if not close(result, qa["exe_ans"]):
        raise ValueError("program_execution_mismatch")
    human = str(qa.get("answer", "")).strip().replace(",", "")
    # Conservative check for directly numeric prose labels. Rounded integers allowed.
    # Percentage prose may use 0.12 or 12%; exe_ans convention is preserved.
    human_check = "not_parseable"
    if re.fullmatch(r"[-+]?\d+(?:\.\d+)?%?", human):
        h = float(number(human))
        candidates = [h, h * 100] if human.endswith("%") else [h]
        decimals = len(human.rstrip("%").split(".")[1]) if "." in human else 0
        tol = 0.5 * 10 ** (-decimals) + 1e-4
        if not any(abs(result - candidate) <= max(tol, abs(candidate) * 1e-5) for candidate in candidates):
            raise ValueError("human_program_answer_disagreement")
        human_check = "compatible_with_rounding_or_percent_convention"
    uid = record["id"]
    parts = uid.split("/")
    return {
        "id": uid, "company": ISSUER_ALIASES.get(parts[0], parts[0]),
        "source_ticker": parts[0], "report_id": "/".join([ISSUER_ALIASES.get(parts[0], parts[0]), *parts[1:2]]),
        "original_split": original_split, "dataset": "FinQA-arithmetic-filtered",
        "source_revision": FINQA_REVISION, "question": qa["question"], "evidence": evidence,
        "answerable": True, "target": {"abstain": False, "steps": steps, "answer": result},
        "gold_evidence_ids": [key for key in gold_ids if key in evidence],
        "audit": {"human_answer_check": human_check, "human_answer": qa.get("answer"),
                  "original_program": raw_program, "original_execution_answer": qa["exe_ans"],
                  "binding_outside_gold_ids": sorted(used - set(gold_ids))},
    }


def prepare(raw_dir, out, seed=42, limit_train=0):
    out = Path(out)
    if (out / "manifest.json").exists():
        raise ValueError("Output already exists. Use a new directory to preserve the frozen split.")
    rows, rejected, seen, hashes = [], [], set(), {}
    for split in ["train", "dev", "test"]:
        path = Path(raw_dir) / f"{split}.json"
        hashes[split] = sha256(path)
        if hashes[split] != FINQA_HASHES[split]:
            raise ValueError(f"Unexpected FinQA source: {path}")
        for record in json.loads(path.read_text(encoding="utf-8")):
            try:
                row = convert(record, split)
                # Deduplicate context + question, including copies across companies/splits.
                key = hashlib.sha256(json.dumps([row["question"], list(row["evidence"].values())], sort_keys=True).encode()).hexdigest()
                if key in seen:
                    raise ValueError("duplicate_context_question")
                seen.add(key)
                rows.append(row)
            except (ValueError, KeyError, TypeError, ArithmeticError) as e:
                rejected.append({"id": record.get("id"), "original_split": split, "reason": str(e)})
    companies = sorted({row["company"] for row in rows})
    random.Random(seed).shuffle(companies)
    n = len(companies)
    if n < 6:
        raise ValueError("Not enough companies for a meaningful split")
    dev_start, test_start = int(n * .7), int(n * .85)
    mapping = {c: "train" if i < dev_start else "dev" if i < test_start else "test" for i, c in enumerate(companies)}
    splits = {s: [] for s in ["train", "dev", "test"]}
    for row in rows:
        row["split"] = mapping[row["company"]]
        splits[row["split"]].append(row)
    for split, items in splits.items():
        random.Random(seed).shuffle(items)
        if split == "train" and limit_train:
            splits[split] = items = items[:limit_train]
        write_jsonl(out / f"{split}.jsonl", items)
    write_jsonl(out / "quarantine.jsonl", rejected)
    manifest = {
        "protocol": "CUSTOM company-disjoint split of pooled public FinQA; NOT official leaderboard",
        "seed": seed, "source_revision": FINQA_REVISION, "raw_sha256": hashes,
        "issuer_aliases": ISSUER_ALIASES,
        "scope": "add/subtract/multiply/divide, full page text+table, numeric evidence occurrence binding",
        "counts": {s: len(v) for s, v in splits.items()},
        "companies": {s: sorted({r['company'] for r in v}) for s, v in splits.items()},
        "sha256": {s: sha256(out / f"{s}.jsonl") for s in splits},
        "quarantine_count": len(rejected), "quarantine_reasons": dict(collections.Counter(r["reason"] for r in rejected)),
        "limitations": ["No proof of pretraining decontamination", "No semantic entailment or unit verification",
                        "Numeric bindings automatically resolved, ambiguous repeated numbers require review",
                        "Full-page context, not full-report retrieval or cross-filing reasoning"],
    }
    write_json(out / "manifest.json", manifest)
    return manifest


def freeze_cohort(input_dir, out, model, revision, max_prompt=1408, max_length=2048, train_limit=1000, eval_limit=200):
    from transformers import AutoTokenizer
    if not revision:
        raise ValueError("Pass an immutable model commit revision")
    out = Path(out)
    if out.exists() and any(out.iterdir()):
        raise ValueError("Cohort directory must be new/empty; never change a test cohort in place")
    tokenizer = AutoTokenizer.from_pretrained(model, revision=revision)
    manifest = dict(model=model, revision=revision, max_prompt=max_prompt, max_length=max_length, splits={})
    for split in ["train", "dev", "test"]:
        rows, skipped = [], collections.Counter()
        source = Path(input_dir) / f"{split}.jsonl"
        limit = train_limit if split == "train" else eval_limit
        for row in read_jsonl(source):
            prefix = tokenizer.apply_chat_template(messages(row), tokenize=False, add_generation_prompt=True, enable_thinking=False)
            full = tokenizer.apply_chat_template(messages(row) + [{"role": "assistant", "content": completion(row["target"])}], tokenize=False, enable_thinking=False)
            if not full.startswith(prefix):
                raise ValueError("Chat-template prefix mismatch")
            p = len(tokenizer(prefix, add_special_tokens=False)["input_ids"])
            t = len(tokenizer(full, add_special_tokens=False)["input_ids"])
            if p > max_prompt or t > max_length or t - p > max_length - max_prompt:
                skipped["too_long"] += 1
                continue
            if limit and len(rows) >= limit:
                skipped["beyond_fixed_sample_limit"] += 1
                continue
            row["token_counts"] = {"prompt": p, "total": t}
            rows.append(row)
        if not rows:
            raise ValueError(f"Empty cohort: {split}")
        write_jsonl(out / f"{split}.jsonl", rows)
        manifest["splits"][split] = dict(count=len(rows), excluded=dict(skipped), source_sha256=sha256(source), sha256=sha256(out / f"{split}.jsonl"))
    write_json(out / "manifest.json", manifest)
    return manifest


def export_sft(input_path, out):
    rows = read_jsonl(input_path)
    if any(r["split"] != "train" for r in rows):
        raise ValueError("Only training split may be exported for SFT")
    write_jsonl(out, [{"id": r["id"], "split": "train", "prompt": messages(r),
                      "completion": [{"role": "assistant", "content": completion(r["target"])}]} for r in rows])
    return {"count": len(rows), "source_sha256": sha256(input_path)}
