#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if ! command -v nvidia-smi >/dev/null; then
  echo 'NVIDIA GPU not visible. Run this on the 4070 machine in Linux/WSL2; check the NVIDIA driver first.'
  exit 1
fi
nvidia-smi
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cu126
python -m pip install -e '.[train,cuda]'
mkdir -p runs
python -m findelta doctor | tee runs/hardware.json
python -m unittest discover -s tests -v
echo 'Setup complete. Continue with docs/RUNBOOK_4070.md. No training has started.'
