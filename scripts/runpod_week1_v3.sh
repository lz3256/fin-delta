#!/usr/bin/env bash
# One exploratory SFT run; dev only. Never touches the held-out test split.
set -euo pipefail
cd /workspace/fin-delta
export HF_HOME=/workspace/findelta-runtime/hf-cache
export TOKENIZERS_PARALLELISM=false
export PYTHONUNBUFFERED=1
PY=/workspace/findelta-runtime/venv/bin/python
RUN=/workspace/findelta-runs/week1-v3
mkdir -p "$RUN"
for item in sft-full base-dev-predictions.jsonl sft-dev-predictions.jsonl protocol.json; do
    if [ -e "$RUN/$item" ]; then
        echo "Refusing to overwrite existing experiment: $RUN/$item" >&2
        exit 1
    fi
done
trap 'echo FAILED > "$RUN/status.txt"' ERR
"$PY" - <<'PY'
import json, hashlib, shutil
from pathlib import Path
from findelta.common import SYSTEM, prompt_sha256, sha256, write_json
root = Path('/workspace/findelta-runs/week1-v3')
config = json.loads(Path('configs/4070-sft.json').read_text())
config['inference_batch_size'] = 8
write_json(root/'config.json', config)
write_json(root/'protocol.json', {
    'purpose': 'Single-seed exploratory base vs SFT comparison on frozen custom dev cohort',
    'training_examples': 1000, 'epochs': 1, 'seed': 42,
    'sft_initialization': 'base model, not the 10-step smoke adapter',
    'dev_examples': 200, 'test_evaluation': False,
    'prompt_sha256': prompt_sha256(), 'system_prompt': SYSTEM,
    'model_lock': json.loads(Path('model-lock.json').read_text()),
    'data_sha256': {split: sha256(f'data/cohort/v1/{split}.jsonl') for split in ['train','dev']},
    'sft_data_sha256': sha256('data/cohort/v1/sft-prompt-v3.jsonl'),
    'code_sha256': {str(p): sha256(p) for p in sorted(Path('findelta').glob('*.py'))},
    'decoding': {'batch_size': 8, 'samples': 1, 'temperature': 0, 'max_new_tokens': 640},
    'caveats': ['Custom filtered FinQA cohort, not official leaderboard scores',
                'Known source percentage-scale and operand-binding ambiguities',
                'No claim of semantic entailment or multi-seed robustness',
                'Old Colab and prompt-v2 results are diagnostics, not this comparison baseline']
})
shutil.copy('findelta/common.py', root/'common-frozen.py')
shutil.copy('findelta/predict.py', root/'predict-frozen.py')
PY
echo SFT > "$RUN/status.txt"
"$PY" -u -m findelta train --mode sft --data data/cohort/v1/sft-prompt-v3.jsonl --config "$RUN/config.json" --out "$RUN/sft-full" > "$RUN/sft-full.log" 2>&1
echo BASE_DEV > "$RUN/status.txt"
"$PY" -u -m findelta predict --data data/cohort/v1/dev.jsonl --config "$RUN/config.json" --out "$RUN/base-dev-predictions.jsonl" > "$RUN/base-dev.log" 2>&1
"$PY" -m findelta evaluate --data data/cohort/v1/dev.jsonl --predictions "$RUN/base-dev-predictions.jsonl" --out "$RUN/base-dev" > "$RUN/base-dev-eval.log"
echo SFT_DEV > "$RUN/status.txt"
"$PY" -u -m findelta predict --data data/cohort/v1/dev.jsonl --config "$RUN/config.json" --adapter "$RUN/sft-full" --out "$RUN/sft-dev-predictions.jsonl" > "$RUN/sft-dev.log" 2>&1
"$PY" -m findelta evaluate --data data/cohort/v1/dev.jsonl --predictions "$RUN/sft-dev-predictions.jsonl" --out "$RUN/sft-dev" > "$RUN/sft-dev-eval.log"
"$PY" -m findelta compare --run "Base=$RUN/base-dev" --run "SFT=$RUN/sft-dev" --out "$RUN/comparison.md"
echo COMPLETE > "$RUN/status.txt"
cat "$RUN/comparison.md"
