# FinDelta

**面向财报数值推理的 LLM 后训练研究项目 · 单卡一周起步版**

当前实现以公开 FinQA 算术数据为第一阶段，目标是产生可信的训练与评测证据。

## 当前运行方式

已接入 RunPod RTX 4090，代码和结果放在云端 `/workspace` 网络存储。本次使用固定的 prompt v3；说明见 [RunPod 实验协议](docs/PROMPT_V3.md)。原 Colab 结果使用不同提示词和硬件环境，不作为此次 SFT 提升的对照基线。

远程实验入口为 `scripts/runpod_week1_v3.sh`，一次完成 1,000 条样本的 SFT 与同一 200 题 dev cohort 的 Base/SFT 对比。它拒绝覆盖已有实验目录；重新实验请明确创建新的目录与协议。

**首轮实测已完成：** 在同一 200 题开发集上，Base → SFT 的数值正确率为 1.5% → 6.0%，严格验证正确率为 0% → 5.5%。额外的“使用确定性执行器计算模型程序”开发集对照达到 16.0%，这是推理流程的改进，不能全部归因于 SFT。结果仍较低，不能用于真实金融决策。详见 [完整实验报告](reports/week1-v3/REPORT.zh.md)。

**训练轮数对照已完成：** 同一模型、1,000 条训练数据、提示词和解码配置下，1 → 3 epochs 的原始输出严格正确率为 **5.5% → 13.5%**；使用同一确定性执行器后为 **16.0% → 44.5%**。在 200 道自定义 dev 题中，3-epoch 模型有 89 个程序执行结果正确，其中只有 27 个原始 answer 同时正确。完整配置、配对区间与原始输出见 [训练轮数实验报告](reports/week1-duration-v1/REPORT.zh.md)。测试集未评测，单 seed 结果仍属探索性结论。

**数据质量发现：** 训练集自动扫描发现 19 个年份候选疑点，其中已有两条由助手对照原始 FinQA 数据确认存在问题要求年份与参考程序年份不一致。19 个疑点不等于 19 个错误；未修改当前训练数据或评分。见 [两题核对说明](reports/train-year-audit-v1/START_HERE.zh.md)。

**DPO 小规模试验已完成：** 先后由助手审核 80 个真实模型错误候选，32 对通过，48 对排除；另有 41 对待审，人工审核数为 0。用 32 对助手审核偏好在 RTX 4090 上运行 1 epoch DPO，policy/reference 同从 3-epoch SFT 开始。200 题 dev 的执行器后 verified 为 **44.5% → 44.0%**，原始输出为 **13.5% → 13.0%**；配对区间均覆盖 0，**未确认提升，保留 SFT 基线**。另修复并回归验证了 BF16 基座上第二个 adapter 加载造成的 reference 精度损失。详见 [DPO 实验报告](reports/week1-dpo-v1/REPORT.zh.md) 与 [新增逐题审核](data/preferences/sft3-expanded-v1/assistant-expanded-v1/REPORT.zh.md)。这些是 AI 审核偏好，不是人工反馈或 RLHF。

**训练数据修正版已完成：** 对已审核的 82 道训练题重新作 SFT 裁定，修复 11 道、保留 37 道、隔离 34 道；其余 918 道仍未逐题审核。`v2-reviewed` 共 966 题，并准备相同 966 题、原标签的匹配对照。7 道修复原始证据行绑定，4 道修正时间方向、负号或金额/比例；dev/test 文件与 v1 完全一致。28 项测试与全量训练长度检查通过。新版的匹配对照训练已完成，结果见下。 详见 [修正版报告](reports/train-repair-v2/REPORT.zh.md)。

**标签修正匹配对照已完成：** 相同 966 题、相同配置，从基座独立训练各 3 epochs（363 步）。旧标签 → 修正版的执行器后 verified 为 **45.5% → 46.0%**，原始输出为 **13.0% → 13.0%**。主指标配对区间覆盖 0，未确认稳定提升。 28 项测试通过，800 个逐题评分复算一致；测试集未评测。详见 [标签修正对照报告](reports/week1-label-repair-v2/REPORT.zh.md)。

**多随机种子复现已完成：** 在 seed 42 后预先固定新增 17、123，共四次新增 GPU 训练；相同 966 题的旧标签与修正版共六个模型。三种子执行器后 verified 均值为 **44.67% → 45.17%**，配对差值均值 **+0.50 个百分点**、样本标准差 **0.50 个百分点**。新增复现出现持平和小幅上升，各 seed 配对区间均覆盖 0，尚未确认稳定收益。 三次均使用同一 200 题 dev，不能当作 600 道独立测试题。全部 2,400 个逐题评分复算通过，测试集未评测。详见 [多种子报告](reports/week1-label-multiseed-v1/REPORT.zh.md) 与 [简历及面试准备](reports/week1-label-multiseed-v1/RESUME.zh.md)。

## 其他运行方式与计划

**4070 主机无法联网时：** 使用 [Colab Notebook](notebooks/FinDelta_Colab_Week1.ipynb)，在能联网的电脑上打开 Colab 并上传 Notebook。详细步骤见 [Colab 指南](docs/COLAB.md)。GPU 在云端运行，无需连接本地 4070。

1. [七天计划：每天做什么、验收什么](docs/PLAN_7_DAYS.md)
2. [4070 运行手册：可直接执行的命令](docs/RUNBOOK_4070.md)

**如果改用本地 4070：** 在 Linux/WSL2 的项目目录执行 `bash scripts/setup_4070.sh`，先检查 GPU 和依赖环境。

