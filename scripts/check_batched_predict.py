"""Check greedy batching with a real tiny CPU model (not a quality benchmark).

First run tiny_smoke.py to create a local fixture model, then pass its output folder.
"""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def main():
    import torch
    from findelta.common import read_jsonl, write_json, write_jsonl
    from findelta.predict import predict

    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    fixture, out = Path(args.fixture), Path(args.out)
    if out.exists() and any(out.iterdir()):
        raise ValueError("Choose a new output folder")
    out.mkdir(parents=True, exist_ok=True)
    row = read_jsonl(fixture / "data.jsonl")[0]
    rows = [{**row, "id": str(i), "question": row["question"] + " additional context" * i}
            for i in range(3)]
    write_jsonl(out / "rows.jsonl", rows)
    config = json.loads((fixture / "config.json").read_text())
    torch.set_num_threads(2)
    for batch_size in [1, 2]:
        config["inference_batch_size"] = batch_size
        write_json(out / f"config-{batch_size}.json", config)
        predict(out / "rows.jsonl", out / f"config-{batch_size}.json",
                out / f"pred-{batch_size}.jsonl", cpu=True)
    def records(batch_size):
        return [(r["id"], r["output"], r["generated_tokens"])
                for r in read_jsonl(out / f"pred-{batch_size}.jsonl")]
    assert records(1) == records(2), "Batching changed greedy fixture outputs"
    assert len(records(2)) == 3, "Partial final batch was lost"
    write_json(out / "result.json", {
        "passed": True, "n": 3, "batch_sizes": [1, 2],
        "checks": ["unequal-length prompts", "same greedy output and token count", "partial final batch"],
        "scope": "Random tiny CPU fixture; no guarantee of bitwise equality across GPU kernels or model quality"
    })
    print("Batched inference integration passed")


if __name__ == "__main__":
    main()
