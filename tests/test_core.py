import copy
import csv
import json
import tempfile
import unittest
from pathlib import Path

from findelta.common import messages, sha256, write_jsonl
from findelta.data import convert, export_sft
from findelta.evaluate import evaluate
from findelta.preferences import build_candidates, export_reviewed
from findelta.verify import evidence_numbers, execute, number, parse_prediction, score


def fixture():
    return {"id": "ACME/2024/p1-1", "company": "ACME", "report_id": "ACME/2024",
            "split": "train", "question": "How much did revenue increase?",
            "evidence": {"table_1": "2024 revenue 120 million", "table_2": "2023 revenue 100 million"},
            "answerable": True, "gold_evidence_ids": ["table_1", "table_2"],
            "target": {"abstain": False, "steps": [{"op": "subtract", "args": [
                {"source": "table_1", "value": "120"}, {"source": "table_2", "value": "100"}]}], "answer": 20}}


class VerifierTests(unittest.TestCase):
    def test_sentence_final_number_and_decimal(self):
        self.assertIn(number("100"), evidence_numbers("revenue was 100."))
        self.assertEqual(evidence_numbers("cost 10.25."), {number("10.25")})

    def test_correct_grounded_program(self):
        row = fixture()
        self.assertTrue(score(row, row["target"])["verified_correct"])

    def test_percentage_scale(self):
        self.assertEqual(float(number("23.6%")), .236)
        value, _ = execute([{"op": "divide", "args": [{"source": "t", "value": "9896"}, {"source": "t", "value": "23.6%"}]}], {"t": "expense 9896; share 23.6%"})
        self.assertAlmostEqual(value, 41932.2033898, places=5)

    def test_correct_answer_with_invented_operand_fails(self):
        row = fixture()
        pred = copy.deepcopy(row["target"])
        pred["steps"][0]["args"][0]["value"] = "999"
        s = score(row, pred)
        self.assertTrue(s["answer_correct"])
        self.assertFalse(s["verified_correct"])
        self.assertEqual(s["error"], "ungrounded_operand")

    def test_answer_and_execution_must_agree(self):
        row = fixture()
        pred = copy.deepcopy(row["target"])
        pred["answer"] = 21
        self.assertFalse(score(row, pred)["verified_correct"])

    def test_no_code_execution(self):
        with self.assertRaises(ValueError):
            execute([{"op": "__import__", "args": ["os", "system"]}], {})

    def test_nonfinite_bool_and_forward_refs_rejected(self):
        for n in ["NaN", "Infinity", True, "1e999"]:
            with self.assertRaises(ValueError):
                number(n)
        with self.assertRaisesRegex(ValueError, "forward_reference"):
            execute([{"op": "add", "args": ["#0", "const_1"]}], {})

    def test_division_zero(self):
        with self.assertRaisesRegex(ValueError, "division_by_zero"):
            execute([{"op": "divide", "args": [{"source": "t", "value": "2"}, "const_0"]}], {"t": "2"})

    def test_constant_only_shortcut_fails(self):
        with self.assertRaisesRegex(ValueError, "no_evidence"):
            execute([{"op": "add", "args": ["const_10", "const_10"]}], {})

    def test_unused_grounding_step_fails(self):
        steps = fixture()["target"]["steps"] + [{"op": "add", "args": ["const_10", "const_10"]}]
        with self.assertRaisesRegex(ValueError, "unused_steps"):
            execute(steps, fixture()["evidence"])

    def test_invalid_json_and_duplicate_keys(self):
        for raw in ['not JSON', '{"abstain":true,"abstain":false,"steps":[],"answer":null}', '[]']:
            with self.assertRaises(ValueError):
                parse_prediction(raw)

    def test_abstention_scored_only_when_expected(self):
        row = fixture()
        pred = {"abstain": True, "steps": [], "answer": None}
        self.assertFalse(score(row, pred)["verified_correct"])
        row["answerable"] = False
        self.assertTrue(score(row, pred)["verified_correct"])


class DataTests(unittest.TestCase):
    def test_synthetic_stress_targets_are_consistent(self):
        from findelta.stress import make_stress
        from findelta.common import read_jsonl
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "stress.jsonl"
            make_stress(path)
            for row in read_jsonl(path):
                self.assertTrue(score(row, row["target"])["verified_correct"], row["id"])

    def test_prompt_excludes_gold_metadata(self):
        row = fixture()
        row["audit"] = {"original_program": "SECRET_LABEL"}
        row["target"]["answer"] = "SECRET_ANSWER"
        text = json.dumps(messages(row))
        self.assertNotIn("SECRET", text)
        self.assertNotIn("gold_evidence_ids", text)

    def test_converter_uses_original_context(self):
        record = {"id": "ACME/2024/p1-1", "table": [["year", "revenue"], ["2024", "120"], ["2023", "100"]], "pre_text": [], "post_text": [],
                  "qa": {"question": "increase?", "program": "subtract(120, 100)", "exe_ans": 20,
                         "answer": "20", "gold_inds": {"table_1": "DO_NOT_COPY_GOLD_TEXT"}, "model_input": ["LEAK"]}}
        row = convert(record, "train")
        self.assertTrue(score(row, row["target"])["verified_correct"])
        self.assertNotIn("DO_NOT_COPY", json.dumps(row["evidence"]))
        record["qa"]["exe_ans"] = 50
        with self.assertRaisesRegex(ValueError, "program_execution_mismatch"):
            convert(record, "train")

    def test_test_data_cannot_become_training_data(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            row = fixture()
            row["split"] = "test"
            write_jsonl(p / "data.jsonl", [row])
            with self.assertRaises(ValueError):
                export_sft(p / "data.jsonl", p / "sft.jsonl")
            with self.assertRaises(ValueError):
                build_candidates(p / "data.jsonl", p / "pairs")

    def test_preferences_require_real_review_decisions(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            write_jsonl(p / "data.jsonl", [fixture()])
            build_candidates(p / "data.jsonl", p / "pairs")
            with self.assertRaises(ValueError):
                export_reviewed(p / "pairs/candidates.jsonl", p / "pairs/review.csv", p / "approved.jsonl")
            with (p / "pairs/review.csv").open("w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "decision"])
                writer.writerow([fixture()["id"], "approve"])
            result = export_reviewed(p / "pairs/candidates.jsonl", p / "pairs/review.csv", p / "approved.jsonl")
            self.assertEqual(result["approved"], 1)

    def test_missing_predictions_are_failures_and_duplicates_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            row = fixture()
            write_jsonl(p / "data.jsonl", [row])
            write_jsonl(p / "pred.jsonl", [])
            report = evaluate(p / "data.jsonl", p / "pred.jsonl", p / "report")
            self.assertEqual(report["missing_predictions"], 1)
            self.assertEqual(report["verified_accuracy"], 0)
            pred = dict(id=row["id"], output=row["target"], dataset_sha256=sha256(p / "data.jsonl"))
            write_jsonl(p / "pred.jsonl", [pred, pred])
            with self.assertRaises(ValueError):
                evaluate(p / "data.jsonl", p / "pred.jsonl", p / "report2")

    def test_provenance_mismatch_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            write_jsonl(p / "data.jsonl", [fixture()])
            write_jsonl(p / "pred.jsonl", [dict(id=fixture()["id"], output=fixture()["target"], dataset_sha256="wrong")])
            with self.assertRaises(ValueError):
                evaluate(p / "data.jsonl", p / "pred.jsonl", p / "r")


if __name__ == "__main__":
    unittest.main()