## 已实现与已验证

- 固定 FinQA commit 和下载 SHA256；只从原始表格与段落构造输入，排除 gold 检索标签。
- 自定义公司隔离的数据划分，UA/UAA 合并为同一发行人；保存过滤与隔离原因。
- 已准备 Qwen3-0.6B 固定 tokenizer 下的 **1,000 train / 200 dev / 200 test** cohort，超长样本显式排除、不裁掉证据。
- JSON schema、来源数字绑定、四则运算、前向引用/除零/无效数字检查；不执行模型输出代码。
- Base 推理、completion-only LoRA SFT、以 SFT 为参考的 DPO、模型错误采样、审核后偏好导出（当前真实审核由 AI 助手完成）。
- 统一评测、逐题结果、按报告分组的 bootstrap 区间、同 cohort 的配对比较报告。
- 100 个合成偏好候选（全部待审核），100 个独立合成压力诊断（数字、期间、单位、拒答）。
- 核心自动测试与真实微型模型的 CPU SFT/DPO/保存/加载/推理集成验证。详情见 [实施检查](reports/implementation_checks.json) 与 [微型训练检查](reports/tiny_cpu_integration.json)。

**已完成真实 GPU 训练：** RTX 4090 上 Qwen3-0.6B 的 10 步 SFT 检查及 1,000 条样本、1 epoch 的正式 LoRA SFT。完整训练约 213 秒，峰值 allocated 显存 3.83 GiB、reserved 显存 20.40 GiB，112 个可训练张量更新。模型质量以独立保存的开发集评测报告为准。

另完成相同 LoRA 配置的 3-epoch 对照（375 步）。入口 `scripts/runpod_duration_ablation.py`，审计与报告入口 `scripts/summarize_duration_ablation.py`。每次实验独立保存 adapter，拒绝覆盖原结果。

**尚未完成：** 确认 DPO 泛化收益、最终测试集评测、更充分的随机种子复现、真实多报告跨期数据集、语义证据蕴含验证、GRPO、多卡训练。

## 最小研究问题

同一模型、同一输入、同一 token 预算下，SFT 与 DPO 是否提高“答案正确且计算操作数出现在指定证据中”的比例？

“Verified” 在本项目仅指受限程序与数字来源验证。它不证明完整事实性、正确的金融期间或单位解释。研究口径见 [实验协议](docs/RESEARCH_PROTOCOL.md)。

## 项目结构

```text
findelta/                 数据、验证器、训练、预测、评测与 CLI
configs/                  4070 SFT / DPO / 可选 QLoRA 配置
data/cohort/v1/           原始冻结子集与 SFT 格式
data/cohort/v2-reviewed/  966 题修正版、同样本原标签对照、隔离及变更清单
data/reviews/train-repair-v2/  AI 审核裁定与原始单元格注解
data/processed/v1/        完整过滤数据、隔离记录、数据 manifest
data/preferences/bootstrap/  合成偏好候选、审核表；未批准
data/stress/              明确标注的合成模板诊断
docs/                     七天计划、GPU 手册、协议、报告模板
reports/                  实施验证、实验协议与评测报告
scripts/                  环境安装与 tiny CPU 集成测试
tests/                    验证器、泄漏防护、审核与评测测试
third_party/              FinQA 许可与来源说明
model-lock.json           固定模型 revision
```

## 没有 GPU 也能运行的检查

核心代码只依赖 Python 标准库：

```bash
python3 -m unittest discover -s tests -v
python3 -m findelta doctor
python3 -m findelta --help
```

安装 `[train]` 依赖后可测试训练接口（随机微型模型，没有金融能力）：

```bash
python scripts/tiny_smoke.py --out runs/tiny-cpu-check
```

## 本周结果怎么写入简历

当前已完成真实 SFT、32 对助手审核偏好的 DPO 试验与同条件开发集评测；DPO 未确认提升。本次实际硬件为 RTX 4090。可基于实测写：

> Built a reproducible LoRA SFT and evidence-bound arithmetic execution pipeline for Qwen3-0.6B on 1,000 public financial QA examples, achieving 44.5% verified arithmetic accuracy on a 200-example company-disjoint development cohort; isolated training-duration and deterministic-execution effects through controlled ablations.

> Implemented and audited DPO with AI-reviewed financial reasoning preferences, diagnosed a BF16 reference-adapter loading mismatch, and evaluated held-out development performance with paired report-cluster bootstrap intervals.

44.5% 是 SFT + 确定性执行器的联合结果，原始模型为 13.5%；不能全部归因于训练，也不能写成官方 FinQA 分数。这些是单 seed、dev-only 的探索性结果，尚需多 seed 与最终 test 验证。可写已实施 DPO 并开展对照评测，但不能声称 DPO 提升。尚未完成 RLHF、多卡集群或真实业务部署。

## 参考资料

- [FinQA 原作者仓库](https://github.com/czyssrs/FinQA)：数据、程序标注与官方评测。项目改编集的指标不等于官方榜单。
- [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B)：项目起始模型，revision 见 model-lock.json。
- [TRL 0.23.1 SFT](https://huggingface.co/docs/trl/v0.23.1/en/sft_trainer) / [DPO](https://huggingface.co/docs/trl/v0.23.1/en/dpo_trainer)：实现按固定版本验证。
- [PEFT 量化说明](https://huggingface.co/docs/peft/developer_guides/quantization)：可选 QLoRA。

项目数据来自公开研究数据；尚未在 GitHub/Hugging Face 发布。当前使用用户租用的 RunPod GPU；GPU 与持久存储按平台规则计费。
