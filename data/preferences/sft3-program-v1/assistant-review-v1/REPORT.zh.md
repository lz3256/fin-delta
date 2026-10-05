# 20 对偏好候选：助手逐题审核结果

**结果：10 对通过，10 对排除，0 对待审。审核由 AI 助手按用户委托完成，人工审核数仍为 0；尚未启动 DPO。**

## 审核标准

逐题阅读全文证据，并对照缓存的原始 FinQA 问题、表格和标注；对通过的 10 对独立用 Decimal 重算。优选必须取对实体、期间、指标、分母和单位，负例必须有明确概念或操作错误。措辞/尺度歧义和需要修复的来源绑定保守排除。

原 FinQA train/dev/test 已按既定协议重新划分为本项目公司隔离 split。本次只核对属于本项目 train 的这 20 个 ID，没有使用本项目 dev/test 生成偏好。此审核也不是第三方独立审核。

## 最重要的发现

- ETR/2004：问题明确 2001→2002，正确变化率约 -82.0165%。原参考写成 +456.0645%；执行器重算后的负例程序实际上正确。模型未经重算的原始数值仍不准确。
- AMAT/2015：参考把 owned+leased 的 2731 千平方英尺当成 owned；owned/other countries 为 1624 千平方英尺。
- DRE 和 RE：算式数值合理，但来源 ID 命中了序列化时重复的首行表头，而非原表中该数值所在行。两对采用相同标准，等待重绑来源。
- 部分候选比较百分比、小数或指数点，不能笼统称为金融推理错误。保留原有评分，但不送入这批偏好训练。

## 逐题结论

| # | ID | 决定 | 类别 |
|---|---|---|---|
| 1 | TSCO/2018/page_34.pdf-1 | 排除 | ambiguous_comparison |
| 2 | MS/2013/page_240.pdf-3 | 排除 | ambiguous_direction |
| 3 | AES/2001/page_33.pdf-4 | 通过 | missing_average_divisor |
| 4 | SNA/2007/page_29.pdf-2 | 通过 | missing_roi_denominator |
| 5 | DRE/2009/page_59.pdf-1 | 排除 | source_binding_repair |
| 6 | PM/2017/page_23.pdf-1 | 通过 | wrong_facility_subset |
| 7 | PKG/2009/page_65.pdf-4 | 通过 | unnecessary_subtraction |
| 8 | GPN/2009/page_70.pdf-3 | 通过 | incomplete_intangible_components |
| 9 | ETR/2004/page_163.pdf-5 | 排除 | reference_reverses_time |
| 10 | ETR/2016/page_17.pdf-2 | 通过 | wrong_net_change_denominator |
| 11 | GPN/2009/page_85.pdf-3 | 通过 | wrong_metric_and_period |
| 12 | CME/2012/page_73.pdf-3 | 通过 | amount_vs_rate |
| 13 | AES/2001/page_78.pdf-2 | 排除 | false_improvement_premise |
| 14 | DG/2010/page_136.pdf-2 | 排除 | unresolved_rate_scale |
| 15 | AAPL/2015/page_24.pdf-2 | 排除 | absolute_vs_relative_change |
| 16 | AMAT/2015/page_31.pdf-2 | 排除 | reference_wrong_asset_category |
| 17 | RE/2010/page_120.pdf-3 | 排除 | source_binding_repair |
| 18 | AES/2011/page_261.pdf-3 | 通过 | wrong_carrying_value_denominator |
| 19 | EW/2014/page_35.pdf-2 | 排除 | equivalent_percentage_scale |
| 20 | ETR/2017/page_352.pdf-1 | 通过 | authorized_vs_outstanding |

### 1. TSCO/2018/page_34.pdf-1

**排除** · `ambiguous_comparison`

(217.01-100)/100 - (117.18-100)/100 = 0.9983

参考表示两组收益率之差（99.83 个百分点）；负例表示期末指数水平相对差约 85.19%。greater return 未明确比较口径，且参考的指数初始值引用另一家公司行。当前版本不作为确定的语义偏好。

