# 4070 运行手册

以下命令在项目根目录执行。首选 NVIDIA 主机的 Linux 或 Windows WSL2 Ubuntu；当前 Mac 只用于开发验证。项目压缩包附带固定的 1000/200/200 数据 cohort，第一周可直接用，不需重新抓数据。

## 1. 环境与资源

需要 NVIDIA 驱动、可用的 nvidia-smi、Python 3.10–3.12、联网下载开源模型与依赖。建议留约 15GB 磁盘空间。

```bash
bash scripts/setup_4070.sh
source .venv/bin/activate
export HF_HOME="$PWD/.cache/huggingface"
export TOKENIZERS_PARALLELISM=false
```

查看 runs/hardware.json：4070 桌面卡/笔记本版本显存不同。本项目默认 0.6B、BF16（不支持则 FP16）、LoRA rank 8、batch 1。配置是起点，未经你的 4070 实测，不保证指定显存下完全不 OOM。

Qwen 的模型版本已固定在 model-lock.json。不要随意替换版本而继续沿用旧结果。脚本不会创建付费实例、上传文件或自动发布模型。

## 2. 本地数据与基线

先检查环境和数据测试：

```bash
python -m unittest discover -s tests -v
python -m findelta export-sft
python -m findelta predict --data data/cohort/v1/dev.jsonl --out runs/base-dev-predictions.jsonl
python -m findelta evaluate --data data/cohort/v1/dev.jsonl --predictions runs/base-dev-predictions.jsonl --out runs/base-dev
```

预测默认为 greedy、关闭 Qwen thinking、每题相同 640 个新 token 预算。固定提示已包含输出 schema、来源引用和运算约束。它是本周的强结构化提示基线；尚未实现独立检索/规则抽取基线。

## 3. SFT：先试跑，再正式跑

```bash
python -m findelta train --mode sft --data data/cohort/v1/sft.jsonl --out runs/sft-smoke --max-steps 10
python -m findelta train --mode sft --data data/cohort/v1/sft.jsonl --out runs/sft
python -m findelta predict --data data/cohort/v1/dev.jsonl --adapter runs/sft --out runs/sft-dev-predictions.jsonl
python -m findelta evaluate --data data/cohort/v1/dev.jsonl --predictions runs/sft-dev-predictions.jsonl --out runs/sft-dev
python -m findelta compare --run Base=runs/base-dev --run SFT=runs/sft-dev --out runs/dev-comparison.md
```

默认从原模型重新开始正式 SFT；10-step 试跑不接续进正式训练。每次新实验用新目录，程序拒绝覆盖已有训练结果。

若 OOM，先尝试：

```bash
python -m findelta train --mode sft --config configs/4070-8gb-qlora.json --data data/cohort/v1/sft.jsonl --out runs/sft-qlora-smoke --max-steps 10
```

采用 QLoRA 后使用同配置做对应基线和预测，并另建结果目录。DPO 也应明确采用相同量化约定，但使用 5e-6 学习率（复制 4070-dpo.json，只改 load_in_4bit=true）；不要拿 SFT 的 1e-4 配置直接做 DPO。

## 4. 偏好数据：从实际模型错误产生

为节约时间，先把训练集前 100 题保存为一个固定采样子集：

```bash
python -c 'from findelta.common import read_jsonl,write_jsonl; write_jsonl("data/cohort/v1/train-sampling.jsonl", read_jsonl("data/cohort/v1/train.jsonl")[:100])'
python -m findelta predict --data data/cohort/v1/train-sampling.jsonl --adapter runs/sft --samples 2 --temperature 0.7 --out runs/train-samples.jsonl
python -m findelta preferences --data data/cohort/v1/train-sampling.jsonl --predictions runs/train-samples.jsonl --out data/preferences/model-v1 --limit 100
```

打开 data/preferences/model-v1/review.md 看每题的证据、chosen、rejected；在 review.csv 把 decision 改为 approve 或 reject。自动构造的 chosen 来自参考程序，仍可能有语义标签问题，必须审查。不要批量无脑 approve。

