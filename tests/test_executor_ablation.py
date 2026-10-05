import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class ExecutorAblationTests(unittest.TestCase):
    def test_uses_program_not_gold_and_abstains_on_invalid_evidence(self):
        script = Path(__file__).resolve().parents[1] / "scripts/executor_ablation.py"
        outputs = []
        with tempfile.TemporaryDirectory() as folder:
            for reference in [20, 987654]:
                root = Path(folder) / str(reference)
                root.mkdir()
                rows = [{"id": uid, "report_id": uid, "split": "dev", "answerable": True,
                         "evidence": {"t": "Revenue was 120 versus 100."},
                         "target": {"answer": reference}, "gold_evidence_ids": ["t"]}
                        for uid in ["valid", "invalid"]]
                data = root / "data.jsonl"
                data.write_text("".join(json.dumps(r) + "\n" for r in rows))
                digest = hashlib.sha256(data.read_bytes()).hexdigest()
                preds = []
                for uid, source in [("valid", "t"), ("invalid", "invented")]:
                    result = {"abstain": False, "answer": 999, "steps": [{"op": "subtract", "args": [
                        {"source": source, "value": "120"}, {"source": source, "value": "100"}]}]}
                    preds.append({"id": uid, "sample": 0, "dataset_sha256": digest,
                                  "prompt_sha256": "fixture", "output": json.dumps(result)})
                predictions = root / "predictions.jsonl"
                predictions.write_text("".join(json.dumps(p) + "\n" for p in preds))
                out = root / "derived.jsonl"
                subprocess.run([sys.executable, str(script), "--data", str(data),
                                "--predictions", str(predictions), "--out", str(out)],
                               check=True, capture_output=True, text=True)
                derived = [json.loads(json.loads(line)["output"]) for line in out.read_text().splitlines()]
                self.assertEqual(derived[0]["answer"], 20)
                self.assertEqual(derived[1], {"abstain": True, "steps": [], "answer": None})
                outputs.append(derived)
            self.assertEqual(outputs[0], outputs[1], "Reference labels leaked into transformation")
