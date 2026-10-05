"""Four fixed GPU jobs; training seed is the only change from the matched pilot."""
import argparse
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from findelta.common import prompt_sha256, read_jsonl, sha256, write_json
from findelta.modeling import doctor


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--out', required=True)
    a = p.parse_args()
    os.chdir(ROOT)
    os.environ.setdefault('HF_HOME', '/workspace/findelta-runtime/hf-cache')
    os.environ.update(TOKENIZERS_PARALLELISM='false', HF_HUB_OFFLINE='1')
    frozen = ROOT/'reports/label-repair-multiseed-v1-plan/protocol.json'
    plan = json.loads(frozen.read_text())
    cohort = ROOT/'data/cohort/v2-reviewed'
    assert plan['new_training_seeds'] == [17, 123]
    assert plan['run_order'] == [[17, 'control'], [17, 'repaired'], [123, 'repaired'], [123, 'control']]
    assert prompt_sha256() == plan['prompt_sha256']
    assert sha256(cohort/'manifest.json') == plan['cohort_manifest_sha256']
    for filename, key in [('sft-control.jsonl', 'control_sft_sha256'), ('sft.jsonl', 'repaired_sft_sha256'), ('dev.jsonl', 'dev_sha256')]:
        assert sha256(cohort/filename) == plan[key]
    control, repaired = [read_jsonl(cohort/f) for f in ['sft-control.jsonl', 'sft.jsonl']]
    assert len(control) == len(repaired) == 966
    assert all(x['id'] == y['id'] and x['prompt'] == y['prompt'] and
               x['split'] == y['split'] == 'train' for x, y in zip(control, repaired))
    assert sum(x['completion'] != y['completion'] for x, y in zip(control, repaired)) == 11
    env = doctor()
    assert env['cuda_available'] and env['bf16_supported']
    run = Path(a.out).resolve()
    run.mkdir(parents=True, exist_ok=False)
    write_json(run/'protocol.json', {**plan, 'status': 'STARTED',
        'started_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'predeclared_protocol_sha256': sha256(frozen), 'environment': env,
        'model_lock': json.loads((ROOT/'model-lock.json').read_text()),
        'code_sha256': {str(p.relative_to(ROOT)): sha256(p) for p in sorted((ROOT/'findelta').glob('*.py'))},
        'runner_sha256': sha256(__file__), 'executor_script_sha256': sha256(ROOT/'scripts/executor_ablation.py')})
    write_json(run/'inference-config.json', plan['inference_config'])

    def command(stage, args):
        (run/'status.txt').write_text(stage+'\n')
        print(stage, flush=True)
        with (run/f'{stage}.log').open('w') as log:
            subprocess.run([sys.executable, '-u', *map(str, args)], stdout=log, stderr=subprocess.STDOUT, check=True)

    try:
        command('tests', ['-m', 'unittest', 'discover', '-s', 'tests', '-v'])
        for seed in plan['new_training_seeds']:
            folder = run/f'seed-{seed}'
            folder.mkdir()
            write_json(folder/'train-config.json', {**plan['fixed_training_config_except_seed'], 'seed': seed})
        for seed, arm in plan['run_order']:
            folder = run/f'seed-{seed}'/arm
            folder.mkdir()
            stage = f'seed-{seed}-{arm}'
            filename = 'sft-control.jsonl' if arm == 'control' else 'sft.jsonl'
            command(stage+'-train', ['-m', 'findelta', 'train', '--mode', 'sft', '--data', cohort/filename,
                '--config', folder.parent/'train-config.json', '--out', folder/'adapter'])
            command(stage+'-predict', ['-m', 'findelta', 'predict', '--data', cohort/'dev.jsonl',
                '--config', run/'inference-config.json', '--adapter', folder/'adapter',
                '--samples', '1', '--temperature', '0', '--out', folder/'dev.jsonl'])
            command(stage+'-evaluate', ['-m', 'findelta', 'evaluate', '--data', cohort/'dev.jsonl',
                '--predictions', folder/'dev.jsonl', '--out', folder/'raw-dev'])
            command(stage+'-executor', ['scripts/executor_ablation.py', '--data', cohort/'dev.jsonl',
                '--predictions', folder/'dev.jsonl', '--out', folder/'executor.jsonl'])
        for seed in plan['new_training_seeds']:
            folder = run/f'seed-{seed}'
            for kind, name in [('sft-executor-dev', 'executor'), ('raw-dev', 'raw')]:
                command(f'seed-{seed}-compare-{name}', ['-m', 'findelta', 'compare',
                    '--run', f'control={folder}/control/{kind}', '--run', f'repaired={folder}/repaired/{kind}',
                    '--out', folder/f'comparison-{name}.md'])
        (run/'status.txt').write_text('COMPLETE\n')
        print('COMPLETE', flush=True)
    except BaseException:
        (run/'status.txt').write_text('FAILED\n')
        raise


if __name__ == '__main__':
    main()
