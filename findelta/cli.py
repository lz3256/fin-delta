import argparse
import json


def main():
    p = argparse.ArgumentParser(description="FinDelta reproducible research commands")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("doctor")
    d = sub.add_parser("probe")
    d.add_argument("--out", required=True)
    d.add_argument("--previous-predictions")
    d = sub.add_parser("compare")
    d.add_argument("--run", action="append", required=True, help="NAME=path/to/evaluation_dir; first is baseline")
    d.add_argument("--out", default="runs/comparison.md")
    d = sub.add_parser("stress")
    d.add_argument("--out", default="data/stress/synthetic-v1.jsonl")
    d.add_argument("--groups", type=int, default=20)
    d = sub.add_parser("download")
    d.add_argument("--out", default="data/raw/finqa")
    d = sub.add_parser("prepare")
    d.add_argument("--raw", default="data/raw/finqa")
    d.add_argument("--out", default="data/processed/v1")
    d.add_argument("--seed", type=int, default=42)
    d = sub.add_parser("resolve-model")
    d.add_argument("--model", default="Qwen/Qwen3-0.6B")
    d.add_argument("--out", default="model-lock.json")
    d = sub.add_parser("freeze")
    d.add_argument("--input", default="data/processed/v1")
    d.add_argument("--out", default="data/cohort/v1")
    d.add_argument("--model-lock", default="model-lock.json")
    d.add_argument("--train-limit", type=int, default=1000)
    d.add_argument("--eval-limit", type=int, default=200)
    d.add_argument("--max-prompt", type=int, default=1408)
    d.add_argument("--max-length", type=int, default=2048)
    d = sub.add_parser("export-sft")
    d.add_argument("--data", default="data/cohort/v1/train.jsonl")
    d.add_argument("--out", default="data/cohort/v1/sft.jsonl")
    d = sub.add_parser("preferences")
    d.add_argument("--data", default="data/cohort/v1/train.jsonl")
    d.add_argument("--predictions")
    d.add_argument("--out", default="data/preferences/v1")
    d.add_argument("--limit", type=int, default=100)
    d = sub.add_parser("export-dpo")
    d.add_argument("--candidates", default="data/preferences/v1/candidates.jsonl")
    d.add_argument("--review", default="data/preferences/v1/review.csv")
    d.add_argument("--out", default="data/preferences/v1/approved.jsonl")
    d = sub.add_parser("evaluate")
    d.add_argument("--data", required=True)
    d.add_argument("--predictions", required=True)
    d.add_argument("--out", required=True)
    for name in ["train", "predict"]:
        d = sub.add_parser(name)
        d.add_argument("--data", required=True)
        d.add_argument("--config", default="configs/4070-sft.json")
        d.add_argument("--model-lock", default="model-lock.json")
        d.add_argument("--out", required=True)
        d.add_argument("--cpu", action="store_true")
        if name == "train":
            d.add_argument("--mode", choices=["sft", "dpo"], required=True)
            d.add_argument("--sft-adapter")
            d.add_argument("--max-steps", type=int)
        else:
            d.add_argument("--adapter")
            d.add_argument("--samples", type=int, default=1)
            d.add_argument("--temperature", type=float, default=0)
    a = p.parse_args()
    if a.command == "doctor":
        from .modeling import doctor
        result = doctor()
    elif a.command == "probe":
        from .probe import probe
        result = probe(a.out, a.previous_predictions)
    elif a.command == "compare":
        from .report import compare
        result = compare(a.run, a.out)
    elif a.command == "stress":
        from .stress import make_stress
        result = make_stress(a.out, a.groups)
    elif a.command == "download":
        from .data import download
        result = download(a.out)
    elif a.command == "prepare":
        from .data import prepare
        result = prepare(a.raw, a.out, a.seed)
    elif a.command == "resolve-model":
        from .modeling import resolve_model
        result = resolve_model(a.model, a.out)
    elif a.command == "freeze":
        from pathlib import Path
        from .data import freeze_cohort
        lock = json.loads(Path(a.model_lock).read_text())
        result = freeze_cohort(a.input, a.out, lock["model"], lock["revision"], a.max_prompt, a.max_length, a.train_limit, a.eval_limit)
    elif a.command == "export-sft":
        from .data import export_sft
        result = export_sft(a.data, a.out)
    elif a.command == "preferences":
        from .preferences import build_candidates
        result = build_candidates(a.data, a.out, a.predictions, a.limit)
    elif a.command == "export-dpo":
        from .preferences import export_reviewed
        result = export_reviewed(a.candidates, a.review, a.out)
    elif a.command == "evaluate":
        from .evaluate import evaluate
        result = evaluate(a.data, a.predictions, a.out)
    elif a.command == "train":
        from .train import train
        result = train(a.mode, a.data, a.config, a.out, a.model_lock, a.sft_adapter, a.cpu, a.max_steps)
    else:
        from .predict import predict
        result = predict(a.data, a.config, a.out, a.model_lock, a.adapter, a.cpu, a.samples, a.temperature)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
