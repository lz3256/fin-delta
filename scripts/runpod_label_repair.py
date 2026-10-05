"""Execute the predeclared, matched 966-row label-repair experiment."""
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    os.chdir(ROOT)
    os.environ.setdefault('HF_HOME', '/workspace/findelta-runtime/hf-cache')
    os.environ['TOKENIZERS_PARALLELISM'] = 'false'
    os.environ['HF_HUB_OFFLINE'] = '1'
    run = Path(args.out).resolve()
    cohort = ROOT / 'data/cohort/v2-reviewed'
    frozen = ROOT / 'reports/train-repair-v2/next-experiment.json'
    protocol = json.loads(frozen.read_text())
    assert protocol['status'] == 'PLANNED_NOT_STARTED'
    assert sha256(cohort / 'manifest.json') == protocol['cohort_manifest_sha256']
    assert prompt_sha256() == protocol['prompt_sha256']
    for filename, field in [('sft-control.jsonl', 'control_sft_sha256'),
                            ('sft.jsonl', 'repaired_sft_sha256'), ('dev.jsonl', 'dev_sha256')]:
        assert sha256(cohort / filename) == protocol[field], filename
    a, b = [read_jsonl(cohort / f) for f in ['sft-control.jsonl', 'sft.jsonl']]
    assert len(a) == len(b) == 966 == len({r['id'] for r in a})
    assert all(x['id'] == y['id'] and x['prompt'] == y['prompt'] and
               x['split'] == y['split'] == 'train' for x, y in zip(a, b))
    assert sum(x['completion'] != y['completion'] for x, y in zip(a, b)) == 11
    dev = read_jsonl(cohort / 'dev.jsonl')
    assert len(dev) == 200 and all(r['split'] == 'dev' for r in dev)
    assert not {r['id'] for r in a} & {r['id'] for r in dev}
    environment = doctor()
    assert environment['cuda_available'] and environment['bf16_supported']
    run.mkdir(parents=True, exist_ok=False)
    write_json(run / 'train-config.json', protocol['training_config'])
    write_json(run / 'inference-config.json', protocol['inference_config'])
    write_json(run / 'protocol.json', {**protocol, 'status': 'STARTED',
        'started_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'predeclared_protocol_sha256': sha256(frozen), 'environment': environment,
        'model_lock': json.loads((ROOT / 'model-lock.json').read_text()),
        'code_sha256': {str(p.relative_to(ROOT)): sha256(p) for p in sorted((ROOT/'findelta').glob('*.py'))},
        'runner_sha256': sha256(__file__),
        'executor_script_sha256': sha256(ROOT/'scripts/executor_ablation.py')})

    def command(stage, arguments):
        (run / 'status.txt').write_text(stage + '\n')
        print(stage, flush=True)
        with (run / f'{stage}.log').open('w') as log:
            subprocess.run([sys.executable, '-u', *map(str, arguments)],
                           stdout=log, stderr=subprocess.STDOUT, check=True)

    try:
        command('tests', ['-m', 'unittest', 'discover', '-s', 'tests', '-v'])
        # Independent processes reset seed/model/optimizer for each arm.
        for arm, filename in [('control', 'sft-control.jsonl'), ('repaired', 'sft.jsonl')]:
            folder = run / arm
            folder.mkdir()
            command(arm + '-train', ['-m', 'findelta', 'train', '--mode', 'sft',
                '--data', cohort/filename, '--config', run/'train-config.json', '--out', folder/'adapter'])
            command(arm + '-predict', ['-m', 'findelta', 'predict', '--data', cohort/'dev.jsonl',
                '--config', run/'inference-config.json', '--adapter', folder/'adapter',
                '--samples', '1', '--temperature', '0', '--out', folder/'dev.jsonl'])
            command(arm + '-evaluate', ['-m', 'findelta', 'evaluate', '--data', cohort/'dev.jsonl',
                '--predictions', folder/'dev.jsonl', '--out', folder/'raw-dev'])
            command(arm + '-executor', ['scripts/executor_ablation.py', '--data', cohort/'dev.jsonl',
                '--predictions', folder/'dev.jsonl', '--out', folder/'executor.jsonl'])
        for kind, name in [('sft-executor-dev', 'executor'), ('raw-dev', 'raw')]:
            command('compare-' + name, ['-m', 'findelta', 'compare',
                '--run', f'control={run}/control/{kind}', '--run', f'repaired={run}/repaired/{kind}',
                '--out', run/f'comparison-{name}.md'])
        (run / 'status.txt').write_text('COMPLETE\n')
        print('COMPLETE', flush=True)
    except BaseException:
        (run / 'status.txt').write_text('FAILED\n')
        raise


if __name__ == '__main__':
    main()
