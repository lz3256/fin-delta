# FinDelta experiment comparison

Custom filtered FinQA cohort; not official leaderboard results.

Dataset SHA256: `68d81d651f57c0adc7b654b291d9d9d780fa4e8ffb23498e22a181f74a29b199`

| Run | N | Schema valid | Numeric accuracy | Verified accuracy | Coverage | Paired improvement vs first run (95% CI) |
|---|---:|---:|---:|---:|---:|---|
| SFT-1epoch+executor | 200 | 100.0% | 16.0% | 16.0% | 85.5% | +0.0 pp [+0.0, +0.0] |
| SFT-3epochs+executor | 200 | 100.0% | 44.5% | 44.5% | 89.5% | +28.5 pp [+20.5, +36.9] |

Intervals describe test-sample uncertainty, not training-seed uncertainty. One seed is exploratory.
Verified accuracy checks executable arithmetic and numeric occurrence in cited evidence; it does not prove semantic entailment, correct period selection, or general factuality.
Never mix synthetic stress fixtures into the real-data score.
