import collections
import json
import random
from pathlib import Path

from .common import read_jsonl


def compare(runs, out):
    """Paired report-cluster bootstrap on the same frozen cohort."""
    loaded = []
    for specification in runs:
        name, path = specification.split("=", 1)
        metrics = json.loads((Path(path) / "metrics.json").read_text())
        rows = read_jsonl(Path(path) / "per_example.jsonl")
        loaded.append((name, metrics, {r["id"]: r for r in rows}))
    if not loaded:
        raise ValueError("At least one run is required")
    _, baseline, base_rows = loaded[0]
    lines = ["# FinDelta experiment comparison", "", "Custom filtered FinQA cohort; not official leaderboard results.",
             "", f"Dataset SHA256: `{baseline['dataset_sha256']}`", "",
             "| Run | N | Schema valid | Numeric accuracy | Verified accuracy | Coverage | Paired improvement vs first run (95% CI) |",
             "|---|---:|---:|---:|---:|---:|---|"
             ]
    for name, metrics, rows in loaded:
        if metrics["dataset_sha256"] != baseline["dataset_sha256"] or set(rows) != set(base_rows):
            raise ValueError("Cannot compare different evaluation cohorts")
        if not metrics.get("prompt_sha256") or metrics["prompt_sha256"] != baseline.get("prompt_sha256"):
            raise ValueError("Comparison requires the same recorded prompt version. Do not attribute a prompt change to training.")
        groups = collections.defaultdict(list)
        for uid, row in rows.items():
            groups[row["report_id"]].append(float(row["verified_correct"]) - float(base_rows[uid]["verified_correct"]))
        keys, rng, samples = sorted(groups), random.Random(42), []
        for _ in range(1000):
            values = [v for k in rng.choices(keys, k=len(keys)) for v in groups[k]]
            samples.append(sum(values) / len(values))
        samples.sort()
        delta = metrics["verified_accuracy"] - baseline["verified_accuracy"]
        fmt = lambda v: "N/A" if v is None else f"{v:.1%}"
        lines.append(f"| {name} | {metrics['n']} | {fmt(metrics['schema_valid_rate'])} | {fmt(metrics['numeric_answer_accuracy_on_answerable'])} | {fmt(metrics['verified_accuracy'])} | {fmt(metrics['answer_coverage'])} | {delta * 100:+.1f} pp [{samples[25] * 100:+.1f}, {samples[975] * 100:+.1f}] |")
    lines += ["", "Intervals describe test-sample uncertainty, not training-seed uncertainty. One seed is exploratory.",
              "Verified accuracy checks executable arithmetic and numeric occurrence in cited evidence; it does not prove semantic entailment, correct period selection, or general factuality.",
              "Never mix synthetic stress fixtures into the real-data score."]
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"report": str(out), "runs": len(loaded)}
