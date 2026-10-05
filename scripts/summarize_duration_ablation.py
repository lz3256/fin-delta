"""Audit provenance and report the completed 1-vs-3-epoch experiment."""
import argparse
import collections
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from findelta.common import read_jsonl, sha256, write_json, write_jsonl
from findelta.verify import close, execute, parse_prediction


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--run', required=True)
    p.add_argument('--previous', required=True)
    p.add_argument('--data', required=True)
    a = p.parse_args()
    run, old = Path(a.run), Path(a.previous)
    assert (run / 'status.txt').read_text().strip() == 'COMPLETE'
    load = lambda path: json.loads(Path(path).read_text())
    prior = load(old / 'sft-full/run_manifest.json')
    trained = load(run / 'sft3-adapter/run_manifest.json')
    protocol = load(run / 'protocol.json')
    differences = {k: [prior['config'].get(k), trained['config'].get(k)]
                   for k in prior['config'].keys() | trained['config'].keys()
                   if prior['config'].get(k) != trained['config'].get(k)}
    assert differences == {'epochs': [1, 3]}, differences
    assert prior['data_sha256'] == trained['data_sha256'] == protocol['sft_data_sha256']
    assert prior['environment'] == trained['environment']
    assert prior['prompt_sha256'] == trained['prompt_sha256'] == protocol['prompt_sha256']
    assert sha256(old / 'sft-full/run_manifest.json') == protocol['old_training_manifest_sha256']
    assert trained['examples'] == prior['examples'] == 1000
    assert trained['metrics']['epoch'] == 3.0 and trained['trainable_tensors_changed'] > 0
    assert load(run / 'sft3-adapter/trainer_state.json')['global_step'] == 375
    assert sha256(run / 'train-probe64.jsonl') == protocol['train_probe_sha256']
    assert sha256(a.data) == protocol['data_sha256']['dev']
    old_protocol = load(old / 'protocol.json')
    assert old_protocol['code_sha256'] == protocol['code_sha256']
    runs = {
        '1epoch-dev': (old / 'sft-dev', old / 'sft-dev-predictions.jsonl', a.data, old / 'sft-full/run_manifest.json'),
        '3epochs-dev': (run / 'sft3-dev', run / 'sft3-dev.jsonl', a.data, run / 'sft3-adapter/run_manifest.json'),
        '1epoch-train64': (run / 'sft1-train64', run / 'sft1-train64.jsonl', run / 'train-probe64.jsonl', old / 'sft-full/run_manifest.json'),
        '3epochs-train64': (run / 'sft3-train64', run / 'sft3-train64.jsonl', run / 'train-probe64.jsonl', run / 'sft3-adapter/run_manifest.json'),
    }
    inference_reference = load(old / 'sft-dev-predictions.jsonl.manifest.json')
    summaries, scores = {}, {}
    for name, (evaluation, predictions, data, adapter_manifest) in runs.items():
        manifest = load(str(predictions) + '.manifest.json')
        metrics = load(evaluation / 'metrics.json')
        rows = {r['id']: r for r in read_jsonl(data)}
        outputs = {r['id']: r for r in read_jsonl(predictions)}
        scored = {r['id']: r for r in read_jsonl(evaluation / 'per_example.jsonl')}
        assert set(rows) == set(outputs) == set(scored)
        assert manifest['dataset_sha256'] == metrics['dataset_sha256'] == sha256(data)
        assert manifest['predictions_sha256'] == metrics['predictions_sha256'] == sha256(predictions)
        assert manifest['adapter_manifest_sha256'] == sha256(adapter_manifest)
        for key in ['config', 'environment', 'samples', 'temperature', 'prompt_sha256']:
            assert manifest[key] == inference_reference[key], (name, key)
        counts = collections.Counter()
        audit = []
        for uid, row in rows.items():
            record = {'id': uid, 'question': row['question'], 'target': row['target'], 'output': outputs[uid]['output'], 'score': scored[uid]}
            try:
                pred = parse_prediction(record['output'])
                if pred['abstain']:
                    category = 'abstained'
                else:
                    value, _ = execute(pred['steps'], row['evidence'])
                    record['executed_answer'] = value
                    category = 'verified_correct' if scored[uid]['verified_correct'] else ('consistent_but_wrong' if close(value, pred['answer']) else 'answer_program_disagreement')
            except (ValueError, TypeError, KeyError, ArithmeticError, RecursionError):
                category = 'invalid_schema_or_program'
            record['category'] = category
            counts[category] += 1
            audit.append(record)
        write_jsonl(run / f'{name}-audit.jsonl', audit)
        groups = {}
        for label, ids in [('one_step', [uid for uid in rows if len(rows[uid]['target']['steps']) == 1]),
                           ('multi_step', [uid for uid in rows if len(rows[uid]['target']['steps']) > 1])]:
            groups[label] = {'n': len(ids), 'verified_correct': sum(scored[i]['verified_correct'] for i in ids),
                             'execution_correct': sum(scored[i]['execution_correct'] for i in ids)}
        summaries[name] = {'metrics': metrics, 'categories': dict(counts), 'step_groups': groups,
                           'program_correct': sum(s['execution_correct'] for s in scored.values()),
                           'execution_valid': sum(s['execution_valid'] for s in scored.values()),
                           'inference_seconds': manifest['elapsed_seconds']}
        scores[name] = scored
    transitions = collections.Counter()
    for uid, first in scores['1epoch-dev'].items():
        second = scores['3epochs-dev'][uid]
        transitions['both_correct' if first['verified_correct'] and second['verified_correct'] else
                    'improved' if second['verified_correct'] else 'regressed' if first['verified_correct'] else 'both_wrong'] += 1
    summary = {'runs': summaries, 'config_differences': differences, 'dev_transitions': dict(transitions),
               'training_seconds': trained['elapsed_seconds'], 'peak_allocated_gib': trained['peak_allocated_gib'],
               'peak_reserved_gib': trained['peak_reserved_gib'], 'test_evaluated': False,
               'executor_metrics': {'1epoch': load(old / 'sft-executor-dev/metrics.json'), '3epochs': load(run / 'sft-executor-dev/metrics.json')}}
    for n, key in [('1epoch', '1epoch-dev'), ('3epochs', '3epochs-dev')]:
        assert round(summary['executor_metrics'][n]['verified_accuracy'] * 200) == summaries[key]['program_correct']
    write_json(run / 'summary.json', summary)
    write_json(run / 'validation.json', {'provenance_checks_passed': True, 'training_config_only_epochs_changed': True,
        'same_inference_config_environment_prompt': True, 'full_cohort_no_missing_predictions': True,
        'training_completed_375_steps': load(run / 'sft3-adapter/trainer_state.json')['global_step'] == 375,
        'test_evaluated': False, 'real_dpo_completed': False})
    lines = ['# FinDelta：SFT 训练轮数对照', '', '单 seed、开发集探索性实验。比较 1 epoch 与 3 epochs；均从相同基础模型重新训练。', '',
             '## 开发集主要结果', '', (run / 'comparison-raw.md').read_text(), '',
             '## 确定性执行器对照', '', '沿用上一轮已定义的推理规则：计算模型生成的程序，非法程序拒答；保留全部 200 题作为分母。不是额外训练，也不使用参考答案来修改输出。', '',
             (run / 'comparison-executor.md').read_text(), '',
             '## 训练题诊断', '', '在本轮观察输出之前，用 seed=20260924 从按 ID 排序的 1,000 道训练题抽取 64 题。这是模型见过的数据，不是泛化结果。', '',
             '| 配置 | 样本数 | 严格正确 | 程序执行结果正确 | 有效程序 |', '|---|---:|---:|---:|---:|']
    for name in ['1epoch-train64', '3epochs-train64', '1epoch-dev', '3epochs-dev']:
        s = summaries[name]
        lines.append(f"| {name} | {s['metrics']['n']} | {s['categories'].get('verified_correct',0)} | {s['program_correct']} | {s['execution_valid']} |")
    lines += ['', '## 逐题变化与剩余错误', '', f"原始模型严格评分：{dict(transitions)}。", '',
              '| 类别 | 1 epoch dev | 3 epochs dev |', '|---|---:|---:|']
    for category in ['verified_correct', 'consistent_but_wrong', 'answer_program_disagreement', 'invalid_schema_or_program', 'abstained']:
        lines.append(f"| {category} | {summaries['1epoch-dev']['categories'].get(category,0)} | {summaries['3epochs-dev']['categories'].get(category,0)} |")
    lines += ['', '## 可复现设置与限制', '',
              '- Qwen3-0.6B 固定 revision；LoRA rank=8、alpha=16、q_proj/v_proj；BF16；RTX 4090；seed=42。',
              '- 同一 1,000 条训练样本、prompt v3、200 题 dev；greedy、batch=8、max_new_tokens=640。',
              '- 训练配置只改 epochs，但 5% warmup 和线性学习率日程按总步数重新计算。因此比较的是训练时长配方，不是同一轨迹的第 1 与第 3 轮 checkpoint。',
              f"- 本轮训练 {trained['elapsed_seconds']:.1f} 秒；显存 allocated 峰值 {trained['peak_allocated_gib']:.2f} GiB、reserved 峰值 {trained['peak_reserved_gib']:.2f} GiB。", 
              '- 原始 adapter、预测、评分、数据/提示词/代码哈希均保留；审计文件为 *-audit.jsonl。',
              '- 数据为自定义过滤后的公司隔离 FinQA cohort，不是官方榜单；来源数字出现不证明期间、单位与语义正确。',
              '- 反复在 dev 上试配方会产生选择偏差；置信区间不校正多次探索，也不包含训练 seed 方差。',
              '- 本轮训练期间发现原始训练标签存在明确的年份矛盾，见 ../train-year-audit-v1/START_HERE.zh.md。没有改动当前数据或重算分数；后续清洗必须另建数据版本。',
              '- test 未做预测；DPO 仍未运行。', '']
    (run / 'REPORT.zh.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
