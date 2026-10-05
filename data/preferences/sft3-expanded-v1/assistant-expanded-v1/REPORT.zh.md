# 新增偏好审核：60 个候选

**22 对通过，38 对保守排除，剩余 41 对待审。与旧 10 对合并为 32 对 DPO 试验数据。全部由 AI 助手审核，人工审核数为 0。**

按采样前固定协议，仅审核新候选前 60 个，不按通过数量追加审核。逐题核对问题、原始表及相关文本；对疑点补读全文。通过样本用独立 Decimal 算式重算。严格区分明确错标、歧义、尺度等价与证据不足；排除并不表示参考一定错误。未修复原数据，未修改 train/dev/test。

新采样 256 个训练题产生 101 个候选；这里只审核预定前 60 个。负例程序来自 SFT 真实输出，数值答案经执行器归一化。筛选依据程序错误和语义审核，不使用 dev 结果。

## 1. ETR/2008/page_153.pdf-3

**通过** · wrong_components

321237 - 137858 = 183379 thousand

总租赁付款减 thereafter；负例把利息另加再换算，指标和单位均错。

## 2. APTV/2013/page_48.pdf-1

**排除** · unsupported_annualization

quarterly difference = 0.08 USD/share

仅声明 2014 首季 0.25，参考年化乘 4 假定全年不变；没有全年实际支付证据。

## 3. GPN/2017/page_77.pdf-1

**排除** · source_binding_repair

45826 / 62154

cash 45826 原表 table_0，却绑定 total 行 table_7 的重复首行表头；数值正确但来源须修复。

## 4. AON/2015/page_96.pdf-1

**排除** · reference_incomplete_average

(411636+439000+556000)/3

参考漏 2013 年且未除以 3，不能作为三年平均值的 chosen。

## 5. SNPS/2012/page_62.pdf-1

**排除** · ambiguous_goodwill_inclusion

184300/550234 vs (316263+184300)/550234

表有 identifiable intangible assets 独立项目；题目 intangible assets 未明确包含 goodwill，负例按该项目取值可以成立。

## 6. MRO/2008/page_119.pdf-2

**通过** · wrong_average_divisor

(164+103)/2 = 133.5 million

2008 current/noncurrent 两项资产平均；负例除以两项合计得到 1，非平均金额。

## 7. CME/2017/page_99.pdf-2

**通过** · missing_year

2.5+2.4+2.5 = 7.4 million

text_15–19 明确为非执行董事股份支付；2015–2017 三年，负例仅加两年。

## 8. GRMN/2006/page_91.pdf-2

**排除** · granted_vs_vested

vested value / granted fair value is not vested share count

参考将 vested 总公允价值除以 granted 的加权均价，未证明同一奖励群体，无法据此算归属股份数。

## 9. ETFC/2015/page_27.pdf-2

**通过** · wrong_return_comparison_denominator

(185.25-100)/100-(180.75-100)/100 = 0.045

题目明确两组五年百分比累计回报之差；两者均从 100 起算，相差 4.5 个百分点。负例除以 S&P 期末 180.75，是期末水平的相对差，非两个回报率的差。

## 10. TSCO/2017/page_73.pdf-1

**排除** · reference_wrong_year

2017 ending goodwill = 93192

参考取 2016 acquisition 84159 与 2016 ending 94417，题目问 2017。2017 acquisition 的 2014 为破折号编码，不是数值。

## 11. AAPL/2005/page_67.pdf-1

**通过** · wrong_period

11.7-8.2 = 3.5 million

2005 末减 2004 末，两个来源均为实际行内值；负例比较 2004 与 2003。

## 12. LKQ/2016/page_26.pdf-2

**排除** · source_binding_repair

(204-100)/100-(178-100)/100 = 0.26

S&P 起始 100 被绑定到 LKQ 行 table_1，而非 table_2；即使数值相同也不满足实体绑定要求。

## 13. STT/2007/page_65.pdf-2

**排除** · rounded_inverse_estimate

9746 / 0.09 is only an estimate

9% 为取整披露比例，反推总资产只能估计；chosen 未表达估计且无法严格验证实际总资产。

## 14. AAP/2016/page_65.pdf-2

**排除** · unsupported_cashflow_reconciliation

inventory balance difference = 151100 thousand

参考把存货账面净增直接等同现金流减少；证据还含 LIFO 估值调整，未提供非现金调整与现金流调节。不批准为严格现金流事实。

## 15. C/2010/page_223.pdf-3

**通过** · wrong_net_carrying_value

((469-77)-(920-95))/(920-95)

期初净额 825、期末 392；负例将已净额 392 再减准备 77 并以准备为分母。

## 16. GPN/2013/page_87.pdf-1

**通过** · wrong_operation

561*44 = 24684 thousand USD

2013 granted 561 千股、每股 grant-date fair value 44；负例将股数相加，量纲不符。

## 17. ETR/2004/page_281.pdf-1

**通过** · wrong_denominator

42.5/(61592/1000)

