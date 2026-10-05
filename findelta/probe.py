"""Small dev-only prompt diagnostic. Never labels a prompt change as training gain."""
import json
from pathlib import Path

from .common import SYSTEM, prompt_sha256, read_jsonl, sha256, write_json, write_jsonl
from .evaluate import evaluate
from .predict import predict
from .verify import score


def probe(out, previous_predictions=None):
    out = Path(out)
    if out.exists() and any(out.iterdir()):
        raise ValueError("Probe output exists; choose a new directory to preserve the experiment")
    source = Path("data/cohort/v1/dev.jsonl")
    rows = read_jsonl(source)[:20]
    if any(row["split"] != "dev" for row in rows):
        raise ValueError("Prompt development must use dev only")
    data = out / "dev-probe20.jsonl"
    write_jsonl(data, rows)
    write_json(out / "protocol.json", {
        "purpose": "dev prompt diagnostic; NOT training improvement or final test",
        "selection": "first 20 rows of the pre-existing shuffled dev cohort, no error-based selection",
        "source_sha256": sha256(source), "prompt_sha256": prompt_sha256(), "system_prompt": SYSTEM,
        "labels_and_scoring_unchanged": True,
        "known_limitation": "Source percentage scales are not universally consistent; separate label audit still needed",
    })
    previous = None
    if previous_predictions:
        preds = read_jsonl(previous_predictions)
        if any(p["dataset_sha256"] != sha256(source) for p in preds):
            raise ValueError("Previous predictions refer to a different full dev cohort")
        mapping = {p["id"]: p for p in preds}
        scored = [score(r, mapping[r["id"]]["output"]) for r in rows]
        previous = {"n": len(rows), "numeric_correct": sum(s["answer_correct"] for s in scored),
                    "verified_correct": sum(s["verified_correct"] for s in scored),
                    "schema_valid": sum(s["schema_valid"] for s in scored),
                    "predictions_sha256": sha256(previous_predictions)}
    output = out / "predictions.jsonl"
    predict(data, "configs/4070-sft.json", output, "model-lock.json")
    current = evaluate(data, output, out / "evaluation")
    summary = {"experiment": "prompt-v2 dev diagnostic, not post-training",
               "previous_prompt_same_20_questions": previous, "current_prompt": current}
    write_json(out / "summary.json", summary)
    return summary
