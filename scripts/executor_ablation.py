"""Post-hoc dev-only execution ablation. Never consults target answers to transform outputs."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def main():
    from findelta.common import read_jsonl, sha256, write_json, write_jsonl
    from findelta.evaluate import evaluate
    from findelta.verify import execute, parse_prediction

    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--predictions", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    out = Path(args.out)
    if out.exists():
        raise ValueError("Refusing to overwrite derived predictions")
    rows = read_jsonl(args.data)
    if any(r["split"] != "dev" for r in rows):
        raise ValueError("This diagnostic is restricted to dev")
    # Only input evidence is exposed to the transformation; no reference answer/program.
    inputs = {r["id"]: r["evidence"] for r in rows}
    preds = read_jsonl(args.predictions)
    if len(preds) != len(inputs) or {p["id"] for p in preds} != set(inputs):
        raise ValueError("Require exactly one prediction per example")
    data_hash, changed, abstained, derived = sha256(args.data), 0, 0, []
    for pred in preds:
        if pred["dataset_sha256"] != data_hash:
            raise ValueError("Dataset provenance mismatch")
        try:
            answer = parse_prediction(pred["output"])
            if not answer["abstain"]:
                value, _ = execute(answer["steps"], inputs[pred["id"]])
                changed += answer["answer"] != value
                answer = {**answer, "answer": value}
        except (ValueError, TypeError, KeyError, ArithmeticError, RecursionError):
            answer = {"abstain": True, "steps": [], "answer": None}
        abstained += answer["abstain"]
        derived.append({**pred, "output": json.dumps(answer, separators=(",", ":")),
                        "postprocessing": "verified_program_execution_or_abstain",
                        "parent_predictions_sha256": sha256(args.predictions)})
    write_jsonl(out, derived)
    write_json(str(out) + ".manifest.json", {
        "experiment": "post-hoc dev inference ablation; NOT an additional training run",
        "rule": "Execute predicted program using input evidence; use its numeric result. Abstain if invalid.",
        "gold_labels_used_for_transformation": False,
        "data_sha256": data_hash, "parent_predictions_sha256": sha256(args.predictions),
        "derived_predictions_sha256": sha256(out), "answers_replaced": changed,
        "abstentions": abstained, "new_generation_tokens": 0,
        "caveat": "Executable, source-bound programs can still select the wrong period, metric or operation."
    })
    result = evaluate(args.data, out, out.parent / "sft-executor-dev")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
