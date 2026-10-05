import copy
import csv
from pathlib import Path

from .common import completion, messages, read_jsonl, sha256, write_json, write_jsonl
from .verify import close, execute, parse_prediction, score


def perturb_target(row):
    """Same-schema arithmetic negatives for pipeline bring-up; NOT human preferences."""
    target = row["target"]
    for index, step in enumerate(target["steps"]):
        for op in ["add", "subtract", "multiply", "divide"]:
            if step["op"] == op:
                continue
            wrong = copy.deepcopy(target)
            wrong["steps"][index]["op"] = op
            try:
                value, _ = execute(wrong["steps"], row["evidence"])
            except ValueError:
                continue
            if not close(value, target["answer"]):
                wrong["answer"] = value
                return wrong
    return None


def build_candidates(data_path, out, predictions_path=None, limit=200):
    rows = read_jsonl(data_path)
    if any(r["split"] != "train" for r in rows):
        raise ValueError("Preferences may only be constructed from training data")
    digest = sha256(data_path)
    sampled = {}
    if predictions_path:
        for pred in read_jsonl(predictions_path):
            if pred.get("dataset_sha256") != digest:
                raise ValueError("Sample provenance mismatch")
            sampled.setdefault(pred["id"], []).append(pred["output"])
        if set(sampled) - {r["id"] for r in rows}:
            raise ValueError("Samples contain IDs outside train")
    pairs = []
    for row in rows:
        if not score(row, row["target"])["verified_correct"]:
            raise ValueError("Chosen target failed verification")
        rejected = None
        if predictions_path:
            for raw in sampled.get(row["id"], []):
                s = score(row, raw)
                # Prefer actual arithmetic mistakes over mere invalid JSON/format differences.
                if s["execution_valid"] and not s["abstained"] and not s["answer_correct"]:
                    rejected = parse_prediction(raw)
                    break
            source = "model_sample_verifier_labeled"
        else:
            rejected, source = perturb_target(row), "synthetic_operator_mutation"
        if rejected is None:
            continue
        pairs.append({"id": row["id"], "split": "train", "source": source,
                      "dataset_sha256": digest, "review_status": "pending", "prompt": messages(row),
                      "chosen": [{"role": "assistant", "content": completion(row["target"])}],
                      "rejected": [{"role": "assistant", "content": completion(rejected)}]})
        if limit and len(pairs) >= limit:
            break
    out = Path(out)
    if out.exists() and any(out.iterdir()):
        raise ValueError("Use a new preferences directory to preserve human review")
    write_jsonl(out / "candidates.jsonl", pairs)
    with (out / "review.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "source", "decision", "notes"])
        writer.writeheader()
        writer.writerows({"id": p["id"], "source": p["source"], "decision": "pending", "notes": ""} for p in pairs)
    # Portable, searchable Markdown for reviewing without exposing anything to external services.
    lines = ["# Preference review", "", "Review evidence, chosen and rejected. Fill review.csv decision=approve/reject.\n"]
    for p in pairs:
        lines += [f"## {p['id']}", "", p["prompt"][-1]["content"], "", "Chosen:", "```json", p["chosen"][0]["content"], "```", "Rejected:", "```json", p["rejected"][0]["content"], "```", ""]
    (out / "review.md").write_text("\n".join(lines), encoding="utf-8")
    report = {"count": len(pairs), "human_reviewed": 0, "source": "model samples" if predictions_path else "synthetic mutations", "training_export_requires_review": True}
    write_json(out / "manifest.json", report)
    return report


def export_reviewed(candidates_path, review_path, out):
    candidates = read_jsonl(candidates_path)
    ids = {p["id"] for p in candidates}
    decisions = {}
    with open(review_path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if row["id"] in decisions or row["id"] not in ids:
                raise ValueError("Duplicate/unknown review ID")
            value = row["decision"].strip().lower()
            if value not in {"pending", "approve", "reject"}:
                raise ValueError("Decision must be pending, approve or reject")
            decisions[row["id"]] = value
    approved = [dict(p, review_status="approved") for p in candidates if decisions.get(p["id"]) == "approve"]
    if not approved:
        raise ValueError("No approved pairs. Review review.md and set decisions in review.csv first.")
    write_jsonl(out, approved)
    return {"approved": len(approved), "total_candidates": len(candidates), "review_sha256": sha256(review_path)}
