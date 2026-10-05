# FinDelta experiment comparison

Custom filtered FinQA cohort; not official leaderboard results.

Dataset SHA256: `68d81d651f57c0adc7b654b291d9d9d780fa4e8ffb23498e22a181f74a29b199`

| Run | N | Schema valid | Numeric accuracy | Verified accuracy | Coverage | Paired improvement vs first run (95% CI) |
|---|---:|---:|---:|---:|---:|---|
| control | 200 | 98.5% | 13.0% | 13.0% | 98.5% | +0.0 pp [+0.0, +0.0] |
| repaired | 200 | 98.5% | 13.0% | 13.0% | 98.5% | +0.0 pp [-2.7, +3.0] |

Intervals describe test-sample uncertainty, not training-seed uncertainty. One seed is exploratory.
Verified accuracy checks executable arithmetic and numeric occurrence in cited evidence; it does not prove semantic entailment, correct period selection, or general factuality.
Never mix synthetic stress fixtures into the real-data score.