如果候选为零，检查输出是否大多非法 JSON 或程序无法执行，先修 SFT；如果大多数答案已正确，则扩大训练采样范围/增加采样，不需要人为制造“提升”。

```bash
python -m findelta export-dpo --candidates data/preferences/model-v1/candidates.jsonl --review data/preferences/model-v1/review.csv --out data/preferences/model-v1/approved.jsonl
```

项目附带 data/preferences/bootstrap/：100 个**合成操作符修改**候选，全部 pending。可用于审核练习或单独的合成偏好实验；它们不是模型实际错误，也不是人类采集偏好。默认正式流程使用 model-v1。

## 5. DPO

```bash
python -m findelta train --mode dpo --config configs/4070-dpo.json --data data/preferences/model-v1/approved.jsonl --sft-adapter runs/sft --out runs/dpo-smoke --max-steps 10
python -m findelta train --mode dpo --config configs/4070-dpo.json --data data/preferences/model-v1/approved.jsonl --sft-adapter runs/sft --out runs/dpo
python -m findelta predict --data data/cohort/v1/dev.jsonl --adapter runs/dpo/policy --out runs/dpo-dev-predictions.jsonl
python -m findelta evaluate --data data/cohort/v1/dev.jsonl --predictions runs/dpo-dev-predictions.jsonl --out runs/dpo-dev
python -m findelta compare --run Base=runs/base-dev --run SFT=runs/sft-dev --run DPO=runs/dpo-dev --out runs/dev-comparison.md
```

DPO adapter 位于 runs/dpo/policy。SFT 参考权重独立加载、冻结、预计算 reference log-prob，不能通过禁用唯一 SFT adapter 把原始 base 当 reference。

## 6. 固定配置之后评测 test

先在研究笔记中记下最终选用的配置和选择理由。然后对三个模型只做这一轮 test 比较；如果之后改方法，旧 test 已经不再是未见测试集。

```bash
python -m findelta predict --data data/cohort/v1/test.jsonl --out runs/base-test-predictions.jsonl
python -m findelta predict --data data/cohort/v1/test.jsonl --adapter runs/sft --out runs/sft-test-predictions.jsonl
python -m findelta predict --data data/cohort/v1/test.jsonl --adapter runs/dpo/policy --out runs/dpo-test-predictions.jsonl
python -m findelta evaluate --data data/cohort/v1/test.jsonl --predictions runs/base-test-predictions.jsonl --out runs/base-test
python -m findelta evaluate --data data/cohort/v1/test.jsonl --predictions runs/sft-test-predictions.jsonl --out runs/sft-test
python -m findelta evaluate --data data/cohort/v1/test.jsonl --predictions runs/dpo-test-predictions.jsonl --out runs/dpo-test
python -m findelta compare --run Base=runs/base-test --run SFT=runs/sft-test --run DPO=runs/dpo-test --out runs/test-comparison.md
```

若本周未完成 DPO，省略 DPO 命令，完整交付 Base/SFT。

## 7. 单独的合成压力诊断

```bash
python -m findelta stress
python -m findelta predict --data data/stress/synthetic-v1.jsonl --adapter runs/sft --out runs/sft-stress-predictions.jsonl
python -m findelta evaluate --data data/stress/synthetic-v1.jsonl --predictions runs/sft-stress-predictions.jsonl --out runs/sft-stress
```

包含数字替换、干扰期间、单位转换和缺证据拒答。明确标注“合成模板诊断”，不混进真实 FinQA 分数，也不声称是真实跨季度财报泛化。

## 从源数据完全重建（可选）

附带的 cohort 已准备好。若要复现原始处理，请使用新目录避免覆盖：

```bash
python -m findelta download
python -m findelta prepare --out data/processed/rebuild
python -m findelta freeze --input data/processed/rebuild --out data/cohort/rebuild
```

下载来源固定到 commit 和 SHA256，默认公司分组 seed=42。所有过滤数、数据哈希、模型 revision 都写入 manifest。底层数据是自定义过滤与重划分，不能把项目指标直接与 FinQA 官方榜单比较。
