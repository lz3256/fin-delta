"""Audit four new jobs plus the untouched pilot; summarize seeds without pooling questions."""
import argparse
import collections
import json
import math
from pathlib import Path
import statistics
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT/'scripts'))
from findelta.common import prompt_sha256, read_jsonl, sha256, write_json, write_jsonl
from findelta.verify import execute, parse_prediction, score
from summarize_label_repair import paired


def distribution(values):
    return {'n_seeds': len(values), 'mean': statistics.mean(values),
            'sample_sd': statistics.stdev(values), 'min': min(values), 'max': max(values)}


def audit_pair(folder, seed, plan, environment, dev):
    j = lambda p: json.loads(p.read_text())
    metrics, per_example, resources, raw_outputs, diagnostics = {}, {}, {}, {}, {}
    for arm, key in [('control', 'control_sft_sha256'), ('repaired', 'repaired_sft_sha256')]:
        path = folder/arm
        train = j(path/'adapter/run_manifest.json')
        state = j(path/'adapter/trainer_state.json')
        assert train['mode'] == 'sft' and train['examples'] == 966
        assert train['config'] == {**plan['fixed_training_config_except_seed'], 'seed': seed}
        assert train['data_sha256'] == plan[key]
        assert train['prompt_sha256'] == plan['prompt_sha256']
        assert train['environment'] == environment
        assert train['actual_max_steps'] == -1 and train['metrics']['epoch'] == 3.0
        assert state['global_step'] == 363 and train['trainable_tensors_changed'] == 112
        assert math.isfinite(train['metrics']['train_loss'])
        assert 'sft_run_manifest_sha256' not in train
        meta = j(path/'dev.jsonl.manifest.json')
        assert meta['config'] == {**plan['inference_config'], **j(ROOT/'model-lock.json')}
        assert meta['environment'] == environment
        assert meta['samples'] == 1 and meta['temperature'] == 0
        assert meta['prompt_sha256'] == plan['prompt_sha256']
        assert meta['dataset_sha256'] == plan['dev_sha256']
        assert meta['predictions_sha256'] == sha256(path/'dev.jsonl')
        assert meta['adapter_manifest_sha256'] == sha256(path/'adapter/run_manifest.json')
        raw_rows, derived_rows = read_jsonl(path/'dev.jsonl'), read_jsonl(path/'executor.jsonl')
        raw, derived = [{r['id']: r for r in rows} for rows in [raw_rows, derived_rows]]
        assert len(raw_rows) == len(derived_rows) == len(raw) == len(derived) == 200
        assert set(raw) == set(derived) == set(dev)
        raw_outputs[arm] = raw
        for uid, pred in raw.items():
            try:
                answer = parse_prediction(pred['output'])
                if not answer['abstain']:
                    value, _ = execute(answer['steps'], dev[uid]['evidence'])
                    answer = {**answer, 'answer': value}
            except (ValueError, TypeError, KeyError, ArithmeticError, RecursionError):
                answer = {'abstain': True, 'steps': [], 'answer': None}
            assert json.loads(derived[uid]['output']) == answer
            assert derived[uid]['parent_predictions_sha256'] == sha256(path/'dev.jsonl')
        for kind, dirname, predfile in [('raw', 'raw-dev', 'dev.jsonl'),
                                        ('executor', 'sft-executor-dev', 'executor.jsonl')]:
            result = j(path/dirname/'metrics.json')
            rows = read_jsonl(path/dirname/'per_example.jsonl')
            per = {r['id']: r for r in rows}
            assert len(rows) == len(per) == 200 and set(per) == set(dev)
            assert result['predictions_sha256'] == sha256(path/predfile)
            assert result['dataset_sha256'] == plan['dev_sha256']
            assert result['prompt_sha256'] == plan['prompt_sha256']
            assert result['n'] == 200 and result['missing_predictions'] == 0
            for pred in read_jsonl(path/predfile):
                assert pred['dataset_sha256'] == plan['dev_sha256']
                assert pred['prompt_sha256'] == plan['prompt_sha256']
                computed = score(dev[pred['id']], pred['output'])
                assert all(computed[k] == per[pred['id']][k] for k in computed)
            assert result['verified_accuracy'] == sum(r['verified_correct'] for r in rows) / 200
            metrics[arm+'_'+kind], per_example[arm+'_'+kind] = result, per
            if kind == 'raw':
                categories = collections.Counter()
                for row in rows:
                    if row['verified_correct']:
                        category = 'verified_correct'
                    elif row['abstained']:
                        category = 'model_abstained'
                    elif not row['execution_valid']:
                        category = 'invalid_schema_or_program'
                    elif row['execution_correct']:
                        category = 'correct_program_wrong_answer'
                    else:
                        category = 'executable_wrong_result'
                    categories[category] += 1
                assert sum(categories.values()) == 200
                diagnostics[arm] = dict(categories)
        resources[arm] = {k: train[k] for k in ['elapsed_seconds', 'peak_allocated_gib', 'peak_reserved_gib', 'metrics']}
    assert sha256(folder/'control/adapter/adapter_model.safetensors') != sha256(folder/'repaired/adapter/adapter_model.safetensors')
    result = {'seed': seed, 'metrics': metrics, 'resources': resources, 'diagnostics': diagnostics,
              'paired': {kind: paired(per_example['control_'+kind], per_example['repaired_'+kind])
                         for kind in ['raw', 'executor']},
              'raw_outputs_changed': sum(raw_outputs['control'][uid]['output'] != raw_outputs['repaired'][uid]['output'] for uid in dev)}
    outcomes = [{'seed': seed, 'id': uid, 'report_id': row['report_id'],
                 **{k: v[uid]['verified_correct'] for k, v in per_example.items()}} for uid, row in dev.items()]
    return result, outcomes


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--run', required=True)
    args = p.parse_args()
    run = Path(args.run).resolve()
    j = lambda p: json.loads(p.read_text())
    assert (run/'status.txt').read_text().strip() == 'COMPLETE'
    frozen = ROOT/'reports/label-repair-multiseed-v1-plan/protocol.json'
    plan, actual = j(frozen), j(run/'protocol.json')
    assert actual['predeclared_protocol_sha256'] == sha256(frozen)
    assert all(actual[k] == v for k, v in plan.items() if k != 'status')
    assert plan['prompt_sha256'] == prompt_sha256()
    for filename, digest in actual['code_sha256'].items():
        assert sha256(ROOT/filename) == digest
    assert actual['runner_sha256'] == sha256(ROOT/'scripts/runpod_label_multiseed.py')
    assert actual['executor_script_sha256'] == sha256(ROOT/'scripts/executor_ablation.py')
    cohort = ROOT/'data/cohort/v2-reviewed'
    for filename, key in [('manifest.json', 'cohort_manifest_sha256'), ('dev.jsonl', 'dev_sha256'),
                          ('sft-control.jsonl', 'control_sft_sha256'), ('sft.jsonl', 'repaired_sft_sha256')]:
        assert sha256(cohort/filename) == plan[key]
    control, repaired = [read_jsonl(cohort/f) for f in ['sft-control.jsonl', 'sft.jsonl']]
    assert len(control) == len(repaired) == 966
    assert all(a['id'] == b['id'] and a['prompt'] == b['prompt'] for a, b in zip(control, repaired))
    assert sum(a['completion'] != b['completion'] for a, b in zip(control, repaired)) == 11
    splits = {s: read_jsonl(cohort/f'{s}.jsonl') for s in ['train', 'dev', 'test']}
    for a, b in [('train', 'dev'), ('train', 'test'), ('dev', 'test')]:
        for key in ['id', 'company']:
            assert not {r[key] for r in splits[a]} & {r[key] for r in splits[b]}
    dev = {r['id']: r for r in splits['dev']}
    prior = ROOT/plan['prior_seed42']['report']
    for filename in ['protocol', 'summary', 'validation']:
        assert sha256(prior/f'{filename}.json') == plan['prior_seed42'][filename+'_sha256']
    assert (prior/'status.txt').read_text().strip() == 'COMPLETE'
    old_protocol = j(prior/'protocol.json')
    assert old_protocol['code_sha256'] == actual['code_sha256']
    assert old_protocol['environment'] == actual['environment']
    assert old_protocol['executor_script_sha256'] == actual['executor_script_sha256']
    tests = (run/'tests.log').read_text()
    assert 'Ran 28 tests' in tests and tests.rstrip().endswith('OK')
    results, outcomes, artifacts = {}, [], {}
    for seed in plan['all_training_seeds']:
        folder = prior if seed == 42 else run/f'seed-{seed}'
        result, rows = audit_pair(folder, seed, plan, actual['environment'], dev)
        results[str(seed)] = result
        outcomes.extend(rows)
        for arm in ['control', 'repaired']:
            artifacts[f'{seed}/{arm}'] = {str(path): sha256(folder/arm/path) for path in [
                Path('adapter/adapter_model.safetensors'), Path('adapter/adapter_config.json'),
                Path('adapter/run_manifest.json'), Path('dev.jsonl'), Path('executor.jsonl')]}
    assert len({v['adapter/adapter_model.safetensors'] for v in artifacts.values()}) == 6
    aggregate = {}
    for label, seeds in [('new_replications_only', plan['new_training_seeds']), ('all_three_descriptive', plan['all_training_seeds'])]:
        aggregate[label] = {'seeds': seeds, 'n_unique_questions': len(dev), 'metrics': {}, 'paired_deltas': {}}
        for arm in ['control', 'repaired']:
            for kind in ['raw', 'executor']:
                key = arm+'_'+kind
                aggregate[label]['metrics'][key] = distribution([results[str(s)]['metrics'][key]['verified_accuracy'] for s in seeds])
        for kind in ['raw', 'executor']:
            aggregate[label]['paired_deltas'][kind] = distribution([results[str(s)]['paired'][kind]['delta'] for s in seeds])
    write_jsonl(run/'paired-outcomes-all-seeds.jsonl', outcomes)
    write_json(run/'artifact-sha256.json', artifacts)
    summary = {'seeds': results, 'aggregate': aggregate, 'test_evaluated': False,
               'seed42_previously_observed': True, 'no_best_seed_selection': True}
    write_json(run/'summary.json', summary)
    validation = {'passed': True, 'tests_passed': 28, 'new_training_jobs': 4, 'total_audited_models': 6,
        'new_seeds': [17, 123], 'paired_training_steps_per_job': 363,
        'all_2400_per_example_scores_recomputed': True, 'all_1200_executor_transformations_recomputed': True,
        'same_966_ids_order_prompts': True, 'changed_completions': 11,
        'six_distinct_adapter_checkpoints': True,
        'company_and_id_disjoint_splits': True, 'same_code_environment_and_inference_config': True,
        'prior_seed42_artifact_hashes_unchanged': True, 'new_seed_choice_and_analysis_frozen_before_execution': True,
        'unique_dev_questions': 200, 'test_evaluated': False, 'audit_script_sha256': sha256(__file__),
        'artifact_inventory_sha256': sha256(run/'artifact-sha256.json')}
    write_json(run/'validation.json', validation)
    lines = ['# FinDelta：标签修正的多随机种子复现', '',
        '在先前 seed 42 之后，预先固定新增 seed 17、123；每个 seed 分别训练旧标签与修正版，共四次新增 GPU 训练。三次均使用相同 966 道训练题和 200 道开发题。', '',
        '| 训练 seed | 原始：旧标签 → 修正版 | 执行器后：旧标签 → 修正版 | 主指标配对变化（百分点） | 95% 报告分组区间 |',
        '|---|---:|---:|---:|---:|']
    for seed in plan['all_training_seeds']:
        r = results[str(seed)]; m = r['metrics']; d = r['paired']['executor']
        label = f'{seed}（先前已观察）' if seed == 42 else f'{seed}（新增）'
        lines.append(f"| {label} | {m['control_raw']['verified_accuracy']:.1%} → {m['repaired_raw']['verified_accuracy']:.1%} | {m['control_executor']['verified_accuracy']:.1%} → {m['repaired_executor']['verified_accuracy']:.1%} | {d['delta']*100:+.1f} | [{d['ci95'][0]*100:+.1f}, {d['ci95'][1]*100:+.1f}] |")
    lines += ['', '## 预先指定的复现汇总', '']
    for label, title in [('new_replications_only', '仅两个新增种子'), ('all_three_descriptive', '三种子描述性汇总（包含已观察 seed 42）')]:
        r = aggregate[label]; a = r['metrics']['control_executor']; b = r['metrics']['repaired_executor']; d = r['paired_deltas']['executor']
        lines += [f"**{title}：** 主指标平均 {a['mean']:.2%} → {b['mean']:.2%}，平均配对变化 {d['mean']*100:+.2f} 个百分点；种子间配对变化的样本标准差 {d['sample_sd']*100:.2f} 个百分点，范围 [{d['min']*100:+.1f}, {d['max']*100:+.1f}]。", '']
    deltas = [results[str(seed)]['paired']['executor']['delta'] for seed in plan['new_training_seeds']]
    if min(deltas) > 0:
        conclusion = '两个新增种子的主指标均向上，方向一致；但仅两个新增种子、同一有噪声开发集，不能据此确认广泛、稳定的泛化收益。'
    elif max(deltas) < 0:
        conclusion = '两个新增种子的主指标均下降，先前的微小正向变化未能复现。不能宣称标签修正提高了模型性能。'
    elif min(deltas) < 0 < max(deltas):
        conclusion = '新增种子的变化方向不一致，未确认标签修正带来稳定提升。'
    else:
        conclusion = '新增复现出现持平或小幅变化；结合种子数量有限，目前仍不足以确认标签修正带来稳定收益。'
    if all(results[str(seed)]['paired']['executor']['ci95'][0] <= 0 <=
           results[str(seed)]['paired']['executor']['ci95'][1] for seed in plan['all_training_seeds']):
        conclusion += '各 seed 的配对报告分组区间均覆盖 0。'
    lines += [f'**{conclusion}**', '',
        '每行区间只描述该 seed 下按年报抽样的不确定性，不包括训练 seed 方差。上面的标准差是不同种子配对差值的离散程度，不是均值的标准误或置信区间。仅三次训练随机性样本，不给出高精度的 seed 总体推断。沿用原训练配方，未启用 full_determinism，因此 GPU 数值非确定性也可能贡献运行间差异，不能把全部波动严格归因于 seed。', '',
        '## 实验控制及审计', '',
        '- Qwen3-0.6B 固定 revision；相同 LoRA r8/alpha16/q_proj+v_proj、LR 1e-4、batch 1、累计 8、BF16、3 epochs、363 optimizer steps。每次独立从基座加载。',
        '- 新增训练 seed 17、123；推理 seed 始终 42，greedy、batch 8、最多 640 新 token。不改变数据、提示词、解码或评分。',
        '- 运行顺序事前固定：17 旧标签、17 修正版、123 修正版、123 旧标签。看到中途分数后未补选种子或调参。',
        '- 28 项测试通过；全部六个模型的数据与配置来源核对一致。复算 1,200 次执行器变换及 2,400 个逐题评分，先前 seed 42 文件哈希不变。',
        '- 三个 seed 反复使用同一批 200 道题，不能当作 600 道独立测试题；没有池化二项式区间、投票集成或挑选最高分模型。', '',
        '## 资源', '', '| Seed / 组别 | 训练分钟 | 峰值 allocated GiB |', '|---|---:|---:|']
    for seed in plan['all_training_seeds']:
        for arm in ['control', 'repaired']:
            r = results[str(seed)]['resources'][arm]
            lines.append(f"| {seed} / {arm} | {r['elapsed_seconds']/60:.1f} | {r['peak_allocated_gib']:.2f} |")
    lines += ['', '## 描述性错误诊断（不用于选 seed）', '',
        '| Seed / 组别 | 原始 verified | 程序结果对但 answer 不对 | 可执行但结果错 | 非法格式或程序 | 模型拒答 |',
        '|---|---:|---:|---:|---:|---:|']
    for seed in plan['all_training_seeds']:
        for arm in ['control', 'repaired']:
            d = results[str(seed)]['diagnostics'][arm]
            values = [d.get(k, 0) for k in ['verified_correct', 'correct_program_wrong_answer',
                'executable_wrong_result', 'invalid_schema_or_program', 'model_abstained']]
            lines.append(f"| {seed} / {arm} | " + ' | '.join(map(str, values)) + ' |')
    lines += ['', '这是评估流程中的错误分型，不是逐题金融语义审核。“程序结果对”仅表示执行值与既有参考答案一致。该附加诊断不改变预先指定的主指标或训练方案。', '',
        '## 解释边界与下一步', '',
        '本项目指标是自定义公司隔离 FinQA cohort 上的受限算术与数字来源核对，不是官方 FinQA 分数，也不是完整金融事实性证明。AI 助手修正了 11 条训练目标、隔离 34 条；仍有 918 条训练记录未经逐题语义审核。开发集标签未重新审核。', '',
        '新增复现是在观察 seed 42 后规划的，仍属于开发阶段。测试集未生成预测。数据修正的审计价值与模型提分是两件不同的事，当前结论只涉及这 11 条修正、这一模型和训练配方。', '',
        '下一步应把失败程序按年份、单位、证据选择和运算分型，扩充经独立复核的数据，提出新的受控改进，再冻结最终方案评估测试集。不能通过继续补 seed 或选最高分把当前结果包装成稳定收益。', '',
        '简历可如实描述：构建有来源追溯的数据修正流程，开展三个随机种子的匹配 SFT 对照，使用配对年报分组评估并量化训练随机性；性能数字应同时标明执行器、自定义开发集和结果限制。', '']
    (run/'REPORT.zh.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps({'passed': True, 'aggregate': aggregate, 'conclusion': conclusion}, ensure_ascii=False))


if __name__ == '__main__':
    main()
