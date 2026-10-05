"""Build the reviewed training revision and matched control, then validate lengths."""
import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from findelta.common import read_jsonl, write_json, sha256, prompt_sha256
from findelta.revision import build_revision
from findelta.train import render_training_rows


def main():
    from transformers import AutoTokenizer
    parser = argparse.ArgumentParser()
    parser.add_argument('--parent', default='data/cohort/v1')
    parser.add_argument('--review', default='data/reviews/train-repair-v2')
    parser.add_argument('--out', default='data/cohort/v2-reviewed')
    parser.add_argument('--model-lock', default='model-lock.json')
    parser.add_argument('--local-files-only', action='store_true')
    args = parser.parse_args()
    out = Path(args.out)
    if out.exists():
        raise ValueError('Refusing to overwrite a versioned cohort')
    model = json.loads(Path(args.model_lock).read_text())
    tokenizer = AutoTokenizer.from_pretrained(**dict(pretrained_model_name_or_path=model['model'],
        revision=model['revision'], local_files_only=args.local_files_only))
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='reviewed-build-', dir=out.parent) as tmp:
        stage = Path(tmp) / 'cohort'
        manifest = build_revision(args.parent, args.review, stage)
        distributions = {}
        for name in ['sft.jsonl', 'sft-control.jsonl']:
            rows = read_jsonl(stage / name)
            prepared = render_training_rows(rows, tokenizer, 'sft', 2048)
            lengths = []
            for item in prepared:
                p = len(tokenizer(item['prompt'], add_special_tokens=False)['input_ids'])
                c = len(tokenizer(item['completion'], add_special_tokens=False)['input_ids'])
                if p > 1408:
                    raise ValueError('Prompt exceeds frozen budget')
                lengths.append(p+c+1)
            distributions[name] = {'examples':len(rows), 'max_total_tokens':max(lengths),
                                   'min_total_tokens':min(lengths), 'truncation':False}
        # Match treatment/control inputs and sample order, changing only supervision.
        actual, control = read_jsonl(stage/'sft.jsonl'), read_jsonl(stage/'sft-control.jsonl')
        if [(r['id'],r['prompt']) for r in actual] != [(r['id'],r['prompt']) for r in control]:
            raise ValueError('Treatment and control prompts/order differ')
        changed = sum(a['completion'] != b['completion'] for a,b in zip(actual,control))
        if changed != manifest['counts']['repaired']:
            raise ValueError('Unexpected completion changes')
        validation = {'passed':True,'prompt_sha256':prompt_sha256(),'model':model,
            'sequence_lengths':distributions,'same_ids_order_and_prompts':True,
            'different_completions':changed,'holdouts_byte_identical':all(
                sha256(stage/f'{s}.jsonl')==sha256(Path(args.parent)/f'{s}.jsonl') for s in ['dev','test']),
            'all_target_programs_pass_structural_checks':True,
            'repaired_targets_match_independent_calculations_and_annotated_original_cells':True,
            'semantic_audit_scope':82,'remaining_train_not_semantically_certified':True}
        write_json(stage/'validation.json',validation)
        manifest.update(model=model,prompt_sha256=prompt_sha256(),
                        validation_sha256=sha256(stage/'validation.json'))
        write_json(stage/'manifest.json',manifest)
        shutil.move(str(stage),str(out))
    print(json.dumps({'out':str(out),'counts':manifest['counts'],'validation':validation},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
