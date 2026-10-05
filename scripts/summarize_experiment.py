"""Build an auditable dev report from completed base/SFT artifacts."""
import argparse
import collections
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def main():
    from findelta.common import read_jsonl, sha256, write_json, write_jsonl
    from findelta.verify import close, execute, parse_prediction

    parser = argparse.ArgumentParser()
    parser.add_argument("--run", required=True)
    parser.add_argument("--data", required=True)
    args = parser.parse_args()
    root = Path(args.run)
    rows = {r["id"]: r for r in read_jsonl(args.data)}
    training = json.loads((root / "sft-full/run_manifest.json").read_text())
    metrics, manifests, predictions, scored = {}, {}, {}, {}
    for name in ["base", "sft"]:
        metrics[name] = json.loads((root / f"{name}-dev/metrics.json").read_text())
        manifests[name] = json.loads((root / f"{name}-dev-predictions.jsonl.manifest.json").read_text())
        predictions[name] = {p["id"]: p for p in read_jsonl(root / f"{name}-dev-predictions.jsonl")}
        scored[name] = {r["id"]: r for r in read_jsonl(root / f"{name}-dev/per_example.jsonl")}
        assert set(predictions[name]) == set(scored[name]) == set(rows)
        assert metrics[name]["dataset_sha256"] == sha256(args.data)
    assert metrics["base"]["prompt_sha256"] == metrics["sft"]["prompt_sha256"] == training["prompt_sha256"]
    assert manifests["base"]["config"] == manifests["sft"]["config"]
    assert manifests["base"]["environment"] == manifests["sft"]["environment"]
    assert manifests["base"]["adapter_manifest_sha256"] is None
    assert manifests["sft"]["adapter_manifest_sha256"] == sha256(root / "sft-full/run_manifest.json")

    audit, counts = [], {name: collections.Counter() for name in metrics}
    transitions = collections.Counter()
    for uid, row in rows.items():
        before, after = scored["base"][uid]["verified_correct"], scored["sft"][uid]["verified_correct"]
        transition = "both_correct" if before and after else "improved" if after else "regressed" if before else "both_wrong"
        transitions[transition] += 1
        item = {"id": uid, "question": row["question"], "target": row["target"],
                "transition": transition, "models": {}}
        for name in metrics:
            record = {"output": predictions[name][uid]["output"], "score": scored[name][uid]}
            try:
                pred = parse_prediction(record["output"])
                if pred["abstain"]:
                    category = "abstained"
                else:
                    value, _ = execute(pred["steps"], row["evidence"])
                    record["executed_answer"] = value
                    consistent = close(value, pred["answer"])
                    record["answer_matches_own_program"] = consistent
                    category = ("verified_correct" if scored[name][uid]["verified_correct"] else
                                "consistent_but_wrong" if consistent else "answer_program_disagreement")
            except (ValueError, TypeError, KeyError, ArithmeticError, RecursionError):
                category = "invalid_schema_or_program"
            counts[name][category] += 1
            record["category"] = category
            item["models"][name] = record
        audit.append(item)
    write_jsonl(root / "paired-audit.jsonl", audit)
    summary = {"n": len(rows), "split": "dev", "training_seconds": training["elapsed_seconds"],
               "peak_allocated_gib": training["peak_allocated_gib"],
               "peak_reserved_gib": training["peak_reserved_gib"],
               "transitions": dict(transitions), "categories": {k: dict(v) for k,v in counts.items()},
               "metrics": metrics, "inference_seconds": {k:v["elapsed_seconds"] for k,v in manifests.items()}}
    ablation_path = root / "sft-executor-dev/metrics.json"
    if ablation_path.exists():
        summary["post_hoc_executor_ablation"] = json.loads(ablation_path.read_text())
    summary["program_result_correct_counts"] = {
        name: sum(r["execution_correct"] for r in values.values()) for name, values in scored.items()
    }
    write_json(root / "summary.json", summary)
    lines = ["# FinDelta 首轮 GPU 实验", "", "本次完成了单卡 LoRA SFT 与受控开发集比较；结果为单随机种子的探索性结果。", "",
             "## 结果", "", (root / "comparison.md").read_text(), "",
             "## 设置与开销", "",
             "- Qwen3-0.6B，固定 revision；RTX 4090；BF16；LoRA rank=8，q_proj/v_proj。",
             "- 1,000 条训练样本，1 epoch，seed=42；从基础模型重新训练，未继续 smoke adapter。",
             "- 同一 200 题自定义公司隔离 dev cohort；prompt v3、greedy、batch=8、最多生成 640 tokens。",
             f"- 训练时间 {training['elapsed_seconds']:.1f} 秒；峰值 allocated {training['peak_allocated_gib']:.2f} GiB，reserved {training['peak_reserved_gib']:.2f} GiB。",
             f"- 推理时间：Base {manifests['base']['elapsed_seconds']:.1f} 秒，SFT {manifests['sft']['elapsed_seconds']:.1f} 秒。不含模型加载、安装和空闲计费时间。", "",
             "## 逐题变化与错误", "",
             f"- 严格验证从错到对：{transitions['improved']} 题；从对到错：{transitions['regressed']} 题。",
             "- `paired-audit.jsonl` 保留全部题目的原始输出、评分、程序执行值和变化类别。", "",
             "| 类别 | Base | SFT |", "|---|---:|---:|"]
    for category in ["verified_correct", "consistent_but_wrong", "answer_program_disagreement", "invalid_schema_or_program", "abstained"]:
        lines.append(f"| {category} | {counts['base'][category]} | {counts['sft'][category]} |")
    if ablation_path.exists():
        a = summary["post_hoc_executor_ablation"]
        lines += ["", "## 额外推理对照：确定性执行器", "",
                  "这是看到 dev 错误后提出的额外对照，不是预先固定的主要实验，也不是又一次训练。保留 SFT 原始预测，执行模型给出的程序并用执行结果作为 answer；程序无效则拒答。转换只读取输入证据，不读取参考答案。", "",
                  f"严格验证正确率 {a['verified_accuracy']:.1%}，覆盖率 {a['answer_coverage']:.1%}，已回答问题错误率 {a['error_rate_among_answered']:.1%}。",
                  "格式合法率会因为程序化输出 JSON 而达到 100%，这不是模型自身的格式能力提升。",
                  "固定的 200 题都保留在分母中；无效程序转为拒答仍按答错计。本 cohort 全部可答，不能据此评估拒答识别能力。",
                  "这个对照分离了算术执行与选数/选运算问题，但仍不能保证期间、单位、语义证据正确。", ""]
        if (root / "executor-comparison.md").exists():
            lines.append((root / "executor-comparison.md").read_text())
    lines += ["", "## 限制与下一步", "",
              "- 这是自定义过滤后的 FinQA 开发集，不是官方榜单或最终测试结果。尚未评测冻结测试集。",
              "- Verified 只检查数值答案、程序计算与来源数字出现，不证明选对期间、单位或语义证据。",
              "- 数据仍存在百分比尺度和操作数绑定歧义；需人工审查，不能事后乘除 100 来改变评分。",
              "- 置信区间按报告分组、配对 bootstrap；不包含训练 seed 方差。尚需多 seed 复现。",
              "- 已实现 DPO 接口，但尚未完成真实偏好审核和 DPO 实验，不能写成 DPO 提升。",
              "- 后续按错误类别审查样本、构造并审核 train-only 偏好对，再做 DPO；固定方法后评测 test。", ""]
    (root / "REPORT.zh.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
