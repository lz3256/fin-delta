<img src="assets/social-preview.jpg" width="560" alt="FinDelta cover">

# FinDelta

**Financial reasoning post-training, with evidence-bound arithmetic and reproducible evaluation.**

FinDelta studies LoRA supervised fine-tuning, small-scale DPO, deterministic program execution and training-label quality on a custom company-separated subset of FinQA. Experiments use Qwen3-0.6B on a single RTX 4090.

## Work completed

The implementation covers a FinQA-derived training/evaluation pipeline, LoRA adapters, an evidence-bound arithmetic executor, debugging of DPO reference-model precision, and training-label audit and repair. Matched original/repaired-label experiments were then run across three seeds. Reports include both improvements and experiments that did not confirm a benefit.

## What this project demonstrates

- A data pipeline with source revision locking, company separation and token-length checks.
- Completion-only LoRA SFT and DPO with an explicit reference model.
- Restricted arithmetic programs and operand-to-evidence checks, without executing generated Python.
- Paired development-set comparisons, grouped bootstrap intervals and three-seed label-repair experiments.
- Documented negative results and a regression fix for reference-adapter precision.

## Selected recorded results

| Comparison | Development-set verified accuracy | Interpretation |
|---|---:|---|
| SFT: 1 → 3 epochs, with the same executor | 16.0% → 44.5% | Training-duration experiment; one seed |
| SFT → 32-pair DPO, with the same executor | 44.5% → 44.0% | No confirmed DPO improvement |
| Original → repaired labels, three-seed mean | 44.67% → 45.17% | Small difference; paired intervals include zero |

All comparisons above use the same 200-question custom development cohort. They are not official FinQA leaderboard scores. The final test set has not been evaluated. Preference judgments were made by an AI assistant, not human raters. Executor gains must be distinguished from training gains.

## Quick start

Python 3.10+ is required. Core validation uses only the standard library:

```bash
python3 -m unittest discover -s tests -v
python3 -m findelta doctor
python3 -m findelta --help
```

For training, use a separate environment and install the declared training dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[train]"
```

Model downloads and training require additional resources. See [research protocol](docs/RESEARCH_PROTOCOL.md), [prompt specification](docs/PROMPT_V3.md), and the [original project guide](GUIDE.zh.md).

## Research reports

- [Training-duration ablation](reports/week1-duration-v1/REPORT.zh.md)
- [DPO experiment and precision regression](reports/week1-dpo-v1/REPORT.zh.md)
- [Training-label repair](reports/train-repair-v2/REPORT.zh.md)
- [Matched label-repair comparison](reports/week1-label-repair-v2/REPORT.zh.md)
- [Three-seed replication](reports/week1-label-multiseed-v1/REPORT.zh.md)

## Repository contents

`findelta/` contains the implementation, `tests/` the core checks, `scripts/` experiment entry points, `configs/` settings, and `reports/` recorded results. Frozen FinQA-derived cohorts and review records are retained in `data/`. Large model weights, tokenizer copies, full processed-source downloads and machine-specific connection details are excluded.

## Attribution

FinQA-derived data retain the [original MIT license](third_party/FinQA-LICENSE.txt) and [attribution notice](third_party/NOTICE.md). Model weights and dependencies retain their respective licenses. No blanket license for this project's own code is granted by those third-party notices.

## Credits

Project owner: [Linfeng Zhao (@lz3256)](https://github.com/lz3256).

Developed with substantial assistance from OpenAI Codex for implementation, analysis, debugging and documentation. Recorded experiments and limitations are described in the linked reports.

FinQA-derived data retain the original authors' attribution and MIT license in [third_party/](third_party/NOTICE.md). Experiments use Qwen3-0.6B; model and dependency licenses remain separate. The custom cohort is not an official FinQA benchmark split.

Detailed recorded predictions and per-question metrics are preserved in [evaluation-artifacts.zip](reports/evaluation-artifacts.zip). Extract it from the repository root to restore their original `reports/` paths.
