# FinDelta 首轮 GPU 实验

本次完成了单卡 LoRA SFT 与受控开发集比较；结果为单随机种子的探索性结果。

## 结果

# FinDelta experiment comparison

Custom filtered FinQA cohort; not official leaderboard results.

Dataset SHA256: `68d81d651f57c0adc7b654b291d9d9d780fa4e8ffb23498e22a181f74a29b199`

| Run | N | Schema valid | Numeric accuracy | Verified accuracy | Coverage | Paired improvement vs first run (95% CI) |
|---|---:|---:|---:|---:|---:|---|
| Base | 200 | 81.0% | 1.5% | 0.0% | 81.0% | +0.0 pp [+0.0, +0.0] |
| SFT | 200 | 96.5% | 6.0% | 5.5% | 96.5% | +5.5 pp [+2.1, +10.1] |

Intervals describe test-sample uncertainty, not training-seed uncertainty. One seed is exploratory.
Verified accuracy checks executable arithmetic and numeric occurrence in cited evidence; it does not prove semantic entailment, correct period selection, or general factuality.
Never mix synthetic stress fixtures into the real-data score.


## 设置与开销

- Qwen3-0.6B，固定 revision；RTX 4090；BF16；LoRA rank=8，q_proj/v_proj。
- 1,000 条训练样本，1 epoch，seed=42；从基础模型重新训练，未继续 smoke adapter。
- 同一 200 题自定义公司隔离 dev cohort；prompt v3、greedy、batch=8、最多生成 640 tokens。
- 训练时间 213.1 秒；峰值 allocated 3.83 GiB，reserved 20.40 GiB。
- 推理时间：Base 352.4 秒，SFT 131.3 秒。不含模型加载、安装和空闲计费时间。

## 逐题变化与错误

- 严格验证从错到对：11 题；从对到错：0 题。
- `paired-audit.jsonl` 保留全部题目的原始输出、评分、程序执行值和变化类别。

| 类别 | Base | SFT |
|---|---:|---:|
| verified_correct | 0 | 11 |
| consistent_but_wrong | 0 | 51 |
| answer_program_disagreement | 0 | 109 |
| invalid_schema_or_program | 200 | 29 |
| abstained | 0 | 0 |

## 额外推理对照：确定性执行器

这是看到 dev 错误后提出的额外对照，不是预先固定的主要实验，也不是又一次训练。保留 SFT 原始预测，执行模型给出的程序并用执行结果作为 answer；程序无效则拒答。转换只读取输入证据，不读取参考答案。

严格验证正确率 16.0%，覆盖率 85.5%，已回答问题错误率 81.3%。
格式合法率会因为程序化输出 JSON 而达到 100%，这不是模型自身的格式能力提升。
固定的 200 题都保留在分母中；无效程序转为拒答仍按答错计。本 cohort 全部可答，不能据此评估拒答识别能力。
这个对照分离了算术执行与选数/选运算问题，但仍不能保证期间、单位、语义证据正确。

# FinDelta experiment comparison

Custom filtered FinQA cohort; not official leaderboard results.

Dataset SHA256: `68d81d651f57c0adc7b654b291d9d9d780fa4e8ffb23498e22a181f74a29b199`

| Run | N | Schema valid | Numeric accuracy | Verified accuracy | Coverage | Paired improvement vs first run (95% CI) |
|---|---:|---:|---:|---:|---:|---|
| SFT | 200 | 96.5% | 6.0% | 5.5% | 96.5% | +0.0 pp [+0.0, +0.0] |
| SFT + executor (post-hoc dev) | 200 | 100.0% | 16.0% | 16.0% | 85.5% | +10.5 pp [+5.5, +15.8] |

Intervals describe test-sample uncertainty, not training-seed uncertainty. One seed is exploratory.
Verified accuracy checks executable arithmetic and numeric occurrence in cited evidence; it does not prove semantic entailment, correct period selection, or general factuality.
Never mix synthetic stress fixtures into the real-data score.


## 限制与下一步

- 这是自定义过滤后的 FinQA 开发集，不是官方榜单或最终测试结果。尚未评测冻结测试集。
- Verified 只检查数值答案、程序计算与来源数字出现，不证明选对期间、单位或语义证据。
- 数据仍存在百分比尺度和操作数绑定歧义；需人工审查，不能事后乘除 100 来改变评分。
- 置信区间按报告分组、配对 bootstrap；不包含训练 seed 方差。尚需多 seed 复现。
- 已实现 DPO 接口，但尚未完成真实偏好审核和 DPO 实验，不能写成 DPO 提升。
- 后续按错误类别审查样本、构造并审核 train-only 偏好对，再做 DPO；固定方法后评测 test。
