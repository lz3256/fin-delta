# FinDelta：SFT 训练轮数对照

单 seed、开发集探索性实验。比较 1 epoch 与 3 epochs；均从相同基础模型重新训练。

## 开发集主要结果

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


## 确定性执行器对照

沿用上一轮已定义的推理规则：计算模型生成的程序，非法程序拒答；保留全部 200 题作为分母。不是额外训练，也不使用参考答案来修改输出。

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


## 训练题诊断

在本轮观察输出之前，用 seed=20260924 从按 ID 排序的 1,000 道训练题抽取 64 题。这是模型见过的数据，不是泛化结果。

| 配置 | 样本数 | 严格正确 | 程序执行结果正确 | 有效程序 |
|---|---:|---:|---:|---:|
| 1epoch-train64 | 64 | 6 | 14 | 58 |
| 3epochs-train64 | 64 | 16 | 42 | 63 |
| 1epoch-dev | 200 | 11 | 32 | 171 |
| 3epochs-dev | 200 | 27 | 89 | 179 |

## 逐题变化与剩余错误

原始模型严格评分：{'both_wrong': 167, 'improved': 22, 'both_correct': 5, 'regressed': 6}。

| 类别 | 1 epoch dev | 3 epochs dev |
|---|---:|---:|
| verified_correct | 11 | 27 |
| consistent_but_wrong | 51 | 19 |
| answer_program_disagreement | 109 | 133 |
| invalid_schema_or_program | 29 | 21 |
| abstained | 0 | 0 |

## 可复现设置与限制

- Qwen3-0.6B 固定 revision；LoRA rank=8、alpha=16、q_proj/v_proj；BF16；RTX 4090；seed=42。
- 同一 1,000 条训练样本、prompt v3、200 题 dev；greedy、batch=8、max_new_tokens=640。
- 训练配置只改 epochs，但 5% warmup 和线性学习率日程按总步数重新计算。因此比较的是训练时长配方，不是同一轨迹的第 1 与第 3 轮 checkpoint。
- 本轮训练 645.7 秒；显存 allocated 峰值 3.83 GiB、reserved 峰值 20.40 GiB。
- 原始 adapter、预测、评分、数据/提示词/代码哈希均保留；审计文件为 *-audit.jsonl。
- 数据为自定义过滤后的公司隔离 FinQA cohort，不是官方榜单；来源数字出现不证明期间、单位与语义正确。
- 反复在 dev 上试配方会产生选择偏差；置信区间不校正多次探索，也不包含训练 seed 方差。
- 本轮训练期间发现原始训练标签存在明确的年份矛盾，见 ../train-year-audit-v1/START_HERE.zh.md。没有改动当前数据或重算分数；后续清洗必须另建数据版本。
- test 未做预测；DPO 仍未运行。
