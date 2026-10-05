# FinDelta experiment comparison

Custom filtered FinQA cohort; not official leaderboard results.

Dataset SHA256: `68d81d651f57c0adc7b654b291d9d9d780fa4e8ffb23498e22a181f74a29b199`

| Run | N | Schema valid | Numeric accuracy | Verified accuracy | Coverage | Paired improvement vs first run (95% CI) |
|---|---:|---:|---:|---:|---:|---|
| SFT-1epoch | 200 | 96.5% | 6.0% | 5.5% | 96.5% | +0.0 pp [+0.0, +0.0] |
| SFT-3epochs | 200 | 98.0% | 13.5% | 13.5% | 98.0% | +8.0 pp [+1.8, +14.6] |

Intervals describe test-sample uncertainty, not training-seed uncertainty. One seed is exploratory.
Verified accuracy checks executable arithmetic and numeric occurrence in cited evidence; it does not prove semantic entailment, correct period selection, or general factuality.
Never mix synthetic stress fixtures into the real-data score.