2004 现金使用 42.5 百万除当年应收 61.592 百万，先统一单位；负例分母为 2002 现金提供额。

## 18. CME/2017/page_57.pdf-4

**排除** · rounded_inverse_estimate

54.4/0.04+54.4 is only an estimate

4% 为整数披露增长，反算 2016 总费用只能近似，不宜训练成精确事实。

## 19. SWKS/2012/page_116.pdf-2

**通过** · reversed_time

(52380-32136)/32136

2011 至 2012 增长约 62.9948%；负例颠倒时间并用期末作基数。

## 20. UAA/2016/page_83.pdf-1

**排除** · source_binding_repair

176138/1355605

首年金额被绑定到 total 行重复表头，原位置 table_0；与此前相同规则，先修来源。

## 21. TSCO/2017/page_28.pdf-1

**排除** · unsupported_expense_classification

260000+32000+8000 = 300000 sqft

输入给办公设施面积，但未给 SG&A 与 cost of sales 会计归类；该筛选依赖未提供的会计政策，保守排除。

## 22. ETR/2017/page_26.pdf-1

**排除** · reference_reverses_time

(1542-1666)/1666 = -0.0744297719

题目 2015→2016，负例的程序实际正确；参考正 8.04% 反转时间和分母。不得训练反偏好。

## 23. ALXN/2007/page_49.pdf-2

**排除** · source_binding_repair

(108.38-128.98)/100 = -0.206

NASDAQ 起始 100 绑定到 Alexion 行；且正文起始 2001 与表 2002 不一致，须修复后再用。

## 24. AON/2007/page_171.pdf-2

**通过** · amount_vs_rate

284-118 = 166 million

明确问余额净变化，负例多除以期初变成增长率。

## 25. SNA/2013/page_84.pdf-2

**排除** · unsupported_receivables_reconciliation

546.5-516.9 = 29.6 million balance change

应收账款余额变动不能单独证明全部销售减全部收款，可能含其他应收和非现金变化；题目所需流量未充分给出。

## 26. AWK/2015/page_115.pdf-2

**排除** · ungrounded_financial_constant

4/11 = 0.363636...

chosen 将真实税收利益 4 写成 const_4 而未绑定 table_5；题目也未指年份。严格事实来源标准下先修复。

## 27. MRO/2008/page_99.pdf-2

**通过** · wrong_average_divisor

(20000+15000)/2 = 17500 barrels/day

2009 put/call 两种期权每日桶量平均应除 2；负例除 100。

## 28. ETR/2008/page_362.pdf-3

**排除** · unsupported_cashflow_reconciliation

47705-60093 = -12388 thousand under cash-only assumption

账户余额上升是明确事实，但仅凭两期余额将净变化等同现金流需无非现金转移假设，当前输入未保证。

## 29. GS/2014/page_80.pdf-2

**通过** · reversed_subtraction

2989-911 = 2078 million

2013 two-notch 要求高于 one-notch；按题目顺序减得到正差，负例反减。

## 30. L/2009/page_84.pdf-2

**通过** · wrong_base_period

(80.74-128.16)/128.16

S&P 2007→2008 ROI 以 2007 的 128.16 为基数；负例用 2004 的 100。

## 31. GRMN/2006/page_68.pdf-1

**排除** · ambiguous_decrease_direction

15477-6040 = 9437 magnitude

题干说 3–5 年到 >5 年 decrease，表中反而增加；chosen 报正差、negative 报反向差，方向前提需澄清。

## 32. AOS/2010/page_18.pdf-1

**排除** · equivalent_percentage_scale

0.55 fractional difference = 55 percentage points

两者表达同一回报差，不能当成明确金融推理负例。

## 33. HUM/2018/page_46.pdf-2

**排除** · source_binding_repair

114-100 = 14 index points

最低为 S&P，但其初始 100 引用 HUM 行，须改正确实体来源；当前不修标签。

## 34. AON/2015/page_96.pdf-4

**排除** · compensation_expense_not_share_price

9 million / 411636 is compensation expense per share

补偿费用不是购买股份对价；参考将费用/股数当平均股价，没有证据支持。

## 35. PKG/2015/page_83.pdf-1

**通过** · wrong_due_period

77/312

after 2020 是 thereafter 77，而负例取 2020 的 23.4；表头虽重复，两 chosen 均为正确实际行内值。

## 36. CE/2014/page_32.pdf-4

**排除** · unspecified_output_unit

199796*60.78 = 12143600.88 USD

参考除百万却无单位字段，题干未要求百万；负例还使用公开计划股数子集。先统一金额输出单位后另建版本。

## 37. PKG/2005/page_74.pdf-4

**排除** · source_binding_repair

2408+1364 = 3772 thousand

2006 的 2408 原在 table_0，却绑定 2007 行 table_1 的重复表头。

## 38. UA/2009/page_50.pdf-2

**通过** · reversed_time

(0.3-1.2)/1.2 = -0.75

