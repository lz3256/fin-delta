"""Controlled, synthetic stress fixtures. Not a real-financial-document benchmark."""
import random

from .common import write_jsonl


def make_stress(out, groups=20, seed=73):
    rng = random.Random(seed)
    rows = []
    for i in range(groups):
        old, new = rng.randrange(80, 180), rng.randrange(180, 280)
        base = dict(company=f"SYNTH-{i}", report_id=f"SYNTH-{i}/2024", split="test",
                    dataset="synthetic-template-stress-v1", synthetic=True,
                    question="What was revenue growth from fiscal year 2023 to fiscal year 2024, expressed as a percentage?",
                    answerable=True)
        for kind in ["original", "number_change", "distractor_period", "unit_change", "missing_evidence"]:
            a, b = (old + 7, new - 11) if kind == "number_change" else (old, new)
            evidence = {"p1": f"Fiscal year 2023 revenue was {a} million USD.",
                        "p2": f"Fiscal year 2024 revenue was {b} million USD."}
            x, y = {"source": "p1", "value": str(a)}, {"source": "p2", "value": str(b)}
            steps = [{"op": "subtract", "args": [y, x]}, {"op": "divide", "args": ["#0", x]},
                     {"op": "multiply", "args": ["#1", "const_100"]}]
            if kind == "distractor_period":
                evidence["p3"] = f"First nine months of 2024 revenue was {b - 30} million USD."
                evidence["p4"] = f"Fiscal year 2022 revenue was {a - 10} million USD."
            elif kind == "unit_change":
                evidence["p2"] = f"Fiscal year 2024 revenue was {b * 1000} thousand USD."
                steps = [{"op": "divide", "args": [{"source": "p2", "value": str(b * 1000)}, "const_1000"]},
                         {"op": "subtract", "args": ["#0", x]},
                         {"op": "divide", "args": ["#1", x]},
                         {"op": "multiply", "args": ["#2", "const_100"]}]
            target = {"abstain": False, "steps": steps, "answer": (b - a) / a * 100}
            if kind == "missing_evidence":
                del evidence["p2"]
                evidence["p3"] = "Fiscal year 2024 operating profit was 17 million USD."
                target = {"abstain": True, "steps": [], "answer": None}
            keys = list(evidence)
            rng.shuffle(keys)
            rows.append(dict(base, id=f"synthetic-{i}-{kind}", variant=kind,
                             answerable=kind != "missing_evidence", evidence={k: evidence[k] for k in keys},
                             target=target, gold_evidence_ids=[] if kind == "missing_evidence" else ["p1", "p2"]))
    write_jsonl(out, rows)
    return {"count": len(rows), "groups": groups, "synthetic": True, "warning": "Template diagnostic only. Do not report as real-financial OOD accuracy."}