### 2. MS/2013/page_240.pdf-3

**排除** · `ambiguous_direction`

(621-656)/656 = -0.0533536585

2015=656、2016=621（百万美元）。参考按 2015 为基期算变化率，负例按 2016 为基期反向比较；题目仅写 percentage difference ... between，未明确方向。两种比较及对称差均可能，排除歧义，不宣称参考必错。

### 3. AES/2001/page_33.pdf-4

**通过** · `missing_average_divisor`

(44.72+34.25)/2 = 39.485 USD/share

2000 年第一季度最高/最低价分别为 44.72 和 34.25 美元/股，平均值 39.485；负例仅相加为 78.97，缺除以 2。table_0 本身是包含真实数据的首行。

### 4. SNA/2007/page_29.pdf-2

**通过** · `missing_roi_denominator`

(198.05-146.97)/146.97 = 0.3475539226

Snap-on：2005 年末 146.97、2007 年末 198.05，ROI 应除以起始值，约 34.7554%；负例 51.08 是指数绝对变化，缺 ROI 分母。

### 5. DRE/2009/page_59.pdf-1

**排除** · `source_binding_repair`

176038/182538 = 0.9643909761

数值比例正确：经营出租物业/总房地产投资，单位同为千美元。但 chosen 的 176038 绑定 table_1（原表 undeveloped land=6500），仅因序列化重复首行表头而出现该数；正确原表行是 table_0。先修来源绑定，当前 pair 不批准。

### 6. PM/2017/page_23.pdf-1

**通过** · `wrong_facility_subset`

13/46 = 0.2826086957

2017 年末 EU 的全部设施为 13、全球总设施 46；负例 7 只取 EU fully integrated 子类，漏掉另两类。

### 7. PKG/2009/page_65.pdf-4

**通过** · `unnecessary_subtraction`

25048/44572 = 0.5619671543

2014 年之后对应 thereafter=25048，总承诺 44572，均为千美元；比例约 56.1967%。负例先减总额，得到负数，计算的不是到期承诺占比。

### 8. GPN/2009/page_70.pdf-3

**通过** · `incomplete_intangible_components`

(13536+4091+1031)/19427 = 0.9604159160

表中非有形收购资产为 goodwill、customer-related 和 contract-based 三项，总额 18658；以 gross total assets acquired=19427 为分母。负例只包括 customer-related=4091，漏掉两项。全部为千美元。

### 9. ETR/2004/page_163.pdf-5

**排除** · `reference_reverses_time`

(4279-23794)/23794 = -0.8201647474

题目明确 from 2001 to 2002；2001=23794、2002=4279。正确变化约 -82.0165%。原 FinQA 参考 (23794-4279)/4279 将方向及基期反转，得到 +456.0645%。执行器归一化后的 rejected 程序实际正确，不得按原标签训练这对偏好。模型原始 answer=-0.8 仍不够精确，不能称其原始回答完全正确。

### 10. ETR/2016/page_17.pdf-2

**通过** · `wrong_net_change_denominator`

289/(6179-5829) = 0.8257142857

2015→2016 净收入总变化 350 百万美元，retail electric price 贡献 289，贡献占比约 82.5714%；负例 5829/6179 是两年收入水平之比。

### 11. GPN/2009/page_85.pdf-3

**通过** · `wrong_metric_and_period`

(6.2-1.7)/1.7 = 2.6470588235

text_2 的总已归属奖励公允价值 2009=6.2、2007=1.7 百万美元，增加约 264.706%；负例使用表内 granted/vested 股数 400/136，混淆金额、数量和期间。

### 12. CME/2012/page_73.pdf-3

**通过** · `amount_vs_rate`

690.6-262.9 = 427.7 million USD

同一 BM&FBovespa 投资、公允价值 690.6、成本 262.9 百万美元，税前未实现收益为 427.7 百万美元；负例再除成本变成收益率，量纲错误。

### 13. AES/2001/page_78.pdf-2