2008→2009 公允价值从 1.2 降至 0.3 百万，负例反转方向与基期。

## 39. GPN/2014/page_92.pdf-1

**排除** · exercise_proceeds_not_security_value

766801*40.85 is hypothetical exercise proceeds

表中是尚未行权、未来可发行数量及行权价，并非已发行证券价值；不能把乘积作为题干事实。

## 40. VLO/2015/page_24.pdf-1

**排除** · ambiguous_denominator

842059/1055917

可解读为十月占季度非计划回购比，也可解读为十月非计划占当月总回购比；负例虽明显错误，chosen 的口径需澄清。

## 41. STT/2008/page_109.pdf-2

**排除** · payments_and_adjustments_not_cash_paid

20/250 = 8% reserve reduction

表合并 payments and adjustments，且正文 severance 243 与表初始 250 不同；不能认定 20 全部已付现金。

## 42. GPN/2007/page_39.pdf-3

**排除** · ambiguous_comparison

80.13 percentage points vs relative outperformance

题目 in comparison 未明确回报差还是相对表现，保守排除。

## 43. ETR/2011/page_145.pdf-2

**通过** · wrong_component

60249/248504

利息 60249 占未来最低付款总额 248504；负例用现值 188255。

## 44. ETR/2004/page_216.pdf-2

**通过** · wrong_period

35.4-14.8 = 20.6 million

2003 与 2004 Waterford 本金支付绝对差；负例比较 2003 与 2002。

## 45. MRO/2015/page_18.pdf-4

**排除** · expiring_acres_not_all_acres

4444/4533 refers only to acres expiring in 2017

题问 2017 未开发总面积分布，表仅 2015 时预计 2017 到期子集且部分计划出售；不能当实际全部面积。

## 46. SWKS/2012/page_116.pdf-3

**通过** · wrong_component

52.4-38.8 = 13.6 million

2012 总未确认税务利益减会影响有效税率部分；负例减去年总额。

## 47. ETR/2008/page_401.pdf-1

**排除** · unsupported_cashflow_reconciliation

53620-42915 = 10705 thousand under cash-only assumption

两期应收差未证明现金流量；正文还说明该 money pool 曾有转为票据的非现金重分类。保守排除，非认定差值算错。

## 48. LLY/2018/page_99.pdf-2

**通过** · missing_benchmark_return

(259.88-100)/100-(150.33-100)/100 = 1.0955

明确问 Lilly 与 S&P 的百分比回报差；负例仅算 Lilly 回报，漏基准。

## 49. RCL/2016/page_37.pdf-2

**排除** · equivalent_percentage_scale

98.18% = 0.9818

正确比例的两种数值尺度，不用作语义负例。

## 50. AES/2001/page_86.pdf-2

**排除** · reference_wrong_sign

-121-4 = -125 million

剔除 +4 公允价值变化应得 -125，与 -93-32 一致；参考 4-121=-117 错误。

## 51. CME/2017/page_99.pdf-5

**通过** · missing_year

0.3+0.2+0.2 = 0.7 million

2017 为 0.3、2016 和 2015 各 0.2，负例漏一年。

## 52. GS/2013/page_220.pdf-3

**排除** · equivalent_percentage_scale

136.2% = 1.362

回报率和指数点/百分数尺度同义弱负例，保守排除。

## 53. LKQ/2010/page_84.pdf-3

**排除** · reference_ratio_not_amount

2014 payments = 37660 thousand

题问 sum/金额，参考给占总额比例 0.1212，量纲不符合。

## 54. GPN/2013/page_92.pdf-3

**排除** · source_binding_repair

11057/57096

首年 11057 被绑定 total 行重复表头，而非 table_0。

## 55. UAA/2016/page_83.pdf-4

**排除** · source_binding_repair

(176138+166961+142987)/1355605

2017 值 176138 被绑定到 2018 行 table_1，须修来源。

## 56. AOS/2010/page_18.pdf-2

**排除** · equivalent_percentage_scale

0.652 = 65.2 percentage points

两程序度量同一收益差，未作为确定错误偏好。

## 57. ETR/2008/page_343.pdf-1

**排除** · unsupported_cashflow_reconciliation

20997-(-66044)=87041 thousand under cash-only assumption

从应收转应付可表示资金流入，但两余额未单独证明全部现金流，且正文提及先前非现金转票据。不把假设作为严格事实。

## 58. SNA/2013/page_84.pdf-1

**通过** · wrong_denominator

14.9/546.5

2013 坏账准备占同年毛应收 546.5 的比例；负例分母是 2012 坏账准备 19。使用准备绝对额为覆盖率惯例。

## 59. APTV/2018/page_36.pdf-2

**排除** · equivalent_percentage_scale

0.2391 = 23.91 percentage points

同一五年表现差，百分比小数尺度负例排除。

## 60. MAS/2018/page_60.pdf-2

**通过** · wrong_denominator

64/549

修订 goodwill 64 除修订总购买价 549；负例以初始 goodwill 46 为分母。
