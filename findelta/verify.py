"""Restricted arithmetic interpreter. Never uses eval/exec or executes model code.

Evidence binding proves numeric occurrence, NOT semantic entailment or unit correctness.
"""
import json
import math
import re
from decimal import Decimal, InvalidOperation, localcontext

CONSTANTS = {f"const_{n}": Decimal(n) for n in [*range(11), 12, 100, 1000, 10000, 100000, 1000000, 1000000000]}
CONSTANTS["const_m1"] = Decimal(-1)
NUMBER = re.compile(r"(?<![\w.])[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:\s*%)?(?!\w|\.\d)")


def number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float, str, Decimal)):
        raise ValueError("not_numeric")
    s = str(value).strip().replace(",", "").replace(" ", "")
    if len(s) > 64:
        raise ValueError("numeric_limit")
    pct = s.endswith("%")
    if pct:
        s = s[:-1]
    try:
        d = Decimal(s)
    except InvalidOperation as e:
        raise ValueError("not_numeric") from e
    if not d.is_finite() or abs(d) > Decimal("1e18"):
        raise ValueError("numeric_limit")
    return d / 100 if pct else d


def evidence_numbers(text):
    values = set()
    for match in NUMBER.finditer(text):
        try:
            values.add(number(match.group()))
        except ValueError:
            pass
    return values


def close(a, b):
    # Project-specific tolerance. This is NOT the official FinQA scorer.
    return math.isclose(float(number(a)), float(number(b)), rel_tol=1e-5, abs_tol=1e-4)


def parse_prediction(raw):
    if isinstance(raw, str):
        if len(raw) > 20000:
            raise ValueError("output_too_long")
        def unique_pairs(pairs):
            out = {}
            for k, v in pairs:
                if k in out:
                    raise ValueError("duplicate_json_key")
                out[k] = v
            return out
        try:
            raw = json.loads(raw, object_pairs_hook=unique_pairs)
        except (json.JSONDecodeError, RecursionError) as e:
            raise ValueError("invalid_json") from e
    if not isinstance(raw, dict) or set(raw) != {"abstain", "steps", "answer"}:
        raise ValueError("invalid_schema")
    if type(raw["abstain"]) is not bool or not isinstance(raw["steps"], list):
        raise ValueError("invalid_schema")
    if raw["abstain"]:
        if raw["steps"] or raw["answer"] is not None:
            raise ValueError("invalid_abstention")
    elif not 1 <= len(raw["steps"]) <= 12:
        raise ValueError("invalid_step_count")
    else:
        number(raw["answer"])
    return raw


def execute(steps, evidence):
    if not isinstance(steps, list) or not 1 <= len(steps) <= 12:
        raise ValueError("invalid_step_count")
    results, dependencies, refs = [], [], set()
    for i, step in enumerate(steps):
        if not isinstance(step, dict) or set(step) != {"op", "args"}:
            raise ValueError("invalid_step")
        if step["op"] not in {"add", "subtract", "multiply", "divide"}:
            raise ValueError("invalid_operation")
        args = step["args"]
        if not isinstance(args, list) or len(args) != 2:
            raise ValueError("invalid_arguments")
        vals, deps = [], {i}
        for arg in args:
            if isinstance(arg, str) and arg in CONSTANTS:
                vals.append(CONSTANTS[arg])
            elif isinstance(arg, str) and re.fullmatch(r"#\d+", arg):
                j = int(arg[1:])
                if j >= i:
                    raise ValueError("forward_reference")
                vals.append(results[j])
                deps.update(dependencies[j])
            elif isinstance(arg, dict) and set(arg) == {"source", "value"}:
                src = arg["source"]
                if not isinstance(src, str) or src not in evidence:
                    raise ValueError("unknown_source")
                val = number(arg["value"])
                if val not in evidence_numbers(evidence[src]):
                    raise ValueError("ungrounded_operand")
                vals.append(val)
                refs.add(src)
            else:
                raise ValueError("unbound_operand")
        a, b = vals
        with localcontext() as ctx:
            ctx.prec = 28
            if step["op"] == "add":
                result = a + b
            elif step["op"] == "subtract":
                result = a - b
            elif step["op"] == "multiply":
                result = a * b
            else:
                if not b:
                    raise ValueError("division_by_zero")
                result = a / b
        number(result)
        results.append(result)
        dependencies.append(deps)
    if not refs:
        raise ValueError("no_evidence")
    if dependencies[-1] != set(range(len(steps))):
        raise ValueError("unused_steps")
    return float(results[-1]), refs


def score(row, raw):
    result = dict(schema_valid=False, abstained=False, execution_valid=False,
                  answer_correct=False, execution_correct=False, verified_correct=False,
                  evidence_id_precision=None, evidence_id_recall=None, error=None)
    try:
        pred = parse_prediction(raw)
        result["schema_valid"] = True
        result["abstained"] = pred["abstain"]
        if pred["abstain"]:
            result["verified_correct"] = not row["answerable"]
            return result
        if row["answerable"]:
            result["answer_correct"] = close(pred["answer"], row["target"]["answer"])
        value, refs = execute(pred["steps"], row["evidence"])
        result["execution_valid"] = True
        result["execution_correct"] = row["answerable"] and close(value, row["target"]["answer"])
        result["verified_correct"] = result["answer_correct"] and result["execution_correct"] and close(value, pred["answer"])
        gold_refs = set(row.get("gold_evidence_ids", []))
        if gold_refs:
            result["evidence_id_precision"] = len(refs & gold_refs) / len(refs)
            result["evidence_id_recall"] = len(refs & gold_refs) / len(gold_refs)
    except (ValueError, TypeError, KeyError, ArithmeticError, RecursionError) as e:
        result["error"] = str(e)
    return result
