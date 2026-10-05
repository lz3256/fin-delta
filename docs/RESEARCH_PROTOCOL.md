# 实验协议 v1

## 任务边界

当前数据是 FinQA 页面级文字+表格算术题，支持 add/subtract/multiply/divide。排除了 greater、table_*、exp 等操作、找不到操作数、无证据或多余步骤、明显答案不一致等样本。具体数量看 manifest，不把被排除样本都称为“错误标签”。其中部分可能有格式、四舍五入或标注约定差异。

它不是完整财报检索、真实跨报告季度比较或一般金融事实性数据集。跨期与单位诊断当前是独立的合成模板。FinDelta 的完整跨期研究留到下一阶段。

## 数据与划分

- 来源 commit：0f16e2867befa6840783e58be38c9efb9229d742。
- 汇集公开 train/dev/test，去重后按发行人分为自定义 train/dev/test。**不是官方 FinQA split。**
- UA/UAA 股票类别名合并；其他发行人身份按照源 ticker。未来加入并购/改名数据时还需扩展实体映射。
- 官方公开测试数据被重新划分是此研究协议的一部分，因此不能再声称使用了官方未见测试集，不能向官方榜单提交这个模型来做公平对比。
- 输入只由 pre_text、post_text、table、question 构造；gold_inds 仅用于构造训练目标/评测参考，不进入模型输入。
- 目标中的操作数优先绑定到 gold evidence IDs 中包含该数值的文本；同一数字出现多次时绑定可能有语义歧义，必须抽样审核。
- 文本中的百分数按 value/100 解析；表格采用 FinQA 已规范化数字。此规范化可能保留如 `-134 (134)` 的重复正负形式，所以“数字出现”不等于该数字的会计解释正确。
- tokenizer revision 固定。所有模型使用相同 cohort。按上下文长度过滤会偏向较短任务，因此不能外推到长财报。
- public benchmark 可能进入过基础模型预训练；公司隔离只约束本项目训练数据，不证明消除了预训练污染。

## 输入与模型设置

Base/SFT/DPO 用同一 system prompt、同样的证据顺序、Qwen non-thinking 模式、greedy 解码和 640 个新 token 上限。

SFT 与 DPO 都训练 LoRA；DPO 从同一 SFT adapter 初始化 policy/reference，reference 冻结。DPO 内部不裁短 prompt/completion；所有数据预先检查 token 长度。

训练阶段只使用 train。开发、选择超参数用 dev。test 仅在方法固定后评测一次。日志记录数据哈希、模型 revision、包版本、随机种子、显存和耗时。

## 指标定义

- **numeric_answer_accuracy_on_answerable**：模型 answer 与参考执行结果在固定容差内相等。schema 合法但程序错误仍可能计入此项。
- **verified_accuracy**：对于可答题，数值答案正确、受限程序执行正确且与 answer 一致；程序中每个证据操作数在指定 source 中出现，所有步骤参与最终结果。对于不可答题，符合规范的拒答算正确。
- **answer_coverage**：成功解析且未拒答的比例。非法格式单独统计，不被当作合理拒答。
- **error_rate_among_answered**：已作答样本中未通过 verified 的比例，需与 coverage 一起解读。
- **evidence_id_precision/recall**：与数据集中标注的来源 ID 的重叠；可能存在多种正确证据，不能等同于语义支持率。
- **abstention precision/recall**：只有含不可答题的数据集能估计完整拒答能力。FinQA 主 cohort 全是可答题，因此 recall 为 null，不会填 0 或伪造结果。
- 数值容差为 abs_tol=1e-4、rel_tol=1e-5，具体见 verify.py；这是本项目口径，非官方 FinQA scorer。
- 每个模型一条预测/题，缺失预测算失败；重复 ID、额外 ID 或数据哈希不一致直接报错。

## 验证器不能证明什么

程序绑定只能证明数字在指定证据里出现，不能证明选对年份、指标、单位或因果关系；同值不同期间、巧合算对和奖励投机仍可能通过。

合成 unit/period 诊断通过已知目标答案间接检测这些错误，尚未实现通用的 period/unit 独立分类指标。README 和简历不能把它表述成完整语义事实验证。

更强的后续版本应增加逐操作数的类型/单位/期间标签、反事实重算和人工语义评测。

## 不确定性与比较

置信区间以 report_id 为分组进行 1000 次 bootstrap，同一报告的问题一起重采样。compare 命令对模型差值做配对重采样；区间覆盖 0 时，不声称确定性提升。

该区间只反映样本不确定性，不反映训练 seed 方差。第一周单 seed 是探索性结果；正式技术报告需要关键实验至少 3 seeds，且分别报告数据区间和 seed 波动。

## 偏好与拒答

