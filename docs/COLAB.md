# 在 Colab 上运行

## 适合当前计划吗？

适合。第一周是 0.6B 模型、小规模 LoRA SFT/DPO，可以先用可获得的 GPU 做十步试跑。T4 是可考虑的起点，有 L4 也可，不必为起步实验专门追求 A100。实际显存与吞吐以 doctor 和试跑结果为准。

Colab 是托管 Notebook 服务，免费/付费都不保证某张指定 GPU，也不是无限时长的独占服务器。额度和运行时会变动。

- 先检查自己的账号是否已有计算单元。
- 免费 GPU 可用就先跑环境检查与试跑。
- 不够时考虑 Pay As You Go 最小档，不必先订高档长期方案。
- 价格、税费、地区资格、可用选项以登录后的官方付费页为准，本项目没有固定价格报价。

官方来源：[FAQ](https://research.google.com/colaboratory/faq.html)、[付费方案](https://colab.research.google.com/signup)。

## 今天的五步

1. 下载本对话中的 FinDelta_Colab_Week1.ipynb 与 FinDelta-Colab-Week1.zip。
2. 打开 https://colab.research.google.com/ ，选择“文件 → 上传笔记本”，上传 ipynb。
3. “运行时 → 更改运行时类型 → GPU”。先选择可用的 T4 或其他 GPU。
4. 只运行 Notebook 第 1–5 步：检测 GPU、上传 zip、安装隔离环境、挂载 Drive、保存 hardware.json。
5. 把 hardware.json 的内容发回 Codex，再开始第 6 步基线与第 7 步十步 SFT。

Notebook 后续实验开关默认 False；不要直接全部运行。购买计算单元和 Drive 授权都由你在 Google 页面完成，项目不会代购或发布文件。

## 环境与结果保存

训练使用独立 Python 3.12 环境，固定 PyTorch/TRL/Transformers 等版本，避开 Colab 预装环境冲突。Notebook 内核只使用标准库与 google.colab 来编排子进程，不用重启内核。

代码/数据/模型下载缓存位于临时的 /content；训练 adapter、日志和预测结果直接写到 MyDrive/FinDelta/<RUN_ID>。请确保 Drive 还有空余空间。

**已完成阶段**可以在重连后继续使用：重新上传项目、重装环境、挂载同一 Drive，并填回同一个 RUN_ID。代码会跳过有完整 manifest 的结果，检测到不完整输出则停止并提醒。

**正在进行的训练**被终止时可能需要重跑。本版训练脚本只保存最终 adapter，尚未实现中途 checkpoint 恢复；不会宣称自动断点续训。保留未完成目录供排查，使用新阶段名称或新的 RUN_ID 重跑。

Notebook 提供结果 zip 下载。结束后手动“断开连接并删除运行时”，不要依赖关浏览器页面来释放 GPU。

## 验证状态

Notebook 的 JSON 结构与全部 Python 单元已在本地检查。核心代码已有 21 项测试和 CPU 微型模型 SFT/DPO 集成验证。尚未在 Colab GPU 上实际执行，不保证特定会话的驱动、GPU 与额度；第一轮以硬件检查和十步试跑确认。
