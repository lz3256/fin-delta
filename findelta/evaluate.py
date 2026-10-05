import collections
import random

from .common import read_jsonl, sha256, write_json, write_jsonl
from .verify import score


def clustered_interval(rows, key="verified_correct", repetitions=1000, seed=42):
    groups = collections.defaultdict(list)
    for row in rows:
        groups[row["report_id"]].append(float(row[key]))
    keys = sorted(groups)
    if not keys:
        return None
    rng = random.Random(seed)
    estimates = []
    for _ in range(repetitions):
        vals = [v for k in rng.choices(keys, k=len(keys)) for v in groups[k]]
        estimates.append(sum(vals) / len(vals))
    estimates.sort()
    return [estimates[int(repetitions * .025)], estimates[min(repetitions - 1, int(repetitions * .975))]]


def evaluate(data_path, predictions_path, out):
    from pathlib import Path
    rows, preds = read_jsonl(data_path), read_jsonl(predictions_path)
    by_id = {}
    for pred in preds:
        if pred["id"] in by_id:
            raise ValueError("Duplicate prediction ID; evaluate only one sample per question")
        by_id[pred["id"]] = pred
    ids = [r["id"] for r in rows]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate data IDs")
    if set(by_id) - set(ids):
        raise ValueError("Predictions contain IDs outside the evaluation cohort")
    digest = sha256(data_path)
    if any(p.get("dataset_sha256") != digest for p in preds):
        raise ValueError("Prediction dataset hash mismatch or absent provenance")
    prompt_hashes = {p.get("prompt_sha256") for p in preds}
    if len(prompt_hashes) > 1:
        raise ValueError("Mixed prediction prompt versions")
    results = []
    for row in rows:
        pred = by_id.get(row["id"])
        s = score(row, pred["output"] if pred else "")
        s.update(id=row["id"], report_id=row["report_id"], answerable=row["answerable"], missing=pred is None)
        results.append(s)
    n = len(rows)
    if not n:
        raise ValueError("Empty evaluation data")
    answered = [r for r in results if r["schema_valid"] and not r["abstained"]]
    answerable = [r for r in results if r["answerable"]]
    refused = [r for r in results if r["abstained"]]
    unanswerable = [r for r in results if not r["answerable"]]
    report = {
        "label": "FinDelta custom filtered-cohort metrics; NOT official FinQA leaderboard scores",
        "dataset_sha256": digest, "predictions_sha256": sha256(predictions_path), "n": n,
        "prompt_sha256": next(iter(prompt_hashes), None),
        "missing_predictions": sum(r["missing"] for r in results),
        "schema_valid_rate": sum(r["schema_valid"] for r in results) / n,
        "numeric_answer_accuracy_on_answerable": sum(r["answer_correct"] for r in answerable) / len(answerable) if answerable else None,
        "verified_accuracy": sum(r["verified_correct"] for r in results) / n,
        "verified_accuracy_report_cluster_bootstrap_95ci": clustered_interval(results),
        "answer_coverage": len(answered) / n,
        "error_rate_among_answered": sum(not r["verified_correct"] for r in answered) / len(answered) if answered else None,
        "abstention_precision": sum(not r["answerable"] for r in refused) / len(refused) if refused else None,
        "abstention_recall": sum(r["abstained"] for r in unanswerable) / len(unanswerable) if unanswerable else None,
        "false_abstention_rate": sum(r["abstained"] for r in answerable) / len(answerable) if answerable else None,
        "evidence_id_overlap_is_not_entailment": True,
        "errors": dict(collections.Counter(r["error"] for r in results if r["error"])),
    }
    for key in ["evidence_id_precision", "evidence_id_recall"]:
        vals = [r[key] for r in results if r[key] is not None]
        report["mean_" + key] = sum(vals) / len(vals) if vals else None
    write_json(Path(out) / "metrics.json", report)
    write_jsonl(Path(out) / "per_example.jsonl", results)
    return report