默认正式 DPO 候选：从 train 上实际 SFT 采样，筛出可解析、可执行但答案错误的输出，与程序参考答案组成偏好；人工审核 approve 后才能训练。

bootstrap 候选：修改正确程序中的算术操作，并重新执行得到自洽但错误的答案；明确标记 synthetic_operator_mutation。仅用于启动检查或单独实验，不是人类自然偏好。

主 SFT/DPO 数据目前不含经过人工审核的真实缺证据拒答训练样本。合成压力测试只用于诊断，不能据此声称已训练出稳健拒答模型。

## 本周不进行的工作

不以收益率或 Sharpe 作为第一阶段主指标；不收集公司内部材料；不搭建多 agent UI；不做 7B/14B 起步或全面框架迁移。有限时间先投入数据与评测质量。

## 2026-09-24：助手审核补充协议

用户明确委托“你来审核”。因此 sft3-program-v1 的这批偏好由助手逐题对照原始材料审核，10 对通过、10 对排除，并标注 reviewer_type=ai_assistant；human_reviewed 仍为 0。approved 只代表本次助手审核批准，不代表独立人工审核。后续若用于 DPO，应报告为助手审核的验证器候选，不能声称人工偏好或 RLHF。

本次没有改 cohort、训练或评测标签，也没有启动 DPO。包含明确原始标注问题的样本不反向用于事后修饰旧分数；未来数据修正须另建版本与比较。

## 2026-09-24：DPO pilot v1

按预先保存的 sampling-protocol.json，以 seed 20260925 新采样 256 道训练题，排除旧 64 题 probe 和年份疑点。101 个候选中固定审核前 60 个，22 对通过、38 对排除，41 对仍 pending。与旧 10 对组成 32 对；全部标注 AI 审核，人工审核为 0。未修复当前 cohort 标签。

一次固定配置 DPO：policy/reference 同从 3-epoch SFT 开始，独立 5 步 smoke 后正式重新初始化，1 epoch、LR 5e-6、beta 0.1、seed 42。主指标为同一执行器后的 200 题 dev verified，次指标为原始输出；采样前已指定。执行器方法本身来自此前 SFT 阶段的事后诊断，不将其描述为最初研究开始时预注册。

GPU 初始化精度断言首次失败，查明 PEFT 第二个 adapter 经过 BF16 舍入；修复为精确复制已加载 policy 到独立 reference，保留逐位相等及训练后不变检查。未调整训练超参数或按 dev 选择不同版本。最终 executor verified 44.5%→44.0%、raw 13.5%→13.0%，配对区间覆盖 0；未确认收益。测试集仍未预测。具体 manifest、首次失败记录、回归检查和原始预测见 reports/week1-dpo-v1。

## 训练目标修正版 v2-reviewed

82 个已知审核项重新按 SFT 目标质量裁定，11 修复、37 保留、34 隔离。其余 918 题未作完整语义认证。修复仅修改训练目标和审计元数据：7 个原始来源行绑定，2 个时间方向，1 个会计负号，1 个金额/比例。保留相同 prompt，未改变 dev/test 原文、标签或评分器。对单位/时期等仍有歧义的样本保守隔离，不自动转成拒答目标。AI 审核，人工审核为 0。

同样本 control 使用相同保留的 966 个 ID、顺序和 prompt，但保持原标签。下一次计划 control/repaired 独立从固定 base 训练 3 epochs、seed42，以同一 dev 和执行器对照；协议保存于 reports/train-repair-v2/next-experiment.json，当前尚未执行。与旧 1000 题模型对比不能单独归因于目标修正。原始单位尺度未全局标准化，新的单元格检查仅适用于显式审核注解，不能称为通用语义验证器。


## 标签修正匹配对照的执行记录

两组真实 GPU 运行已完成，各 966 题、3 epochs、363 步，只有 11 条 completion 不同。预先冻结的 next-experiment.json 保留 PLANNED_NOT_STARTED 作为历史快照；实际执行协议、完成状态、模型、预测与审核结果在 reports/week1-label-repair-v2。运行入口为 scripts/runpod_label_repair.py --out <新的实验目录>，结果审核为 scripts/summarize_label_repair.py --run <实验目录>。测试集未生成预测。


## 标签修正多种子复现

观察 seed 42 后，预先固定新增训练 seed 17、123，推理 seed 保持 42。四次新增独立基座训练均为 966 题、3 epochs、363 steps。分别报告新增种子与包含 seed 42 的描述性汇总；不按最高分选 seed，不将重复的 200 题合并视作独立样本。协议位于 reports/label-repair-multiseed-v1-plan，完整结果位于 reports/week1-label-multiseed-v1。每个 seed 的报告分组区间不代表训练 seed 不确定性。
