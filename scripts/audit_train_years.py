"""Flag absent question years for review, without editing labels or filtering metrics."""
import argparse
import csv
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from findelta.common import read_jsonl, sha256, write_json, write_jsonl

YEAR = re.compile(r'\b(?:19|20)\d{2}\b')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--data', required=True)
    p.add_argument('--out', required=True)
    a = p.parse_args()
    rows = read_jsonl(a.data)
    if not rows or any(r['split'] != 'train' for r in rows):
        raise ValueError('This audit is restricted to nonempty training data')
    out = Path(a.out)
    out.mkdir(exist_ok=False, parents=True)
    flagged = []
    for row in rows:
        asked = set(YEAR.findall(row['question']))
        present = set(YEAR.findall('\n'.join(row['evidence'].values())))
        missing = asked - present
        if missing:
            flagged.append({'id': row['id'], 'question': row['question'], 'question_years': sorted(asked),
                            'evidence_year_like_numbers': sorted(present), 'absent_years': sorted(missing),
                            'status': 'pending_review', 'target': row['target'], 'evidence': row['evidence']})
    write_jsonl(out / 'flags.jsonl', flagged)
    write_json(out / 'manifest.json', {'training_rows': len(rows), 'flags': len(flagged), 'data_sha256': sha256(a.data),
        'rule': YEAR.pattern, 'automatic_label_changes': 0, 'excluded_training_rows': 0,
        'human_reviewed': 0, 'test_or_dev_scanned': False,
        'limitation': 'Year-like numerals are only a heuristic: monetary values can match years, relative dates may be valid, and a present year does not prove correct operand selection. Two-digit dates and concatenated date headers can also cause false positives.'})
    with (out / 'review.csv').open('w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=['id', 'decision', 'notes'])
        w.writeheader()
        w.writerows({'id':r['id'], 'decision':'pending', 'notes':''} for r in flagged)
    lines = ['# 训练标签年份疑点', '',
             '自动规则只筛出“问题中的独立四位年份未出现在输入证据里”的样本，不自动判错、改标签或删数据。人工复核前全部保持 pending。', '',
             '请检查：年份是否真的缺失？是否为相对期间或非年份数字？参考程序实际使用哪一年？若确有问题，请在 review.csv 中记录；将来创建新的数据版本时再处理。', '',
             f'共 {len(rows)} 道训练题，发现 {len(flagged)} 条候选疑点；没有扫描 dev/test。', '']
    for r in flagged:
        lines += [f"## {r['id']}", '', r['question'], '', f"未出现的年份：{', '.join(r['absent_years'])}", '',
                  '参考程序：', '```json', json.dumps(r['target'], ensure_ascii=False, indent=2), '```', '', '完整输入证据：', '']
        lines += [f'- **{k}**：{v}' for k,v in r['evidence'].items()]
        lines.append('')
    (out / 'REVIEW.zh.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps({'rows':len(rows), 'flagged':len(flagged), 'ids':[r['id'] for r in flagged]}, indent=2))


if __name__ == '__main__':
    main()
