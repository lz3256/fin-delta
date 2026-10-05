"""Frozen, single-variable SFT duration comparison; never evaluates test."""
import json
import os
from pathlib import Path
import random
import subprocess
import sys

ROOT = Path('/workspace/fin-delta')
sys.path.insert(0, str(ROOT))
from findelta.common import prompt_sha256, read_jsonl, sha256, write_json, write_jsonl


def main():
    os.chdir(ROOT)
    os.environ['HF_HOME'] = '/workspace/findelta-runtime/hf-cache'
    os.environ['TOKENIZERS_PARALLELISM'] = 'false'
    old = Path('/workspace/findelta-runs/week1-v3')
    run = Path('/workspace/findelta-runs/week1-duration-v1')
    run.mkdir(exist_ok=False)
    config = json.loads((old / 'config.json').read_text())
    longer = {**config, 'epochs': 3}
    write_json(run / 'inference-config.json', config)
    write_json(run / 'train-config.json', longer)
    train = read_jsonl('data/cohort/v1/train.jsonl')
    assert len(train) == 1000 and all(r['split'] == 'train' for r in train)
    subset = random.Random(20260924).sample(sorted(train, key=lambda r:r['id']), 64)
    write_jsonl(run / 'train-probe64.jsonl', subset)
    prior = json.loads((old / 'protocol.json').read_text())
    assert prior['prompt_sha256'] == prompt_sha256()
    for split in ['train', 'dev']:
        assert sha256(f'data/cohort/v1/{split}.jsonl') == prior['data_sha256'][split]
    assert sha256('data/cohort/v1/sft-prompt-v3.jsonl') == prior['sft_data_sha256']
    write_json(run / 'protocol.json', {
        'purpose': 'Exploratory duration ablation: 1 vs 3 SFT epochs from the same base',
        'primary_endpoint': 'raw model verified accuracy on frozen 200-question dev',
        'secondary_endpoint': 'execution-correct rate and existing deterministic executor dev ablation',
        'diagnostic': '64 training rows sampled before observing their predictions; in-sample, not generalization',
        'train_probe_selection_seed': 20260924,
        'train_probe_sha256': sha256(run / 'train-probe64.jsonl'),
        'base_run': str(old), 'old_training_manifest_sha256': sha256(old / 'sft-full/run_manifest.json'),
        'changed_training_config': {'epochs': [1, 3]},
        'schedule_caveat': 'Same warmup ratio and default linear schedule are recomputed for 375 rather than 125 steps. This is a duration-recipe comparison, not an identical first-epoch prefix.',
        'initialization': 'base model, never continue the 1-epoch adapter',
        'inference_config_note': 'Identical config reused for inference; its epochs field is unused during inference.',
        'prompt_sha256': prompt_sha256(), 'data_sha256': prior['data_sha256'],
        'sft_data_sha256': prior['sft_data_sha256'], 'model_lock': prior['model_lock'],
        'test_evaluation': False, 'training_seed': 42,
        'code_sha256': {str(p): sha256(p) for p in sorted(Path('findelta').glob('*.py'))},
        'runner_sha256': sha256(__file__),
    })

    def command(stage, args):
        (run / 'status.txt').write_text(stage + '\n')
        print(stage, flush=True)
        with (run / f'{stage}.log').open('w') as log:
            subprocess.run([sys.executable, '-u', *map(str, args)], stdout=log, stderr=subprocess.STDOUT, check=True)

    def prediction(name, data, adapter):
        command(name, ['-m', 'findelta', 'predict', '--data', data, '--config', run / 'inference-config.json', '--adapter', adapter, '--out', run / f'{name}.jsonl'])
        command(name + '-eval', ['-m', 'findelta', 'evaluate', '--data', data, '--predictions', run / f'{name}.jsonl', '--out', run / name])

    try:
        prediction('sft1-train64', run / 'train-probe64.jsonl', old / 'sft-full')
        command('sft3-train', ['-m', 'findelta', 'train', '--mode', 'sft', '--data', 'data/cohort/v1/sft-prompt-v3.jsonl', '--config', run / 'train-config.json', '--out', run / 'sft3-adapter'])
        prediction('sft3-train64', run / 'train-probe64.jsonl', run / 'sft3-adapter')
        prediction('sft3-dev', 'data/cohort/v1/dev.jsonl', run / 'sft3-adapter')
        command('executor-dev', ['scripts/executor_ablation.py', '--data', 'data/cohort/v1/dev.jsonl', '--predictions', run / 'sft3-dev.jsonl', '--out', run / 'sft3-executor.jsonl'])
        command('compare-raw', ['-m', 'findelta', 'compare', '--run', f'SFT-1epoch={old}/sft-dev', '--run', f'SFT-3epochs={run}/sft3-dev', '--out', run / 'comparison-raw.md'])
        command('compare-executor', ['-m', 'findelta', 'compare', '--run', f'SFT-1epoch+executor={old}/sft-executor-dev', '--run', f'SFT-3epochs+executor={run}/sft-executor-dev', '--out', run / 'comparison-executor.md'])
        (run / 'status.txt').write_text('COMPLETE\n')
        print('COMPLETE', flush=True)
    except BaseException:
        (run / 'status.txt').write_text('FAILED\n')
        raise


if __name__ == '__main__':
    main()