**排除** · `false_improvement_premise`

58-31 = 27 million USD increase in losses

终止经营税前损失从 2000 年 31 增至 2001 年 58 百万美元，是损失扩大，问题却写 improved；参考给正 27000000，未表达恶化。负例又比较 2001/1999 且使用百万单位。题干前提与单位需明确后另建版本，不批准两者中的任何一个作为当前优选。

### 14. DG/2010/page_136.pdf-2

**排除** · `unresolved_rate_scale`

1/10 = 0.1 = 10% per year

直线折旧、寿命 3–10 年，对应最低年度率 10%。原始答案为 10%，参考 JSON 却是裸数 10；当前数据中比例多用小数，rate 未有独立单位字段。实际金融答案并非不明，但输出尺度需统一；负例 10/3 也错误。先修尺度契约，不自动把参考改成 0.1。

### 15. AAPL/2015/page_24.pdf-2

**排除** · `absolute_vs_relative_change`

187-100 = 87 index points; (187-100)/100 = 0.87

2010→2015 的指数绝对变化为 87 点，增长率为 87%；chosen/rejected 是同一变化的两种度量。题目仅写 change，且输入为总回报图，不足以把相对变化当作明确金融错误。保守排除语义弱偏好。

### 16. AMAT/2015/page_31.pdf-2

**排除** · `reference_wrong_asset_category`

owned outside US = 1624 thousand sq ft

表格 owned/other countries=1624，owned+leased/other countries=2731。参考 7035-4304=2731 混入租赁面积，与题目 owned 不符；how much more 也缺明确比较对象。负例同样不对，不能用错误参考做 chosen。

### 17. RE/2010/page_120.pdf-3

**排除** · `source_binding_repair`

8346/65658 = 0.1271132231

税额的绝对值 8346 除税前毛调整 65658，约 12.7113%，数值合理；gross 65658 的原始位置是 table_0，chosen 却绑定税额行 table_1 的重复表头。与 DRE 采用相同严格来源标准，先重绑来源；并非认定 12.7113% 错误。

### 18. AES/2011/page_261.pdf-3

**通过** · `wrong_carrying_value_denominator`

200/288 = 0.6944444444

Huntington Beach 账面价值 288、减记 200、剩余公允价值 88 百万美元，减记/原账面约 69.4444%；负例 200/389 的 389 是所有设施减记总额，不是该设施账面价值。

### 19. EW/2014/page_35.pdf-2

**排除** · `equivalent_percentage_scale`

0.8819 fractional return difference = 88.19 percentage points

两组初始投资均 100，2014 期末值 293.33 和 205.14。参考收益率差 0.8819 与负例指数差 88.19 在本基准下对应同一 88.19 个百分点差。问题明确 percentage，而 prompt 的 fractional-ratio 与显式百分数要求边界不够清楚。按语义偏好排除尺度负例，不改变旧评分。

### 20. ETR/2017/page_352.pdf-1

**通过** · `authorized_vs_outstanding`

15/350 = 0.0428571429

题目询问信用证获授权额度占借款容量：同一 facility 的授权 15 百万美元、总容量 350 百万美元，约 4.2857%；负例 9.1 是已发行余额，且方向为 15/9.1，分母概念错误。

## 交付与后续

- review.csv 已填完，approved.jsonl 含 10 对可供后续试验使用的助手审核数据，每条保留审核来源和理由。
- 原 candidates.jsonl 未改；审核前文件保存在本目录 before-*。逐题原始材料与哈希见 source-crosschecks.json。
- 不为凑训练数量批准歧义样本。这 10 对只能作为种子/流程检查数据，尚不足以支撑可靠的 DPO 效果结论；下一步扩充训练题采样并沿用此标准。
- 没有修改训练/开发/测试 cohort，也没有重算此前分数。旧指标仍衡量与有噪声参考标签的一致性，不能称作已证明的金融语义准确率。
- 本轮只完成审核与导出，未启动 GPU 训练。
