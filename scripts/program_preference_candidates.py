"""Prepare pending train-only preferences for incorrect executable programs."""
import argparse
import csv
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from findelta.common import completion, messages, prompt_sha256, read_jsonl, sha256, write_json, write_jsonl
from findelta.verify import execute, parse_prediction, score


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--data', required=True)
    p.add_argument('--predictions', required=True)
    p.add_argument('--year-flags', required=True)
    p.add_argument('--out', required=True)
    a = p.parse_args()
    rows, preds = read_jsonl(a.data), read_jsonl(a.predictions)
    if not rows or any(r['split'] != 'train' for r in rows):
        raise ValueError('Only training rows may generate preference candidates')
    by_id = {r['id']:r for r in rows}
    if len(by_id) != len(rows) or len(preds) != len(rows) or {r['id'] for r in preds} != set(by_id):
        raise ValueError('Require exactly one prediction per training example')
    digest = sha256(a.data)
    flagged = {r['id'] for r in read_jsonl(a.year_flags)}
    out = Path(a.out)
    out.mkdir(exist_ok=False, parents=True)
    pairs, skipped = [], []
    for pred in preds:
        if pred['dataset_sha256'] != digest or pred['prompt_sha256'] != prompt_sha256():
            raise ValueError('Prediction provenance or prompt mismatch')
        row = by_id[pred['id']]
        scored = score(row, pred['output'])
        if not scored['execution_valid'] or scored['execution_correct'] or scored['abstained']:
            continue
        if row['id'] in flagged:
            skipped.append(row['id'])
            continue
        if not score(row, row['target'])['verified_correct']:
            raise ValueError('Chosen target failed verification')
        rejected = parse_prediction(pred['output'])
        value, _ = execute(rejected['steps'], row['evidence'])
        rejected = {**rejected, 'answer':value}
        # Equalize arithmetic consistency, so preferences focus on the predicted program.
        if score(row, rejected)['answer_correct']:
            raise ValueError('Rejected program unexpectedly matches target')
        pairs.append({'id':row['id'], 'split':'train', 'review_status':'pending',
            'source':'model_greedy_program_error_executor_normalized', 'dataset_sha256':digest,
            'prompt':messages(row), 'chosen':[{'role':'assistant','content':completion(row['target'])}],
            'rejected':[{'role':'assistant','content':completion(rejected)}],
            'raw_model_output':pred['output']})
    write_jsonl(out / 'candidates.jsonl', pairs)
    with (out / 'review.csv').open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id','source','decision','notes'])
        writer.writeheader()
        writer.writerows({'id':r['id'], 'source':r['source'], 'decision':'pending','notes':''} for r in pairs)
    manifest = {'count':len(pairs), 'human_reviewed':0, 'training_export_requires_review':True,
        'rule':'Valid but numerically incorrect predicted program; rejected answer normalized by execution; skip year-flagged inputs pending label review.',
        'data_sha256':digest, 'predictions_sha256':sha256(a.predictions),
        'prediction_manifest_sha256':sha256(a.predictions + '.manifest.json'),
        'year_flags_sha256':sha256(a.year_flags), 'skipped_pending_year_review':skipped,
        'generation':'Existing 3-epoch greedy train diagnostic; no new sampling or training',
        'caveat':'Verifier-labeled candidates, not human preferences. Correct arithmetic does not establish semantic correctness.'}
    write_json(out / 'manifest.json', manifest)
    lines = ['# 真实模型错误：DPO 偏好候选审核', '',
        f'共 {len(pairs)} 对，全部 pending。来自 3-epoch SFT 模型在 train 上的真实输出，不是人工反馈，尚未用于 DPO。', '',
        '## 你怎么审核', '',
        '先看前 5 对，每题核对：chosen 的公司、年份、指标、分母、单位是否正确；rejected 的程序是否确实错误。两边可能都合理、有标签疑点或无法判断时，不要批准。', '',
        '在 review.csv 中填写 decision=approve/reject，未看完保持 pending；notes 记录理由。只有 approve 才能由 export-dpo 导出。', '',
        'rejected 保留模型选出的程序，但 answer 已替换成该程序的真实执行值，因此比较针对选数/选运算；原始模型输出也保留供审计。自动年份疑点未加入候选，但其余样本不保证没有语义错误。', '',
        '这批是审核起点，不承诺其数量足够得到可靠 DPO 提升；先确认标签质量，再扩充训练集采样。', '']
    for i,r in enumerate(pairs,1):
        lines += [f"## {i}. {r['id']}", '', r['prompt'][-1]['content'], '', 'Chosen（参考标签，仍需核对）：',
                  '```json',r['chosen'][0]['content'],'```','', 'Rejected（模型错误程序，执行器重算 answer）：',
                  '```json',r['rejected'][0]['content'],'```','', '模型原始输出：','```json',r['raw_model_output'],'```','']
    (out / 'REVIEW.zh.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps(manifest, indent=2))


if __name__ == '__main__':
    main()
