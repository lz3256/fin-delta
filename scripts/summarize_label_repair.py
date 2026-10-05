"""Validate both completed arms and summarize the predeclared label comparison."""
import argparse
import collections
import json
import math
from pathlib import Path
import random
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from findelta.common import prompt_sha256, read_jsonl, sha256, write_json, write_jsonl
from findelta.verify import execute, parse_prediction, score


def paired(control, repaired):
    assert set(control) == set(repaired)
    groups = collections.defaultdict(list)
    transitions = collections.Counter()
    for uid, x in control.items():
        y = repaired[uid]
        assert x['report_id'] == y['report_id']
        a, b = int(x['verified_correct']), int(y['verified_correct'])
        groups[x['report_id']].append(b - a)
        transitions[f'{a}->{b}'] += 1
    rng, keys, samples = random.Random(42), sorted(groups), []
    for _ in range(1000):
        values = [v for k in rng.choices(keys, k=len(keys)) for v in groups[k]]
        samples.append(sum(values) / len(values))
    samples.sort()
    return {'delta': sum(sum(v) for v in groups.values()) / len(control),
            'ci95': [samples[25], samples[975]], 'transitions': dict(transitions),
            'reports': len(keys), 'bootstrap_seed': 42, 'bootstrap_repetitions': 1000}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--run', required=True)
    args = parser.parse_args()
    run = Path(args.run).resolve()
    j = lambda p: json.loads(p.read_text())
    assert (run / 'status.txt').read_text().strip() == 'COMPLETE'
    protocol = j(run / 'protocol.json')
    frozen = ROOT / 'reports/train-repair-v2/next-experiment.json'
    plan = j(frozen)
    assert protocol['predeclared_protocol_sha256'] == sha256(frozen)
    for key, value in plan.items():
        if key != 'status':
            assert protocol[key] == value, key
    assert protocol['prompt_sha256'] == prompt_sha256()
    for path, digest in protocol['code_sha256'].items():
        assert sha256(ROOT / path) == digest, path
    assert sha256(ROOT/'scripts/runpod_label_repair.py') == protocol['runner_sha256']
    assert sha256(ROOT/'scripts/executor_ablation.py') == protocol['executor_script_sha256']
    cohort = ROOT / 'data/cohort/v2-reviewed'
    assert sha256(cohort/'manifest.json') == plan['cohort_manifest_sha256']
    assert sha256(cohort/'dev.jsonl') == plan['dev_sha256']
    dev = {r['id']: r for r in read_jsonl(cohort/'dev.jsonl')}
    assert len(dev) == 200
    splits = {split: read_jsonl(cohort/f'{split}.jsonl') for split in ['train', 'dev', 'test']}
    for x, y in [('train', 'dev'), ('train', 'test'), ('dev', 'test')]:
        assert not {r['id'] for r in splits[x]} & {r['id'] for r in splits[y]}
        assert not {r['company'] for r in splits[x]} & {r['company'] for r in splits[y]}
    inputs = {arm: read_jsonl(cohort/filename) for arm, filename in
              [('control', 'sft-control.jsonl'), ('repaired', 'sft.jsonl')]}
    a, b = inputs['control'], inputs['repaired']
    assert len(a) == len(b) == 966
    assert all(x['id'] == y['id'] and x['prompt'] == y['prompt'] for x, y in zip(a, b))
    assert sum(x['completion'] != y['completion'] for x, y in zip(a, b)) == 11
    results, audits, trains, prediction_metadata, outputs = {}, {}, {}, {}, {}
    for arm, filename, hashkey in [('control', 'sft-control.jsonl', 'control_sft_sha256'),
                                   ('repaired', 'sft.jsonl', 'repaired_sft_sha256')]:
        folder = run / arm
        train = j(folder/'adapter/run_manifest.json')
        state = j(folder/'adapter/trainer_state.json')
        assert train['mode'] == 'sft' and train['examples'] == 966
        assert train['config'] == plan['training_config']
        assert train['data_sha256'] == plan[hashkey] == sha256(cohort/filename)
        assert train['prompt_sha256'] == prompt_sha256()
        assert train['actual_max_steps'] == -1 and train['metrics']['epoch'] == 3.0
        assert state['global_step'] == 3 * math.ceil(966 / 8)
        assert train['trainable_tensors_changed'] > 0 and math.isfinite(train['metrics']['train_loss'])
        assert 'sft_run_manifest_sha256' not in train
        assert train['environment'] == protocol['environment']
        meta = j(folder/'dev.jsonl.manifest.json')
        assert meta['config'] == {**plan['inference_config'], **protocol['model_lock']}
        assert meta['environment'] == protocol['environment']
        assert meta['dataset_sha256'] == plan['dev_sha256']
        assert meta['prompt_sha256'] == prompt_sha256()
        assert meta['samples'] == 1 and meta['temperature'] == 0
        assert meta['adapter_manifest_sha256'] == sha256(folder/'adapter/run_manifest.json')
        assert meta['predictions_sha256'] == sha256(folder/'dev.jsonl')
        raw = {r['id']: r for r in read_jsonl(folder/'dev.jsonl')}
        outputs[arm] = raw
        derived = {r['id']: r for r in read_jsonl(folder/'executor.jsonl')}
        assert set(raw) == set(derived) == set(dev)
        # Recompute the executor without exposing reference targets to it.
        for uid, pred in raw.items():
            try:
                answer = parse_prediction(pred['output'])
                if not answer['abstain']:
                    value, _ = execute(answer['steps'], dev[uid]['evidence'])
                    answer = {**answer, 'answer': value}
            except (ValueError, TypeError, KeyError, ArithmeticError, RecursionError):
                answer = {'abstain': True, 'steps': [], 'answer': None}
            assert json.loads(derived[uid]['output']) == answer
            assert derived[uid]['parent_predictions_sha256'] == sha256(folder/'dev.jsonl')
        for kind, evaluation, predfile in [('raw', 'raw-dev', 'dev.jsonl'),
                                           ('executor', 'sft-executor-dev', 'executor.jsonl')]:
            metrics = j(folder/evaluation/'metrics.json')
            per = {r['id']: r for r in read_jsonl(folder/evaluation/'per_example.jsonl')}
            predictions = read_jsonl(folder/predfile)
            assert len(predictions) == len(per) == 200 and set(per) == set(dev)
            assert metrics['dataset_sha256'] == plan['dev_sha256']
            assert metrics['predictions_sha256'] == sha256(folder/predfile)
            assert metrics['n'] == 200 and metrics['missing_predictions'] == 0
            for pred in predictions:
                assert pred['dataset_sha256'] == plan['dev_sha256']
                assert pred['prompt_sha256'] == prompt_sha256()
                s = score(dev[pred['id']], pred['output'])
                assert all(s[k] == per[pred['id']][k] for k in s)
            assert metrics['verified_accuracy'] == sum(x['verified_correct'] for x in per.values()) / 200
            results[arm+'_'+kind], audits[arm+'_'+kind] = metrics, per
        trains[arm] = {k: train[k] for k in ['elapsed_seconds', 'peak_allocated_gib',
            'peak_reserved_gib', 'metrics', 'trainable_tensors_changed', 'examples']}
        prediction_metadata[arm] = meta
    assert prediction_metadata['control']['config'] == prediction_metadata['repaired']['config']
    assert sha256(run/'control/adapter/adapter_model.safetensors') != sha256(run/'repaired/adapter/adapter_model.safetensors')
    raw_delta = paired(audits['control_raw'], audits['repaired_raw'])
    exe_delta = paired(audits['control_executor'], audits['repaired_executor'])
    outcomes = []
    for uid, row in dev.items():
        outcomes.append({'id': uid, 'report_id': row['report_id'],
                         'raw_output_changed': outputs['control'][uid]['output'] != outputs['repaired'][uid]['output'],
                         **{key: values[uid]['verified_correct'] for key, values in audits.items()}})
    write_jsonl(run/'paired-outcomes.jsonl', outcomes)
    tests = (run/'tests.log').read_text()
    assert 'Ran 28 tests' in tests and tests.rstrip().endswith('OK')
    validation = {'passed': True, 'tests_passed': 28, 'same_966_ids_order_prompts': True,
        'completion_changes': 11, 'independent_base_initialization': True,
        'same_config_environment_and_dev': True, 'training_steps_per_arm': 363,
        'company_and_id_disjoint_splits': True,
        'executor_transformations_recomputed': True, 'all_800_per_example_scores_recomputed': True,
        'test_evaluated': False, 'audit_script_sha256': sha256(__file__)}
    write_json(run/'validation.json', validation)
    write_json(run/'summary.json', {'metrics': results, 'paired_raw': raw_delta,
        'paired_executor': exe_delta, 'train': trains, 'test_evaluated': False,
        'raw_outputs_changed': sum(r['raw_output_changed'] for r in outcomes)})
    lines = ['# FinDelta：训练标签修正的匹配对照实验', '',
        '两组均用相同 966 道训练题，从固定 Qwen3-0.6B 基座独立训练 3 轮；仅 11 条 completion 不同。', '',
        '| 方法 | 原始 verified | 执行器后 verified（预先指定主指标） |',
        '|---|---:|---:|']
    for arm, label in [('control', '旧标签匹配对照'), ('repaired', '修正标签')]:
        a, b = [results[arm+'_'+k]['verified_accuracy'] for k in ['raw', 'executor']]
        lines.append(f'| {label} | {a:.1%}（{round(a*200)}/200） | {b:.1%}（{round(b*200)}/200） |')
    for label, d in [('主指标', exe_delta), ('原始输出次指标', raw_delta)]:
        lines += ['', f"{label}变化 **{d['delta']*100:+.1f} 个百分点**；按年报分组的配对 bootstrap 95% 区间为 **[{d['ci95'][0]*100:+.1f}, {d['ci95'][1]*100:+.1f}]**。错转对 {d['transitions'].get('0->1', 0)} 题，对转错 {d['transitions'].get('1->0', 0)} 题。"]
    if exe_delta['ci95'][0] <= 0 <= exe_delta['ci95'][1]:
        lines += ['', '**本轮没有证据确认修正标签带来稳定的主指标提升。** 数据修正仍有审计价值，但不能写成模型性能显著提高。']
    elif exe_delta['delta'] < 0:
        lines += ['', '**本轮主指标下降。** 不能把修正标签等同于模型变好，需要进一步诊断并多 seed 复现。']
    else:
        lines += ['', '**本轮开发集主指标提高。** 仅一次 seed，仍需多 seed 和最终独立测试确认。']
    lines += ['', '## 实验与验证', '',
        '- 固定 seed 42、LoRA r8/alpha16/q_proj+v_proj、LR 1e-4、batch 1、累计 8、BF16；各 363 optimizer steps。两组共享同一提示词、解码设置及原始 200 题 dev。',
        '- 两组均从基座重新训练，不延续先前 SFT 或 DPO。保存模型、manifest、训练日志、逐题输出及评分，可独立复算。',
        '- 28 项测试通过；核对代码、数据和协议哈希；重新执行全部预测程序并复算 800 个逐题评分。',
        '- 七条修正涉及来源行绑定，四条改变数值答案。34 条存疑训练样本在两组中均被排除，因此本轮隔离标签修正效果，并未测量隔离样本本身的效果。',
        '- 先前 1,000 题 SFT + 执行器的 44.5% 只作历史参考，不能与本轮直接作单变量归因。', '',
        '## 资源', '', '| 组别 | 训练时间 | 峰值 allocated 显存 | 训练 loss（非质量指标） |', '|---|---:|---:|---:|']
    for arm, label in [('control', '旧标签'), ('repaired', '修正标签')]:
        t = trains[arm]
        lines.append(f"| {label} | {t['elapsed_seconds']/60:.1f} 分钟 | {t['peak_allocated_gib']:.2f} GiB | {t['metrics']['train_loss']:.4f} |")
    lines += ['', '## 解释边界及下一步', '',
        '这是自定义公司隔离 FinQA 开发集的探索性结果，不是官方榜单分数。执行器检查数值与证据绑定，不能证明年份、单位和实体语义均正确。开发集未重新标注；训练集仍有 918 条未经逐条语义审核。所有本轮修正为 AI 助手审核，并非独立人工真值。', '',
        '区间只反映年报样本不确定性，不含训练 seed 方差，也不消除多次使用开发集的选择偏差。测试集未预测。下一步应优先做多 seed 复现及针对错误类型的诊断，之后再冻结最终方案评测测试集。', '',
        '简历可以描述建立了有版本与来源追溯的数据修正、匹配对照训练及配对统计评估流程；模型提升须按以上实测结果和限制表述。', '']
    (run/'REPORT.zh.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps({'passed': True, 'primary': exe_delta, 'secondary': raw_delta}, ensure_ascii=False))


if __name__ == '__main__':
    main()
