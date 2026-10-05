# 真实模型错误：DPO 偏好候选审核

共 101 对。按事前协议由助手审核前 60 对：22 对通过、38 对排除，余下 41 对 pending；人工审核数为 0。通过样本已与此前 10 对合并，用于 week1-dpo-v1 小规模 DPO。详见 [逐题审核报告](assistant-expanded-v1/REPORT.zh.md)。下方保留生成时的原始候选与证据。

## 你怎么审核

先看前 5 对，每题核对：chosen 的公司、年份、指标、分母、单位是否正确；rejected 的程序是否确实错误。两边可能都合理、有标签疑点或无法判断时，不要批准。

在 review.csv 中填写 decision=approve/reject，未看完保持 pending；notes 记录理由。只有 approve 才能由 export-dpo 导出。

rejected 保留模型选出的程序，但 answer 已替换成该程序的真实执行值，因此比较针对选数/选运算；原始模型输出也保留供审计。自动年份疑点未加入候选，但其余样本不保证没有语义错误。

这批是审核起点，不承诺其数量足够得到可靠 DPO 提升；先确认标签质量，再扩充训练集采样。

## 1. ETR/2008/page_153.pdf-3

Evidence:
[text_0] entergy corporation and subsidiaries notes to financial statements computed on a rolling 12 month basis .
[text_1] as of december 31 , 2008 , entergy louisiana was in compliance with these provisions .
[text_2] as of december 31 , 2008 , entergy louisiana had future minimum lease payments ( reflecting an overall implicit rate of 7.45% ( 7.45 % ) ) in connection with the waterford 3 sale and leaseback transactions , which are recorded as long-term debt , as follows : amount ( in thousands ) .
[text_3] grand gulf lease obligations in december 1988 , in two separate but substantially identical transactions , system energy sold and leased back undivided ownership interests in grand gulf for the aggregate sum of $ 500 million .
[text_4] the interests represent approximately 11.5% ( 11.5 % ) of grand gulf .
[text_5] the leases expire in 2015 .
[text_6] under certain circumstances , system entergy may repurchase the leased interests prior to the end of the term of the leases .
[text_7] at the end of the lease terms , system energy has the option to repurchase the leased interests in grand gulf at fair market value or to renew the leases for either fair market value or , under certain conditions , a fixed rate .
[text_8] in may 2004 , system energy caused the grand gulf lessors to refinance the outstanding bonds that they had issued to finance the purchase of their undivided interest in grand gulf .
[text_9] the refinancing is at a lower interest rate , and system energy's lease payments have been reduced to reflect the lower interest costs .
[text_10] system energy is required to report the sale-leaseback as a financing transaction in its financial statements .
[text_11] for financial reporting purposes , system energy expenses the interest portion of the lease obligation and the plant depreciation .
[text_12] however , operating revenues include the recovery of the lease payments because the transactions are accounted for as a sale and leaseback for ratemaking purposes .
[text_13] consistent with a recommendation contained in a ferc audit report , system energy initially recorded as a net regulatory asset the difference between the recovery of the lease payments and the amounts expensed for interest and depreciation and continues to record this difference as a regulatory asset or liability on an ongoing basis , resulting in a zero net balance for the regulatory asset at the end of the lease term .
[text_14] the amount of this net regulatory asset was $ 19.2 million and $ 36.6 million as of december 31 , 2008 and 2007 , respectively. .
[table_0]  | amount ( in thousands )
[table_1] : 2009 | amount ( in thousands ): $ 32452
[table_2] : 2010 | amount ( in thousands ): 35138
[table_3] : 2011 | amount ( in thousands ): 50421
[table_4] : 2012 | amount ( in thousands ): 39067
[table_5] : 2013 | amount ( in thousands ): 26301
[table_6] : years thereafter | amount ( in thousands ): 137858
[table_7] : total | amount ( in thousands ): 321237
[table_8] : less : amount representing interest | amount ( in thousands ): 73512
[table_9] : present value of net minimum lease payments | amount ( in thousands ): $ 247725

Question: not including years 'thereafter' , what is the total lease payments ? ( in $ thousands )

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_7","value":"321237"},{"source":"table_6","value":"137858"}]}],"answer":183379.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_7","value":"321237"},{"source":"table_8","value":"73512"}]},{"op":"divide","args":["#0","const_1000"]}],"answer":394.749}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_7","value":"321237"},{"source":"table_8","value":"73512"}]},{"op":"divide","args":["#0","const_1000"]}],"answer":404749.0}
```

## 2. APTV/2013/page_48.pdf-1

Evidence:
[text_0] stock performance graph * $ 100 invested on 11/17/11 in our stock or 10/31/11 in the relevant index , including reinvestment of dividends .
[text_1] fiscal year ending december 31 , 2013 .
[text_2] ( 1 ) delphi automotive plc ( 2 ) s&p 500 2013 standard & poor 2019s 500 total return index ( 3 ) automotive supplier peer group 2013 russell 3000 auto parts index , including american axle & manufacturing , borgwarner inc. , cooper tire & rubber company , dana holding corp. , delphi automotive plc , dorman products inc. , federal-mogul corp. , ford motor co. , fuel systems solutions inc. , general motors co. , gentex corp. , gentherm inc. , genuine parts co. , johnson controls inc. , lkq corp. , lear corp. , meritor inc. , remy international inc. , standard motor products inc. , stoneridge inc. , superior industries international , trw automotive holdings corp. , tenneco inc. , tesla motors inc. , the goodyear tire & rubber co. , tower international inc. , visteon corp. , and wabco holdings inc .
[text_3] company index november 17 , december 31 , december 31 , december 31 .
[text_4] dividends on february 26 , 2013 , the board of directors approved the initiation of dividend payments on the company's ordinary shares .
[text_5] the board of directors declared a regular quarterly cash dividend of $ 0.17 per ordinary share that was paid in each quarter of 2013 .
[text_6] in addition , in january 2014 , the board of directors declared a regular quarterly cash dividend of $ 0.25 per ordinary share , payable on february 27 , 2014 to shareholders of record at the close of business on february 18 , 2014 .
[text_7] in october 2011 , the board of managers of delphi automotive llp approved a distribution of approximately $ 95 million , which was paid on december 5 , 2011 , principally in respect of taxes , to members of delphi automotive llp who held membership interests as of the close of business on october 31 , 2011. .
[table_0] company index | november 17 2011 | december 31 2011 | december 31 2012 | december 31 2013
[table_1] company index: delphi automotive plc ( 1 ) | november 17 2011: $ 100.00 | december 31 2011: $ 100.98 | december 31 2012: $ 179.33 | december 31 2013: $ 285.81
[table_2] company index: s&p 500 ( 2 ) | november 17 2011: 100.00 | december 31 2011: 100.80 | december 31 2012: 116.93 | december 31 2013: 154.80
[table_3] company index: automotive supplier peer group ( 3 ) | november 17 2011: 100.00 | december 31 2011: 89.27 | december 31 2012: 110.41 | december 31 2013: 166.46

Question: what is the increase in the dividend in total for the year of 2014?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_6","value":"0.25"},{"source":"text_5","value":"0.17"}]},{"op":"multiply","args":["#0","const_4"]}],"answer":0.32}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_6","value":"0.25"},{"source":"text_5","value":"0.17"}]}],"answer":0.08}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_6","value":"0.25"},{"source":"text_5","value":"0.17"}]}],"answer":0.08}
```

## 3. GPN/2017/page_77.pdf-1

Evidence:
[text_0] the estimated acquisition-date fair values of major classes of assets acquired and liabilities assumed , including a reconciliation to the total purchase consideration , are as follows ( in thousands ) : .
[text_1] goodwill of $ 203.8 million arising from the acquisition , included in the asia-pacific segment , was attributable to expected growth opportunities in australia and new zealand , as well as growth opportunities and operating synergies in integrated payments in our existing asia-pacific and north america markets .
[text_2] goodwill associated with this acquisition is not deductible for income tax purposes .
[text_3] the customer-related intangible assets have an estimated amortization period of 15 years .
[text_4] the acquired technology has an estimated amortization period of 15 years .
[text_5] the trade name has an estimated amortization period of 5 years .
[text_6] note 3 2014 settlement processing assets and obligations funds settlement refers to the process of transferring funds for sales and credits between card issuers and merchants .
[text_7] for transactions processed on our systems , we use our internal network to provide funding instructions to financial institutions that in turn fund the merchants .
[text_8] we process funds settlement under two models , a sponsorship model and a direct membership model .
[text_9] under the sponsorship model , we are designated as a merchant service provider by mastercard and an independent sales organization by visa , which means that member clearing banks ( 201cmember 201d ) sponsor us and require our adherence to the standards of the payment networks .
[text_10] in certain markets , we have sponsorship or depository and clearing agreements with financial institution sponsors .
[text_11] these agreements allow us to route transactions under the members 2019 control and identification numbers to clear credit card transactions through mastercard and visa .
[text_12] in this model , the standards of the payment networks restrict us from performing funds settlement or accessing merchant settlement funds , and , instead , require that these funds be in the possession of the member until the merchant is funded .
[text_13] under the direct membership model , we are members in various payment networks , allowing us to process and fund transactions without third-party sponsorship .
[text_14] in this model , we route and clear transactions directly through the card brand 2019s network and are not restricted from performing funds settlement .
[text_15] otherwise , we process these transactions similarly to how we process transactions in the sponsorship model .
[text_16] we are required to adhere to the standards of the payment networks in which we are direct members .
[text_17] we maintain relationships with financial institutions , which may also serve as our member sponsors for other card brands or in other markets , to assist with funds settlement .
[text_18] timing differences , interchange fees , merchant reserves and exception items cause differences between the amount received from the payment networks and the amount funded to the merchants .
[text_19] these intermediary balances arising in our settlement process for direct merchants are reflected as settlement processing assets and obligations on our consolidated balance sheets .
[text_20] settlement processing assets and obligations include the components outlined below : 2022 interchange reimbursement .
[text_21] our receivable from merchants for the portion of the discount fee related to reimbursement of the interchange fee .
[text_22] global payments inc .
[text_23] | 2017 form 10-k annual report 2013 77 .
[table_0] cash | $ 45826
[table_1] cash: customer-related intangible assets | $ 45826: 42721
[table_2] cash: acquired technology | $ 45826: 27954
[table_3] cash: trade name | $ 45826: 2901
[table_4] cash: other assets | $ 45826: 2337
[table_5] cash: deferred income tax assets ( liabilities ) | $ 45826: -9788 ( 9788 )
[table_6] cash: other liabilities | $ 45826: -49797 ( 49797 )
[table_7] cash: total identifiable net assets | $ 45826: 62154
[table_8] cash: goodwill | $ 45826: 203828
[table_9] cash: total purchase consideration | $ 45826: $ 265982

Question: what portion of the total identifiable net assets is in cash?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_7","value":"45826"},{"source":"table_7","value":"62154"}]}],"answer":0.7372976799562377}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_7","value":"62154"},{"source":"table_7","value":"45826"}]}],"answer":1.3563042814122988}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_7","value":"62154"},{"source":"table_7","value":"45826"}]}],"answer":1.3511111111111112}
```

## 4. AON/2015/page_96.pdf-1

Evidence:
[text_0] other information related to the company's share options is as follows ( in millions ) : .
[text_1] unamortized deferred compensation expense , which includes both options and rsus , amounted to $ 378 million as of december 31 , 2015 , with a remaining weighted-average amortization period of approximately 2.1 years .
[text_2] employee share purchase plan united states the company has an employee share purchase plan that provides for the purchase of a maximum of 7.5 million shares of the company's ordinary shares by eligible u.s .
[text_3] employees .
[text_4] the company's ordinary shares were purchased at 6-month intervals at 85% ( 85 % ) of the lower of the fair market value of the ordinary shares on the first or last day of each 6-month period .
[text_5] in 2015 , 2014 , and 2013 , 411636 shares , 439000 shares and 556000 shares , respectively , were issued to employees under the plan .
[text_6] compensation expense recognized was $ 9 million in 2015 , $ 7 million in 2014 , and $ 6 million in 2013 .
[text_7] united kingdom the company also has an employee share purchase plan for eligible u.k .
[text_8] employees that provides for the purchase of shares after a 3-year period and that is similar to the u.s .
[text_9] plan previously described .
[text_10] three-year periods began in 2015 , 2014 , 2013 , allowing for the purchase of a maximum of 100000 , 300000 , and 350000 shares , respectively .
[text_11] in 2015 , 2014 , and 2013 , 2779 shares , 642 shares , and 172110 shares , respectively , were issued under the plan .
[text_12] compensation expense of $ 2 million was recognized in 2015 and 2014 , as compared to $ 1 million of compensation expense in 2013 .
[text_13] 12 .
[text_14] derivatives and hedging the company is exposed to market risks , including changes in foreign currency exchange rates and interest rates .
[text_15] to manage the risk related to these exposures , the company enters into various derivative instruments that reduce these risks by creating offsetting exposures .
[text_16] the company does not enter into derivative transactions for trading or speculative purposes .
[text_17] foreign exchange risk management the company is exposed to foreign exchange risk when it earns revenues , pays expenses , or enters into monetary intercompany transfers denominated in a currency that differs from its functional currency , or other transactions that are denominated in a currency other than its functional currency .
[text_18] the company uses foreign exchange derivatives , typically forward contracts , options and cross-currency swaps , to reduce its overall exposure to the effects of currency fluctuations on cash flows .
[text_19] these exposures are hedged , on average , for less than two years .
[text_20] these derivatives are accounted for as hedges , and changes in fair value are recorded each period in other comprehensive income ( loss ) in the consolidated statements of comprehensive income .
[text_21] the company also uses foreign exchange derivatives , typically forward contracts and options to economically hedge the currency exposure of the company's global liquidity profile , including monetary assets or liabilities that are denominated in a non-functional currency of an entity , typically on a rolling 30-day basis , but may be for up to one year in the future .
[text_22] these derivatives are not accounted for as hedges , and changes in fair value are recorded each period in other income in the consolidated statements of income. .
[table_0]  | 2015 | 2014 | 2013
[table_1] : aggregate intrinsic value of stock options exercised | 2015: $ 104 | 2014: $ 61 | 2013: $ 73
[table_2] : cash received from the exercise of stock options | 2015: 40 | 2014: 38 | 2013: 61
[table_3] : tax benefit realized from the exercise of stock options | 2015: 36 | 2014: 16 | 2013: 15

Question: what was the average number of shares issued to employees from 2013 to 2015

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_5","value":"411636"},{"source":"text_5","value":"439000"}]}],"answer":850636.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_5","value":"411636"},{"source":"text_5","value":"411636"}]}],"answer":1.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_5","value":"411636"},{"source":"text_5","value":"411636"}]}],"answer":1.0}
```

## 5. SNPS/2012/page_62.pdf-1

Evidence:
[text_0] synopsys , inc .
[text_1] notes to consolidated financial statements 2014continued acquisition of magma design automation , inc .
[text_2] ( magma ) on february 22 , 2012 , the company acquired all outstanding shares of magma , a chip design software provider , at a per-share price of $ 7.35 .
[text_3] additionally , the company assumed unvested restricted stock units ( rsus ) and stock options , collectively called 201cequity awards . 201d the aggregate purchase price was approximately $ 550.2 million .
[text_4] this acquisition enables the company to more rapidly meet the needs of leading-edge semiconductor designers for more sophisticated design tools .
[text_5] as of october 31 , 2012 , the total purchase consideration and the preliminary purchase price allocation were as follows: .
[text_6] goodwill of $ 316.3 million , which is not deductible for tax purposes , primarily resulted from the company 2019s expectation of sales growth and cost synergies from the integration of magma 2019s technology and operations with the company 2019s technology and operations .
[text_7] identifiable intangible assets , consisting primarily of technology , customer relationships , backlog and trademarks , were valued using the income method , and are being amortized over three to ten years .
[text_8] acquisition-related costs directly attributable to the business combination totaling $ 33.5 million for fiscal 2012 were expensed as incurred in the consolidated statements of operations and consist primarily of employee separation costs , contract terminations , professional services , and facilities closure costs .
[text_9] fair value of equity awards assumed .
[text_10] the company assumed unvested restricted stock units ( rsus ) and stock options with a fair value of $ 22.2 million .
[text_11] the black-scholes option-pricing model was used to determine the fair value of these stock options , whereas the fair value of the rsus was based on the market price on the grant date of the instruments .
[text_12] the black-scholes option-pricing model incorporates various subjective assumptions including expected volatility , expected term and risk-free interest rates .
[text_13] the expected volatility was estimated by a combination of implied and historical stock price volatility of the options .
[text_14] of the total fair value of the equity awards assumed , $ 6.8 million was allocated to the purchase consideration and $ 15.4 million was allocated to future services to be expensed over their remaining service periods on a straight-line basis .
[text_15] supplemental pro forma information ( unaudited ) .
[text_16] the financial information in the table below summarizes the combined results of operations of the company and magma , on a pro forma basis , as though the companies had been combined as of the beginning of fiscal 2011. .
[table_0]  | ( in thousands )
[table_1] : cash paid | ( in thousands ): $ 543437
[table_2] : fair value of assumed equity awards allocated to purchase consideration | ( in thousands ): 6797
[table_3] : total purchase consideration | ( in thousands ): $ 550234
[table_4] : goodwill | ( in thousands ): 316263
[table_5] : identifiable intangibles assets acquired | ( in thousands ): 184300
[table_6] : cash and other assets acquired | ( in thousands ): 116265
[table_7] : debt and liabilities assumed | ( in thousands ): -66594 ( 66594 )
[table_8] : total purchase allocation | ( in thousands ): $ 550234

Question: what percentage of the total purchase consideration was for intangible assets?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_4","value":"316263"},{"source":"table_5","value":"184300"}]},{"op":"divide","args":["#0",{"source":"table_3","value":"550234"}]}],"answer":0.9097274977555004}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_5","value":"184300"},{"source":"table_8","value":"550234"}]}],"answer":0.3349484037700324}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_5","value":"184300"},{"source":"table_8","value":"550234"}]}],"answer":0.3341111111111111}
```

## 6. MRO/2008/page_119.pdf-2

Evidence:
[text_0] marathon oil corporation notes to consolidated financial statements 7 .
[text_1] dispositions outside-operated norwegian properties 2013 on october 31 , 2008 , we closed the sale of our norwegian outside-operated properties and undeveloped offshore acreage in the heimdal area of the norwegian north sea for net proceeds of $ 301 million , with a pretax gain of $ 254 million as of december 31 , 2008 .
[text_2] pilot travel centers 2013 on october 8 , 2008 , we completed the sale of our 50 percent ownership interest in ptc .
[text_3] sale proceeds were $ 625 million , with a pretax gain on the sale of $ 126 million .
[text_4] immediately preceding the sale , we received a $ 75 million partial redemption of our ownership interest from ptc that was accounted for as a return of investment .
[text_5] operated irish properties 2013 on december 17 , 2008 , we agreed to sell our operated properties located in ireland for proceeds of $ 180 million , before post-closing adjustments and cash on hand at closing .
[text_6] closing is subject to completion of the necessary administrative processes .
[text_7] as of december 31 , 2008 , operating assets and liabilities were classified as held for sale , as disclosed by major class in the following table : ( in millions ) 2008 .
[text_8] 8 .
[text_9] discontinued operations on june 2 , 2006 , we sold our russian oil exploration and production businesses in the khanty-mansiysk region of western siberia .
[text_10] under the terms of the agreement , we received $ 787 million for these businesses , plus preliminary working capital and other closing adjustments of $ 56 million , for a total transaction value of $ 843 million .
[text_11] proceeds net of transaction costs and cash held by the russian businesses at the transaction date totaled $ 832 million .
[text_12] a gain on the sale of $ 243 million ( $ 342 million before income taxes ) was reported in discontinued operations for 2006 .
[text_13] income taxes on this gain were reduced by the utilization of a capital loss carryforward .
[text_14] exploration and production segment goodwill of $ 21 million was allocated to the russian assets and reduced the reported gain .
[text_15] adjustments to the sales price were completed in 2007 and an additional gain on the sale of $ 8 million ( $ 13 million before income taxes ) was recognized .
[text_16] the activities of the russian businesses have been reported as discontinued operations in the consolidated statements of income and the consolidated statements of cash flows for 2006 .
[text_17] revenues applicable to discontinued operations were $ 173 million and pretax income from discontinued operations was $ 45 million for 2006. .
[table_0] ( in millions ) | 2008
[table_1] ( in millions ): current assets | 2008: $ 164
[table_2] ( in millions ): noncurrent assets | 2008: 103
[table_3] ( in millions ): total assets | 2008: 267
[table_4] ( in millions ): current liabilities | 2008: 62
[table_5] ( in millions ): noncurrent liabilities | 2008: 199
[table_6] ( in millions ): total liabilities | 2008: 261
[table_7] ( in millions ): net assets held for sale | 2008: $ 6

Question: as of december 31 , 2008 what was the average of current assets and \\nnoncurrent assets , in millions?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"164"},{"source":"table_2","value":"103"}]},{"op":"divide","args":["#0","const_2"]}],"answer":133.5}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"164"},{"source":"table_2","value":"103"}]},{"op":"divide","args":["#0",{"source":"table_3","value":"267"}]}],"answer":1.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"164"},{"source":"table_2","value":"103"}]},{"op":"divide","args":["#0",{"source":"table_3","value":"267"}]}],"answer":140.0}
```

## 7. CME/2017/page_99.pdf-2

Evidence:
[text_0] in 2017 , the company granted 440076 shares of restricted class a common stock and 7568 shares of restricted stock units .
[text_1] restricted common stock and restricted stock units generally have a vesting period of two to four years .
[text_2] the fair value related to these grants was $ 58.7 million , which is recognized as compensation expense on an accelerated basis over the vesting period .
[text_3] dividends are accrued on restricted class a common stock and restricted stock units and are paid once the restricted stock vests .
[text_4] in 2017 , the company also granted 203298 performance shares .
[text_5] the fair value related to these grants was $ 25.3 million , which is recognized as compensation expense on an accelerated and straight-lined basis over the vesting period .
[text_6] the vesting of these shares is contingent on meeting stated performance or market conditions .
[text_7] the following table summarizes restricted stock , restricted stock units , and performance shares activity for 2017 : number of shares weighted average grant date fair value .
[text_8] the total fair value of restricted stock , restricted stock units , and performance shares that vested during 2017 , 2016 and 2015 was $ 66.0 million , $ 59.8 million and $ 43.3 million , respectively .
[text_9] under the espp , eligible employees may acquire shares of class a common stock using after-tax payroll deductions made during consecutive offering periods of approximately six months in duration .
[text_10] shares are purchased at the end of each offering period at a price of 90% ( 90 % ) of the closing price of the class a common stock as reported on the nasdaq global select market .
[text_11] compensation expense is recognized on the dates of purchase for the discount from the closing price .
[text_12] in 2017 , 2016 and 2015 , a total of 19936 , 19858 and 19756 shares , respectively , of class a common stock were issued to participating employees .
[text_13] these shares are subject to a six-month holding period .
[text_14] annual expense of $ 0.3 million for the purchase discount was recognized in 2017 , and $ 0.2 million was recognized in both 2016 and 2015 .
[text_15] non-executive directors receive an annual award of class a common stock with a value equal to $ 100000 .
[text_16] non-executive directors may also elect to receive some or all of the cash portion of their annual stipend , up to $ 60000 , in shares of stock based on the closing price at the date of distribution .
[text_17] as a result , 19736 shares , 26439 shares and 25853 shares of class a common stock were issued to non-executive directors during 2017 , 2016 and 2015 , respectively .
[text_18] these shares are not subject to any vesting restrictions .
[text_19] expense of $ 2.5 million , $ 2.4 million and $ 2.5 million related to these stock-based payments was recognized for the years ended december 31 , 2017 , 2016 and 2015 , respectively. .
[table_0]  | number of shares | weightedaveragegrant datefair value
[table_1] : outstanding at december 31 2016 | number of shares: 1820578 | weightedaveragegrant datefair value: $ 98
[table_2] : granted | number of shares: 650942 | weightedaveragegrant datefair value: 129
[table_3] : vested | number of shares: -510590 ( 510590 ) | weightedaveragegrant datefair value: 87
[table_4] : cancelled | number of shares: -401699 ( 401699 ) | weightedaveragegrant datefair value: 95
[table_5] : outstanding at december 31 2017 | number of shares: 1559231 | weightedaveragegrant datefair value: 116

Question: in millions , how much compensation expense was attributable to directors in the years ended december 31 , 2015 through 2017?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_19","value":"2.4"},{"source":"text_19","value":"2.5"}]},{"op":"add","args":["#0",{"source":"text_19","value":"2.5"}]}],"answer":7.4}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_19","value":"2.5"},{"source":"text_19","value":"2.4"}]}],"answer":4.9}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_19","value":"2.5"},{"source":"text_19","value":"2.4"}]}],"answer":4.9}
```

## 8. GRMN/2006/page_91.pdf-2

Evidence:
[text_0] the fair value for these options was estimated at the date of grant using a black-scholes option pricing model with the following weighted-average assumptions for 2006 , 2005 and 2004: .
[text_1] the black-scholes option valuation model was developed for use in estimating the fair value of traded options which have no vesting restrictions and are fully transferable .
[text_2] in addition , option valuation models require the input of highly subjective assumptions , including the expected stock price volatility .
[text_3] because the company 2019s employee stock options have characteristics significantly different from those of traded options , and because changes in the subjective input assumptions can materially affect the fair value estimate , in management 2019s opinion , the existing models do not necessarily provide a reliable single measure of the fair value of its employee stock options .
[text_4] the total fair value of shares vested during 2006 , 2005 , and 2004 was $ 9413 , $ 8249 , and $ 6418 respectively .
[text_5] the aggregate intrinsic values of options outstanding and exercisable at december 30 , 2006 were $ 204.1 million and $ 100.2 million , respectively .
[text_6] the aggregate intrinsic value of options exercised during the year ended december 30 , 2006 was $ 42.8 million .
[text_7] aggregate intrinsic value represents the positive difference between the company 2019s closing stock price on the last trading day of the fiscal period , which was $ 55.66 on december 29 , 2006 , and the exercise price multiplied by the number of options outstanding .
[text_8] as of december 30 , 2006 , there was $ 64.2 million of total unrecognized compensation cost related to unvested share-based compensation awards granted to employees under the option plans .
[text_9] that cost is expected to be recognized over a period of five years .
[text_10] employee stock purchase plan the shareholders also adopted an employee stock purchase plan ( espp ) .
[text_11] up to 2000000 shares of common stock have been reserved for the espp .
[text_12] shares will be offered to employees at a price equal to the lesser of 85% ( 85 % ) of the fair market value of the stock on the date of purchase or 85% ( 85 % ) of the fair market value on the enrollment date .
[text_13] the espp is intended to qualify as an 201cemployee stock purchase plan 201d under section 423 of the internal revenue code .
[text_14] during 2006 , 2005 , and 2004 , 124693 , 112798 , and 117900 shares were purchased under the plan for a total purchase price of $ 3569 , $ 2824 , and $ 2691 , respectively .
[text_15] at december 30 , 2006 , approximately 1116811 shares were available for future issuance. .
[table_0]  | 2006 | 2005 | 2004
[table_1] : weighted average fair value of options granted | 2006: $ 20.01 | 2005: $ 9.48 | 2004: $ 7.28
[table_2] : expected volatility | 2006: 0.3534 | 2005: 0.3224 | 2004: 0.3577
[table_3] : distribution yield | 2006: 1.00% ( 1.00 % ) | 2005: 0.98% ( 0.98 % ) | 2004: 1.30% ( 1.30 % )
[table_4] : expected life of options in years | 2006: 6.3 | 2005: 6.3 | 2004: 6.3
[table_5] : risk-free interest rate | 2006: 5% ( 5 % ) | 2005: 4% ( 4 % ) | 2004: 4% ( 4 % )

Question: considering the weighted average fair value of options , what was the decrease between shares that vested in 2006 and 2005?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_4","value":"9413"},{"source":"table_1","value":"20.01"}]},{"op":"divide","args":[{"source":"text_4","value":"8249"},{"source":"table_1","value":"9.48"}]},{"op":"subtract","args":["#1","#0"]}],"answer":399.73288672119634}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"20.01"},{"source":"table_1","value":"9.48"}]}],"answer":10.53}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"20.01"},{"source":"table_1","value":"9.48"}]}],"answer":0.53}
```

## 9. ETFC/2015/page_27.pdf-2

Evidence:
[text_0] table of contents performance graph the following performance graph shows the cumulative total return to a holder of the company 2019s common stock , assuming dividend reinvestment , compared with the cumulative total return , assuming dividend reinvestment , of the standard & poor ( "s&p" ) 500 index and the dow jones us financials index during the period from december 31 , 2010 through december 31 , 2015. .
[text_1] .
[table_0]  | 12/10 | 12/11 | 12/12 | 12/13 | 12/14 | 12/15
[table_1] : e*trade financial corporation | 12/10: 100.00 | 12/11: 49.75 | 12/12: 55.94 | 12/13: 122.75 | 12/14: 151.59 | 12/15: 185.25
[table_2] : s&p 500 index | 12/10: 100.00 | 12/11: 102.11 | 12/12: 118.45 | 12/13: 156.82 | 12/14: 178.29 | 12/15: 180.75
[table_3] : dow jones us financials index | 12/10: 100.00 | 12/11: 87.16 | 12/12: 110.56 | 12/13: 148.39 | 12/14: 170.04 | 12/15: 170.19

Question: what was the difference in percentage cumulative total return for e*trade financial corporation and the s&p 500 index for the five years ended 12/15?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"185.25"},"const_100"]},{"op":"divide","args":["#0","const_100"]},{"op":"subtract","args":[{"source":"table_2","value":"180.75"},"const_100"]},{"op":"divide","args":["#2","const_100"]},{"op":"subtract","args":["#1","#3"]}],"answer":0.045}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"185.25"},{"source":"table_2","value":"180.75"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"180.75"}]}],"answer":0.024896265560165973}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"185.25"},{"source":"table_2","value":"180.75"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"180.75"}]}],"answer":0.02594117647058824}
```

## 10. TSCO/2017/page_73.pdf-1

Evidence:
[text_0] note 4 - goodwill and other intangible assets : goodwill the company had approximately $ 93.2 million and $ 94.4 million of goodwill at december 30 , 2017 and december 31 , 2016 , respectively .
[text_1] the changes in the carrying amount of goodwill for the years ended december 30 , 2017 and december 31 , 2016 are as follows ( in thousands ) : .
[text_2] goodwill is allocated to each identified reporting unit , which is defined as an operating segment or one level below the operating segment .
[text_3] goodwill is not amortized , but is evaluated for impairment annually and whenever events or changes in circumstances indicate the carrying value of goodwill may not be recoverable .
[text_4] the company completes its impairment evaluation by performing valuation analyses and considering other publicly available market information , as appropriate .
[text_5] the test used to identify the potential for goodwill impairment compares the fair value of a reporting unit with its carrying value .
[text_6] an impairment charge would be recorded to the company 2019s operations for the amount , if any , in which the carrying value exceeds the fair value .
[text_7] in the fourth quarter of fiscal 2017 , the company completed its annual impairment testing of goodwill and no impairment was identified .
[text_8] the company determined that the fair value of each reporting unit ( including goodwill ) was in excess of the carrying value of the respective reporting unit .
[text_9] in reaching this conclusion , the fair value of each reporting unit was determined based on either a market or an income approach .
[text_10] under the market approach , the fair value is based on observed market data .
[text_11] other intangible assets the company had approximately $ 31.3 million of intangible assets other than goodwill at december 30 , 2017 and december 31 , 2016 .
[text_12] the intangible asset balance represents the estimated fair value of the petsense tradename , which is not subject to amortization as it has an indefinite useful life on the basis that it is expected to contribute cash flows beyond the foreseeable horizon .
[text_13] with respect to intangible assets , we evaluate for impairment annually and whenever events or changes in circumstances indicate that the carrying value may not be recoverable .
[text_14] we recognize an impairment loss only if the carrying amount is not recoverable through its discounted cash flows and measure the impairment loss based on the difference between the carrying value and fair value .
[text_15] in the fourth quarter of fiscal 2017 , the company completed its annual impairment testing of intangible assets and no impairment was identified. .
[table_0]  | 2017 | 2016
[table_1] : balance beginning of year | 2017: $ 94417 | 2016: $ 10258
[table_2] : goodwill acquired as part of acquisition | 2017: 2014 | 2016: 84159
[table_3] : working capital settlement | 2017: -1225 ( 1225 ) | 2016: 2014
[table_4] : impairment loss | 2017: 2014 | 2016: 2014
[table_5] : balance end of year | 2017: $ 93192 | 2016: $ 94417

Question: what percent of the 2017 end goodwill balance is the goodwill from the acquisition?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"84159"},{"source":"table_5","value":"94417"}]}],"answer":0.8913543111939587}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"2014"},{"source":"table_5","value":"93192"}]}],"answer":0.021611297107047817}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"2014"},{"source":"table_5","value":"93192"}]}],"answer":0.02121212121212121}
```

## 11. AAPL/2005/page_67.pdf-1

Evidence:
[text_0] notes to consolidated financial statements ( continued ) note 1 2014summary of significant accounting policies ( continued ) asset retirement obligations the company records obligations associated with the retirement of tangible long-lived assets and the associated asset retirement costs in accordance with sfas no .
[text_1] 143 , accounting for asset retirement obligations .
[text_2] the company reviews legal obligations associated with the retirement of long-lived assets that result from the acquisition , construction , development and/or normal use of the assets .
[text_3] if it is determined that a legal obligation exists , the fair value of the liability for an asset retirement obligation is recognized in the period in which it is incurred if a reasonable estimate of fair value can be made .
[text_4] the fair value of the liability is added to the carrying amount of the associated asset and this additional carrying amount is depreciated over the life of the asset .
[text_5] the difference between the gross expected future cash flow and its present value is accreted over the life of the related lease as an operating expense .
[text_6] all of the company 2019s existing asset retirement obligations are associated with commitments to return property subject to operating leases to original condition upon lease termination .
[text_7] the following table reconciles changes in the company 2019s asset retirement liabilities for fiscal 2004 and 2005 ( in millions ) : .
[text_8] cumulative effects of accounting changes in 2003 , the company recognized a net favorable cumulative effect type adjustment of approximately $ 1 million from the adoption of sfas no .
[text_9] 150 , accounting for certain financial instruments with characteristic of both liabilities and equity and sfas no .
[text_10] 143 .
[text_11] long-lived assets including goodwill and other acquired intangible assets the company reviews property , plant , and equipment and certain identifiable intangibles , excluding goodwill , for impairment whenever events or changes in circumstances indicate the carrying amount of an asset may not be recoverable .
[text_12] recoverability of these assets is measured by comparison of its carrying amount to future undiscounted cash flows the assets are expected to generate .
[text_13] if property , plant , and equipment and certain identifiable intangibles are considered to be impaired , the impairment to be recognized equals the amount by which the carrying value of the assets exceeds its fair market value .
[text_14] for the three fiscal years ended september 24 , 2005 , the company had no material impairment of its long-lived assets , except for the impairment of certain assets in connection with the restructuring actions described in note 5 of these notes to consolidated financial statements .
[text_15] sfas no .
[text_16] 142 , goodwill and other intangible assets requires that goodwill and intangible assets with indefinite useful lives should not be amortized but rather be tested for impairment at least annually or sooner whenever events or changes in circumstances indicate that they may be impaired .
[text_17] the company performs its goodwill impairment tests on or about august 30 of each year .
[text_18] the company did not recognize any goodwill or intangible asset impairment charges in 2005 , 2004 , or 2003 .
[text_19] the company established reporting units based on its current reporting structure .
[text_20] for purposes of testing goodwill for .
[table_0] asset retirement liability as of september 27 2003 | $ 7.2
[table_1] asset retirement liability as of september 27 2003: additional asset retirement obligations recognized | $ 7.2: 0.5
[table_2] asset retirement liability as of september 27 2003: accretion recognized | $ 7.2: 0.5
[table_3] asset retirement liability as of september 27 2003: asset retirement liability as of september 25 2004 | $ 7.2: $ 8.2
[table_4] asset retirement liability as of september 27 2003: additional asset retirement obligations recognized | $ 7.2: 2.8
[table_5] asset retirement liability as of september 27 2003: accretion recognized | $ 7.2: 0.7
[table_6] asset retirement liability as of september 27 2003: asset retirement liability as of september 24 2005 | $ 7.2: $ 11.7

Question: what was the change in asset retirement liability between september 2004 and 2005 , in millions?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_6","value":"11.7"},{"source":"table_3","value":"8.2"}]}],"answer":3.5}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_3","value":"8.2"},{"source":"table_3","value":"7.2"}]}],"answer":1.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_3","value":"8.2"},{"source":"table_3","value":"7.2"}]}],"answer":1.0}
```

## 12. LKQ/2016/page_26.pdf-2

Evidence:
[text_0] comparison of cumulative return among lkq corporation , the nasdaq stock market ( u.s. ) index and the peer group .
[text_1] this stock performance information is "furnished" and shall not be deemed to be "soliciting material" or subject to rule 14a , shall not be deemed "filed" for purposes of section 18 of the securities exchange act of 1934 or otherwise subject to the liabilities of that section , and shall not be deemed incorporated by reference in any filing under the securities act of 1933 or the securities exchange act of 1934 , whether made before or after the date of this report and irrespective of any general incorporation by reference language in any such filing , except to the extent that it specifically incorporates the information by reference .
[text_2] information about our common stock that may be issued under our equity compensation plans as of december 31 , 2016 included in part iii , item 12 of this annual report on form 10-k is incorporated herein by reference. .
[table_0]  | 12/31/2011 | 12/31/2012 | 12/31/2013 | 12/31/2014 | 12/31/2015 | 12/31/2016
[table_1] : lkq corporation | 12/31/2011: $ 100 | 12/31/2012: $ 140 | 12/31/2013: $ 219 | 12/31/2014: $ 187 | 12/31/2015: $ 197 | 12/31/2016: $ 204
[table_2] : s&p 500 index | 12/31/2011: $ 100 | 12/31/2012: $ 113 | 12/31/2013: $ 147 | 12/31/2014: $ 164 | 12/31/2015: $ 163 | 12/31/2016: $ 178
[table_3] : peer group | 12/31/2011: $ 100 | 12/31/2012: $ 111 | 12/31/2013: $ 140 | 12/31/2014: $ 177 | 12/31/2015: $ 188 | 12/31/2016: $ 217

Question: what was the difference in percentage cumulative return for lkq corporation and the s&p 500 index for the five years ended 12/31/2016?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"204"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100"}]},{"op":"subtract","args":[{"source":"table_2","value":"178"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#2",{"source":"table_1","value":"100"}]},{"op":"subtract","args":["#1","#3"]}],"answer":0.26}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"204"},{"source":"table_2","value":"178"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"178"}]}],"answer":0.14606741573033707}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"204"},{"source":"table_2","value":"178"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"178"}]}],"answer":0.14214214214214214}
```

## 13. STT/2007/page_65.pdf-2

Evidence:
[text_0] cross-border outstandings to countries in which we do business which amounted to at least 1% ( 1 % ) of our consolidated total assets were as follows as of december 31 : 2007 2006 2005 ( in millions ) .
[text_1] the total cross-border outstandings presented in the table represented 12% ( 12 % ) , 9% ( 9 % ) and 11% ( 11 % ) of our consolidated total assets as of december 31 , 2007 , 2006 and 2005 , respectively .
[text_2] there were no cross- border outstandings to countries which totaled between .75% ( .75 % ) and 1% ( 1 % ) of our consolidated total assets as of december 31 , 2007 .
[text_3] aggregate cross-border outstandings to countries which totaled between .75% ( .75 % ) and 1% ( 1 % ) of our consolidated total assets at december 31 , 2006 , amounted to $ 1.05 billion ( canada ) and at december 31 , 2005 , amounted to $ 1.86 billion ( belgium and japan ) .
[text_4] capital regulatory and economic capital management both use key metrics evaluated by management to ensure that our actual level of capital is commensurate with our risk profile , is in compliance with all regulatory requirements , and is sufficient to provide us with the financial flexibility to undertake future strategic business initiatives .
[text_5] regulatory capital our objective with respect to regulatory capital management is to maintain a strong capital base in order to provide financial flexibility for our business needs , including funding corporate growth and supporting customers 2019 cash management needs , and to provide protection against loss to depositors and creditors .
[text_6] we strive to maintain an optimal level of capital , commensurate with our risk profile , on which an attractive return to shareholders will be realized over both the short and long term , while protecting our obligations to depositors and creditors and satisfying regulatory requirements .
[text_7] our capital management process focuses on our risk exposures , our capital position relative to our peers , regulatory capital requirements and the evaluations of the major independent credit rating agencies that assign ratings to our public debt .
[text_8] the capital committee , working in conjunction with the asset and liability committee , referred to as 2018 2018alco , 2019 2019 oversees the management of regulatory capital , and is responsible for ensuring capital adequacy with respect to regulatory requirements , internal targets and the expectations of the major independent credit rating agencies .
[text_9] the primary regulator of both state street and state street bank for regulatory capital purposes is the federal reserve board .
[text_10] both state street and state street bank are subject to the minimum capital requirements established by the federal reserve board and defined in the federal deposit insurance corporation improvement act of 1991 .
[text_11] state street bank must meet the regulatory capital thresholds for 2018 2018well capitalized 2019 2019 in order for the parent company to maintain its status as a financial holding company. .
[table_0] ( in millions ) | 2007 | 2006 | 2005
[table_1] ( in millions ): united kingdom | 2007: $ 5951 | 2006: $ 5531 | 2005: $ 2696
[table_2] ( in millions ): canada | 2007: 4565 | 2006: 2014 | 2005: 1463
[table_3] ( in millions ): australia | 2007: 3567 | 2006: 1519 | 2005: 1441
[table_4] ( in millions ): netherlands | 2007: 2014 | 2006: 2014 | 2005: 992
[table_5] ( in millions ): germany | 2007: 2944 | 2006: 2696 | 2005: 4217
[table_6] ( in millions ): total cross-border outstandings | 2007: $ 17027 | 2006: $ 9746 | 2005: $ 10809

Question: what are the total consolidated assets in 2006?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"9746"},{"source":"text_1","value":"9%"}]}],"answer":108288.88888888889}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"9746"},{"source":"text_1","value":"12%"}]}],"answer":81216.66666666667}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"9746"},{"source":"text_1","value":"12%"}]}],"answer":812.1666666666666}
```

## 14. AAP/2016/page_65.pdf-2

Evidence:
[text_0] advance auto parts , inc .
[text_1] and subsidiaries notes to the consolidated financial statements december 31 , 2016 , january 2 , 2016 and january 3 , 2015 ( in thousands , except per share data ) 2 .
[text_2] inventories , net : merchandise inventory the company used the lifo method of accounting for approximately 89% ( 89 % ) of inventories at both december 31 , 2016 and january 2 , 2016 .
[text_3] under lifo , the company 2019s cost of sales reflects the costs of the most recently purchased inventories , while the inventory carrying balance represents the costs for inventories purchased in 2016 and prior years .
[text_4] as a result of utilizing lifo , the company recorded a reduction to cost of sales of $ 40711 and $ 42295 in 2016 and 2015 , respectively , and an increase to cost of sales of $ 8930 in 2014 .
[text_5] historically , the company 2019s overall costs to acquire inventory for the same or similar products have generally decreased as the company has been able to leverage its continued growth and execution of merchandise strategies .
[text_6] the increase in cost of sales for 2014 was the result of an increase in supply chain costs .
[text_7] product cores the remaining inventories are comprised of product cores , the non-consumable portion of certain parts and batteries and the inventory of certain subsidiaries , which are valued under the first-in , first-out ( 201cfifo 201d ) method .
[text_8] product cores are included as part of the company 2019s merchandise costs and are either passed on to the customer or returned to the vendor .
[text_9] because product cores are not subject to frequent cost changes like the company 2019s other merchandise inventory , there is no material difference when applying either the lifo or fifo valuation method .
[text_10] inventory overhead costs purchasing and warehousing costs included in inventory as of december 31 , 2016 and january 2 , 2016 , were $ 395240 and $ 359829 , respectively .
[text_11] inventory balance and inventory reserves inventory balances at the end of 2016 and 2015 were as follows : december 31 , january 2 .
[text_12] inventory quantities are tracked through a perpetual inventory system .
[text_13] the company completes physical inventories and other targeted inventory counts in its store locations to ensure the accuracy of the perpetual inventory quantities of merchandise and core inventory .
[text_14] in its distribution centers and branches , the company uses a cycle counting program to ensure the accuracy of the perpetual inventory quantities of merchandise and product core inventory .
[text_15] reserves for estimated shrink are established based on the results of physical inventories conducted by the company and other targeted inventory counts in its stores , results from recent cycle counts in its distribution facilities and historical and current loss trends .
[text_16] the company also establishes reserves for potentially excess and obsolete inventories based on ( i ) current inventory levels , ( ii ) the historical analysis of product sales and ( iii ) current market conditions .
[text_17] the company has return rights with many of its vendors and the majority of excess inventory is returned to its vendors for full credit .
[text_18] in certain situations , the company establishes reserves when less than full credit is expected from a vendor or when liquidating product will result in retail prices below recorded costs. .
[table_0]  | december 312016 | january 22016
[table_1] : inventories at fifo net | december 312016: $ 4120030 | january 22016: $ 4009641
[table_2] : adjustments to state inventories at lifo | december 312016: 205838 | january 22016: 165127
[table_3] : inventories at lifo net | december 312016: $ 4325868 | january 22016: $ 4174768

Question: how the cash flow from operations affected by the increase in inventories at lifo net in 2016?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_3","value":"4174768"},{"source":"table_3","value":"4325868"}]}],"answer":-151100.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"4120030"},{"source":"table_1","value":"4009641"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"4009641"}]}],"answer":0.027530893663547436}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"4120030"},{"source":"table_1","value":"4009641"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"4009641"}]}],"answer":0.0024999999999999998}
```

## 15. C/2010/page_223.pdf-3

Evidence:
[text_0] included in the corporate and consumer loan tables above are purchased distressed loans , which are loans that have evidenced significant credit deterioration subsequent to origination but prior to acquisition by citigroup .
[text_1] in accordance with sop 03-3 , the difference between the total expected cash flows for these loans and the initial recorded investments is recognized in income over the life of the loans using a level yield .
[text_2] accordingly , these loans have been excluded from the impaired loan information presented above .
[text_3] in addition , per sop 03-3 , subsequent decreases to the expected cash flows for a purchased distressed loan require a build of an allowance so the loan retains its level yield .
[text_4] however , increases in the expected cash flows are first recognized as a reduction of any previously established allowance and then recognized as income prospectively over the remaining life of the loan by increasing the loan 2019s level yield .
[text_5] where the expected cash flows cannot be reliably estimated , the purchased distressed loan is accounted for under the cost recovery method .
[text_6] the carrying amount of the company 2019s purchased distressed loan portfolio at december 31 , 2010 was $ 392 million , net of an allowance of $ 77 million as of december 31 , 2010 .
[text_7] the changes in the accretable yield , related allowance and carrying amount net of accretable yield for 2010 are as follows : in millions of dollars accretable carrying amount of loan receivable allowance .
[text_8] ( 1 ) the balance reported in the column 201ccarrying amount of loan receivable 201d consists of $ 130 million of purchased loans accounted for under the level-yield method and $ 0 under the cost-recovery method .
[text_9] these balances represent the fair value of these loans at their acquisition date .
[text_10] the related total expected cash flows for the level-yield loans were $ 131 million at their acquisition dates .
[text_11] ( 2 ) the balance reported in the column 201ccarrying amount of loan receivable 201d consists of $ 315 million of loans accounted for under the level-yield method and $ 154 million accounted for under the cost-recovery method. .
[table_0] in millions of dollars | accretable yield | carrying amount of loan receivable | allowance
[table_1] in millions of dollars: beginning balance | accretable yield: $ 27 | carrying amount of loan receivable: $ 920 | allowance: $ 95
[table_2] in millions of dollars: purchases ( 1 ) | accretable yield: 1 | carrying amount of loan receivable: 130 | allowance: 2014
[table_3] in millions of dollars: disposals/payments received | accretable yield: -11 ( 11 ) | carrying amount of loan receivable: -594 ( 594 ) | allowance: 2014
[table_4] in millions of dollars: accretion | accretable yield: -44 ( 44 ) | carrying amount of loan receivable: 44 | allowance: 2014
[table_5] in millions of dollars: builds ( reductions ) to the allowance | accretable yield: 128 | carrying amount of loan receivable: 2014 | allowance: -18 ( 18 )
[table_6] in millions of dollars: increase to expected cash flows | accretable yield: -2 ( 2 ) | carrying amount of loan receivable: 19 | allowance: 2014
[table_7] in millions of dollars: fx/other | accretable yield: 17 | carrying amount of loan receivable: -50 ( 50 ) | allowance: 2014
[table_8] in millions of dollars: balance at december 31 2010 ( 2 ) | accretable yield: $ 116 | carrying amount of loan receivable: $ 469 | allowance: $ 77

Question: in 2010 what was the percentage change of the carrying amount of loan receivable net of the allowance

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"920"},{"source":"table_1","value":"95"}]},{"op":"subtract","args":[{"source":"table_8","value":"469"},{"source":"table_8","value":"77"}]},{"op":"subtract","args":["#1","#0"]},{"op":"divide","args":["#2","#0"]}],"answer":-0.5248484848484849}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_6","value":"392"},{"source":"text_6","value":"77"}]},{"op":"divide","args":["#0",{"source":"text_6","value":"77"}]}],"answer":4.090909090909091}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_6","value":"392"},{"source":"text_6","value":"77"}]},{"op":"divide","args":["#0",{"source":"text_6","value":"77"}]}],"answer":0.5459016393442553}
```

## 16. GPN/2013/page_87.pdf-1

Evidence:
[text_0] grants of restricted awards are subject to forfeiture if a grantee , among other conditions , leaves our employment prior to expiration of the restricted period .
[text_1] new grants of restricted awards generally vest one year after the date of grant in 25% ( 25 % ) increments over a four year period , with the exception of tsrs which vest after a three year period .
[text_2] the following table summarizes the changes in non-vested restricted stock awards for the years ended may 31 , 2013 and 2012 ( share awards in thousands ) : shares weighted average grant-date fair value .
[text_3] the total fair value of share awards vested during the years ended may 31 , 2013 , 2012 and 2011 was $ 13.6 million , $ 12.9 million and $ 10.8 million , respectively .
[text_4] we recognized compensation expense for restricted stock of $ 16.2 million , $ 13.6 million , and $ 12.5 million in the years ended may 31 , 2013 , 2012 and 2011 , respectively .
[text_5] as of may 31 , 2013 , there was $ 33.5 million of total unrecognized compensation cost related to unvested restricted stock awards that is expected to be recognized over a weighted average period of 2.5 years .
[text_6] employee stock purchase plan we have an employee stock purchase plan under which the sale of 2.4 million shares of our common stock has been authorized .
[text_7] employees may designate up to the lesser of $ 25000 or 20% ( 20 % ) of their annual compensation for the purchase of stock .
[text_8] the price for shares purchased under the plan is 85% ( 85 % ) of the market value on the last day of the quarterly purchase period .
[text_9] as of may 31 , 2013 , 1.0 million shares had been issued under this plan , with 1.4 million shares reserved for future issuance .
[text_10] we recognized compensation expense for the plan of $ 0.5 million in the years ended may 31 , 2013 , 2012 and 2011 .
[text_11] the weighted average grant-date fair value of each designated share purchased under this plan during the years ended may 31 , 2013 , 2012 and 2011 was $ 6 , $ 7 and $ 6 , respectively , which represents the fair value of the 15% ( 15 % ) discount .
[text_12] stock options stock options are granted at 100% ( 100 % ) of fair market value on the date of grant and have 10-year terms .
[text_13] stock options granted vest one year after the date of grant in 25% ( 25 % ) increments over a four year period .
[text_14] the plans provide for accelerated vesting under certain conditions .
[text_15] there were no options granted under the plans during the years ended may 31 , 2013 and may 31 , 2012. .
[table_0]  | shares | weighted averagegrant-datefair value
[table_1] : non-vested at may 31 2011 | shares: 869 | weighted averagegrant-datefair value: $ 40
[table_2] : granted | shares: 472 | weighted averagegrant-datefair value: 48
[table_3] : vested | shares: -321 ( 321 ) | weighted averagegrant-datefair value: 40
[table_4] : forfeited | shares: -79 ( 79 ) | weighted averagegrant-datefair value: 43
[table_5] : non-vested at may 31 2012 | shares: 941 | weighted averagegrant-datefair value: 44
[table_6] : granted | shares: 561 | weighted averagegrant-datefair value: 44
[table_7] : vested | shares: -315 ( 315 ) | weighted averagegrant-datefair value: 43
[table_8] : forfeited | shares: -91 ( 91 ) | weighted averagegrant-datefair value: 44
[table_9] : non-vested at may 31 2013 | shares: 1096 | weighted averagegrant-datefair value: $ 44

Question: what is the total fair value of the granted shares in 2013 , ( in thousands ) ?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"table_6","value":"561"},{"source":"table_6","value":"44"}]}],"answer":24684.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_6","value":"561"},{"source":"table_6","value":"561"}]}],"answer":1122.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_6","value":"561"},{"source":"table_6","value":"561"}]}],"answer":1122.0}
```

## 17. ETR/2004/page_281.pdf-1

Evidence:
[text_0] system energy resources , inc .
[text_1] management's financial discussion and analysis operating activities cash flow from operations increased by $ 232.1 million in 2004 primarily due to income tax refunds of $ 70.6 million in 2004 compared to income tax payments of $ 230.9 million in 2003 .
[text_2] the increase was partially offset by money pool activity , as discussed below .
[text_3] in 2003 , the domestic utility companies and system energy filed , with the irs , a change in tax accounting method notification for their respective calculations of cost of goods sold .
[text_4] the adjustment implemented a simplified method of allocation of overhead to the production of electricity , which is provided under the irs capitalization regulations .
[text_5] the cumulative adjustment placing these companies on the new methodology resulted in a $ 430 million deduction for system energy on entergy's 2003 income tax return .
[text_6] there was no cash benefit from the method change in 2003 .
[text_7] in 2004 system energy realized $ 144 million in cash tax benefit from the method change .
[text_8] this tax accounting method change is an issue across the utility industry and will likely be challenged by the irs on audit .
[text_9] cash flow from operations decreased by $ 124.8 million in 2003 primarily due to the following : 2022 an increase in federal income taxes paid of $ 74.0 million in 2003 compared to 2002 ; 2022 the cessation of the entergy mississippi ggart .
[text_10] system energy collected $ 21.7 million in 2003 and $ 40.8 million in 2002 from entergy mississippi in conjunction with the ggart , which provided for the acceleration of entergy mississippi's grand gulf purchased power obligation .
[text_11] the mpsc authorized cessation of the ggart effective july 1 , 2003 .
[text_12] see note 2 to the domestic utility companies and system energy financial statements for further discussion of the ggart ; and 2022 money pool activity , as discussed below .
[text_13] system energy's receivables from the money pool were as follows as of december 31 for each of the following years: .
[text_14] money pool activity used $ 42.5 million of system energy's operating cash flows in 2004 , used $ 12.0 million in 2003 , and provided $ 6.8 million in 2002 .
[text_15] see note 4 to the domestic utility companies and system energy financial statements for a description of the money pool .
[text_16] investing activities net cash used for investing activities was practically unchanged in 2004 compared to 2003 primarily because an increase in construction expenditures caused by a reclassification of inventory items to capital was significantly offset by the maturity of $ 6.5 million of other temporary investments that had been made in 2003 , which provided cash in 2004 .
[text_17] the increase of $ 16.2 million in net cash used in investing activities in 2003 was primarily due to the following : 2022 the maturity in 2002 of $ 22.4 million of other temporary investments that had been made in 2001 , which provided cash in 2002 ; 2022 an increase in decommissioning trust contributions and realized change in trust assets of $ 8.2 million in 2003 compared to 2002 ; and 2022 other temporary investments of $ 6.5 million made in 2003 .
[text_18] partially offsetting the increases in net cash used in investing activities was a decrease in construction expenditures of $ 22.1 million in 2003 compared to 2002 primarily due to the power uprate project in 2002. .
[table_0] 2004 | 2003 | 2002 | 2001
[table_1] 2004: ( in thousands ) | 2003: ( in thousands ) | 2002: ( in thousands ) | 2001: ( in thousands )
[table_2] 2004: $ 61592 | 2003: $ 19064 | 2002: $ 7046 | 2001: $ 13853

Question: what is the money pool activity use of operating cash flows as a percentage of receivables from the money pool in 2004?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"61592"},"const_1000"]},{"op":"divide","args":[{"source":"text_14","value":"42.5"},"#0"]}],"answer":0.6900246785296792}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_14","value":"42.5"},{"source":"text_14","value":"6.8"}]}],"answer":6.25}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_14","value":"42.5"},{"source":"text_14","value":"6.8"}]}],"answer":62.5}
```

## 18. CME/2017/page_57.pdf-4

Evidence:
[text_0] recognized total losses and expenses of $ 28.6 million , including a net loss on write-down to fair value of the assets and certain other transaction fees of $ 27.1 million within other expenses and $ 1.5 million of legal and other fees .
[text_1] 2022 professional fees and outside services expense decreased in 2017 compared to 2016 , largely due to higher legal and regulatory fees in 2016 related to our business activities and product offerings as well as higher professional fees related to a greater reliance on consultants for security and systems enhancement work .
[text_2] the overall decrease in operating expenses in 2017 when compared with 2016 was partially offset by the following increases : 2022 licensing and other fee sharing agreements expense increased due to higher expense resulting from incentive payments made to facilitate the transition of the russell contract open interest , as well as increased costs of revenue sharing agreements for certain licensed products .
[text_3] the overall increase in 2017 was partially offset by lower expense related to revenue sharing agreements for certain equity and energy contracts due to lower volume for these products compared to 2016 .
[text_4] 2022 compensation and benefits expense increased as a result of higher average headcount primarily in our international locations as well as normal cost of living adjustments .
[text_5] 2016 compared with 2015 operating expenses increased by $ 54.4 million in 2016 when compared with 2015 .
[text_6] the following table shows the estimated impact of key factors resulting in the net decrease in operating expenses .
[text_7] ( dollars in millions ) over-year change change as a percentage of 2015 expenses .
[text_8] overall operating expenses increased in 2016 when compared with 2015 due to the following reasons : 2022 in 2016 , we recognized total losses and expenses of $ 28.6 million , including a net loss on write-down to fair value of the assets and certain other transaction fees of $ 27.1 million within other expenses and $ 1.5 million of legal and other fees as a result of our sale and leaseback of our datacenter .
[text_9] 2022 professional fees and outside services expense increased in 2016 largely due to an increase in legal and regulatory efforts related to our business activities and product offerings as well as an increase in professional fees related to a greater reliance on consultants for security and systems enhancement work .
[text_10] 2022 in 2016 , we recognized a net loss of $ 24.5 million due to an unfavorable change in exchange rates on foreign cash balances , compared with a net loss of $ 11.3 million in 2015 .
[text_11] 2022 licensing and other fee sharing agreements expense increased due to higher expense related to revenue sharing agreements for certain equity and energy contracts due to both higher volume and an increase in license rates for certain equity and energy products. .
[table_0] ( dollars in millions ) | year-over-yearchange | change as apercentage of2015 expenses
[table_1] ( dollars in millions ): loss on datacenter and related legal fees | year-over-yearchange: $ 28.6 | change as apercentage of2015 expenses: 2% ( 2 % )
[table_2] ( dollars in millions ): professional fees and outside services | year-over-yearchange: 24.4 | change as apercentage of2015 expenses: 2
[table_3] ( dollars in millions ): foreign currency exchange rate fluctuation | year-over-yearchange: 13.2 | change as apercentage of2015 expenses: 1
[table_4] ( dollars in millions ): licensing and other fee agreements | year-over-yearchange: 12.0 | change as apercentage of2015 expenses: 1
[table_5] ( dollars in millions ): reorganization severance and retirement costs | year-over-yearchange: -8.1 ( 8.1 ) | change as apercentage of2015 expenses: -1 ( 1 )
[table_6] ( dollars in millions ): real estate taxes and fees | year-over-yearchange: -10.0 ( 10.0 ) | change as apercentage of2015 expenses: -1 ( 1 )
[table_7] ( dollars in millions ): other expenses net | year-over-yearchange: -5.7 ( 5.7 ) | change as apercentage of2015 expenses: 2014
[table_8] ( dollars in millions ): total | year-over-yearchange: $ 54.4 | change as apercentage of2015 expenses: 4% ( 4 % )

Question: how much was the total operating expenses in 2016 in millions of dollars?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_8","value":"54.4"},{"source":"table_8","value":"4%"}]},{"op":"add","args":["#0",{"source":"table_8","value":"54.4"}]}],"answer":1414.4}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_8","value":"54.4"},{"source":"text_5","value":"54.4"}]}],"answer":108.8}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_8","value":"54.4"},{"source":"text_5","value":"54.4"}]}],"answer":108.8}
```

## 19. SWKS/2012/page_116.pdf-2

Evidence:
[text_0] skyworks solutions , inc .
[text_1] notes to consolidated financial statements 2014 ( continued ) maintained a valuation allowance of $ 47.0 million .
[text_2] this valuation allowance is comprised of $ 33.6 million related to u.s .
[text_3] state tax credits , of which $ 3.6 million are state tax credits acquired from aati in fiscal year 2012 , and $ 13.4 million related to foreign deferred tax assets .
[text_4] if these benefits are recognized in a future period the valuation allowance on deferred tax assets will be reversed and up to a $ 46.6 million income tax benefit , and up to a $ 0.4 million reduction to goodwill may be recognized .
[text_5] the company will need to generate $ 209.0 million of future united states federal taxable income to utilize our united states deferred tax assets as of september 28 , 2012 .
[text_6] deferred tax assets are recognized for foreign operations when management believes it is more likely than not that the deferred tax assets will be recovered during the carry forward period .
[text_7] the company will continue to assess its valuation allowance in future periods .
[text_8] as of september 28 , 2012 , the company has united states federal net operating loss carry forwards of approximately $ 74.3 million , including $ 29.5 million related to the acquisition of sige , which will expire at various dates through 2030 and $ 28.1 million related to the acquisition of aati , which will expire at various dates through 2031 .
[text_9] the utilization of these net operating losses is subject to certain annual limitations as required under internal revenue code section 382 and similar state income tax provisions .
[text_10] the company also has united states federal income tax credit carry forwards of $ 37.8 million , of which $ 30.4 million of federal income tax credit carry forwards have not been recorded as a deferred tax asset .
[text_11] the company also has state income tax credit carry forwards of $ 33.6 million , for which the company has provided a valuation allowance .
[text_12] the united states federal tax credits expire at various dates through 2032 .
[text_13] the state tax credits relate primarily to california research tax credits which can be carried forward indefinitely .
[text_14] the company has continued to expand its operations and increase its investments in numerous international jurisdictions .
[text_15] these activities will increase the company 2019s earnings attributable to foreign jurisdictions .
[text_16] as of september 28 , 2012 , no provision has been made for united states federal , state , or additional foreign income taxes related to approximately $ 371.5 million of undistributed earnings of foreign subsidiaries which have been or are intended to be permanently reinvested .
[text_17] it is not practicable to determine the united states federal income tax liability , if any , which would be payable if such earnings were not permanently reinvested .
[text_18] the company 2019s gross unrecognized tax benefits totaled $ 52.4 million and $ 32.1 million as of september 28 , 2012 and september 30 , 2011 , respectively .
[text_19] of the total unrecognized tax benefits at september 28 , 2012 , $ 38.8 million would impact the effective tax rate , if recognized .
[text_20] the remaining unrecognized tax benefits would not impact the effective tax rate , if recognized , due to the company 2019s valuation allowance and certain positions which were required to be capitalized .
[text_21] there are no positions which the company anticipates could change within the next twelve months .
[text_22] a reconciliation of the beginning and ending amount of gross unrecognized tax benefits is as follows ( in thousands ) : unrecognized tax benefits .
[text_23] page 114 annual report .
[table_0]  | unrecognized tax benefits
[table_1] : balance at september 30 2011 | unrecognized tax benefits: $ 32136
[table_2] : increases based on positions related to prior years | unrecognized tax benefits: 9004
[table_3] : increases based on positions related to current year | unrecognized tax benefits: 11265
[table_4] : decreases relating to settlements with taxing authorities | unrecognized tax benefits: 2014
[table_5] : decreases relating to lapses of applicable statutes of limitations | unrecognized tax benefits: -25 ( 25 )
[table_6] : balance at september 28 2012 | unrecognized tax benefits: $ 52380

Question: in 2012 what was the percentage change in the gross unrecognized tax benefits

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_6","value":"52380"},{"source":"table_1","value":"32136"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"32136"}]}],"answer":0.6299477221807319}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"32136"},{"source":"table_6","value":"52380"}]},{"op":"divide","args":["#0",{"source":"table_6","value":"52380"}]}],"answer":-0.38648339060710196}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"32136"},{"source":"table_6","value":"52380"}]},{"op":"divide","args":["#0",{"source":"table_6","value":"52380"}]}],"answer":-0.034234234234234234}
```

## 20. UAA/2016/page_83.pdf-1

Evidence:
[text_0] 2016 , as well as significant sponsorship and other marketing agreements entered into during the period after december 31 , 2016 through the date of this report : ( in thousands ) .
[text_1] total future minimum sponsorship and other payments $ 1355605 the amounts listed above are the minimum compensation obligations and guaranteed royalty fees required to be paid under the company 2019s sponsorship and other marketing agreements .
[text_2] the amounts listed above do not include additional performance incentives and product supply obligations provided under certain agreements .
[text_3] it is not possible to determine how much the company will spend on product supply obligations on an annual basis as contracts generally do not stipulate specific cash amounts to be spent on products .
[text_4] the amount of product provided to the sponsorships depends on many factors including general playing conditions , the number of sporting events in which they participate and the company 2019s decisions regarding product and marketing initiatives .
[text_5] in addition , the costs to design , develop , source and purchase the products furnished to the endorsers are incurred over a period of time and are not necessarily tracked separately from similar costs incurred for products sold to customers .
[text_6] in connection with various contracts and agreements , the company has agreed to indemnify counterparties against certain third party claims relating to the infringement of intellectual property rights and other items .
[text_7] generally , such indemnification obligations do not apply in situations in which the counterparties are grossly negligent , engage in willful misconduct , or act in bad faith .
[text_8] based on the company 2019s historical experience and the estimated probability of future loss , the company has determined that the fair value of such indemnifications is not material to its consolidated financial position or results of operations .
[text_9] from time to time , the company is involved in litigation and other proceedings , including matters related to commercial and intellectual property disputes , as well as trade , regulatory and other claims related to its business .
[text_10] other than as described below , the company believes that all current proceedings are routine in nature and incidental to the conduct of its business , and that the ultimate resolution of any such proceedings will not have a material adverse effect on its consolidated financial position , results of operations or cash flows .
[text_11] on february 10 , 2017 , a shareholder filed a securities case in the united states district court for the district of maryland ( the 201ccourt 201d ) against the company , the company 2019s chief executive officer and the company 2019s former chief financial officer ( brian breece v .
[text_12] under armour , inc. ) .
[text_13] on february 16 , 2017 , a second shareholder filed a securities case in the court against the same defendants ( jodie hopkins v .
[text_14] under armour , inc. ) .
[text_15] the plaintiff in each case purports to represent a class of shareholders for the period between april 21 , 2016 and january 30 , 2017 , inclusive .
[text_16] the complaints allege violations of section 10 ( b ) ( and rule 10b-5 ) of the securities exchange act of 1934 , as amended ( the 201cexchange act 201d ) and section 20 ( a ) control person liability under the exchange act against the officers named in the complaints .
[text_17] in general , the allegations in each case concern disclosures and statements made by .
[table_0] 2017 | $ 176138
[table_1] 2017: 2018 | $ 176138: 166961
[table_2] 2017: 2019 | $ 176138: 142987
[table_3] 2017: 2020 | $ 176138: 124856
[table_4] 2017: 2021 | $ 176138: 118168
[table_5] 2017: 2022 and thereafter | $ 176138: 626495
[table_6] 2017: total future minimum sponsorship and other payments | $ 176138: $ 1355605

Question: what portion of the total future minimum sponsorship and other payments will be due in the next 12 months?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"176138"},{"source":"table_6","value":"1355605"}]}],"answer":0.12993312948830965}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"1355605"},{"source":"table_6","value":"176138"}]}],"answer":7.696266563717085}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"1355605"},{"source":"table_6","value":"176138"}]}],"answer":7.713912091209121}
```

## 21. TSCO/2017/page_28.pdf-1

Evidence:
[text_0] the following is a list of distribution locations including the approximate square footage and if the location is leased or owned: .
[text_1] longview , texas ( b ) 63000 owned ( a ) the leased facility in hagerstown is treated as an extension of the existing owned hagerstown location and is not considered a separate distribution center .
[text_2] ( b ) this is a mixing center designed to process certain high-volume bulk products .
[text_3] the company 2019s store support center occupies approximately 260000 square feet of owned building space in brentwood , tennessee , and the company 2019s merchandising innovation center occupies approximately 32000 square feet of leased building space in nashville , tennessee .
[text_4] the company also leases approximately 8000 square feet of building space for the petsense corporate headquarters located in scottsdale , arizona .
[text_5] in fiscal 2017 , we began construction on a new northeast distribution center in frankfort , new york , as well as an expansion of our existing distribution center in waverly , nebraska , which will provide additional distribution capacity once construction is completed .
[text_6] item 3 .
[text_7] legal proceedings item 103 of sec regulation s-k requires disclosure of certain environmental legal proceedings if the proceeding reasonably involves potential monetary sanctions of $ 100000 or more .
[text_8] we periodically receive information requests and notices of potential noncompliance with environmental laws and regulations from governmental agencies , which are addressed on a case-by-case basis with the relevant agency .
[text_9] the company received a subpoena from the district attorney of yolo county , california , requesting records and information regarding its hazardous waste management and disposal practices in california .
[text_10] the company and the office of the district attorney of yolo county engaged in settlement discussions which resulted in the settlement of the matter .
[text_11] a consent decree reflecting the terms of settlement was filed with the yolo county superior court on june 23 , 2017 .
[text_12] under the settlement , the company agreed to a compliance plan and also agreed to pay a civil penalty and fund supplemental environmental projects furthering consumer protection and environmental enforcement in california .
[text_13] the civil penalty did not differ materially from the amount accrued .
[text_14] the cost of the settlement and the compliance with the consent decree will not have a material effect on our consolidated financial position , results of operations or cash flows .
[text_15] the company is also involved in various litigation matters arising in the ordinary course of business .
[text_16] the company believes that any estimated loss related to such matters has been adequately provided for in accrued liabilities to the extent probable and reasonably estimable .
[text_17] accordingly , the company currently expects these matters will be resolved without material adverse effect on its consolidated financial position , results of operations or cash flows .
[text_18] item 4 .
[text_19] mine safety disclosures not applicable. .
[table_0] distribution facility location | approximate square footage | owned/leased facility
[table_1] distribution facility location: franklin kentucky | approximate square footage: 833000 | owned/leased facility: owned
[table_2] distribution facility location: pendleton indiana | approximate square footage: 764000 | owned/leased facility: owned
[table_3] distribution facility location: macon georgia | approximate square footage: 684000 | owned/leased facility: owned
[table_4] distribution facility location: waco texas | approximate square footage: 666000 | owned/leased facility: owned
[table_5] distribution facility location: casa grande arizona | approximate square footage: 650000 | owned/leased facility: owned
[table_6] distribution facility location: hagerstown maryland ( a ) | approximate square footage: 482000 | owned/leased facility: owned
[table_7] distribution facility location: hagerstown maryland ( a ) | approximate square footage: 309000 | owned/leased facility: leased
[table_8] distribution facility location: waverly nebraska | approximate square footage: 422000 | owned/leased facility: owned
[table_9] distribution facility location: seguin texas ( b ) | approximate square footage: 71000 | owned/leased facility: owned
[table_10] distribution facility location: lakewood washington | approximate square footage: 64000 | owned/leased facility: leased
[table_11] distribution facility location: longview texas ( b ) | approximate square footage: 63000 | owned/leased facility: owned

Question: what is the total square footage of properties charged to sg&a and not cost of sales?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_4","value":"8000"},{"source":"text_3","value":"260000"}]},{"op":"add","args":["#0",{"source":"text_3","value":"32000"}]}],"answer":300000.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_3","value":"684000"},{"source":"table_7","value":"309000"}]}],"answer":993000.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_3","value":"684000"},{"source":"table_7","value":"309000"}]}],"answer":1000000.0}
```

## 22. ETR/2017/page_26.pdf-1

Evidence:
[text_0] amortized over a nine-year period beginning december 2015 .
[text_1] see note 2 to the financial statements for further discussion of the business combination and customer credits .
[text_2] the volume/weather variance is primarily due to the effect of more favorable weather during the unbilled period and an increase in industrial usage , partially offset by the effect of less favorable weather on residential sales .
[text_3] the increase in industrial usage is primarily due to expansion projects , primarily in the chemicals industry , and increased demand from new customers , primarily in the industrial gases industry .
[text_4] the louisiana act 55 financing savings obligation variance results from a regulatory charge for tax savings to be shared with customers per an agreement approved by the lpsc .
[text_5] the tax savings resulted from the 2010-2011 irs audit settlement on the treatment of the louisiana act 55 financing of storm costs for hurricane gustav and hurricane ike .
[text_6] see note 3 to the financial statements for additional discussion of the settlement and benefit sharing .
[text_7] included in other is a provision of $ 23 million recorded in 2016 related to the settlement of the waterford 3 replacement steam generator prudence review proceeding , offset by a provision of $ 32 million recorded in 2015 related to the uncertainty at that time associated with the resolution of the waterford 3 replacement steam generator prudence review proceeding . a0 see note 2 to the financial statements for a discussion of the waterford 3 replacement steam generator prudence review proceeding .
[text_8] entergy wholesale commodities following is an analysis of the change in net revenue comparing 2016 to 2015 .
[text_9] amount ( in millions ) .
[text_10] as shown in the table above , net revenue for entergy wholesale commodities decreased by approximately $ 124 million in 2016 primarily due to : 2022 lower realized wholesale energy prices and lower capacity prices , the amortization of the palisades below- market ppa , and vermont yankee capacity revenue .
[text_11] the effect of the amortization of the palisades below- market ppa and vermont yankee capacity revenue on the net revenue variance from 2015 to 2016 is minimal ; 2022 the sale of the rhode island state energy center in december 2015 .
[text_12] see note 14 to the financial statements for further discussion of the rhode island state energy center sale ; and 2022 lower volume in the entergy wholesale commodities nuclear fleet resulting from more refueling outage days in 2016 as compared to 2015 and larger exercise of resupply options in 2016 as compared to 2015 .
[text_13] see 201cnuclear matters - indian point 201d below for discussion of the extended indian point 2 outage in the second quarter entergy corporation and subsidiaries management 2019s financial discussion and analysis .
[table_0]  | amount ( in millions )
[table_1] : 2015 net revenue | amount ( in millions ): $ 1666
[table_2] : nuclear realized price changes | amount ( in millions ): -149 ( 149 )
[table_3] : rhode island state energy center | amount ( in millions ): -44 ( 44 )
[table_4] : nuclear volume | amount ( in millions ): -36 ( 36 )
[table_5] : fitzpatrick reimbursement agreement | amount ( in millions ): 41
[table_6] : nuclear fuel expenses | amount ( in millions ): 68
[table_7] : other | amount ( in millions ): -4 ( 4 )
[table_8] : 2016 net revenue | amount ( in millions ): $ 1542

Question: what is the percent change in net revenue from 2015 to 2016?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"1666"},{"source":"table_8","value":"1542"}]},{"op":"divide","args":["#0",{"source":"table_8","value":"1542"}]}],"answer":0.08041504539559015}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_8","value":"1542"},{"source":"table_1","value":"1666"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"1666"}]}],"answer":-0.0744297719087635}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_8","value":"1542"},{"source":"table_1","value":"1666"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"1666"}]}],"answer":-0.007154563333333333}
```

## 23. ALXN/2007/page_49.pdf-2

Evidence:
[text_0] the company 2019s stock performance the following graph compares cumulative total return of the company 2019s common stock with the cumulative total return of ( i ) the nasdaq stock market-united states , and ( ii ) the nasdaq biotechnology index .
[text_1] the graph assumes ( a ) $ 100 was invested on july 31 , 2001 in each of the company 2019s common stock , the stocks comprising the nasdaq stock market-united states and the stocks comprising the nasdaq biotechnology index , and ( b ) the reinvestment of dividends .
[text_2] comparison of 65 month cumulative total return* among alexion pharmaceuticals , inc. , the nasdaq composite index and the nasdaq biotechnology index alexion pharmaceuticals , inc .
[text_3] nasdaq composite nasdaq biotechnology .
[text_4] .
[table_0]  | 7/02 | 7/03 | 7/04 | 7/05 | 12/05 | 12/06 | 12/07
[table_1] : alexion pharmaceuticals inc . | 7/02: 100.00 | 7/03: 108.38 | 7/04: 102.64 | 7/05: 167.89 | 12/05: 130.56 | 12/06: 260.41 | 12/07: 483.75
[table_2] : nasdaq composite | 7/02: 100.00 | 7/03: 128.98 | 7/04: 142.51 | 7/05: 164.85 | 12/05: 168.24 | 12/06: 187.43 | 12/07: 204.78
[table_3] : nasdaq biotechnology | 7/02: 100.00 | 7/03: 149.29 | 7/04: 146.51 | 7/05: 176.75 | 12/05: 186.10 | 12/06: 183.89 | 12/07: 187.04

Question: what is the difference between the percent change between 7/02 and 7/03 of the investments into axion and the nasdaq composite?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"128.98"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100"}]},{"op":"subtract","args":[{"source":"table_1","value":"108.38"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#2",{"source":"table_1","value":"100"}]},{"op":"subtract","args":["#3","#1"]}],"answer":-0.206}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"108.38"},{"source":"table_1","value":"100.00"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100.00"}]}],"answer":0.0838}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"108.38"},{"source":"table_1","value":"100.00"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100.00"}]}],"answer":0.0838}
```

## 24. AON/2007/page_171.pdf-2

Evidence:
[text_0] notes to consolidated financial statements the components of accumulated other comprehensive loss , net of related tax , are as follows: .
[text_1] aon corporation .
[table_0] ( millions ) as of december 31 | 2007 | 2006 | 2005
[table_1] ( millions ) as of december 31: net derivative gains ( losses ) | 2007: $ 24 | 2006: $ 15 | 2005: $ -11 ( 11 )
[table_2] ( millions ) as of december 31: net unrealized investment gains | 2007: 76 | 2006: 73 | 2005: 52
[table_3] ( millions ) as of december 31: net foreign exchange translation | 2007: 284 | 2006: 118 | 2005: -119 ( 119 )
[table_4] ( millions ) as of december 31: postretirement plans | 2007: -1110 ( 1110 ) | 2006: -1216 ( 1216 ) | 2005: -1077 ( 1077 )
[table_5] ( millions ) as of december 31: accumulated other comprehensive loss | 2007: $ -726 ( 726 ) | 2006: $ -1010 ( 1010 ) | 2005: $ -1155 ( 1155 )

Question: what is the net change in the balance of net foreign exchange translation from 2006 to 2007?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_3","value":"284"},{"source":"table_3","value":"118"}]}],"answer":166.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_3","value":"284"},{"source":"table_3","value":"118"}]},{"op":"divide","args":["#0",{"source":"table_3","value":"118"}]}],"answer":1.4067796610169492}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_3","value":"284"},{"source":"table_3","value":"118"}]},{"op":"divide","args":["#0",{"source":"table_3","value":"118"}]}],"answer":1.3241975306419753}
```

## 25. SNA/2013/page_84.pdf-2

Evidence:
[text_0] notes to consolidated financial statements ( continued ) goodwill and other intangible assets : goodwill and other indefinite-lived assets are tested for impairment annually or more frequently if events or changes in circumstances indicate that the assets might be impaired .
[text_1] annual impairment tests are performed by the company in the second quarter of each year .
[text_2] snap-on evaluates the existence of goodwill and indefinite-lived intangible asset impairment on the basis of whether the assets are fully recoverable from projected , discounted cash flows of the related business unit or asset .
[text_3] intangible assets with finite lives are amortized over their estimated useful lives using straight-line and accelerated methods depending on the nature of the particular asset .
[text_4] see note 6 for further information on goodwill and other intangible assets .
[text_5] new accounting standards disclosures relating to accumulated other comprehensive income the financial accounting standards board ( 201cfasb 201d ) issued authoritative guidance in february 2013 that amends the presentation of accumulated other comprehensive income and clarifies how to report the effect of significant reclassifications out of accumulated other comprehensive income .
[text_6] the guidance , which became effective for snap-on on a prospective basis at the beginning of its 2013 fiscal year , requires footnote disclosure regarding the changes in accumulated other comprehensive income by component and the line items affected in the statements of earnings .
[text_7] the adoption of this updated authoritative guidance did not have a significant impact on the company 2019s consolidated financial statements .
[text_8] see note 17 for additional information .
[text_9] note 2 : acquisition on may 13 , 2013 , snap-on acquired 100% ( 100 % ) of challenger lifts , inc .
[text_10] ( 201cchallenger 201d ) for a cash purchase price of $ 38.2 million , including post-closing adjustments .
[text_11] challenger designs , manufactures and distributes a comprehensive line of vehicle lifts and accessories to a diverse customer base in the automotive repair sector .
[text_12] the acquisition of the challenger vehicle lift product line complemented and increased snap-on 2019s existing undercar equipment offering , broadened its established capabilities in serving vehicle repair facilities and expanded the company 2019s presence with repair shop owners and managers .
[text_13] for segment reporting purposes , the results of operations and assets of challenger have been included in the repair systems & information group since the date of acquisition .
[text_14] pro forma financial information has not been presented as the net effects of the challenger acquisition were neither significant nor material to snap-on 2019s results of operations or financial position .
[text_15] note 3 : receivables trade and other accounts receivable snap-on 2019s trade and other accounts receivable primarily arise from the sale of tools and diagnostic and equipment products to a broad range of industrial and commercial customers and to snap-on 2019s independent franchise van channel on a non-extended-term basis with payment terms generally ranging from 30 to 120 days .
[text_16] the components of snap-on 2019s trade and other accounts receivable as of 2013 and 2012 year end are as follows : ( amounts in millions ) 2013 2012 .
[text_17] finance and contract receivables soc originates extended-term finance and contract receivables on sales of snap-on product sold through the u.s .
[text_18] franchisee and customer network and to snap-on 2019s industrial and other customers ; snap-on 2019s foreign finance subsidiaries provide similar financing internationally .
[text_19] interest income on finance and contract receivables is included in 201cfinancial services revenue 201d on the accompanying consolidated statements of earnings .
[text_20] 74 snap-on incorporated .
[table_0] ( amounts in millions ) | 2013 | 2012
[table_1] ( amounts in millions ): trade and other accounts receivable | 2013: $ 546.5 | 2012: $ 516.9
[table_2] ( amounts in millions ): allowances for doubtful accounts | 2013: -14.9 ( 14.9 ) | 2012: -19.0 ( 19.0 )
[table_3] ( amounts in millions ): total trade and other accounts receivable 2013 net | 2013: $ 531.6 | 2012: $ 497.9

Question: what is the difference between total sales and total payments received during 2013?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"546.5"},{"source":"table_1","value":"516.9"}]}],"answer":29.6}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_3","value":"531.6"},{"source":"table_3","value":"497.9"}]}],"answer":33.7}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_3","value":"531.6"},{"source":"table_3","value":"497.9"}]}],"answer":33.7}
```

## 26. AWK/2015/page_115.pdf-2

Evidence:
[text_0] note 9 : stock based compensation the company has granted stock option and restricted stock unit ( 201crsus 201d ) awards to non-employee directors , officers and other key employees of the company pursuant to the terms of its 2007 omnibus equity compensation plan ( the 201c2007 plan 201d ) .
[text_1] the total aggregate number of shares of common stock that may be issued under the 2007 plan is 15.5 .
[text_2] as of december 31 , 2015 , 8.4 shares were available for grant under the 2007 plan .
[text_3] shares issued under the 2007 plan may be authorized-but-unissued shares of company stock or reacquired shares of company stock , including shares purchased by the company on the open market .
[text_4] the company recognizes compensation expense for stock awards over the vesting period of the award .
[text_5] the following table presents stock-based compensation expense recorded in operation and maintenance expense in the accompanying consolidated statements of operations for the years ended december 31: .
[text_6] there were no significant stock-based compensation costs capitalized during the years ended december 31 , 2015 , 2014 and 2013 .
[text_7] the cost of services received from employees in exchange for the issuance of stock options and restricted stock awards is measured based on the grant date fair value of the awards issued .
[text_8] the value of stock options and rsus awards at the date of the grant is amortized through expense over the three-year service period .
[text_9] all awards granted in 2015 , 2014 and 2013 are classified as equity .
[text_10] the company receives a tax deduction based on the intrinsic value of the award at the exercise date for stock options and the distribution date for rsus .
[text_11] for each award , throughout the requisite service period , the company recognizes the tax benefits , which have been included in deferred income tax assets , related to compensation costs .
[text_12] the tax deductions in excess of the benefits recorded throughout the requisite service period are recorded to common stockholders 2019 equity or the statement of operations and are presented in the financing section of the consolidated statements of cash flows .
[text_13] the company stratified its grant populations and used historic employee turnover rates to estimate employee forfeitures .
[text_14] the estimated rate is compared to the actual forfeitures at the end of the reporting period and adjusted as necessary .
[text_15] stock options in 2015 , 2014 and 2013 , the company granted non-qualified stock options to certain employees under the 2007 plan .
[text_16] the stock options vest ratably over the three-year service period beginning on january 1 of the year of the grant .
[text_17] these awards have no performance vesting conditions and the grant date fair value is amortized through expense over the requisite service period using the straight-line method and is included in operations and maintenance expense in the accompanying consolidated statements of operations. .
[table_0]  | 2015 | 2014 | 2013
[table_1] : stock options | 2015: $ 2 | 2014: $ 2 | 2013: $ 3
[table_2] : rsus | 2015: 8 | 2014: 10 | 2013: 9
[table_3] : espp | 2015: 1 | 2014: 1 | 2013: 1
[table_4] : stock-based compensation | 2015: 11 | 2014: 13 | 2013: 13
[table_5] : income tax benefit | 2015: -4 ( 4 ) | 2014: -5 ( 5 ) | 2013: -5 ( 5 )
[table_6] : stock-based compensation expense net of tax | 2015: $ 7 | 2014: $ 8 | 2013: $ 8

Question: what was the rate of the income tax benefit based on the stock compensation

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":["const_4",{"source":"table_4","value":"11"}]}],"answer":0.36363636363636365}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_5","value":"4"},{"source":"table_6","value":"8"}]}],"answer":0.5}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_5","value":"4"},{"source":"table_6","value":"8"}]}],"answer":0.5}
```

## 27. MRO/2008/page_99.pdf-2

Evidence:
[text_0] underlying physical transaction occurs .
[text_1] we have not qualified commodity derivative instruments used in our osm or rm&t segments for hedge accounting .
[text_2] as a result , we recognize in net income all changes in the fair value of derivative instruments used in those operations .
[text_3] open commodity derivative positions as of december 31 , 2008 and sensitivity analysis at december 31 , 2008 , our e&p segment held open derivative contracts to mitigate the price risk on natural gas held in storage or purchased to be marketed with our own natural gas production in amounts that were in line with normal levels of activity .
[text_4] at december 31 , 2008 , we had no significant open derivative contracts related to our future sales of liquid hydrocarbons and natural gas and therefore remained substantially exposed to market prices of these commodities .
[text_5] the osm segment holds crude oil options which were purchased by western for a three year period ( january 2007 to december 2009 ) .
[text_6] the premiums for the purchased put options had been partially offset through the sale of call options for the same three-year period , resulting in a net premium liability .
[text_7] payment of the net premium liability is deferred until the settlement of the option contracts .
[text_8] as of december 31 , 2008 , the following put and call options were outstanding: .
[text_9] in the first quarter of 2009 , we sold derivative instruments at an average exercise price of $ 50.50 which effectively offset the open put options for the remainder of 2009 .
[text_10] at december 31 , 2008 , the number of open derivative contracts held by our rm&t segment was lower than in previous periods .
[text_11] starting in the second quarter of 2008 , we decreased our use of derivatives to mitigate crude oil price risk between the time that domestic spot crude oil purchases are priced and when they are actually refined into salable petroleum products .
[text_12] instead , we are addressing this price risk through other means , including changes in contractual terms and crude oil acquisition practices .
[text_13] additionally , in previous periods , certain contracts in our rm&t segment for the purchase or sale of commodities were not qualified or designated as normal purchase or normal sales under generally accepted accounting principles and therefore were accounted for as derivative instruments .
[text_14] during the second quarter of 2008 , as we decreased our use of derivatives , we began to designate such contracts for the normal purchase and normal sale exclusion. .
[table_0] option expiration date | 2009
[table_1] option expiration date: option contract volumes ( barrels per day ) : | 2009: 
[table_2] option expiration date: put options purchased | 2009: 20000
[table_3] option expiration date: call options sold | 2009: 15000
[table_4] option expiration date: average exercise price ( dollars per barrel ) : | 2009: 
[table_5] option expiration date: put options | 2009: $ 50.50
[table_6] option expiration date: call options | 2009: $ 90.50

Question: for option expiration dates in 2009 , what was the average option contract volumes ( barrels per day ) for put options purchased and \\ncall options sold?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"20000"},{"source":"table_3","value":"15000"}]},{"op":"divide","args":["#0","const_2"]}],"answer":17500.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"20000"},{"source":"table_3","value":"15000"}]},{"op":"divide","args":["#0","const_100"]}],"answer":350.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"20000"},{"source":"table_3","value":"15000"}]},{"op":"divide","args":["#0","const_100"]}],"answer":3500.0}
```

## 28. ETR/2008/page_362.pdf-3

Evidence:
[text_0] entergy new orleans , inc .
[text_1] management's financial discussion and analysis ( 1 ) includes approximately $ 30 million annually for maintenance capital , which is planned spending on routine capital projects that are necessary to support reliability of service , equipment or systems and to support normal customer growth .
[text_2] ( 2 ) purchase obligations represent the minimum purchase obligation or cancellation charge for contractual obligations to purchase goods or services .
[text_3] for entergy new orleans , almost all of the total consists of unconditional fuel and purchased power obligations , including its obligations under the unit power sales agreement , which is discussed in note 8 to the financial statements .
[text_4] in addition to the contractual obligations given above , entergy new orleans expects to make payments of approximately $ 113 million for the years 2009-2011 related to hurricane katrina and hurricane gustav restoration work and its gas rebuild project , of which $ 32 million is expected to be incurred in 2009 .
[text_5] also , entergy new orleans expects to contribute $ 1.7 million to its pension plan and $ 5.9 million to its other postretirement plans in 2009 .
[text_6] guidance pursuant to the pension protection act of 2006 rules , effective for the 2008 plan year and beyond , may affect the level of entergy new orleans' pension contributions in the future .
[text_7] also in addition to the contractual obligations , entergy new orleans has $ 26.1 million of unrecognized tax benefits and interest for which the timing of payments beyond 12 months cannot be reasonably estimated due to uncertainties in the timing of effective settlement of tax positions .
[text_8] see note 3 to the financial statements for additional information regarding unrecognized tax benefits .
[text_9] the planned capital investment estimate for entergy new orleans reflects capital required to support existing business .
[text_10] the estimated capital expenditures are subject to periodic review and modification and may vary based on the ongoing effects of regulatory constraints , environmental compliance , market volatility , economic trends , and the ability to access capital .
[text_11] management provides more information on long-term debt and preferred stock maturities in notes 5 and 6 and to the financial statements .
[text_12] sources of capital entergy new orleans' sources to meet its capital requirements include : internally generated funds ; cash on hand ; and debt and preferred stock issuances .
[text_13] entergy new orleans' receivables from or ( payables to ) the money pool were as follows as of december 31 for each of the following years: .
[text_14] see note 4 to the financial statements for a description of the money pool .
[text_15] as discussed above in "bankruptcy proceedings" , entergy new orleans issued notes due in three years in satisfaction of its affiliate prepetition accounts payable , including its indebtedness to the entergy system money pool of $ 37.2 million .
[text_16] entergy new orleans has obtained short-term borrowing authorization from the ferc under which it may borrow through march 2010 , up to the aggregate amount , at any one time outstanding , of $ 100 million .
[text_17] see note 4 to the financial statements for further discussion of entergy new orleans' short-term borrowing limits .
[text_18] the long- term securities issuances of entergy new orleans are limited to amounts authorized by the city council , and the current authorization extends through august 2010. .
[table_0] 2008 | 2007 | 2006 | 2005
[table_1] 2008: ( in thousands ) | 2007: ( in thousands ) | 2006: ( in thousands ) | 2005: ( in thousands )
[table_2] 2008: $ 60093 | 2007: $ 47705 | 2006: ( $ 37166 ) | 2005: ( $ 37166 )

Question: how is cash flow of entergy new orleans affected by the change in balance of money pool from 2007 to 2008 , in thousands?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"47705"},{"source":"table_2","value":"60093"}]}],"answer":-12388.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"60093"},{"source":"table_2","value":"47705"}]}],"answer":12388.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"60093"},{"source":"table_2","value":"47705"}]}],"answer":12388.0}
```

## 29. GS/2014/page_80.pdf-2

Evidence:
[text_0] management 2019s discussion and analysis we believe our credit ratings are primarily based on the credit rating agencies 2019 assessment of : 2030 our liquidity , market , credit and operational risk management practices ; 2030 the level and variability of our earnings ; 2030 our capital base ; 2030 our franchise , reputation and management ; 2030 our corporate governance ; and 2030 the external operating environment , including , in some cases , the assumed level of government or other systemic support .
[text_1] certain of our derivatives have been transacted under bilateral agreements with counterparties who may require us to post collateral or terminate the transactions based on changes in our credit ratings .
[text_2] we assess the impact of these bilateral agreements by determining the collateral or termination payments that would occur assuming a downgrade by all rating agencies .
[text_3] a downgrade by any one rating agency , depending on the agency 2019s relative ratings of us at the time of the downgrade , may have an impact which is comparable to the impact of a downgrade by all rating agencies .
[text_4] we allocate a portion of our gcla to ensure we would be able to make the additional collateral or termination payments that may be required in the event of a two-notch reduction in our long-term credit ratings , as well as collateral that has not been called by counterparties , but is available to them .
[text_5] the table below presents the additional collateral or termination payments related to our net derivative liabilities under bilateral agreements that could have been called at the reporting date by counterparties in the event of a one-notch and two-notch downgrade in our credit ratings. .
[text_6] $ in millions 2014 2013 additional collateral or termination payments for a one-notch downgrade $ 1072 $ 911 additional collateral or termination payments for a two-notch downgrade 2815 2989 cash flows as a global financial institution , our cash flows are complex and bear little relation to our net earnings and net assets .
[text_7] consequently , we believe that traditional cash flow analysis is less meaningful in evaluating our liquidity position than the liquidity and asset-liability management policies described above .
[text_8] cash flow analysis may , however , be helpful in highlighting certain macro trends and strategic initiatives in our businesses .
[text_9] year ended december 2014 .
[text_10] our cash and cash equivalents decreased by $ 3.53 billion to $ 57.60 billion at the end of 2014 .
[text_11] we used $ 22.53 billion in net cash for operating and investing activities , which reflects an initiative to reduce our balance sheet , and the funding of loans receivable .
[text_12] we generated $ 19.00 billion in net cash from financing activities from an increase in bank deposits and net proceeds from issuances of unsecured long-term borrowings , partially offset by repurchases of common stock .
[text_13] year ended december 2013 .
[text_14] our cash and cash equivalents decreased by $ 11.54 billion to $ 61.13 billion at the end of 2013 .
[text_15] we generated $ 4.54 billion in net cash from operating activities .
[text_16] we used net cash of $ 16.08 billion for investing and financing activities , primarily to fund loans receivable and repurchases of common stock .
[text_17] year ended december 2012 .
[text_18] our cash and cash equivalents increased by $ 16.66 billion to $ 72.67 billion at the end of 2012 .
[text_19] we generated $ 9.14 billion in net cash from operating and investing activities .
[text_20] we generated $ 7.52 billion in net cash from financing activities from an increase in bank deposits , partially offset by net repayments of unsecured and secured long-term borrowings .
[text_21] 78 goldman sachs 2014 annual report .
[table_0] $ in millions | as of december 2014 | as of december 2013
[table_1] $ in millions: additional collateral or termination payments for a one-notch downgrade | as of december 2014: $ 1072 | as of december 2013: $ 911
[table_2] $ in millions: additional collateral or termination payments for a two-notch downgrade | as of december 2014: 2815 | as of december 2013: 2989

Question: what is the difference in the required additional collateral or termination payments for a two-notch downgrade and additional collateral or termination payments for a one-notch downgrade in millions in 2013?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"2989"},{"source":"table_1","value":"911"}]}],"answer":2078.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"911"},{"source":"table_2","value":"2989"}]}],"answer":-2078.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"911"},{"source":"table_2","value":"2989"}]}],"answer":-2078.0}
```

## 30. L/2009/page_84.pdf-2

Evidence:
[text_0] item 5 .
[text_1] market for the registrant 2019s common equity , related stockholder matters and issuer purchases of equity securities the following graph compares annual total return of our common stock , the standard & poor 2019s 500 composite stock index ( 201cs&p 500 index 201d ) and our peer group ( 201cloews peer group 201d ) for the five years ended december 31 , 2009 .
[text_2] the graph assumes that the value of the investment in our common stock , the s&p 500 index and the loews peer group was $ 100 on december 31 , 2004 and that all dividends were reinvested. .
[text_3] ( a ) the loews peer group consists of the following companies that are industry competitors of our principal operating subsidiaries : ace limited , w.r .
[text_4] berkley corporation , cabot oil & gas corporation , the chubb corporation , energy transfer partners l.p. , ensco international incorporated , the hartford financial services group , inc. , kinder morgan energy partners , l.p. , noble corporation , range resources corporation , spectra energy corporation ( included from december 14 , 2006 when it began trading ) , transocean , ltd .
[text_5] and the travelers companies , inc .
[text_6] dividend information we have paid quarterly cash dividends on loews common stock in each year since 1967 .
[text_7] regular dividends of $ 0.0625 per share of loews common stock were paid in each calendar quarter of 2009 and 2008 .
[text_8] we paid quarterly cash dividends on the former carolina group stock until the separation .
[text_9] regular dividends of $ 0.455 per share of the former carolina group stock were paid in the first and second quarters of 2008. .
[table_0]  | 2004 | 2005 | 2006 | 2007 | 2008 | 2009
[table_1] : loews common stock | 2004: 100.00 | 2005: 135.92 | 2006: 179.47 | 2007: 219.01 | 2008: 123.70 | 2009: 160.62
[table_2] : s&p 500 index | 2004: 100.00 | 2005: 104.91 | 2006: 121.48 | 2007: 128.16 | 2008: 80.74 | 2009: 102.11
[table_3] : loews peer group ( a ) | 2004: 100.00 | 2005: 133.59 | 2006: 152.24 | 2007: 174.46 | 2008: 106.30 | 2009: 136.35

Question: what is the return on investment for s&p500 from 2007 to 2008?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"80.74"},{"source":"table_2","value":"128.16"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"128.16"}]}],"answer":-0.3700062421972534}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"80.74"},{"source":"table_2","value":"100.00"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"100.00"}]}],"answer":-0.1926}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"80.74"},{"source":"table_2","value":"100.00"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"100.00"}]}],"answer":-0.1926}
```

## 31. GRMN/2006/page_68.pdf-1

Evidence:
[text_0] contractual obligations and commercial commitments future payments due from garmin , as of december 30 , 2006 , aggregated by type of contractual obligation .
[text_1] operating leases describes lease obligations associated with garmin facilities located in the u.s. , taiwan , the u.k. , and canada .
[text_2] purchase obligations are the aggregate of those purchase orders that were outstanding on december 30 , 2006 ; these obligations are created and then paid off within 3 months during the normal course of our manufacturing business .
[text_3] off-balance sheet arrangements we do not have any off-balance sheet arrangements .
[text_4] item 7a .
[text_5] quantitative and qualitative disclosures about market risk market sensitivity we have market risk primarily in connection with the pricing of our products and services and the purchase of raw materials .
[text_6] product pricing and raw materials costs are both significantly influenced by semiconductor market conditions .
[text_7] historically , during cyclical industry downturns , we have been able to offset pricing declines for our products through a combination of improved product mix and success in obtaining price reductions in raw materials costs .
[text_8] inflation we do not believe that inflation has had a material effect on our business , financial condition or results of operations .
[text_9] if our costs were to become subject to significant inflationary pressures , we may not be able to fully offset such higher costs through price increases .
[text_10] our inability or failure to do so could adversely affect our business , financial condition and results of operations .
[text_11] foreign currency exchange rate risk the operation of garmin 2019s subsidiaries in international markets results in exposure to movements in currency exchange rates .
[text_12] we generally have not been significantly affected by foreign exchange fluctuations because the taiwan dollar and british pound have proven to be relatively stable .
[text_13] however , periodically we have experienced significant foreign currency gains and losses due to the strengthening and weakening of the u.s .
[text_14] dollar .
[text_15] the potential of volatile foreign exchange rate fluctuations in the future could have a significant effect on our results of operations .
[text_16] the currencies that create a majority of the company 2019s exchange rate exposure are the taiwan dollar and british pound .
[text_17] garmin corporation , located in shijr , taiwan , uses the local currency as the functional currency .
[text_18] the company translates all assets and liabilities at year-end exchange rates and income and expense accounts at average rates during the year .
[text_19] in order to minimize the effect of the currency exchange fluctuations on our net assets , we have elected to retain most of our taiwan subsidiary 2019s cash and investments in marketable securities denominated in u.s .
[text_20] dollars .
[text_21] the td/usd exchange rate decreased 0.7% ( 0.7 % ) during 2006 , which resulted in a cumulative translation adjustment of negative $ 1.2 million at the end of fiscal 2006 and a net foreign currency loss of $ 3.1 million at garmin corporation during 2006. .
[table_0] contractual obligations | payments due by period total | payments due by period less than 1 year | payments due by period 1-3 years | payments due by period 3-5 years | payments due by period more than 5 years
[table_1] contractual obligations: operating leases | payments due by period total: $ 31145 | payments due by period less than 1 year: $ 3357 | payments due by period 1-3 years: $ 6271 | payments due by period 3-5 years: $ 6040 | payments due by period more than 5 years: $ 15477
[table_2] contractual obligations: purchase obligations | payments due by period total: $ 265409 | payments due by period less than 1 year: $ 265409 | payments due by period 1-3 years: $ 0 | payments due by period 3-5 years: $ 0 | payments due by period more than 5 years: $ 0
[table_3] contractual obligations: total | payments due by period total: $ 296554 | payments due by period less than 1 year: $ 268766 | payments due by period 1-3 years: $ 6271 | payments due by period 3-5 years: $ 6040 | payments due by period more than 5 years: $ 15477

Question: what is the decrease observed in the operating leases with payments due to 3-5 years and payments due to more than 5 years?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"15477"},{"source":"table_1","value":"6040"}]}],"answer":9437.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"6040"},{"source":"table_3","value":"15477"}]}],"answer":-9437.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"6040"},{"source":"table_3","value":"15477"}]}],"answer":-9437.0}
```

## 32. AOS/2010/page_18.pdf-1

Evidence:
[text_0] the graph below shows a five-year comparison of the cumulative shareholder return on the company's common stock with the cumulative total return of the s&p small cap 600 index and the russell 1000 index , both of which are published indices .
[text_1] comparison of five-year cumulative total return from december 31 , 2005 to december 31 , 2010 assumes $ 100 invested with reinvestment of dividends period indexed returns .
[text_2] 2005 2006 2007 2008 2009 2010 smith ( a o ) corp s&p smallcap 600 index russell 1000 index .
[table_0] company/index | baseperiod 12/31/05 | baseperiod 12/31/06 | baseperiod 12/31/07 | baseperiod 12/31/08 | baseperiod 12/31/09 | 12/31/10
[table_1] company/index: a o smith corp | baseperiod 12/31/05: 100.0 | baseperiod 12/31/06: 108.7 | baseperiod 12/31/07: 103.3 | baseperiod 12/31/08: 88.8 | baseperiod 12/31/09: 133.6 | 12/31/10: 178.8
[table_2] company/index: s&p small cap 600 index | baseperiod 12/31/05: 100.0 | baseperiod 12/31/06: 115.1 | baseperiod 12/31/07: 114.8 | baseperiod 12/31/08: 78.1 | baseperiod 12/31/09: 98.0 | 12/31/10: 123.8
[table_3] company/index: russell 1000 index | baseperiod 12/31/05: 100.0 | baseperiod 12/31/06: 115.5 | baseperiod 12/31/07: 122.1 | baseperiod 12/31/08: 76.2 | baseperiod 12/31/09: 97.9 | 12/31/10: 113.6

Question: what was the difference in the cumulative total return for a o smith corp and the s&p small cap 600 index for the five year period ended 12/31/10?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"178.8"},"const_100"]},{"op":"divide","args":["#0","const_100"]},{"op":"subtract","args":[{"source":"table_2","value":"123.8"},"const_100"]},{"op":"divide","args":["#2","const_100"]},{"op":"subtract","args":["#1","#3"]}],"answer":0.55}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"178.8"},{"source":"table_2","value":"123.8"}]}],"answer":55.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"178.8"},{"source":"table_2","value":"123.8"}]}],"answer":55.0}
```

## 33. HUM/2018/page_46.pdf-2

Evidence:
[text_0] stock total return performance the following graph compares our total return to stockholders with the returns of the standard & poor 2019s composite 500 index ( 201cs&p 500 201d ) and the dow jones us select health care providers index ( 201cpeer group 201d ) for the five years ended december 31 , 2018 .
[text_1] the graph assumes an investment of $ 100 in each of our common stock , the s&p 500 , and the peer group on december 31 , 2013 , and that dividends were reinvested when paid. .
[text_2] the stock price performance included in this graph is not necessarily indicative of future stock price performance. .
[table_0]  | 12/31/2013 | 12/31/2014 | 12/31/2015 | 12/31/2016 | 12/31/2017 | 12/31/2018
[table_1] : hum | 12/31/2013: $ 100 | 12/31/2014: $ 140 | 12/31/2015: $ 176 | 12/31/2016: $ 202 | 12/31/2017: $ 247 | 12/31/2018: $ 287
[table_2] : s&p 500 | 12/31/2013: $ 100 | 12/31/2014: $ 114 | 12/31/2015: $ 115 | 12/31/2016: $ 129 | 12/31/2017: $ 157 | 12/31/2018: $ 150
[table_3] : peer group | 12/31/2013: $ 100 | 12/31/2014: $ 128 | 12/31/2015: $ 135 | 12/31/2016: $ 137 | 12/31/2017: $ 173 | 12/31/2018: $ 191

Question: what is the lowest return for the first year of investment?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"114"},{"source":"table_1","value":"100"}]}],"answer":14.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"140"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100"}]}],"answer":0.4}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"140"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100"}]}],"answer":0.4}
```

## 34. AON/2015/page_96.pdf-4

Evidence:
[text_0] other information related to the company's share options is as follows ( in millions ) : .
[text_1] unamortized deferred compensation expense , which includes both options and rsus , amounted to $ 378 million as of december 31 , 2015 , with a remaining weighted-average amortization period of approximately 2.1 years .
[text_2] employee share purchase plan united states the company has an employee share purchase plan that provides for the purchase of a maximum of 7.5 million shares of the company's ordinary shares by eligible u.s .
[text_3] employees .
[text_4] the company's ordinary shares were purchased at 6-month intervals at 85% ( 85 % ) of the lower of the fair market value of the ordinary shares on the first or last day of each 6-month period .
[text_5] in 2015 , 2014 , and 2013 , 411636 shares , 439000 shares and 556000 shares , respectively , were issued to employees under the plan .
[text_6] compensation expense recognized was $ 9 million in 2015 , $ 7 million in 2014 , and $ 6 million in 2013 .
[text_7] united kingdom the company also has an employee share purchase plan for eligible u.k .
[text_8] employees that provides for the purchase of shares after a 3-year period and that is similar to the u.s .
[text_9] plan previously described .
[text_10] three-year periods began in 2015 , 2014 , 2013 , allowing for the purchase of a maximum of 100000 , 300000 , and 350000 shares , respectively .
[text_11] in 2015 , 2014 , and 2013 , 2779 shares , 642 shares , and 172110 shares , respectively , were issued under the plan .
[text_12] compensation expense of $ 2 million was recognized in 2015 and 2014 , as compared to $ 1 million of compensation expense in 2013 .
[text_13] 12 .
[text_14] derivatives and hedging the company is exposed to market risks , including changes in foreign currency exchange rates and interest rates .
[text_15] to manage the risk related to these exposures , the company enters into various derivative instruments that reduce these risks by creating offsetting exposures .
[text_16] the company does not enter into derivative transactions for trading or speculative purposes .
[text_17] foreign exchange risk management the company is exposed to foreign exchange risk when it earns revenues , pays expenses , or enters into monetary intercompany transfers denominated in a currency that differs from its functional currency , or other transactions that are denominated in a currency other than its functional currency .
[text_18] the company uses foreign exchange derivatives , typically forward contracts , options and cross-currency swaps , to reduce its overall exposure to the effects of currency fluctuations on cash flows .
[text_19] these exposures are hedged , on average , for less than two years .
[text_20] these derivatives are accounted for as hedges , and changes in fair value are recorded each period in other comprehensive income ( loss ) in the consolidated statements of comprehensive income .
[text_21] the company also uses foreign exchange derivatives , typically forward contracts and options to economically hedge the currency exposure of the company's global liquidity profile , including monetary assets or liabilities that are denominated in a non-functional currency of an entity , typically on a rolling 30-day basis , but may be for up to one year in the future .
[text_22] these derivatives are not accounted for as hedges , and changes in fair value are recorded each period in other income in the consolidated statements of income. .
[table_0]  | 2015 | 2014 | 2013
[table_1] : aggregate intrinsic value of stock options exercised | 2015: $ 104 | 2014: $ 61 | 2013: $ 73
[table_2] : cash received from the exercise of stock options | 2015: 40 | 2014: 38 | 2013: 61
[table_3] : tax benefit realized from the exercise of stock options | 2015: 36 | 2014: 16 | 2013: 15

Question: what is the average share price for the shares issued to employees in 2015 in u.s.?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"text_6","value":"9"},"const_1000000"]},{"op":"divide","args":["#0",{"source":"text_5","value":"411636"}]}],"answer":21.863976911640382}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_5","value":"411636"},{"source":"text_5","value":"411636"}]}],"answer":1.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_5","value":"411636"},{"source":"text_5","value":"411636"}]}],"answer":1.0}
```

## 35. PKG/2015/page_83.pdf-1

Evidence:
[text_0] interest expense related to capital lease obligations was $ 1.6 million during the year ended december 31 , 2015 , and $ 1.6 million during both the years ended december 31 , 2014 and 2013 .
[text_1] purchase commitments in the table below , we set forth our enforceable and legally binding purchase obligations as of december 31 , 2015 .
[text_2] some of the amounts are based on management 2019s estimates and assumptions about these obligations , including their duration , the possibility of renewal , anticipated actions by third parties , and other factors .
[text_3] because these estimates and assumptions are necessarily subjective , our actual payments may vary from those reflected in the table .
[text_4] purchase orders made in the ordinary course of business are excluded below .
[text_5] any amounts for which we are liable under purchase orders are reflected on the consolidated balance sheets as accounts payable and accrued liabilities .
[text_6] these obligations relate to various purchase agreements for items such as minimum amounts of fiber and energy purchases over periods ranging from one year to 20 years .
[text_7] total purchase commitments were as follows ( dollars in millions ) : .
[text_8] the company purchased a total of $ 299.6 million , $ 265.9 million , and $ 61.7 million during the years ended december 31 , 2015 , 2014 , and 2013 , respectively , under these purchase agreements .
[text_9] the increase in purchases the increase in purchases under these agreements in 2014 , compared with 2013 , relates to the acquisition of boise in fourth quarter 2013 .
[text_10] environmental liabilities the potential costs for various environmental matters are uncertain due to such factors as the unknown magnitude of possible cleanup costs , the complexity and evolving nature of governmental laws and regulations and their interpretations , and the timing , varying costs and effectiveness of alternative cleanup technologies .
[text_11] from 2006 through 2015 , there were no significant environmental remediation costs at pca 2019s mills and corrugated plants .
[text_12] at december 31 , 2015 , the company had $ 24.3 million of environmental-related reserves recorded on its consolidated balance sheet .
[text_13] of the $ 24.3 million , approximately $ 15.8 million related to environmental-related asset retirement obligations discussed in note 12 , asset retirement obligations , and $ 8.5 million related to our estimate of other environmental contingencies .
[text_14] the company recorded $ 7.9 million in 201caccrued liabilities 201d and $ 16.4 million in 201cother long-term liabilities 201d on the consolidated balance sheet .
[text_15] liabilities recorded for environmental contingencies are estimates of the probable costs based upon available information and assumptions .
[text_16] because of these uncertainties , pca 2019s estimates may change .
[text_17] the company believes that it is not reasonably possible that future environmental expenditures for remediation costs and asset retirement obligations above the $ 24.3 million accrued as of december 31 , 2015 , will have a material impact on its financial condition , results of operations , or cash flows .
[text_18] guarantees and indemnifications we provide guarantees , indemnifications , and other assurances to third parties in the normal course of our business .
[text_19] these include tort indemnifications , environmental assurances , and representations and warranties in commercial agreements .
[text_20] at december 31 , 2015 , we are not aware of any material liabilities arising from any guarantee , indemnification , or financial assurance we have provided .
[text_21] if we determined such a liability was probable and subject to reasonable determination , we would accrue for it at that time. .
[table_0] 2016 | $ 95.3
[table_1] 2016: 2017 | $ 95.3: 60.3
[table_2] 2016: 2018 | $ 95.3: 28.0
[table_3] 2016: 2019 | $ 95.3: 28.0
[table_4] 2016: 2020 | $ 95.3: 23.4
[table_5] 2016: thereafter | $ 95.3: 77.0
[table_6] 2016: total | $ 95.3: $ 312.0

Question: \\n\\n\\n\\nof the total purchase commitments , what percentage were due after 2020?\\n

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_5","value":"77.0"},{"source":"table_6","value":"312.0"}]}],"answer":0.2467948717948718}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_4","value":"23.4"},{"source":"table_6","value":"312.0"}]}],"answer":0.075}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_4","value":"23.4"},{"source":"table_6","value":"312.0"}]}],"answer":0.07549019607843148}
```

## 36. CE/2014/page_32.pdf-4

Evidence:
[text_0] celanese purchases of its equity securities information regarding repurchases of our common stock during the three months ended december 31 , 2014 is as follows : period number of shares purchased ( 1 ) average price paid per share total number of shares purchased as part of publicly announced program approximate dollar value of shares remaining that may be purchased under the program ( 2 ) .
[text_1] ___________________________ ( 1 ) includes 27780 and 9537 for october and december 2014 , respectively , related to shares withheld from employees to cover their statutory minimum withholding requirements for personal income taxes related to the vesting of restricted stock units .
[text_2] ( 2 ) our board of directors has authorized the aggregate repurchase of $ 1.4 billion of our common stock since february 2008 .
[text_3] see note 17 - stockholders' equity in the accompanying consolidated financial statements for further information .
[text_4] performance graph the following performance graph and related information shall not be deemed "soliciting material" or to be "filed" with the securities and exchange commission , nor shall such information be incorporated by reference into any future filing under the securities act of 1933 or securities exchange act of 1934 , each as amended , except to the extent that we specifically incorporate it by reference into such filing .
[text_5] comparison of cumulative total return .
[table_0] period | totalnumberof sharespurchased ( 1 ) | averageprice paidper share | total numberof sharespurchased aspart of publiclyannounced program | approximatedollarvalue of sharesremaining thatmay bepurchased underthe program ( 2 )
[table_1] period: october 1 - 31 2014 | totalnumberof sharespurchased ( 1 ): 192580 | averageprice paidper share: $ 58.02 | total numberof sharespurchased aspart of publiclyannounced program: 164800 | approximatedollarvalue of sharesremaining thatmay bepurchased underthe program ( 2 ): $ 490000000
[table_2] period: november 1 - 30 2014 | totalnumberof sharespurchased ( 1 ): 468128 | averageprice paidper share: $ 59.25 | total numberof sharespurchased aspart of publiclyannounced program: 468128 | approximatedollarvalue of sharesremaining thatmay bepurchased underthe program ( 2 ): $ 463000000
[table_3] period: december 1 - 31 2014 | totalnumberof sharespurchased ( 1 ): 199796 | averageprice paidper share: $ 60.78 | total numberof sharespurchased aspart of publiclyannounced program: 190259 | approximatedollarvalue of sharesremaining thatmay bepurchased underthe program ( 2 ): $ 451000000
[table_4] period: total | totalnumberof sharespurchased ( 1 ): 860504 | averageprice paidper share:  | total numberof sharespurchased aspart of publiclyannounced program: 823187 | approximatedollarvalue of sharesremaining thatmay bepurchased underthe program ( 2 ): 

Question: what is the total value paid for purchased shares during december 2014?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"table_3","value":"199796"},{"source":"table_3","value":"60.78"}]},{"op":"divide","args":["#0","const_1000000"]}],"answer":12.14360088}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"table_3","value":"190259"},{"source":"table_3","value":"60.78"}]}],"answer":11563942.02}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"table_3","value":"190259"},{"source":"table_3","value":"60.78"}]}],"answer":115800000.0}
```

## 37. PKG/2005/page_74.pdf-4

Evidence:
[text_0] packaging corporation of america notes to consolidated financial statements ( continued ) december 31 , 2005 10 .
[text_1] commitments and contingencies ( continued ) purchase commitments the company has entered into various purchase agreements to buy minimum amounts of energy over periods ranging from one to two years at fixed prices .
[text_2] total purchase commitments over the next two years are as follows : ( in thousands ) .
[text_3] these purchase agreements are not marked to market .
[text_4] the company purchased $ 12.8 million during the year ended december 31 , 2005 , $ 17.6 million during the year ended december 31 , 2004 , and $ 19.3 million during the year ended december 31 , 2003 under these purchase agreements .
[text_5] litigation on may 14 , 1999 , pca was named as a defendant in two consolidated class action complaints which alleged a civil violation of section 1 of the sherman act .
[text_6] the suits , then captioned winoff industries , inc .
[text_7] v .
[text_8] stone container corporation , mdl no .
[text_9] 1261 ( e.d .
[text_10] pa. ) and general refractories co .
[text_11] v .
[text_12] gaylord container corporation , mdl no .
[text_13] 1261 ( e.d .
[text_14] pa. ) , name pca as a defendant based solely on the allegation that pca is successor to the interests of tenneco packaging inc .
[text_15] and tenneco inc. , both of which were also named as defendants in the suits , along with nine other linerboard and corrugated sheet manufacturers .
[text_16] the complaints allege that the defendants , during the period october 1 , 1993 through november 30 , 1995 , conspired to limit the supply of linerboard , and that the purpose and effect of the alleged conspiracy was to artificially increase prices of corrugated containers and corrugated sheets , respectively .
[text_17] on november 3 , 2003 , pactiv ( formerly known as tenneco packaging ) , tenneco and pca entered into an agreement to settle the class action lawsuits .
[text_18] the settlement agreement provided for a full release of all claims against pca as a result of the class action lawsuits and was approved by the court in an opinion issued on april 21 , 2004 .
[text_19] approximately 160 plaintiffs opted out of the class and together filed about ten direct action complaints in various federal courts across the country .
[text_20] all of the opt-out complaints make allegations against the defendants , including pca , substantially similar to those made in the class actions .
[text_21] the settlement agreement does not cover these direct action cases .
[text_22] these actions have almost all been consolidated as in re linerboard , mdl 1261 ( e.d .
[text_23] pa. ) for pretrial purposes .
[text_24] pactiv , tenneco and pca have reached an agreement to settle all of the opt-out cases .
[text_25] these agreements provide for a full release of all claims against pca as a result of litigation .
[text_26] pca has made no payments to the plaintiffs as a result of the settlement of any of the opt-out suits .
[text_27] as of the date of this filing , we believe it is not reasonably possible that the outcome of any pending litigation related to these matters will have a material adverse effect on our financial position , results of operations or cash flows .
[text_28] pca is also party to various legal actions arising in the ordinary course of business .
[text_29] these legal actions cover a broad variety of claims spanning our entire business .
[text_30] as of the date of this filing , we believe it is .
[table_0] 2006 | $ 2408
[table_1] 2006: 2007 | $ 2408: 1364
[table_2] 2006: total | $ 2408: $ 3772

Question: total purchase commitments over the next two years are what ( in thousands ) ?\\n\\n\\n

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"2408"},{"source":"table_1","value":"1364"}]}],"answer":3772.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"2408"},{"source":"table_2","value":"3772"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"3772"}]}],"answer":1.6383881230116648}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"2408"},{"source":"table_2","value":"3772"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"3772"}]}],"answer":1.2435098039215686}
```

## 38. UA/2009/page_50.pdf-2

Evidence:
[text_0] addition , we are exposed to gains and losses resulting from fluctuations in foreign currency exchange rates on transactions generated by our international subsidiaries in currencies other than their local currencies .
[text_1] these gains and losses are primarily driven by inter-company transactions .
[text_2] these exposures are included in other income ( expense ) , net on the consolidated statements of income .
[text_3] since 2007 , we have used foreign currency forward contracts to reduce the risk from exchange rate fluctuations on inter-company transactions and projected inventory purchases for our canadian subsidiary .
[text_4] beginning in december 2008 , we began using foreign currency forward contracts in order to reduce the risk associated with foreign currency exchange rate fluctuations on inter-company transactions for our european subsidiary .
[text_5] we do not enter into derivative financial instruments for speculative or trading purposes .
[text_6] based on the foreign currency forward contracts outstanding as of december 31 , 2009 , we receive us dollars in exchange for canadian dollars at a weighted average contractual forward foreign currency exchange rate of 1.04 cad per $ 1.00 and us dollars in exchange for euros at a weighted average contractual foreign currency exchange rate of 0.70 eur per $ 1.00 .
[text_7] as of december 31 , 2009 , the notional value of our outstanding foreign currency forward contracts for our canadian subsidiary was $ 15.4 million with contract maturities of 1 month , and the notional value of our outstanding foreign currency forward contracts for our european subsidiary was $ 56.0 million with contract maturities of 1 month .
[text_8] the foreign currency forward contracts are not designated as cash flow hedges , and accordingly , changes in their fair value are recorded in other income ( expense ) , net on the consolidated statements of income .
[text_9] the fair value of our foreign currency forward contracts was $ 0.3 million and $ 1.2 million as of december 31 , 2009 and 2008 , respectively .
[text_10] these amounts are included in prepaid expenses and other current assets on the consolidated balance sheet .
[text_11] refer to note 9 for a discussion of the fair value measurements .
[text_12] other income ( expense ) , net included the following amounts related to changes in foreign currency exchange rates and derivative foreign currency forward contracts: .
[text_13] although we have entered into foreign currency forward contracts to minimize some of the impact of foreign currency exchange rate fluctuations on future cash flows , we cannot be assured that foreign currency exchange rate fluctuations will not have a material adverse impact on our financial condition and results of operations .
[text_14] inflation inflationary factors such as increases in the cost of our product and overhead costs may adversely affect our operating results .
[text_15] although we do not believe that inflation has had a material impact on our financial position or results of operations to date , a high rate of inflation in the future may have an adverse effect on our ability to maintain current levels of gross margin and selling , general and administrative expenses as a percentage of net revenues if the selling prices of our products do not increase with these increased costs. .
[table_0] year ended december 31 , ( in thousands ) | year ended december 31 , 2009 | year ended december 31 , 2008 | 2007
[table_1] year ended december 31 , ( in thousands ): unrealized foreign currency exchange rate gains ( losses ) | year ended december 31 , 2009: $ 5222 | year ended december 31 , 2008: $ -5459 ( 5459 ) | 2007: $ 2567
[table_2] year ended december 31 , ( in thousands ): realized foreign currency exchange rate gains ( losses ) | year ended december 31 , 2009: -261 ( 261 ) | year ended december 31 , 2008: -2166 ( 2166 ) | 2007: 174
[table_3] year ended december 31 , ( in thousands ): unrealized derivative gains ( losses ) | year ended december 31 , 2009: -1060 ( 1060 ) | year ended december 31 , 2008: 1650 | 2007: -243 ( 243 )
[table_4] year ended december 31 , ( in thousands ): realized derivative losses | year ended december 31 , 2009: -4412 ( 4412 ) | year ended december 31 , 2008: -204 ( 204 ) | 2007: -469 ( 469 )

Question: what was the percentage change in the the fair value of our foreign currency forward contracts from 2008 to 2009

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_9","value":"0.3"},{"source":"text_9","value":"1.2"}]},{"op":"divide","args":["#0",{"source":"text_9","value":"1.2"}]}],"answer":-0.75}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_9","value":"1.2"},{"source":"text_9","value":"0.3"}]},{"op":"divide","args":["#0",{"source":"text_9","value":"0.3"}]}],"answer":3.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_9","value":"1.2"},{"source":"text_9","value":"0.3"}]},{"op":"divide","args":["#0",{"source":"text_9","value":"0.3"}]}],"answer":1.0}
```

## 39. GPN/2014/page_92.pdf-1

Evidence:
[text_0] the following table provides certain information as of may 31 , 2014 concerning the shares of the company 2019s common stock that may be issued under existing equity compensation plans .
[text_1] for more information on these plans , see note 11 to notes to consolidated financial statements .
[text_2] plan category number of securities to be issued upon exercise of outstanding options , warrants and rights weighted- average exercise price of outstanding options , warrants and rights number of securities remaining available for future issuance under equity compensation plans ( excluding securities reflected in column ( a ) ) equity compensation plans approved by security holders 766801 $ 40.85 8945694 equity compensation plans not approved by security holders 2014 2014 2014 .
[text_3] the information presented in the table above includes shares of common stock available for issuance other than upon the exercise of an option , warrant or right under the employee stock purchase plan and the 2011 incentive plan .
[text_4] in addition , it includes 977296 shares authorized under the amended and restated 2005 incentive plan and 584004 shares authorized under the 2000 long-term incentive plan .
[text_5] as previously disclosed , we do not intend to issue shares under either the amended and restated 2005 incentive plan or the 2000 long-term incentive plan .
[text_6] item 13 2014 certain relationships and related transactions , and director independence we incorporate by reference in this item 13 the information regarding certain relationships and related transactions between us and our affiliates and the independence of our directors contained under the headings 201ccertain relationships and related transactions 201d and 201cboard independence 201d from our proxy statement to be delivered in connection with our 2014 annual meeting of shareholders .
[text_7] item 14 2014principal accounting fees and services we incorporate by reference in this item 14 the information regarding principal accounting fees and services contained under the heading 201cratification of the reappointment of auditors 201d from our proxy statement to be delivered in connection with our 2014 annual meeting of shareholders. .
[table_0] plan category | number of securities to be issued upon exercise of outstanding options warrants and rights ( a ) | weighted-average exerciseprice of outstanding options warrants and rights ( b ) | number of securitiesremaining available forfuture issuance under equity compensation plans ( excluding securities reflected in column ( a ) ) ( c )
[table_1] plan category: equity compensation plans approved by security holders | number of securities to be issued upon exercise of outstanding options warrants and rights ( a ): 766801 | weighted-average exerciseprice of outstanding options warrants and rights ( b ): $ 40.85 | number of securitiesremaining available forfuture issuance under equity compensation plans ( excluding securities reflected in column ( a ) ) ( c ): 8945694
[table_2] plan category: equity compensation plans not approved by security holders | number of securities to be issued upon exercise of outstanding options warrants and rights ( a ): 2014 | weighted-average exerciseprice of outstanding options warrants and rights ( b ): 2014 | number of securitiesremaining available forfuture issuance under equity compensation plans ( excluding securities reflected in column ( a ) ) ( c ): 2014
[table_3] plan category: total | number of securities to be issued upon exercise of outstanding options warrants and rights ( a ): 766801 | weighted-average exerciseprice of outstanding options warrants and rights ( b ): $ 40.85 | number of securitiesremaining available forfuture issuance under equity compensation plans ( excluding securities reflected in column ( a ) ) ( c ): 8945694

Question: what is the total value of securities issued and approved by security holders , ( in millions ) ?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"table_1","value":"766801"},{"source":"table_1","value":"40.85"}]},{"op":"divide","args":["#0","const_1000000"]}],"answer":31.32382085}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"766801"},{"source":"table_1","value":"8945694"}]},{"op":"divide","args":["#0","const_1000000"]}],"answer":9.712495}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"766801"},{"source":"table_1","value":"8945694"}]},{"op":"divide","args":["#0","const_1000000"]}],"answer":9712595.0}
```

## 40. VLO/2015/page_24.pdf-1

Evidence:
[text_0] table of contents the following table discloses purchases of shares of our common stock made by us or on our behalf during the fourth quarter of 2015 .
[text_1] period total number of shares purchased average price paid per share total number of shares not purchased as part of publicly announced plans or programs ( a ) total number of shares purchased as part of publicly announced plans or programs approximate dollar value of shares that may yet be purchased under the plans or programs ( b ) .
[text_2] ( a ) the shares reported in this column represent purchases settled in the fourth quarter of 2015 relating to ( i ) our purchases of shares in open-market transactions to meet our obligations under stock-based compensation plans , and ( ii ) our purchases of shares from our employees and non-employee directors in connection with the exercise of stock options , the vesting of restricted stock , and other stock compensation transactions in accordance with the terms of our stock-based compensation plans .
[text_3] ( b ) on july 13 , 2015 , we announced that our board of directors approved our purchase of $ 2.5 billion of our outstanding common stock ( with no expiration date ) , which was in addition to the remaining amount available under our $ 3 billion program previously authorized .
[text_4] during the third quarter of 2015 , we completed our purchases under the $ 3 billion program .
[text_5] as of december 31 , 2015 , we had $ 1.3 billion remaining available for purchase under the $ 2.5 billion program. .
[table_0] period | total numberof sharespurchased | averageprice paidper share | total number ofshares notpurchased as part ofpublicly announcedplans or programs ( a ) | total number ofshares purchased aspart of publiclyannounced plans orprograms | approximate dollarvalue of shares thatmay yet be purchasedunder the plans orprograms ( b )
[table_1] period: october 2015 | total numberof sharespurchased: 1658771 | averageprice paidper share: $ 62.12 | total number ofshares notpurchased as part ofpublicly announcedplans or programs ( a ): 842059 | total number ofshares purchased aspart of publiclyannounced plans orprograms: 816712 | approximate dollarvalue of shares thatmay yet be purchasedunder the plans orprograms ( b ): $ 2.0 billion
[table_2] period: november 2015 | total numberof sharespurchased: 2412467 | averageprice paidper share: $ 71.08 | total number ofshares notpurchased as part ofpublicly announcedplans or programs ( a ): 212878 | total number ofshares purchased aspart of publiclyannounced plans orprograms: 2199589 | approximate dollarvalue of shares thatmay yet be purchasedunder the plans orprograms ( b ): $ 1.8 billion
[table_3] period: december 2015 | total numberof sharespurchased: 7008414 | averageprice paidper share: $ 70.31 | total number ofshares notpurchased as part ofpublicly announcedplans or programs ( a ): 980 | total number ofshares purchased aspart of publiclyannounced plans orprograms: 7007434 | approximate dollarvalue of shares thatmay yet be purchasedunder the plans orprograms ( b ): $ 1.3 billion
[table_4] period: total | total numberof sharespurchased: 11079652 | averageprice paidper share: $ 69.25 | total number ofshares notpurchased as part ofpublicly announcedplans or programs ( a ): 1055917 | total number ofshares purchased aspart of publiclyannounced plans orprograms: 10023735 | approximate dollarvalue of shares thatmay yet be purchasedunder the plans orprograms ( b ): $ 1.3 billion

Question: for the fourth quarter ended december 312015 what was the percent of the total number of shares not purchased as part of publicly announced plans or programs in october

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"842059"},{"source":"table_4","value":"1055917"}]}],"answer":0.7974670357613335}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_3","value":"980"},{"source":"table_4","value":"11079652"}]}],"answer":8.845043147564563e-05}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_3","value":"980"},{"source":"table_4","value":"11079652"}]}],"answer":0.0008843304884330488}
```

## 41. STT/2008/page_109.pdf-2

Evidence:
[text_0] as described above , the borrowings are extended on a non-recourse basis .
[text_1] as such , there is no credit or market risk exposure to us on the assets , and as a result the terms of the amlf permit exclusion of the assets from regulatory leverage and risk-based capital calculations .
[text_2] the interest rate on the borrowings is set by the federal reserve bank , and we earn net interest revenue by earning a spread on the difference between the yield we earn on the assets and the rate we pay on the borrowings .
[text_3] for 2008 , we earned net interest revenue associated with this facility of approximately $ 68 million .
[text_4] separately , we currently maintain a commercial paper program under which we can issue up to $ 3 billion with original maturities of up to 270 days from the date of issue .
[text_5] at december 31 , 2008 and 2007 , $ 2.59 billion and $ 2.36 billion , respectively , of commercial paper were outstanding .
[text_6] in addition , state street bank currently has board authority to issue bank notes up to an aggregate of $ 5 billion , including up to $ 2.48 billion of senior notes under the fdic 2019s temporary liquidity guarantee program , instituted by the fdic in october 2008 for qualified senior debt issued through june 30 , 2009 , and up to $ 1 billion of subordinated bank notes ( see note 10 ) .
[text_7] at december 31 , 2008 and 2007 , no notes payable were outstanding , and at december 31 , 2008 , all $ 5 billion was available for issuance .
[text_8] state street bank currently maintains a line of credit of cad $ 800 million , or approximately $ 657 million , to support its canadian securities processing operations .
[text_9] the line of credit has no stated termination date and is cancelable by either party with prior notice .
[text_10] at december 31 , 2008 , no balance was due on this line of credit .
[text_11] note 9 .
[text_12] restructuring charges in december 2008 , we implemented a plan to reduce our expenses from operations and support our long- term growth .
[text_13] in connection with this plan , we recorded aggregate restructuring charges of $ 306 million in our consolidated statement of income .
[text_14] the primary component of the plan was an involuntary reduction of approximately 7% ( 7 % ) of our global workforce , which reduction we expect to be substantially completed by the end of the first quarter of 2009 .
[text_15] other components of the plan included costs related to lease and software license terminations , restructuring of agreements with technology providers and other costs .
[text_16] of the aggregate restructuring charges of $ 306 million , $ 243 million related to severance , a portion of which will be paid in a lump sum or over a defined period , and a portion of which will provide related benefits and outplacement services for approximately 2100 employees identified for involuntary termination in connection with the plan ; $ 49 million related to future lease obligations and write-offs of capitalized assets , including $ 23 million for impairment of other intangible assets ; $ 10 million of costs associated with information technology and $ 4 million of other restructuring costs .
[text_17] the severance component included $ 47 million related to accelerated vesting of equity-based compensation .
[text_18] in december 2008 , approximately 620 employees were involuntarily terminated and left state street .
[text_19] the following table presents the activity in the related balance sheet reserve for 2008 .
[text_20] ( in millions ) severance lease and write-offs information technology other total .
[text_21] .
[table_0] ( in millions ) | severance | lease and asset write-offs | information technology | other | total
[table_1] ( in millions ): initial accrual | severance: $ 250 | lease and asset write-offs: $ 42 | information technology: $ 10 | other: $ 4 | total: $ 306
[table_2] ( in millions ): payments and adjustments | severance: -20 ( 20 ) | lease and asset write-offs: -25 ( 25 ) | information technology: -10 ( 10 ) | other: -1 ( 1 ) | total: -56 ( 56 )
[table_3] ( in millions ): balance at december 31 2008 | severance: $ 230 | lease and asset write-offs: $ 17 | information technology: 2014 | other: $ 3 | total: $ 250

Question: what percent of severence was paid off in 2008?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"20"},{"source":"table_1","value":"250"}]}],"answer":0.08}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"20"},{"source":"table_2","value":"56"}]}],"answer":0.35714285714285715}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"20"},{"source":"table_2","value":"56"}]}],"answer":0.35714285714285716}
```

## 42. GPN/2007/page_39.pdf-3

Evidence:
[text_0] stock performance graph the following line-graph presentation compares our cumulative shareholder returns with the standard & poor 2019s information technology index and the standard & poor 2019s 500 stock index for the past five years .
[text_1] the line graph assumes the investment of $ 100 in our common stock , the standard & poor 2019s information technology index , and the standard & poor 2019s 500 stock index on may 31 , 2002 and assumes reinvestment of all dividends .
[text_2] comparison of 5 year cumulative total return* among global payments inc. , the s&p 500 index and the s&p information technology index 5/02 5/03 5/04 5/05 5/06 5/07 global payments inc .
[text_3] s&p 500 s&p information technology * $ 100 invested on 5/31/02 in stock or index-including reinvestment of dividends .
[text_4] fiscal year ending may 31 .
[text_5] global payments s&p 500 information technology .
[text_6] issuer purchases of equity securities on april 5 , 2007 , our board of directors authorized repurchases of our common stock in an amount up to $ 100 million .
[text_7] the board has authorized us to purchase shares from time to time as market conditions permit .
[text_8] there is no expiration date with respect to this authorization .
[text_9] no amounts have been repurchased during the fiscal year ended may 31 , 2007. .
[table_0]  | global payments | s&p 500 | s&p information technology
[table_1] : may 31 2002 | global payments: $ 100.00 | s&p 500: $ 100.00 | s&p information technology: $ 100.00
[table_2] : may 31 2003 | global payments: 94.20 | s&p 500: 91.94 | s&p information technology: 94.48
[table_3] : may 31 2004 | global payments: 129.77 | s&p 500: 108.79 | s&p information technology: 115.24
[table_4] : may 31 2005 | global payments: 193.30 | s&p 500: 117.75 | s&p information technology: 116.29
[table_5] : may 31 2006 | global payments: 260.35 | s&p 500: 127.92 | s&p information technology: 117.14
[table_6] : may 31 2007 | global payments: 224.24 | s&p 500: 157.08 | s&p information technology: 144.11

Question: in comparison to overall information technology sector , how much percentage would global payments have earned the investor .

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_6","value":"224.24"},"const_100"]},{"op":"subtract","args":[{"source":"table_6","value":"144.11"},"const_100"]},{"op":"subtract","args":["#0","#1"]}],"answer":80.13}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_6","value":"224.24"},{"source":"table_6","value":"144.11"}]},{"op":"divide","args":["#0",{"source":"table_6","value":"144.11"}]}],"answer":0.5560335854555548}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_6","value":"224.24"},{"source":"table_6","value":"144.11"}]},{"op":"divide","args":["#0",{"source":"table_6","value":"144.11"}]}],"answer":0.5412512512512512}
```

## 43. ETR/2011/page_145.pdf-2

Evidence:
[text_0] entergy corporation and subsidiaries notes to financial statements sale and leaseback transactions waterford 3 lease obligations in 1989 , in three separate but substantially identical transactions , entergy louisiana sold and leased back undivided interests in waterford 3 for the aggregate sum of $ 353.6 million .
[text_1] the interests represent approximately 9.3% ( 9.3 % ) of waterford 3 .
[text_2] the leases expire in 2017 .
[text_3] under certain circumstances , entergy louisiana may repurchase the leased interests prior to the end of the term of the leases .
[text_4] at the end of the lease terms , entergy louisiana has the option to repurchase the leased interests in waterford 3 at fair market value or to renew the leases for either fair market value or , under certain conditions , a fixed rate .
[text_5] entergy louisiana issued $ 208.2 million of non-interest bearing first mortgage bonds as collateral for the equity portion of certain amounts payable under the leases .
[text_6] upon the occurrence of certain events , entergy louisiana may be obligated to assume the outstanding bonds used to finance the purchase of the interests in the unit and to pay an amount sufficient to withdraw from the lease transaction .
[text_7] such events include lease events of default , events of loss , deemed loss events , or certain adverse 201cfinancial events . 201d 201cfinancial events 201d include , among other things , failure by entergy louisiana , following the expiration of any applicable grace or cure period , to maintain ( i ) total equity capital ( including preferred membership interests ) at least equal to 30% ( 30 % ) of adjusted capitalization , or ( ii ) a fixed charge coverage ratio of at least 1.50 computed on a rolling 12 month basis .
[text_8] as of december 31 , 2011 , entergy louisiana was in compliance with these provisions .
[text_9] as of december 31 , 2011 , entergy louisiana had future minimum lease payments ( reflecting an overall implicit rate of 7.45% ( 7.45 % ) ) in connection with the waterford 3 sale and leaseback transactions , which are recorded as long-term debt , as follows : amount ( in thousands ) .
[text_10] grand gulf lease obligations in 1988 , in two separate but substantially identical transactions , system energy sold and leased back undivided ownership interests in grand gulf for the aggregate sum of $ 500 million .
[text_11] the interests represent approximately 11.5% ( 11.5 % ) of grand gulf .
[text_12] the leases expire in 2015 .
[text_13] under certain circumstances , system entergy may repurchase the leased interests prior to the end of the term of the leases .
[text_14] at the end of the lease terms , system energy has the option to repurchase the leased interests in grand gulf at fair market value or to renew the leases for either fair market value or , under certain conditions , a fixed rate .
[text_15] system energy is required to report the sale-leaseback as a financing transaction in its financial statements .
[text_16] for financial reporting purposes , system energy expenses the interest portion of the lease obligation and the plant depreciation .
[text_17] however , operating revenues include the recovery of the lease payments because the transactions are accounted for as a sale and leaseback for ratemaking purposes .
[text_18] consistent with a recommendation contained in a .
[table_0]  | amount ( in thousands )
[table_1] : 2012 | amount ( in thousands ): $ 39067
[table_2] : 2013 | amount ( in thousands ): 26301
[table_3] : 2014 | amount ( in thousands ): 31036
[table_4] : 2015 | amount ( in thousands ): 28827
[table_5] : 2016 | amount ( in thousands ): 16938
[table_6] : years thereafter | amount ( in thousands ): 106335
[table_7] : total | amount ( in thousands ): 248504
[table_8] : less : amount representing interest | amount ( in thousands ): 60249
[table_9] : present value of net minimum lease payments | amount ( in thousands ): $ 188255

Question: what portion of the total future minimum lease payments is expected to go for interest?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_8","value":"60249"},{"source":"table_7","value":"248504"}]}],"answer":0.24244680166114027}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_9","value":"188255"},{"source":"table_7","value":"248504"}]}],"answer":0.7575531983388597}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_9","value":"188255"},{"source":"table_7","value":"248504"}]}],"answer":0.7641000000000001}
```

## 44. ETR/2004/page_216.pdf-2

Evidence:
[text_0] entergy louisiana , inc .
[text_1] management's financial discussion and analysis setting any of entergy louisiana's rates .
[text_2] therefore , to the extent entergy louisiana's use of the proceeds would ordinarily have reduced its rate base , no change in rate base shall be reflected for ratemaking purposes .
[text_3] the sec approval for additional return of equity capital is now expired .
[text_4] entergy louisiana's receivables from or ( payables to ) the money pool were as follows as of december 31 for each of the following years: .
[text_5] money pool activity used $ 81.9 million of entergy louisiana's operating cash flow in 2004 , provided $ 60.2 million in 2003 , and used $ 15.0 million in 2002 .
[text_6] see note 4 to the domestic utility companies and system energy financial statements for a description of the money pool .
[text_7] investing activities the decrease of $ 25.1 million in net cash used by investing activities in 2004 was primarily due to decreased spending on customer service projects , partially offset by increases in spending on transmission projects and fossil plant projects .
[text_8] the increase of $ 56.0 million in net cash used by investing activities in 2003 was primarily due to increased spending on customer service , transmission , and nuclear projects .
[text_9] financing activities the decrease of $ 404.4 million in net cash used by financing activities in 2004 was primarily due to : 2022 the net issuance of $ 98.0 million of long-term debt in 2004 compared to the retirement of $ 261.0 million in 2022 a principal payment of $ 14.8 million in 2004 for the waterford lease obligation compared to a principal payment of $ 35.4 million in 2003 ; and 2022 a decrease of $ 29.0 million in common stock dividends paid .
[text_10] the decrease of $ 105.5 million in net cash used by financing activities in 2003 was primarily due to : 2022 a decrease of $ 125.9 million in common stock dividends paid ; and 2022 the repurchase of $ 120 million of common stock from entergy corporation in 2002 .
[text_11] the decrease in net cash used in 2003 was partially offset by the following : 2022 the retirement in 2003 of $ 150 million of 8.5% ( 8.5 % ) series first mortgage bonds compared to the net retirement of $ 134.6 million of first mortgage bonds in 2002 ; and 2022 principal payments of $ 35.4 million in 2003 for the waterford 3 lease obligation compared to principal payments of $ 15.9 million in 2002 .
[text_12] see note 5 to the domestic utility companies and system energy financial statements for details of long-term debt .
[text_13] uses of capital entergy louisiana requires capital resources for : 2022 construction and other capital investments ; 2022 debt and preferred stock maturities ; 2022 working capital purposes , including the financing of fuel and purchased power costs ; and 2022 dividend and interest payments. .
[table_0] 2004 | 2003 | 2002 | 2001
[table_1] 2004: ( in thousands ) | 2003: ( in thousands ) | 2002: ( in thousands ) | 2001: ( in thousands )
[table_2] 2004: $ 40549 | 2003: ( $ 41317 ) | 2002: $ 18854 | 2001: $ 3812

Question: what is the difference of the payment for waterford lease obligation between 2003 and 2004?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_9","value":"35.4"},{"source":"text_9","value":"14.8"}]}],"answer":20.6}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_11","value":"35.4"},{"source":"text_11","value":"15.9"}]}],"answer":19.5}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_11","value":"35.4"},{"source":"text_11","value":"15.9"}]}],"answer":19.5}
```

## 45. MRO/2015/page_18.pdf-4

Evidence:
[text_0] in the ordinary course of business , based on our evaluations of certain geologic trends and prospective economics , we have allowed certain lease acreage to expire and may allow additional acreage to expire in the future .
[text_1] if production is not established or we take no other action to extend the terms of the leases , licenses or concessions , undeveloped acreage listed in the table below will expire over the next three years .
[text_2] we plan to continue the terms of certain of these licenses and concession areas or retain leases through operational or administrative actions ; however , the majority of the undeveloped acres associated with other africa as listed in the table below pertains to our licenses in ethiopia and kenya , for which we executed agreements in 2015 to sell .
[text_3] the kenya transaction closed in february 2016 and the ethiopia transaction is expected to close in the first quarter of 2016 .
[text_4] see item 8 .
[text_5] financial statements and supplementary data - note 5 to the consolidated financial statements for additional information about this disposition .
[text_6] net undeveloped acres expiring year ended december 31 .
[text_7] .
[table_0] ( in thousands ) | net undeveloped acres expiring year ended december 31 , 2016 | net undeveloped acres expiring year ended december 31 , 2017 | net undeveloped acres expiring year ended december 31 , 2018
[table_1] ( in thousands ): u.s . | net undeveloped acres expiring year ended december 31 , 2016: 68 | net undeveloped acres expiring year ended december 31 , 2017: 89 | net undeveloped acres expiring year ended december 31 , 2018: 128
[table_2] ( in thousands ): e.g . | net undeveloped acres expiring year ended december 31 , 2016: 2014 | net undeveloped acres expiring year ended december 31 , 2017: 92 | net undeveloped acres expiring year ended december 31 , 2018: 36
[table_3] ( in thousands ): other africa | net undeveloped acres expiring year ended december 31 , 2016: 189 | net undeveloped acres expiring year ended december 31 , 2017: 4352 | net undeveloped acres expiring year ended december 31 , 2018: 854
[table_4] ( in thousands ): total africa | net undeveloped acres expiring year ended december 31 , 2016: 189 | net undeveloped acres expiring year ended december 31 , 2017: 4444 | net undeveloped acres expiring year ended december 31 , 2018: 890
[table_5] ( in thousands ): other international | net undeveloped acres expiring year ended december 31 , 2016: 2014 | net undeveloped acres expiring year ended december 31 , 2017: 2014 | net undeveloped acres expiring year ended december 31 , 2018: 2014
[table_6] ( in thousands ): total | net undeveloped acres expiring year ended december 31 , 2016: 257 | net undeveloped acres expiring year ended december 31 , 2017: 4533 | net undeveloped acres expiring year ended december 31 , 2018: 1018

Question: in 2017 , what percentage of undeveloped acres were located in africa?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_4","value":"4444"},{"source":"table_6","value":"4533"}]}],"answer":0.9803662033973086}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"89"},{"source":"table_4","value":"4444"}]}],"answer":0.020027002700270028}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"89"},{"source":"table_4","value":"4444"}]}],"answer":0.020000000000000004}
```

## 46. SWKS/2012/page_116.pdf-3

Evidence:
[text_0] skyworks solutions , inc .
[text_1] notes to consolidated financial statements 2014 ( continued ) maintained a valuation allowance of $ 47.0 million .
[text_2] this valuation allowance is comprised of $ 33.6 million related to u.s .
[text_3] state tax credits , of which $ 3.6 million are state tax credits acquired from aati in fiscal year 2012 , and $ 13.4 million related to foreign deferred tax assets .
[text_4] if these benefits are recognized in a future period the valuation allowance on deferred tax assets will be reversed and up to a $ 46.6 million income tax benefit , and up to a $ 0.4 million reduction to goodwill may be recognized .
[text_5] the company will need to generate $ 209.0 million of future united states federal taxable income to utilize our united states deferred tax assets as of september 28 , 2012 .
[text_6] deferred tax assets are recognized for foreign operations when management believes it is more likely than not that the deferred tax assets will be recovered during the carry forward period .
[text_7] the company will continue to assess its valuation allowance in future periods .
[text_8] as of september 28 , 2012 , the company has united states federal net operating loss carry forwards of approximately $ 74.3 million , including $ 29.5 million related to the acquisition of sige , which will expire at various dates through 2030 and $ 28.1 million related to the acquisition of aati , which will expire at various dates through 2031 .
[text_9] the utilization of these net operating losses is subject to certain annual limitations as required under internal revenue code section 382 and similar state income tax provisions .
[text_10] the company also has united states federal income tax credit carry forwards of $ 37.8 million , of which $ 30.4 million of federal income tax credit carry forwards have not been recorded as a deferred tax asset .
[text_11] the company also has state income tax credit carry forwards of $ 33.6 million , for which the company has provided a valuation allowance .
[text_12] the united states federal tax credits expire at various dates through 2032 .
[text_13] the state tax credits relate primarily to california research tax credits which can be carried forward indefinitely .
[text_14] the company has continued to expand its operations and increase its investments in numerous international jurisdictions .
[text_15] these activities will increase the company 2019s earnings attributable to foreign jurisdictions .
[text_16] as of september 28 , 2012 , no provision has been made for united states federal , state , or additional foreign income taxes related to approximately $ 371.5 million of undistributed earnings of foreign subsidiaries which have been or are intended to be permanently reinvested .
[text_17] it is not practicable to determine the united states federal income tax liability , if any , which would be payable if such earnings were not permanently reinvested .
[text_18] the company 2019s gross unrecognized tax benefits totaled $ 52.4 million and $ 32.1 million as of september 28 , 2012 and september 30 , 2011 , respectively .
[text_19] of the total unrecognized tax benefits at september 28 , 2012 , $ 38.8 million would impact the effective tax rate , if recognized .
[text_20] the remaining unrecognized tax benefits would not impact the effective tax rate , if recognized , due to the company 2019s valuation allowance and certain positions which were required to be capitalized .
[text_21] there are no positions which the company anticipates could change within the next twelve months .
[text_22] a reconciliation of the beginning and ending amount of gross unrecognized tax benefits is as follows ( in thousands ) : unrecognized tax benefits .
[text_23] page 114 annual report .
[table_0]  | unrecognized tax benefits
[table_1] : balance at september 30 2011 | unrecognized tax benefits: $ 32136
[table_2] : increases based on positions related to prior years | unrecognized tax benefits: 9004
[table_3] : increases based on positions related to current year | unrecognized tax benefits: 11265
[table_4] : decreases relating to settlements with taxing authorities | unrecognized tax benefits: 2014
[table_5] : decreases relating to lapses of applicable statutes of limitations | unrecognized tax benefits: -25 ( 25 )
[table_6] : balance at september 28 2012 | unrecognized tax benefits: $ 52380

Question: what amount of unrecognized tax benefits would not impact the effective tax rate , ( in millions ) ?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_18","value":"52.4"},{"source":"text_19","value":"38.8"}]}],"answer":13.6}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_18","value":"52.4"},{"source":"text_18","value":"32.1"}]}],"answer":20.3}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_18","value":"52.4"},{"source":"text_18","value":"32.1"}]}],"answer":20.3}
```

## 47. ETR/2008/page_401.pdf-1

Evidence:
[text_0] system energy resources , inc .
[text_1] management's financial discussion and analysis with syndicated bank letters of credit .
[text_2] in december 2004 , system energy amended these letters of credit and they now expire in may 2009 .
[text_3] system energy may refinance or redeem debt prior to maturity , to the extent market conditions and interest and dividend rates are favorable .
[text_4] all debt and common stock issuances by system energy require prior regulatory approval .
[text_5] debt issuances are also subject to issuance tests set forth in its bond indentures and other agreements .
[text_6] system energy has sufficient capacity under these tests to meet its foreseeable capital needs .
[text_7] system energy has obtained a short-term borrowing authorization from the ferc under which it may borrow , through march 31 , 2010 , up to the aggregate amount , at any one time outstanding , of $ 200 million .
[text_8] see note 4 to the financial statements for further discussion of system energy's short-term borrowing limits .
[text_9] system energy has also obtained an order from the ferc authorizing long-term securities issuances .
[text_10] the current long- term authorization extends through june 2009 .
[text_11] system energy's receivables from the money pool were as follows as of december 31 for each of the following years: .
[text_12] in may 2007 , $ 22.5 million of system energy's receivable from the money pool was replaced by a note receivable from entergy new orleans .
[text_13] see note 4 to the financial statements for a description of the money pool .
[text_14] nuclear matters system energy owns and operates grand gulf .
[text_15] system energy is , therefore , subject to the risks related to owning and operating a nuclear plant .
[text_16] these include risks from the use , storage , handling and disposal of high-level and low-level radioactive materials , regulatory requirement changes , including changes resulting from events at other plants , limitations on the amounts and types of insurance commercially available for losses in connection with nuclear operations , and technological and financial uncertainties related to decommissioning nuclear plants at the end of their licensed lives , including the sufficiency of funds in decommissioning trusts .
[text_17] in the event of an unanticipated early shutdown of grand gulf , system energy may be required to provide additional funds or credit support to satisfy regulatory requirements for decommissioning .
[text_18] environmental risks system energy's facilities and operations are subject to regulation by various governmental authorities having jurisdiction over air quality , water quality , control of toxic substances and hazardous and solid wastes , and other environmental matters .
[text_19] management believes that system energy is in substantial compliance with environmental regulations currently applicable to its facilities and operations .
[text_20] because environmental regulations are subject to change , future compliance costs cannot be precisely estimated .
[text_21] critical accounting estimates the preparation of system energy's financial statements in conformity with generally accepted accounting principles requires management to apply appropriate accounting policies and to make estimates and judgments that .
[table_0] 2008 | 2007 | 2006 | 2005
[table_1] 2008: ( in thousands ) | 2007: ( in thousands ) | 2006: ( in thousands ) | 2005: ( in thousands )
[table_2] 2008: $ 42915 | 2007: $ 53620 | 2006: $ 88231 | 2005: $ 277287

Question: how is cash flow of system energy affected by the change in balance of money pool from 2007 to 2008?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"53620"},{"source":"table_2","value":"42915"}]}],"answer":10705.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"42915"},{"source":"table_2","value":"53620"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"53620"}]}],"answer":-0.1996456546064901}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"42915"},{"source":"table_2","value":"53620"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"53620"}]}],"answer":-0.04254191489361705}
```

## 48. LLY/2018/page_99.pdf-2

Evidence:
[text_0] performance graph this graph compares the return on lilly stock with that of the standard & poor 2019s 500 stock index and our peer group for the years 2014 through 2018 .
[text_1] the graph assumes that , on december 31 , 2013 , a person invested $ 100 each in lilly stock , the s&p 500 stock index , and the peer groups' common stock .
[text_2] the graph measures total shareholder return , which takes into account both stock price and dividends .
[text_3] it assumes that dividends paid by a company are reinvested in that company 2019s stock .
[text_4] value of $ 100 invested on last business day of 2013 comparison of five-year cumulative total return among lilly , s&p 500 stock index , peer group ( 1 ) .
[text_5] ( 1 ) we constructed the peer group as the industry index for this graph .
[text_6] it comprises the companies in the pharmaceutical and biotech industries that we used to benchmark the compensation of our executive officers for 2018 : abbvie inc. ; amgen inc. ; astrazeneca plc ; baxter international inc. ; biogen idec inc. ; bristol-myers squibb company ; celgene corporation ; gilead sciences inc. ; glaxosmithkline plc ; johnson & johnson ; medtronic plc ; merck & co. , inc. ; novartis ag. ; pfizer inc. ; roche holdings ag ; sanofi ; and shire plc. .
[table_0]  | lilly | peer group | s&p 500
[table_1] : dec-13 | lilly: $ 100.00 | peer group: $ 100.00 | s&p 500: $ 100.00
[table_2] : dec-14 | lilly: $ 139.75 | peer group: $ 114.39 | s&p 500: $ 113.69
[table_3] : dec-15 | lilly: $ 175.21 | peer group: $ 116.56 | s&p 500: $ 115.26
[table_4] : dec-16 | lilly: $ 157.03 | peer group: $ 112.80 | s&p 500: $ 129.05
[table_5] : dec-17 | lilly: $ 185.04 | peer group: $ 128.90 | s&p 500: $ 157.22
[table_6] : dec-18 | lilly: $ 259.88 | peer group: $ 136.56 | s&p 500: $ 150.33

Question: what was the difference in percentage return for lilly compared to the s&p 500 for the five years ended dec-18?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_6","value":"259.88"},"const_100"]},{"op":"divide","args":["#0","const_100"]},{"op":"subtract","args":[{"source":"table_6","value":"150.33"},"const_100"]},{"op":"divide","args":["#2","const_100"]},{"op":"subtract","args":["#1","#3"]}],"answer":1.0955}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_6","value":"259.88"},"const_100"]},{"op":"divide","args":["#0","const_100"]}],"answer":1.5988}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_6","value":"259.88"},"const_100"]},{"op":"divide","args":["#0","const_100"]}],"answer":1.5988}
```

## 49. RCL/2016/page_37.pdf-2

Evidence:
[text_0] performance graph the following graph compares the total return , assuming reinvestment of dividends , on an investment in the company , based on performance of the company's common stock , with the total return of the standard & poor's 500 composite stock index and the dow jones united states travel and leisure index for a five year period by measuring the changes in common stock prices from december 31 , 2011 to december 31 , 2016. .
[text_1] the stock performance graph assumes for comparison that the value of the company's common stock and of each index was $ 100 on december 31 , 2011 and that all dividends were reinvested .
[text_2] past performance is not necessarily an indicator of future results. .
[table_0]  | 12/11 | 12/12 | 12/13 | 12/14 | 12/15 | 12/16
[table_1] : royal caribbean cruises ltd . | 12/11: 100.00 | 12/12: 139.36 | 12/13: 198.03 | 12/14: 350.40 | 12/15: 437.09 | 12/16: 362.38
[table_2] : s&p 500 | 12/11: 100.00 | 12/12: 116.00 | 12/13: 153.58 | 12/14: 174.60 | 12/15: 177.01 | 12/16: 198.18
[table_3] : dow jones us travel & leisure | 12/11: 100.00 | 12/12: 113.33 | 12/13: 164.87 | 12/14: 191.85 | 12/15: 203.17 | 12/16: 218.56

Question: what is the percentage increase of the s&p 500 from 2011 to 2016?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"198.18"},"const_100"]},{"op":"divide","args":["#0","const_100"]},{"op":"multiply","args":["#1","const_100"]}],"answer":98.18}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"198.18"},{"source":"table_2","value":"100.00"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"100.00"}]}],"answer":0.9818}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"198.18"},{"source":"table_2","value":"100.00"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"100.00"}]}],"answer":0.9818}
```

## 50. AES/2001/page_86.pdf-2

Evidence:
[text_0] 7 .
[text_1] derivative instruments effective january 1 , 2001 , aes adopted sfas no .
[text_2] 133 , 2018 2018accounting for derivative instruments and hedging activities , 2019 2019 which , as amended , establishes accounting and reporting standards for derivative instruments and hedging activities .
[text_3] the adoption of sfas no .
[text_4] 133 on january 1 , 2001 , resulted in a cumulative reduction to income of less than $ 1 million , net of deferred income tax effects , and a cumulative reduction of accumulated other comprehensive income in stockholders 2019 equity of $ 93 million , net of deferred income tax effects .
[text_5] for the year ended december 31 , 2001 , the impact of changes in derivative fair value primarily related to derivatives that do not qualify for hedge accounting treatment was a charge of $ 36 million , after income taxes .
[text_6] this amount includes a charge of $ 6 million , after income taxes , related to the ineffective portion of derivatives qualifying as cash flow and fair value hedges for the year ended december 31 , 2001 .
[text_7] there was no net effect on results of operations for the year ended december 31 , 2001 , of derivative and non-derivative instruments that have been designated and qualified as hedging net investments in foreign operations .
[text_8] approximately $ 35 million of other comprehensive loss related to derivative instruments as of december 31 , 2001 is expected to be recognized as a reduction to earnings over the next twelve months .
[text_9] a portion of this amount is expected to be offset by the effects of hedge accounting .
[text_10] the balance in accumulated other comprehensive loss related to derivative transactions will be reclassified into earnings as interest expense is recognized for hedges of interest rate risk , as foreign currency transaction and translation gains and losses are recognized for hedges of foreign currency exposure and as electric and gas sales and purchases are recognized for hedges of forecasted electric and gas transactions .
[text_11] amounts recorded in accumulated other comprehensive income , net of tax , during the year-ended december 31 , 2001 , were as follows ( in millions ) : .
[text_12] aes utilizes derivative financial instruments to hedge interest rate risk , foreign exchange risk and commodity price risk .
[text_13] the company utilizes interest rate swap , cap and floor agreements to hedge interest rate risk on floating rate debt .
[text_14] the majority of aes 2019s interest rate derivatives are designated and qualify as cash flow hedges .
[text_15] currency forward and swap agreements are utilized to hedge foreign exchange risk which is a result of aes or one of its subsidiaries entering into monetary obligations in currencies other than its own functional currency .
[text_16] the majority of aes 2019s foreign currency derivatives are designated and qualify as either fair value hedges or cash flow hedges .
[text_17] certain derivative instruments and other non-derivative instruments are designated and qualify as hedges of the foreign currency exposure of a net investment in a foreign operation .
[text_18] the company utilizes electric and gas derivative instruments , including swaps , options , forwards and futures , to hedge the risk related to electricity and gas sales and purchases .
[text_19] the majority of aes 2019s electric and gas derivatives are designated and qualify as cash flow hedges .
[text_20] the maximum length of time over which aes is hedging its exposure to variability in future cash flows for forecasted transactions , excluding forecasted transactions related to the payment of variable interest , is three years .
[text_21] for the year ended december 31 , 2001 , a charge of $ 4 million , after income taxes , was recorded for two cash flow hedges that were discontinued because it is probable that the hedged forecasted transaction will not occur .
[text_22] a portion of this charge has been classified as discontinued operations .
[text_23] for the year ended december 31 , 2001 , no fair value hedges were de-recognized or discontinued. .
[table_0] transition adjustment on january 1 2001 | $ -93 ( 93 )
[table_1] transition adjustment on january 1 2001: reclassification to earnings | $ -93 ( 93 ): -32 ( 32 )
[table_2] transition adjustment on january 1 2001: change in fair value | $ -93 ( 93 ): 4
[table_3] transition adjustment on january 1 2001: balance december 31 2001 | $ -93 ( 93 ): $ -121 ( 121 )

Question: without the adjustment for the change in fair value , what would the aoci balance have been in millions at december 31 2001?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"4"},{"source":"table_3","value":"121"}]}],"answer":-117.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_3","value":"121"},{"source":"table_1","value":"32"}]}],"answer":153.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_3","value":"121"},{"source":"table_1","value":"32"}]}],"answer":153.0}
```

## 51. CME/2017/page_99.pdf-5

Evidence:
[text_0] in 2017 , the company granted 440076 shares of restricted class a common stock and 7568 shares of restricted stock units .
[text_1] restricted common stock and restricted stock units generally have a vesting period of two to four years .
[text_2] the fair value related to these grants was $ 58.7 million , which is recognized as compensation expense on an accelerated basis over the vesting period .
[text_3] dividends are accrued on restricted class a common stock and restricted stock units and are paid once the restricted stock vests .
[text_4] in 2017 , the company also granted 203298 performance shares .
[text_5] the fair value related to these grants was $ 25.3 million , which is recognized as compensation expense on an accelerated and straight-lined basis over the vesting period .
[text_6] the vesting of these shares is contingent on meeting stated performance or market conditions .
[text_7] the following table summarizes restricted stock , restricted stock units , and performance shares activity for 2017 : number of shares weighted average grant date fair value .
[text_8] the total fair value of restricted stock , restricted stock units , and performance shares that vested during 2017 , 2016 and 2015 was $ 66.0 million , $ 59.8 million and $ 43.3 million , respectively .
[text_9] under the espp , eligible employees may acquire shares of class a common stock using after-tax payroll deductions made during consecutive offering periods of approximately six months in duration .
[text_10] shares are purchased at the end of each offering period at a price of 90% ( 90 % ) of the closing price of the class a common stock as reported on the nasdaq global select market .
[text_11] compensation expense is recognized on the dates of purchase for the discount from the closing price .
[text_12] in 2017 , 2016 and 2015 , a total of 19936 , 19858 and 19756 shares , respectively , of class a common stock were issued to participating employees .
[text_13] these shares are subject to a six-month holding period .
[text_14] annual expense of $ 0.3 million for the purchase discount was recognized in 2017 , and $ 0.2 million was recognized in both 2016 and 2015 .
[text_15] non-executive directors receive an annual award of class a common stock with a value equal to $ 100000 .
[text_16] non-executive directors may also elect to receive some or all of the cash portion of their annual stipend , up to $ 60000 , in shares of stock based on the closing price at the date of distribution .
[text_17] as a result , 19736 shares , 26439 shares and 25853 shares of class a common stock were issued to non-executive directors during 2017 , 2016 and 2015 , respectively .
[text_18] these shares are not subject to any vesting restrictions .
[text_19] expense of $ 2.5 million , $ 2.4 million and $ 2.5 million related to these stock-based payments was recognized for the years ended december 31 , 2017 , 2016 and 2015 , respectively. .
[table_0]  | number of shares | weightedaveragegrant datefair value
[table_1] : outstanding at december 31 2016 | number of shares: 1820578 | weightedaveragegrant datefair value: $ 98
[table_2] : granted | number of shares: 650942 | weightedaveragegrant datefair value: 129
[table_3] : vested | number of shares: -510590 ( 510590 ) | weightedaveragegrant datefair value: 87
[table_4] : cancelled | number of shares: -401699 ( 401699 ) | weightedaveragegrant datefair value: 95
[table_5] : outstanding at december 31 2017 | number of shares: 1559231 | weightedaveragegrant datefair value: 116

Question: what was the sum of the shares purchase discount from 2015 to 2017 in millions

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_14","value":"0.3"},{"source":"text_14","value":"0.2"}]},{"op":"add","args":["#0",{"source":"text_14","value":"0.2"}]}],"answer":0.7}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_14","value":"0.3"},{"source":"text_14","value":"0.2"}]}],"answer":0.5}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_14","value":"0.3"},{"source":"text_14","value":"0.2"}]}],"answer":0.5}
```

## 52. GS/2013/page_220.pdf-3

Evidence:
[text_0] supplemental financial information common stock performance the following graph compares the performance of an investment in the firm 2019s common stock from december 26 , 2008 ( the last trading day before the firm 2019s 2009 fiscal year ) through december 31 , 2013 , with the s&p 500 index and the s&p 500 financials index .
[text_1] the graph assumes $ 100 was invested on december 26 , 2008 in each of the firm 2019s common stock , the s&p 500 index and the s&p 500 financials index , and the dividends were reinvested on the date of payment without payment of any commissions .
[text_2] the performance shown in the graph represents past performance and should not be considered an indication of future performance .
[text_3] the goldman sachs group , inc .
[text_4] s&p 500 index s&p 500 financials index dec-09 dec-10 dec-11 dec-12 dec-13dec-08 the table below shows the cumulative total returns in dollars of the firm 2019s common stock , the s&p 500 index and the s&p 500 financials index for goldman sachs 2019 last five fiscal year ends , assuming $ 100 was invested on december 26 , 2008 in each of the firm 2019s common stock , the s&p 500 index and the s&p 500 financials index , and the dividends were reinvested on the date of payment without payment of any commissions .
[text_5] the performance shown in the table represents past performance and should not be considered an indication of future performance. .
[text_6] 218 goldman sachs 2013 annual report .
[table_0]  | 12/26/08 | 12/31/09 | 12/31/10 | 12/31/11 | 12/31/12 | 12/31/13
[table_1] : the goldman sachs group inc . | 12/26/08: $ 100.00 | 12/31/09: $ 224.98 | 12/31/10: $ 226.19 | 12/31/11: $ 123.05 | 12/31/12: $ 176.42 | 12/31/13: $ 248.36
[table_2] : s&p 500 index | 12/26/08: 100.00 | 12/31/09: 130.93 | 12/31/10: 150.65 | 12/31/11: 153.83 | 12/31/12: 178.42 | 12/31/13: 236.20
[table_3] : s&p 500 financials index | 12/26/08: 100.00 | 12/31/09: 124.38 | 12/31/10: 139.47 | 12/31/11: 115.67 | 12/31/12: 148.92 | 12/31/13: 201.92

Question: what is the five year total return on the s&p 500 index?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"236.20"},"const_100"]}],"answer":136.2}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"236.20"},{"source":"table_2","value":"100.00"}]},{"op":"divide","args":["#0","const_100"]}],"answer":1.362}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"236.20"},{"source":"table_2","value":"100.00"}]},{"op":"divide","args":["#0","const_100"]}],"answer":136.2}
```

## 53. LKQ/2010/page_84.pdf-3

Evidence:
[text_0] the future minimum lease commitments under these leases at december 31 , 2010 are as follows ( in thousands ) : years ending december 31: .
[text_1] rental expense for operating leases was approximately $ 66.9 million , $ 57.2 million and $ 49.0 million during the years ended december 31 , 2010 , 2009 and 2008 , respectively .
[text_2] in connection with the acquisitions of several businesses , we entered into agreements with several sellers of those businesses , some of whom became stockholders as a result of those acquisitions , for the lease of certain properties used in our operations .
[text_3] typical lease terms under these agreements include an initial term of five years , with three to five five-year renewal options and purchase options at various times throughout the lease periods .
[text_4] we also maintain the right of first refusal concerning the sale of the leased property .
[text_5] lease payments to an employee who became an officer of the company after the acquisition of his business were approximately $ 1.0 million , $ 0.9 million and $ 0.9 million during each of the years ended december 31 , 2010 , 2009 and 2008 , respectively .
[text_6] we guarantee the residual values of the majority of our truck and equipment operating leases .
[text_7] the residual values decline over the lease terms to a defined percentage of original cost .
[text_8] in the event the lessor does not realize the residual value when a piece of equipment is sold , we would be responsible for a portion of the shortfall .
[text_9] similarly , if the lessor realizes more than the residual value when a piece of equipment is sold , we would be paid the amount realized over the residual value .
[text_10] had we terminated all of our operating leases subject to these guarantees at december 31 , 2010 , the guaranteed residual value would have totaled approximately $ 31.4 million .
[text_11] we have not recorded a liability for the guaranteed residual value of equipment under operating leases as the recovery on disposition of the equipment under the leases is expected to approximate the guaranteed residual value .
[text_12] litigation and related contingencies in december 2005 and may 2008 , ford global technologies , llc filed complaints with the international trade commission against us and others alleging that certain aftermarket parts imported into the u.s .
[text_13] infringed on ford design patents .
[text_14] the parties settled these matters in april 2009 pursuant to a settlement arrangement that expires in september 2011 .
[text_15] pursuant to the settlement , we ( and our designees ) became the sole distributor in the u.s .
[text_16] of aftermarket automotive parts that correspond to ford collision parts that are covered by a u.s .
[text_17] design patent .
[text_18] we have paid ford an upfront fee for these rights and will pay a royalty for each such part we sell .
[text_19] the amortization of the upfront fee and the royalty expenses are reflected in cost of goods sold on the accompanying consolidated statements of income .
[text_20] we also have certain other contingencies resulting from litigation , claims and other commitments and are subject to a variety of environmental and pollution control laws and regulations incident to the ordinary course of business .
[text_21] we currently expect that the resolution of such contingencies will not materially affect our financial position , results of operations or cash flows. .
[table_0] 2011 | $ 62465
[table_1] 2011: 2012 | $ 62465: 54236
[table_2] 2011: 2013 | $ 62465: 47860
[table_3] 2011: 2014 | $ 62465: 37660
[table_4] 2011: 2015 | $ 62465: 28622
[table_5] 2011: thereafter | $ 62465: 79800
[table_6] 2011: future minimum lease payments | $ 62465: $ 310643

Question: in 2010 what was the sum of the future minimum lease commitments due in 2014

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_3","value":"37660"},{"source":"table_6","value":"310643"}]}],"answer":0.12123241148199058}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_5","value":"79800"},{"source":"table_6","value":"310643"}]}],"answer":390443.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_5","value":"79800"},{"source":"table_6","value":"310643"}]}],"answer":390543.0}
```

## 54. GPN/2013/page_92.pdf-3

Evidence:
[text_0] future minimum lease payments for all non-cancelable operating leases at may 31 , 2013 were as follows : fiscal years ending may 31: .
[text_1] we are party to a number of claims and lawsuits incidental to our business .
[text_2] in our opinion , the liabilities , if any , which may ultimately result from the outcome of such matters , individually or in the aggregate , are not expected to have a material adverse impact on our financial position , liquidity or results of operations .
[text_3] operating taxes we define operating taxes as taxes that are unrelated to income taxes , such as sales , property , value-add and other business taxes .
[text_4] during the course of operations , we must interpret the meaning of various operating tax matters in the united states and in the foreign jurisdictions in which we do business .
[text_5] taxing authorities in those various jurisdictions may arrive at different interpretations of applicable tax laws and regulations as they relate to such operating tax matters , which could result in the payment of additional taxes in those jurisdictions .
[text_6] as of may 31 , 2013 and 2012 , we did not have liabilities for contingencies related to operating tax items based on management 2019s best estimate given our history with similar matters and interpretations of current laws and regulations .
[text_7] bin/ica agreements we have entered into sponsorship or depository and processing agreements with certain banks .
[text_8] these agreements allow us to use the banks 2019 identification numbers , referred to as bank identification number ( 201cbin 201d ) for visa transactions and interbank card association ( 201cica 201d ) number for mastercard transactions , to clear credit card transactions through visa and mastercard .
[text_9] certain of such agreements contain financial covenants , and we were in compliance with all such covenants as of may 31 , 2013 .
[text_10] our canadian visa sponsorship , which was originally obtained through a canadian financial institution , expired in march 2011 .
[text_11] we have filed an application with the office of the superintendent of financial institutions canada ( 201cosfi 201d ) for the formation of a wholly owned loan company in canada which would serve as our financial institution sponsor .
[text_12] on december 12 , 2012 , the loan company received a restricted order to commence and carry on business from osfi which will enable the loan company to become a direct visa member at such time that global payments concludes the appropriate bin transfer process with visa .
[text_13] in march 2011 , we obtained temporary direct participation in the visa canada system , while the loan company application was pending .
[text_14] we anticipate that the bin transfer process with visa will be completed by september 30 , 2013. .
[table_0] 2014 | $ 11057
[table_1] 2014: 2015 | $ 11057: 8985
[table_2] 2014: 2016 | $ 11057: 7378
[table_3] 2014: 2017 | $ 11057: 6700
[table_4] 2014: 2018 | $ 11057: 6164
[table_5] 2014: thereafter | $ 11057: 16812
[table_6] 2014: total future minimum lease payments | $ 11057: $ 57096

Question: what portion of the future minimum lease payments are due in the next 12 months?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"11057"},{"source":"table_6","value":"57096"}]}],"answer":0.1936562981644949}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"57096"},{"source":"table_6","value":"11057"}]}],"answer":5.163787645835217}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"57096"},{"source":"table_6","value":"11057"}]}],"answer":5.12145603121456}
```

## 55. UAA/2016/page_83.pdf-4

Evidence:
[text_0] 2016 , as well as significant sponsorship and other marketing agreements entered into during the period after december 31 , 2016 through the date of this report : ( in thousands ) .
[text_1] total future minimum sponsorship and other payments $ 1355605 the amounts listed above are the minimum compensation obligations and guaranteed royalty fees required to be paid under the company 2019s sponsorship and other marketing agreements .
[text_2] the amounts listed above do not include additional performance incentives and product supply obligations provided under certain agreements .
[text_3] it is not possible to determine how much the company will spend on product supply obligations on an annual basis as contracts generally do not stipulate specific cash amounts to be spent on products .
[text_4] the amount of product provided to the sponsorships depends on many factors including general playing conditions , the number of sporting events in which they participate and the company 2019s decisions regarding product and marketing initiatives .
[text_5] in addition , the costs to design , develop , source and purchase the products furnished to the endorsers are incurred over a period of time and are not necessarily tracked separately from similar costs incurred for products sold to customers .
[text_6] in connection with various contracts and agreements , the company has agreed to indemnify counterparties against certain third party claims relating to the infringement of intellectual property rights and other items .
[text_7] generally , such indemnification obligations do not apply in situations in which the counterparties are grossly negligent , engage in willful misconduct , or act in bad faith .
[text_8] based on the company 2019s historical experience and the estimated probability of future loss , the company has determined that the fair value of such indemnifications is not material to its consolidated financial position or results of operations .
[text_9] from time to time , the company is involved in litigation and other proceedings , including matters related to commercial and intellectual property disputes , as well as trade , regulatory and other claims related to its business .
[text_10] other than as described below , the company believes that all current proceedings are routine in nature and incidental to the conduct of its business , and that the ultimate resolution of any such proceedings will not have a material adverse effect on its consolidated financial position , results of operations or cash flows .
[text_11] on february 10 , 2017 , a shareholder filed a securities case in the united states district court for the district of maryland ( the 201ccourt 201d ) against the company , the company 2019s chief executive officer and the company 2019s former chief financial officer ( brian breece v .
[text_12] under armour , inc. ) .
[text_13] on february 16 , 2017 , a second shareholder filed a securities case in the court against the same defendants ( jodie hopkins v .
[text_14] under armour , inc. ) .
[text_15] the plaintiff in each case purports to represent a class of shareholders for the period between april 21 , 2016 and january 30 , 2017 , inclusive .
[text_16] the complaints allege violations of section 10 ( b ) ( and rule 10b-5 ) of the securities exchange act of 1934 , as amended ( the 201cexchange act 201d ) and section 20 ( a ) control person liability under the exchange act against the officers named in the complaints .
[text_17] in general , the allegations in each case concern disclosures and statements made by .
[table_0] 2017 | $ 176138
[table_1] 2017: 2018 | $ 176138: 166961
[table_2] 2017: 2019 | $ 176138: 142987
[table_3] 2017: 2020 | $ 176138: 124856
[table_4] 2017: 2021 | $ 176138: 118168
[table_5] 2017: 2022 and thereafter | $ 176138: 626495
[table_6] 2017: total future minimum sponsorship and other payments | $ 176138: $ 1355605

Question: what portion of the total future minimum sponsorship and other payments will be due in the next three years?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"176138"},{"source":"table_1","value":"166961"}]},{"op":"add","args":["#0",{"source":"table_2","value":"142987"}]},{"op":"divide","args":["#1",{"source":"table_6","value":"1355605"}]}],"answer":0.35857495361849506}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"1355605"},{"source":"table_6","value":"1355605"}]}],"answer":1.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"1355605"},{"source":"table_6","value":"1355605"}]}],"answer":1.0}
```

## 56. AOS/2010/page_18.pdf-2

Evidence:
[text_0] the graph below shows a five-year comparison of the cumulative shareholder return on the company's common stock with the cumulative total return of the s&p small cap 600 index and the russell 1000 index , both of which are published indices .
[text_1] comparison of five-year cumulative total return from december 31 , 2005 to december 31 , 2010 assumes $ 100 invested with reinvestment of dividends period indexed returns .
[text_2] 2005 2006 2007 2008 2009 2010 smith ( a o ) corp s&p smallcap 600 index russell 1000 index .
[table_0] company/index | baseperiod 12/31/05 | baseperiod 12/31/06 | baseperiod 12/31/07 | baseperiod 12/31/08 | baseperiod 12/31/09 | 12/31/10
[table_1] company/index: a o smith corp | baseperiod 12/31/05: 100.0 | baseperiod 12/31/06: 108.7 | baseperiod 12/31/07: 103.3 | baseperiod 12/31/08: 88.8 | baseperiod 12/31/09: 133.6 | 12/31/10: 178.8
[table_2] company/index: s&p small cap 600 index | baseperiod 12/31/05: 100.0 | baseperiod 12/31/06: 115.1 | baseperiod 12/31/07: 114.8 | baseperiod 12/31/08: 78.1 | baseperiod 12/31/09: 98.0 | 12/31/10: 123.8
[table_3] company/index: russell 1000 index | baseperiod 12/31/05: 100.0 | baseperiod 12/31/06: 115.5 | baseperiod 12/31/07: 122.1 | baseperiod 12/31/08: 76.2 | baseperiod 12/31/09: 97.9 | 12/31/10: 113.6

Question: what was the difference in the cumulative total return for a o smith corp and the russell 1000 index for the five year period ended 12/31/10?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"178.8"},"const_100"]},{"op":"divide","args":["#0","const_100"]},{"op":"subtract","args":[{"source":"table_3","value":"113.6"},"const_100"]},{"op":"divide","args":["#2","const_100"]},{"op":"subtract","args":["#1","#3"]}],"answer":0.652}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"178.8"},{"source":"table_3","value":"113.6"}]}],"answer":65.2}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"178.8"},{"source":"table_3","value":"113.6"}]}],"answer":65.2}
```

## 57. ETR/2008/page_343.pdf-1

Evidence:
[text_0] entergy mississippi , inc .
[text_1] management's financial discussion and analysis sources of capital entergy mississippi's sources to meet its capital requirements include : internally generated funds ; cash on hand ; debt or preferred stock issuances ; and bank financing under new or existing facilities .
[text_2] entergy mississippi may refinance or redeem debt and preferred stock prior to maturity , to the extent market conditions and interest and dividend rates are favorable .
[text_3] all debt and common and preferred stock issuances by entergy mississippi require prior regulatory approval .
[text_4] preferred stock and debt issuances are also subject to issuance tests set forth in its corporate charter , bond indenture , and other agreements .
[text_5] entergy mississippi has sufficient capacity under these tests to meet its foreseeable capital needs .
[text_6] entergy mississippi has two separate credit facilities in the aggregate amount of $ 50 million and renewed both facilities through may 2009 .
[text_7] borrowings under the credit facilities may be secured by a security interest in entergy mississippi's accounts receivable .
[text_8] no borrowings were outstanding under either credit facility as of december 31 , 2008 .
[text_9] entergy mississippi has obtained short-term borrowing authorization from the ferc under which it may borrow through march 31 , 2010 , up to the aggregate amount , at any one time outstanding , of $ 175 million .
[text_10] see note 4 to the financial statements for further discussion of entergy mississippi's short-term borrowing limits .
[text_11] entergy mississippi has also obtained an order from the ferc authorizing long-term securities issuances .
[text_12] the current long-term authorization extends through june 30 , 2009 .
[text_13] entergy mississippi's receivables from or ( payables to ) the money pool were as follows as of december 31 for each of the following years: .
[text_14] in may 2007 , $ 6.6 million of entergy mississippi's receivable from the money pool was replaced by a note receivable from entergy new orleans .
[text_15] see note 4 to the financial statements for a description of the money pool .
[text_16] state and local rate regulation the rates that entergy mississippi charges for electricity significantly influence its financial position , results of operations , and liquidity .
[text_17] entergy mississippi is regulated and the rates charged to its customers are determined in regulatory proceedings .
[text_18] a governmental agency , the mpsc , is primarily responsible for approval of the rates charged to customers .
[text_19] formula rate plan in march 2008 , entergy mississippi made its annual scheduled formula rate plan filing for the 2007 test year with the mpsc .
[text_20] the filing showed that a $ 10.1 million increase in annual electric revenues is warranted .
[text_21] in june 2008 , entergy mississippi reached a settlement with the mississippi public utilities staff that would result in a $ 3.8 million rate increase .
[text_22] in january 2009 the mpsc rejected the settlement and left the current rates in effect .
[text_23] entergy mississippi appealed the mpsc's decision to the mississippi supreme court. .
[table_0] 2008 | 2007 | 2006 | 2005
[table_1] 2008: ( in thousands ) | 2007: ( in thousands ) | 2006: ( in thousands ) | 2005: ( in thousands )
[table_2] 2008: ( $ 66044 ) | 2007: $ 20997 | 2006: $ 39573 | 2005: ( $ 84066 )

Question: how is the cash flow of entergy mississippi affected by the balance in money pool from 2007 to 2008?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"20997"},{"source":"table_2","value":"66044"}]}],"answer":87041.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"66044"},{"source":"table_2","value":"20997"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"20997"}]}],"answer":2.1454017240558176}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"66044"},{"source":"table_2","value":"20997"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"20997"}]}],"answer":2.8141612903225806}
```

## 58. SNA/2013/page_84.pdf-1

Evidence:
[text_0] notes to consolidated financial statements ( continued ) goodwill and other intangible assets : goodwill and other indefinite-lived assets are tested for impairment annually or more frequently if events or changes in circumstances indicate that the assets might be impaired .
[text_1] annual impairment tests are performed by the company in the second quarter of each year .
[text_2] snap-on evaluates the existence of goodwill and indefinite-lived intangible asset impairment on the basis of whether the assets are fully recoverable from projected , discounted cash flows of the related business unit or asset .
[text_3] intangible assets with finite lives are amortized over their estimated useful lives using straight-line and accelerated methods depending on the nature of the particular asset .
[text_4] see note 6 for further information on goodwill and other intangible assets .
[text_5] new accounting standards disclosures relating to accumulated other comprehensive income the financial accounting standards board ( 201cfasb 201d ) issued authoritative guidance in february 2013 that amends the presentation of accumulated other comprehensive income and clarifies how to report the effect of significant reclassifications out of accumulated other comprehensive income .
[text_6] the guidance , which became effective for snap-on on a prospective basis at the beginning of its 2013 fiscal year , requires footnote disclosure regarding the changes in accumulated other comprehensive income by component and the line items affected in the statements of earnings .
[text_7] the adoption of this updated authoritative guidance did not have a significant impact on the company 2019s consolidated financial statements .
[text_8] see note 17 for additional information .
[text_9] note 2 : acquisition on may 13 , 2013 , snap-on acquired 100% ( 100 % ) of challenger lifts , inc .
[text_10] ( 201cchallenger 201d ) for a cash purchase price of $ 38.2 million , including post-closing adjustments .
[text_11] challenger designs , manufactures and distributes a comprehensive line of vehicle lifts and accessories to a diverse customer base in the automotive repair sector .
[text_12] the acquisition of the challenger vehicle lift product line complemented and increased snap-on 2019s existing undercar equipment offering , broadened its established capabilities in serving vehicle repair facilities and expanded the company 2019s presence with repair shop owners and managers .
[text_13] for segment reporting purposes , the results of operations and assets of challenger have been included in the repair systems & information group since the date of acquisition .
[text_14] pro forma financial information has not been presented as the net effects of the challenger acquisition were neither significant nor material to snap-on 2019s results of operations or financial position .
[text_15] note 3 : receivables trade and other accounts receivable snap-on 2019s trade and other accounts receivable primarily arise from the sale of tools and diagnostic and equipment products to a broad range of industrial and commercial customers and to snap-on 2019s independent franchise van channel on a non-extended-term basis with payment terms generally ranging from 30 to 120 days .
[text_16] the components of snap-on 2019s trade and other accounts receivable as of 2013 and 2012 year end are as follows : ( amounts in millions ) 2013 2012 .
[text_17] finance and contract receivables soc originates extended-term finance and contract receivables on sales of snap-on product sold through the u.s .
[text_18] franchisee and customer network and to snap-on 2019s industrial and other customers ; snap-on 2019s foreign finance subsidiaries provide similar financing internationally .
[text_19] interest income on finance and contract receivables is included in 201cfinancial services revenue 201d on the accompanying consolidated statements of earnings .
[text_20] 74 snap-on incorporated .
[table_0] ( amounts in millions ) | 2013 | 2012
[table_1] ( amounts in millions ): trade and other accounts receivable | 2013: $ 546.5 | 2012: $ 516.9
[table_2] ( amounts in millions ): allowances for doubtful accounts | 2013: -14.9 ( 14.9 ) | 2012: -19.0 ( 19.0 )
[table_3] ( amounts in millions ): total trade and other accounts receivable 2013 net | 2013: $ 531.6 | 2012: $ 497.9

Question: in 2013 what was the percent of the allowances for doubtful accounts

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"14.9"},{"source":"table_1","value":"546.5"}]}],"answer":0.0272644098810613}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"14.9"},{"source":"table_2","value":"19.0"}]}],"answer":0.7842105263157895}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"14.9"},{"source":"table_2","value":"19.0"}]}],"answer":0.7736842105263158}
```

## 59. APTV/2018/page_36.pdf-2

Evidence:
[text_0] part ii item 5 .
[text_1] market for registrant 2019s common equity , related stockholder matters and issuer purchases of equity securities our ordinary shares have been publicly traded since november 17 , 2011 when our ordinary shares were listed and began trading on the new york stock exchange ( 201cnyse 201d ) under the symbol 201cdlph . 201d on december 4 , 2017 , following the spin-off of delphi technologies , the company changed its name to aptiv plc and its nyse symbol to 201captv . 201d as of january 25 , 2019 , there were 2 shareholders of record of our ordinary shares .
[text_2] the following graph reflects the comparative changes in the value from december 31 , 2013 through december 31 , 2018 , assuming an initial investment of $ 100 and the reinvestment of dividends , if any in ( 1 ) our ordinary shares , ( 2 ) the s&p 500 index and ( 3 ) the automotive peer group .
[text_3] historical share prices of our ordinary shares have been adjusted to reflect the separation .
[text_4] historical performance may not be indicative of future shareholder returns .
[text_5] stock performance graph * $ 100 invested on december 31 , 2013 in our stock or in the relevant index , including reinvestment of dividends .
[text_6] fiscal year ended december 31 , 2018 .
[text_7] ( 1 ) aptiv plc , adjusted for the distribution of delphi technologies on december 4 , 2017 ( 2 ) s&p 500 2013 standard & poor 2019s 500 total return index ( 3 ) automotive peer group 2013 adient plc , american axle & manufacturing holdings inc , aptiv plc , borgwarner inc , cooper tire & rubber co , cooper- standard holdings inc , dana inc , dorman products inc , ford motor co , garrett motion inc. , general motors co , gentex corp , gentherm inc , genuine parts co , goodyear tire & rubber co , lear corp , lkq corp , meritor inc , motorcar parts of america inc , standard motor products inc , stoneridge inc , superior industries international inc , tenneco inc , tesla inc , tower international inc , visteon corp , wabco holdings inc company index december 31 , december 31 , december 31 , december 31 , december 31 , december 31 .
[text_8] .
[table_0] company index | december 31 2013 | december 31 2014 | december 31 2015 | december 31 2016 | december 31 2017 | december 31 2018
[table_1] company index: aptiv plc ( 1 ) | december 31 2013: $ 100.00 | december 31 2014: $ 122.75 | december 31 2015: $ 146.49 | december 31 2016: $ 117.11 | december 31 2017: $ 178.46 | december 31 2018: $ 130.80
[table_2] company index: s&p 500 ( 2 ) | december 31 2013: 100.00 | december 31 2014: 113.69 | december 31 2015: 115.26 | december 31 2016: 129.05 | december 31 2017: 157.22 | december 31 2018: 150.33
[table_3] company index: automotive peer group ( 3 ) | december 31 2013: 100.00 | december 31 2014: 107.96 | december 31 2015: 108.05 | december 31 2016: 107.72 | december 31 2017: 134.04 | december 31 2018: 106.89

Question: what is the difference in percentage performance for aptiv plc versus the automotive peer group for the five year period ending december 31 2018?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"130.80"},"const_100"]},{"op":"subtract","args":[{"source":"table_3","value":"106.89"},"const_100"]},{"op":"divide","args":["#0","const_100"]},{"op":"divide","args":["#1","const_100"]},{"op":"subtract","args":["#2","#3"]}],"answer":0.2391}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"130.80"},{"source":"table_3","value":"106.89"}]}],"answer":23.91}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"130.80"},{"source":"table_3","value":"106.89"}]}],"answer":23.91}
```

## 60. MAS/2018/page_60.pdf-2

Evidence:
[text_0] masco corporation notes to consolidated financial statements ( continued ) c .
[text_1] acquisitions on march 9 , 2018 , we acquired substantially all of the net assets of the l.d .
[text_2] kichler co .
[text_3] ( "kichler" ) , a leader in decorative residential and light commercial lighting products , ceiling fans and led lighting systems .
[text_4] this business expands our product offerings to our customers .
[text_5] the results of this acquisition for the period from the acquisition date are included in the consolidated financial statements and are reported in the decorative architectural products segment .
[text_6] we recorded $ 346 million of net sales as a result of this acquisition during 2018 .
[text_7] the purchase price , net of $ 2 million cash acquired , consisted of $ 549 million paid with cash on hand .
[text_8] since the acquisition , we have revised the allocation of the purchase price to identifiable assets and liabilities based on analysis of information as of the acquisition date that has been made available through december 31 , 2018 .
[text_9] the allocation will continue to be updated through the measurement period , if necessary .
[text_10] the preliminary allocation of the fair value of the acquisition of kichler is summarized in the following table , in millions. .
[text_11] the goodwill acquired , which is generally tax deductible , is related primarily to the operational and financial synergies we expect to derive from combining kichler's operations into our business , as well as the assembled workforce .
[text_12] the other intangible assets acquired consist of $ 59 million of indefinite-lived intangible assets , which is related to trademarks , and $ 181 million of definite-lived intangible assets .
[text_13] the definite-lived intangible assets consist of $ 145 million related to customer relationships , which is being amortized on a straight-line basis over 20 years , and $ 36 million of other definite-lived intangible assets , which is being amortized over a weighted average amortization period of three years .
[text_14] in the fourth quarter of 2017 , we acquired mercury plastics , inc. , a plastics processor and manufacturer of water handling systems for appliance and faucet applications , for approximately $ 89 million in cash .
[text_15] this business is included in the plumbing products segment .
[text_16] this acquisition enhances our ability to develop faucet technology and provides continuity of supply of quality faucet components .
[text_17] in connection with this acquisition , we recognized $ 38 million of goodwill , which is tax deductible , and is related primarily to the expected synergies from combining the operations into our business. .
[table_0]  | initial | revised
[table_1] : receivables | initial: $ 101 | revised: $ 100
[table_2] : inventories | initial: 173 | revised: 166
[table_3] : prepaid expenses and other | initial: 5 | revised: 5
[table_4] : property and equipment | initial: 33 | revised: 33
[table_5] : goodwill | initial: 46 | revised: 64
[table_6] : other intangible assets | initial: 243 | revised: 240
[table_7] : accounts payable | initial: -24 ( 24 ) | revised: -24 ( 24 )
[table_8] : accrued liabilities | initial: -25 ( 25 ) | revised: -30 ( 30 )
[table_9] : other liabilities | initial: -4 ( 4 ) | revised: -5 ( 5 )
[table_10] : total | initial: $ 548 | revised: $ 549

Question: what portion of the revised purchase price of kichler is dedicated to goodwill?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_5","value":"64"},{"source":"table_10","value":"549"}]}],"answer":0.11657559198542805}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_5","value":"64"},{"source":"table_5","value":"46"}]}],"answer":1.391304347826087}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_5","value":"64"},{"source":"table_5","value":"46"}]}],"answer":1.3846153846153846}
```

## 61. RSG/2013/page_16.pdf-1

Evidence:
[text_0] fleet automation approximately 66% ( 66 % ) of our residential routes have been converted to automated single driver trucks .
[text_1] by converting our residential routes to automated service , we reduce labor costs , improve driver productivity and create a safer work environment for our employees .
[text_2] additionally , communities using automated vehicles have higher participation rates in recycling programs , thereby complementing our initiative to expand our recycling capabilities .
[text_3] fleet conversion to compressed natural gas ( cng ) approximately 12% ( 12 % ) of our fleet operates on natural gas .
[text_4] we expect to continue our gradual fleet conversion to cng , our preferred alternative fuel technology , as part of our ordinary annual fleet replacement process .
[text_5] we believe a gradual fleet conversion is most prudent to realize the full value of our previous fleet investments .
[text_6] approximately 50% ( 50 % ) of our replacement vehicle purchases during 2013 were cng vehicles .
[text_7] we believe using cng vehicles provides us a competitive advantage in communities with strict clean emission objectives or initiatives that focus on protecting the environment .
[text_8] although upfront costs are higher , we expect that using natural gas will reduce our overall fleet operating costs through lower fuel expenses .
[text_9] standardized maintenance based on an industry trade publication , we operate the eighth largest vocational fleet in the united states .
[text_10] as of december 31 , 2013 , our average fleet age in years , by line of business , was as follows : approximate number of vehicles average age .
[text_11] through standardization of core functions , we believe we can minimize variability in our maintenance processes resulting in higher vehicle quality while extending the service life of our fleet .
[text_12] we believe operating a more reliable , safer and efficient fleet will lower our operating costs .
[text_13] we have completed implementation of standardized maintenance programs for approximately 45% ( 45 % ) of our fleet maintenance operations as of december 31 , 2013 .
[text_14] cash utilization strategy key components of our cash utilization strategy include increasing free cash flow and improving our return on invested capital .
[text_15] our definition of free cash flow , which is not a measure determined in accordance with united states generally accepted accounting principles ( u.s .
[text_16] gaap ) , is cash provided by operating activities less purchases of property and equipment , plus proceeds from sales of property and equipment as presented in our consolidated statements of cash flows .
[text_17] for a discussion and reconciliation of free cash flow , you should read the 201cfree cash flow 201d section of our management 2019s discussion and analysis of financial condition and results of operations contained in item 7 of this form 10-k .
[text_18] we believe free cash flow drives shareholder value and provides useful information regarding the recurring cash provided by our operations .
[text_19] free cash flow also demonstrates our ability to execute our cash utilization strategy , which includes investments in acquisitions and returning a majority of free cash flow to our shareholders through dividends and share repurchases .
[text_20] we are committed to an efficient capital structure and maintaining our investment grade rating .
[text_21] we manage our free cash flow by ensuring that capital expenditures and operating asset levels are appropriate in light of our existing business and growth opportunities , as well as by closely managing our working capital , which consists primarily of accounts receivable , accounts payable , and accrued landfill and environmental costs. .
[table_0]  | approximate number of vehicles | average age
[table_1] : residential | approximate number of vehicles: 7600 | average age: 7
[table_2] : commercial | approximate number of vehicles: 4300 | average age: 6
[table_3] : industrial | approximate number of vehicles: 3600 | average age: 9
[table_4] : total | approximate number of vehicles: 15500 | average age: 7

Question: as of december 31 , 2013 what was the ratio of the number of vehicles for the residential to the industrial

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"7600"},{"source":"table_3","value":"3600"}]}],"answer":2.111111111111111}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"4300"},{"source":"table_3","value":"3600"}]}],"answer":1.1944444444444444}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"4300"},{"source":"table_3","value":"3600"}]}],"answer":1.1944444444444444}
```

## 62. MRO/2011/page_39.pdf-1

Evidence:
[text_0] 2022 increased proved liquid hydrocarbon , including synthetic crude oil , reserves to 78 percent from 75 percent of proved reserves 2022 increased e&p net sales volumes , excluding libya , by 7 percent 2022 recorded 96 percent average operational availability for all major company-operated e&p assets , compared to 94 percent in 2010 2022 completed debottlenecking work that increased crude oil production capacity at the alvheim fpso in norway to 150000 gross bbld from the previous capacity of 142000 gross bbld and the original 2008 capacity of 120000 gross bbld 2022 announced two non-operated discoveries in the iraqi kurdistan region and began drilling in poland 2022 completed aosp expansion 1 , including the start-up of the expanded scotford upgrader , realizing an increase in net synthetic crude oil sales volumes of 48 percent 2022 completed dispositions of non-core assets and interests in acreage positions for net proceeds of $ 518 million 2022 repurchased 12 million shares of our common stock at a cost of $ 300 million 2022 retired $ 2498 million principal of our long-term debt 2022 resumed limited production in libya in the fourth quarter of 2011 following the february 2011 temporary suspension of operations consolidated results of operations : 2011 compared to 2010 due to the spin-off of our downstream business on june 30 , 2011 , which is reported as discontinued operations , income from continuing operations is more representative of marathon oil as an independent energy company .
[text_1] consolidated income from continuing operations before income taxes was 9 percent higher in 2011 than in 2010 , largely due to higher liquid hydrocarbon prices .
[text_2] this improvement was offset by increased income taxes primarily the result of excess foreign tax credits generated during 2011 that we do not expect to utilize in the future .
[text_3] the effective income tax rate for continuing operations was 61 percent in 2011 compared to 54 percent in 2010 .
[text_4] revenues are summarized in the following table : ( in millions ) 2011 2010 .
[text_5] e&p segment revenues increased $ 2247 million from 2010 to 2011 , primarily due to higher average liquid hydrocarbon realizations , which were $ 99.37 per bbl in 2011 , a 31 percent increase over 2010 .
[text_6] revenues in 2010 included net pre-tax gains of $ 95 million on derivative instruments intended to mitigate price risk on future sales of liquid hydrocarbons and natural gas .
[text_7] included in our e&p segment are supply optimization activities which include the purchase of commodities from third parties for resale .
[text_8] supply optimization serves to aggregate volumes in order to satisfy transportation commitments and to achieve flexibility within product types and delivery points .
[text_9] see the cost of revenues discussion as revenues from supply optimization approximate the related costs .
[text_10] higher average crude oil prices in 2011 compared to 2010 increased revenues related to supply optimization .
[text_11] revenues from the sale of our u.s .
[text_12] production are higher in 2011 primarily as a result of higher liquid hydrocarbon and natural gas price realizations , but sales volumes declined. .
[table_0] ( in millions ) | 2011 | 2010
[table_1] ( in millions ): e&p | 2011: $ 13029 | 2010: $ 10782
[table_2] ( in millions ): osm | 2011: 1588 | 2010: 833
[table_3] ( in millions ): ig | 2011: 93 | 2010: 150
[table_4] ( in millions ): segment revenues | 2011: 14710 | 2010: 11765
[table_5] ( in millions ): elimination of intersegment revenues | 2011: -47 ( 47 ) | 2010: -75 ( 75 )
[table_6] ( in millions ): total revenues | 2011: $ 14663 | 2010: $ 11690

Question: by how much did total revenues increase from 2010 to 2011?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_6","value":"14663"},{"source":"table_6","value":"11690"}]},{"op":"divide","args":["#0",{"source":"table_6","value":"11690"}]}],"answer":0.2543199315654405}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_6","value":"14663"},{"source":"table_6","value":"11690"}]}],"answer":2973.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_6","value":"14663"},{"source":"table_6","value":"11690"}]}],"answer":300.0}
```

## 63. CME/2010/page_123.pdf-4

Evidence:
[text_0] compensation plan approved by security holders .
[text_1] the employee stock purchase plan and the 2005 director stock plan were approved by shareholders at our 2005 annual meeting of shareholders .
[text_2] in connection with our mergers with cbot holdings and nymex holdings , we assumed their existing equity plans .
[text_3] the shares relating to the cbot holdings and nymex holdings plans are listed in the table below as being made under an equity compensation plan approved by security holders based upon the fact that shareholders of the company approved the related merger transactions .
[text_4] plan category number of securities to be issued upon exercise of outstanding options ( a ) weighted-average exercise price of outstanding options ( b ) number of securities remaining available for future issuance under equity compensation plans ( excluding securities reflected in column ( a ) ) ( c ) equity compensation plans approved by security holders .
[text_5] .
[text_6] .
[text_7] .
[text_8] .
[text_9] .
[text_10] .
[text_11] .
[text_12] .
[text_13] .
[text_14] .
[text_15] .
[text_16] .
[text_17] .
[text_18] .
[text_19] .
[text_20] .
[text_21] .
[text_22] .
[text_23] 1211143 $ 308.10 5156223 equity compensation plans not approved by security holders .
[text_24] .
[text_25] .
[text_26] .
[text_27] .
[text_28] .
[text_29] .
[text_30] .
[text_31] .
[text_32] .
[text_33] .
[text_34] .
[text_35] .
[text_36] .
[text_37] .
[text_38] .
[text_39] 5978 22.00 2014 .
[text_40] item 13 .
[text_41] certain relationships , related transactions and director independence the information required by this item is included in cme group 2019s proxy statement under the heading 201ccertain business relationships with related parties 201d and 201ccorporate governance 2014director independence 201d and is incorporated herein by reference , pursuant to general instruction g ( 3 ) .
[text_42] item 14 .
[text_43] principal accountant fees and services the information required by this item is included in cme group 2019s proxy statement under the heading 201caudit committee disclosures 2014principal accountant fees and services 201d and 201caudit committee disclosures 2014audit committee policy for approval of audit and permitted non-audit services 201d and is incorporated herein by reference , pursuant to general instruction g ( 3 ) . .
[table_0] plan category | number of securities to be issued upon exercise of outstanding options ( a ) | weighted-average exercise price of outstanding options ( b ) | number of securities remaining available for future issuance underequity compensation plans ( excluding securities reflected in column ( a ) ) ( c )
[table_1] plan category: equity compensation plans approved by security holders | number of securities to be issued upon exercise of outstanding options ( a ): 1211143 | weighted-average exercise price of outstanding options ( b ): $ 308.10 | number of securities remaining available for future issuance underequity compensation plans ( excluding securities reflected in column ( a ) ) ( c ): 5156223
[table_2] plan category: equity compensation plans not approved by security holders | number of securities to be issued upon exercise of outstanding options ( a ): 5978 | weighted-average exercise price of outstanding options ( b ): 22.00 | number of securities remaining available for future issuance underequity compensation plans ( excluding securities reflected in column ( a ) ) ( c ): 2014
[table_3] plan category: total | number of securities to be issued upon exercise of outstanding options ( a ): 1217121 | weighted-average exercise price of outstanding options ( b ):  | number of securities remaining available for future issuance underequity compensation plans ( excluding securities reflected in column ( a ) ) ( c ): 5156223

Question: what percentage of the outstanding options were from plans approved by security holders?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"1211143"},{"source":"table_3","value":"1217121"}]}],"answer":0.9950884094514842}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"1211143"},{"source":"table_1","value":"5156223"}]}],"answer":0.23488956936113894}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"1211143"},{"source":"table_1","value":"5156223"}]}],"answer":0.2341414141414141}
```

## 64. ETR/2016/page_23.pdf-3

Evidence:
[text_0] entergy corporation and subsidiaries management 2019s financial discussion and analysis a result of the entergy louisiana and entergy gulf states louisiana business combination , results of operations for 2015 also include two items that occurred in october 2015 : 1 ) a deferred tax asset and resulting net increase in tax basis of approximately $ 334 million and 2 ) a regulatory liability of $ 107 million ( $ 66 million net-of-tax ) as a result of customer credits to be realized by electric customers of entergy louisiana , consistent with the terms of the stipulated settlement in the business combination proceeding .
[text_1] see note 2 to the financial statements for further discussion of the business combination and customer credits .
[text_2] results of operations for 2015 also include the sale in december 2015 of the 583 mw rhode island state energy center for a realized gain of $ 154 million ( $ 100 million net-of-tax ) on the sale and the $ 77 million ( $ 47 million net-of-tax ) write-off and regulatory charges to recognize that a portion of the assets associated with the waterford 3 replacement steam generator project is no longer probable of recovery .
[text_3] see note 14 to the financial statements for further discussion of the rhode island state energy center sale .
[text_4] see note 2 to the financial statements for further discussion of the waterford 3 write-off .
[text_5] results of operations for 2014 include $ 154 million ( $ 100 million net-of-tax ) of charges related to vermont yankee primarily resulting from the effects of an updated decommissioning cost study completed in the third quarter 2014 along with reassessment of the assumptions regarding the timing of decommissioning cash flows and severance and employee retention costs .
[text_6] see note 14 to the financial statements for further discussion of the charges .
[text_7] results of operations for 2014 also include the $ 56.2 million ( $ 36.7 million net-of-tax ) write-off in 2014 of entergy mississippi 2019s regulatory asset associated with new nuclear generation development costs as a result of a joint stipulation entered into with the mississippi public utilities staff , subsequently approved by the mpsc , in which entergy mississippi agreed not to pursue recovery of the costs deferred by an mpsc order in the new nuclear generation docket .
[text_8] see note 2 to the financial statements for further discussion of the new nuclear generation development costs and the joint stipulation .
[text_9] net revenue utility following is an analysis of the change in net revenue comparing 2015 to 2014 .
[text_10] amount ( in millions ) .
[text_11] the retail electric price variance is primarily due to : 2022 formula rate plan increases at entergy louisiana , as approved by the lpsc , effective december 2014 and january 2015 ; 2022 an increase in energy efficiency rider revenue primarily due to increases in the energy efficiency rider at entergy arkansas , as approved by the apsc , effective july 2015 and july 2014 , and new energy efficiency riders at entergy louisiana and entergy mississippi that began in the fourth quarter 2014 ; and 2022 an annual net rate increase at entergy mississippi of $ 16 million , effective february 2015 , as a result of the mpsc order in the june 2014 rate case .
[text_12] see note 2 to the financial statements for a discussion of rate and regulatory proceedings. .
[table_0]  | amount ( in millions )
[table_1] : 2014 net revenue | amount ( in millions ): $ 5735
[table_2] : retail electric price | amount ( in millions ): 187
[table_3] : volume/weather | amount ( in millions ): 95
[table_4] : waterford 3 replacement steam generator provision | amount ( in millions ): -32 ( 32 )
[table_5] : miso deferral | amount ( in millions ): -35 ( 35 )
[table_6] : louisiana business combination customer credits | amount ( in millions ): -107 ( 107 )
[table_7] : other | amount ( in millions ): -14 ( 14 )
[table_8] : 2015 net revenue | amount ( in millions ): $ 5829

Question: what would 2015 net revenue have been in millions assuming there was no impact from both the retail electric price change and the impact of volume/weather in the year?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"187"},{"source":"table_3","value":"95"}]},{"op":"add","args":[{"source":"table_8","value":"5829"},"#0"]}],"answer":6111.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_8","value":"5829"},{"source":"table_1","value":"5735"}]}],"answer":94.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_8","value":"5829"},{"source":"table_1","value":"5735"}]}],"answer":94.0}
```

## 65. KMI/2018/page_14.pdf-2

Evidence:
[text_0] ( c ) effective january 1 , 2019 , these assets were transferred from the products pipelines business segment to the natural gas pipelines business segment .
[text_1] ( d ) effective january 1 , 2019 , a small number of terminals were transferred between the products pipelines and terminals business segments .
[text_2] competition our products pipelines 2019 pipeline operations compete against proprietary pipelines owned and operated by major oil companies , other independent products pipelines , trucking and marine transportation firms ( for short-haul movements of products ) and railcars .
[text_3] our products pipelines 2019 terminal operations compete with proprietary terminals owned and operated by major oil companies and other independent terminal operators , and our transmix operations compete with refineries owned by major oil companies and independent transmix facilities .
[text_4] terminals our terminals business segment includes the operations of our refined petroleum product , crude oil , chemical , ethanol and other liquid terminal facilities ( other than those included in the products pipelines business segment ) and all of our petroleum coke , metal and ores facilities .
[text_5] our terminals are located throughout the u.s .
[text_6] and in portions of canada .
[text_7] we believe the location of our facilities and our ability to provide flexibility to customers help attract new and retain existing customers at our terminals and provide expansion opportunities .
[text_8] we often classify our terminal operations based on the handling of either liquids or dry-bulk material products .
[text_9] in addition , terminals 2019 marine operations include jones act-qualified product tankers that provide marine transportation of crude oil , condensate and refined petroleum products between u.s .
[text_10] ports .
[text_11] the following summarizes our terminals business segment assets , as of december 31 , 2018 : number capacity ( mmbbl ) .
[text_12] _______ ( a ) effective january 1 , 2019 , a small number of terminals were transferred between the terminals and products pipelines business segments .
[text_13] competition we are one of the largest independent operators of liquids terminals in north america , based on barrels of liquids terminaling capacity .
[text_14] our liquids terminals compete with other publicly or privately held independent liquids terminals , and terminals owned by oil , chemical , pipeline , and refining companies .
[text_15] our bulk terminals compete with numerous independent terminal operators , terminals owned by producers and distributors of bulk commodities , stevedoring companies and other industrial companies opting not to outsource terminaling services .
[text_16] in some locations , competitors are smaller , independent operators with lower cost structures .
[text_17] our jones act-qualified product tankers compete with other jones act qualified vessel fleets .
[text_18] our co2 business segment produces , transports , and markets co2 for use in enhanced oil recovery projects as a flooding medium for recovering crude oil from mature oil fields .
[text_19] our co2 pipelines and related assets allow us to market a complete package of co2 supply and transportation services to our customers .
[text_20] we also hold ownership interests in several oil-producing fields and own a crude oil pipeline , all located in the permian basin region of west texas. .
[table_0]  | number | capacity ( mmbbl )
[table_1] : liquids terminals ( a ) | number: 52 | capacity ( mmbbl ): 89.6
[table_2] : bulk terminals | number: 34 | capacity ( mmbbl ): 2014
[table_3] : jones act tankers | number: 16 | capacity ( mmbbl ): 5.3

Question: what percent of storage facilities are liquid terminals

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"52"},{"source":"table_2","value":"34"}]},{"op":"add","args":["#0",{"source":"table_3","value":"16"}]},{"op":"divide","args":[{"source":"table_1","value":"52"},"#1"]}],"answer":0.5098039215686274}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"89.6"},{"source":"table_2","value":"2014"}]}],"answer":0.04448857994041708}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"89.6"},{"source":"table_2","value":"2014"}]}],"answer":0.04464912280769231}
```

## 66. UPS/2014/page_35.pdf-2

Evidence:
[text_0] shareowner return performance graph the following performance graph and related information shall not be deemed 201csoliciting material 201d or to be 201cfiled 201d with the sec , nor shall such information be incorporated by reference into any future filing under the securities act of 1933 or securities exchange act of 1934 , each as amended , except to the extent that the company specifically incorporates such information by reference into such filing .
[text_1] the following graph shows a five year comparison of cumulative total shareowners 2019 returns for our class b common stock , the standard & poor 2019s 500 index , and the dow jones transportation average .
[text_2] the comparison of the total cumulative return on investment , which is the change in the quarterly stock price plus reinvested dividends for each of the quarterly periods , assumes that $ 100 was invested on december 31 , 2009 in the standard & poor 2019s 500 index , the dow jones transportation average , and our class b common stock. .
[text_3] .
[table_0]  | 12/31/2009 | 12/31/2010 | 12/31/2011 | 12/31/2012 | 12/31/2013 | 12/31/2014
[table_1] : united parcel service inc . | 12/31/2009: $ 100.00 | 12/31/2010: $ 130.29 | 12/31/2011: $ 135.35 | 12/31/2012: $ 140.54 | 12/31/2013: $ 205.95 | 12/31/2014: $ 223.79
[table_2] : standard & poor 2019s 500 index | 12/31/2009: $ 100.00 | 12/31/2010: $ 115.06 | 12/31/2011: $ 117.48 | 12/31/2012: $ 136.26 | 12/31/2013: $ 180.38 | 12/31/2014: $ 205.05
[table_3] : dow jones transportation average | 12/31/2009: $ 100.00 | 12/31/2010: $ 126.74 | 12/31/2011: $ 126.75 | 12/31/2012: $ 136.24 | 12/31/2013: $ 192.61 | 12/31/2014: $ 240.91

Question: what is the roi of an investment in s&p500 from 2010 to 2012?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"136.26"},{"source":"table_2","value":"115.06"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"115.06"}]}],"answer":0.18425169476794717}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"136.26"},{"source":"table_2","value":"115.06"}]},{"op":"divide","args":["#0","const_100"]}],"answer":0.212}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"136.26"},{"source":"table_2","value":"115.06"}]},{"op":"divide","args":["#0","const_100"]}],"answer":0.216}
```

## 67. DG/2010/page_136.pdf-1

Evidence:
[text_0] dollar general corporation and subsidiaries notes to consolidated financial statements ( continued ) 1 .
[text_1] basis of presentation and accounting policies ( continued ) vendor rebates the company accounts for all cash consideration received from vendors in accordance with applicable accounting standards pertaining to such arrangements .
[text_2] cash consideration received from a vendor is generally presumed to be a rebate or an allowance and is accounted for as a reduction of merchandise purchase costs as earned .
[text_3] however , certain specific , incremental and otherwise qualifying sg&a expenses related to the promotion or sale of vendor products may be offset by cash consideration received from vendors , in accordance with arrangements such as cooperative advertising , when earned for dollar amounts up to but not exceeding actual incremental costs .
[text_4] the company recognizes amounts received for cooperative advertising on performance , 2018 2018first showing 2019 2019 or distribution , consistent with its policy for advertising expense in accordance with applicable accounting standards for reporting on advertising costs .
[text_5] prepaid expenses and other current assets prepaid expenses and other current assets include prepaid amounts for rent , maintenance , advertising , and insurance , as well as amounts receivable for certain vendor rebates ( primarily those expected to be collected in cash ) , coupons , and other items .
[text_6] property and equipment property and equipment are recorded at cost .
[text_7] the company provides for depreciation and amortization on a straight-line basis over the following estimated useful lives: .
[text_8] improvements of leased properties are amortized over the shorter of the life of the applicable lease term or the estimated useful life of the asset .
[text_9] impairment of long-lived assets when indicators of impairment are present , the company evaluates the carrying value of long-lived assets , other than goodwill , in relation to the operating performance and future cash flows or the appraised values of the underlying assets .
[text_10] in accordance with accounting standards for long-lived assets , the company reviews for impairment stores open more than two years for which current cash flows from operations are negative .
[text_11] impairment results when the carrying value of the assets exceeds the undiscounted future cash flows over the life of the lease .
[text_12] the company 2019s estimate of undiscounted future cash flows over the lease term is based upon historical operations of the stores and estimates of future store profitability which encompasses many factors that are subject to variability and difficult to predict .
[text_13] if a long-lived asset is found to be impaired , the amount recognized for impairment is equal to the difference between the carrying value and the asset 2019s estimated fair value .
[text_14] the fair value is estimated based primarily upon estimated future cash flows ( discounted at the company 2019s credit adjusted risk-free rate ) or other reasonable estimates of fair market value .
[text_15] assets to be disposed of are adjusted to the fair value less the cost to sell if less than the book value. .
[table_0] land improvements | 20
[table_1] land improvements: buildings | 20: 39 - 40
[table_2] land improvements: furniture fixtures and equipment | 20: 3 - 10

Question: what is the maximum depreciation rate that can be used for furniture fixtures and equipment?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":["const_100",{"source":"table_2","value":"3"}]}],"answer":33.333333333333336}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"10"},{"source":"table_2","value":"3"}]}],"answer":3.3333333333333335}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"10"},{"source":"table_2","value":"3"}]}],"answer":3.333333333333333}
```

## 68. ANET/2017/page_156.pdf-3

Evidence:
[text_0] as of december 31 , 2017 , the aggregate future minimum payments under non-cancelable operating leases consist of the following ( in thousands ) : years ending december 31 .
[text_1] rent expense for all operating leases amounted to $ 9.4 million , $ 8.1 million and $ 5.4 million for the years ended december 31 , 2017 , 2016 and 2015 , respectively .
[text_2] financing obligation 2014build-to-suit lease in august 2012 , we executed a lease for a building then under construction in santa clara , california to serve as our headquarters .
[text_3] the lease term is 120 months and commenced in august 2013 .
[text_4] based on the terms of the lease agreement and due to our involvement in certain aspects of the construction , we were deemed the owner of the building ( for accounting purposes only ) during the construction period .
[text_5] upon completion of construction in 2013 , we concluded that we had forms of continued economic involvement in the facility , and therefore did not meet with the provisions for sale-leaseback accounting .
[text_6] we continue to maintain involvement in the property post construction and lack transferability of the risks and rewards of ownership , due to our required maintenance of a $ 4.0 million letter of credit , in addition to our ability and option to sublease our portion of the leased building for fees substantially higher than our base rate .
[text_7] therefore , the lease is accounted for as a financing obligation and lease payments will be attributed to ( 1 ) a reduction of the principal financing obligation ; ( 2 ) imputed interest expense ; and ( 3 ) land lease expense , representing an imputed cost to lease the underlying land of the building .
[text_8] at the conclusion of the initial lease term , we will de-recognize both the net book values of the asset and the remaining financing obligation .
[text_9] as of december 31 , 2017 and 2016 , we have recorded assets of $ 53.4 million , representing the total costs of the building and improvements incurred , including the costs paid by the lessor ( the legal owner of the building ) and additional improvement costs paid by us , and a corresponding financing obligation of $ 39.6 million and $ 41.2 million , respectively .
[text_10] as of december 31 , 2017 , $ 1.9 million and $ 37.7 million were recorded as short-term and long-term financing obligations , respectively .
[text_11] land lease expense under our lease financing obligation amounted to $ 1.3 million for each of the years ended december 31 , 2017 , 2016 and 2015 respectively. .
[table_0] 2018 | $ 9127
[table_1] 2018: 2019 | $ 9127: 8336
[table_2] 2018: 2020 | $ 9127: 8350
[table_3] 2018: 2021 | $ 9127: 7741
[table_4] 2018: 2022 | $ 9127: 7577
[table_5] 2018: thereafter | $ 9127: 9873
[table_6] 2018: total minimum future lease payments | $ 9127: $ 51004

Question: what portion of the future future minimum payments under non-cancelable operating leases is due in the next 12 months?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"9127"},{"source":"table_6","value":"51004"}]}],"answer":0.1789467492745667}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"51004"},{"source":"table_6","value":"9127"}]}],"answer":5.5882546291223845}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"51004"},{"source":"table_6","value":"9127"}]}],"answer":5.511111111111111}
```

## 69. APD/2016/page_109.pdf-2

Evidence:
[text_0] we , in the normal course of business operations , have issued product warranties related to equipment sales .
[text_1] also , contracts often contain standard terms and conditions which typically include a warranty and indemnification to the buyer that the goods and services purchased do not infringe on third-party intellectual property rights .
[text_2] the provision for estimated future costs relating to warranties is not material to the consolidated financial statements .
[text_3] we do not expect that any sum we may have to pay in connection with guarantees and warranties will have a material adverse effect on our consolidated financial condition , liquidity , or results of operations .
[text_4] unconditional purchase obligations we are obligated to make future payments under unconditional purchase obligations as summarized below: .
[text_5] approximately $ 4000 of our unconditional purchase obligations relate to helium purchases , which include crude feedstock supply to multiple helium refining plants in north america as well as refined helium purchases from sources around the world .
[text_6] as a rare byproduct of natural gas production in the energy sector , these helium sourcing agreements are medium- to long-term and contain take-or-pay provisions .
[text_7] the refined helium is distributed globally and sold as a merchant gas , primarily under medium-term requirements contracts .
[text_8] while contract terms in the energy sector are longer than those in merchant , helium is a rare gas used in applications with few or no substitutions because of its unique physical and chemical properties .
[text_9] approximately $ 330 of our long-term unconditional purchase obligations relate to feedstock supply for numerous hyco ( hydrogen , carbon monoxide , and syngas ) facilities .
[text_10] the price of feedstock supply is principally related to the price of natural gas .
[text_11] however , long-term take-or-pay sales contracts to hyco customers are generally matched to the term of the feedstock supply obligations and provide recovery of price increases in the feedstock supply .
[text_12] due to the matching of most long-term feedstock supply obligations to customer sales contracts , we do not believe these purchase obligations would have a material effect on our financial condition or results of operations .
[text_13] the unconditional purchase obligations also include other product supply and purchase commitments and electric power and natural gas supply purchase obligations , which are primarily pass-through contracts with our customers .
[text_14] purchase commitments to spend approximately $ 350 for additional plant and equipment are included in the unconditional purchase obligations in 2017 .
[text_15] in addition , we have purchase commitments totaling approximately $ 500 in 2017 and 2018 relating to our long-term sale of equipment project for saudi aramco 2019s jazan oil refinery .
[text_16] 18 .
[text_17] capital stock common stock authorized common stock consists of 300 million shares with a par value of $ 1 per share .
[text_18] as of 30 september 2016 , 249 million shares were issued , with 217 million outstanding .
[text_19] on 15 september 2011 , the board of directors authorized the repurchase of up to $ 1000 of our outstanding common stock .
[text_20] we repurchase shares pursuant to rules 10b5-1 and 10b-18 under the securities exchange act of 1934 , as amended , through repurchase agreements established with several brokers .
[text_21] we did not purchase any of our outstanding shares during fiscal year 2016 .
[text_22] at 30 september 2016 , $ 485.3 in share repurchase authorization remains. .
[table_0] 2017 | $ 942
[table_1] 2017: 2018 | $ 942: 525
[table_2] 2017: 2019 | $ 942: 307
[table_3] 2017: 2020 | $ 942: 298
[table_4] 2017: 2021 | $ 942: 276
[table_5] 2017: thereafter | $ 942: 2983
[table_6] 2017: total | $ 942: $ 5331

Question: what is the percentage of outstanding shares among all issued shares?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_18","value":"217"},{"source":"text_18","value":"249"}]}],"answer":0.8714859437751004}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_18","value":"249"},{"source":"text_17","value":"300"}]}],"answer":0.83}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_18","value":"249"},{"source":"text_17","value":"300"}]}],"answer":0.8266666666666666}
```

## 70. AAPL/2013/page_78.pdf-4

Evidence:
[text_0] table of contents rent expense under all operating leases , including both cancelable and noncancelable leases , was $ 645 million , $ 488 million and $ 338 million in 2013 , 2012 and 2011 , respectively .
[text_1] future minimum lease payments under noncancelable operating leases having remaining terms in excess of one year as of september 28 , 2013 , are as follows ( in millions ) : other commitments as of september 28 , 2013 , the company had outstanding off-balance sheet third-party manufacturing commitments and component purchase commitments of $ 18.6 billion .
[text_2] in addition to the off-balance sheet commitments mentioned above , the company had outstanding obligations of $ 1.3 billion as of september 28 , 2013 , which consisted mainly of commitments to acquire capital assets , including product tooling and manufacturing process equipment , and commitments related to advertising , research and development , internet and telecommunications services and other obligations .
[text_3] contingencies the company is subject to various legal proceedings and claims that have arisen in the ordinary course of business and that have not been fully adjudicated .
[text_4] in the opinion of management , there was not at least a reasonable possibility the company may have incurred a material loss , or a material loss in excess of a recorded accrual , with respect to loss contingencies .
[text_5] however , the outcome of litigation is inherently uncertain .
[text_6] therefore , although management considers the likelihood of such an outcome to be remote , if one or more of these legal matters were resolved against the company in a reporting period for amounts in excess of management 2019s expectations , the company 2019s consolidated financial statements for that reporting period could be materially adversely affected .
[text_7] apple inc .
[text_8] v .
[text_9] samsung electronics co. , ltd , et al .
[text_10] on august 24 , 2012 , a jury returned a verdict awarding the company $ 1.05 billion in its lawsuit against samsung electronics co. , ltd and affiliated parties in the united states district court , northern district of california , san jose division .
[text_11] on march 1 , 2013 , the district court upheld $ 599 million of the jury 2019s award and ordered a new trial as to the remainder .
[text_12] because the award is subject to entry of final judgment , partial re-trial and appeal , the company has not recognized the award in its results of operations .
[text_13] virnetx , inc .
[text_14] v .
[text_15] apple inc .
[text_16] et al .
[text_17] on august 11 , 2010 , virnetx , inc .
[text_18] filed an action against the company alleging that certain of its products infringed on four patents relating to network communications technology .
[text_19] on november 6 , 2012 , a jury returned a verdict against the company , and awarded damages of $ 368 million .
[text_20] the company is challenging the verdict , believes it has valid defenses and has not recorded a loss accrual at this time. .
[text_21] .
[table_0] 2014 | $ 610
[table_1] 2014: 2015 | $ 610: 613
[table_2] 2014: 2016 | $ 610: 587
[table_3] 2014: 2017 | $ 610: 551
[table_4] 2014: 2018 | $ 610: 505
[table_5] 2014: thereafter | $ 610: 1855
[table_6] 2014: total minimum lease payments | $ 610: $ 4721

Question: why is the information relative to 2012 costs incorrect and what would the correct information be?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_0","value":"488"},{"source":"text_19","value":"368"}]}],"answer":856.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_0","value":"488"},{"source":"text_0","value":"645"}]},{"op":"divide","args":["#0",{"source":"text_0","value":"645"}]}],"answer":-0.2434108527131783}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_0","value":"488"},{"source":"text_0","value":"645"}]},{"op":"divide","args":["#0",{"source":"text_0","value":"645"}]}],"answer":-0.00645}
```

## 71. JKHY/2019/page_18.pdf-2

Evidence:
[text_0] 2 0 1 9 a n n u a l r e p o r t1 6 performance graph the following chart presents a comparison for the five-year period ended june 30 , 2019 , of the market performance of the company 2019s common stock with the s&p 500 index and an index of peer companies selected by the company .
[text_1] historic stock price performance is not necessarily indicative of future stock price performance .
[text_2] comparison of 5 year cumulative total return among jack henry & associates , inc. , the s&p 500 index , and a peer group the following information depicts a line graph with the following values: .
[text_3] this comparison assumes $ 100 was invested on june 30 , 2014 , and assumes reinvestments of dividends .
[text_4] total returns are calculated according to market capitalization of peer group members at the beginning of each period .
[text_5] peer companies selected are in the business of providing specialized computer software , hardware and related services to financial institutions and other businesses .
[text_6] some peer participant companies were different for fiscal year ended 2019 compared to fiscal year ended 2018 .
[text_7] the company 2019s compensation committee of the board of directors adjusted the peer participants due to consolidations within the industry during the 2019 fiscal year .
[text_8] companies in the 2019 peer group are aci worldwide , inc. ; black knight , inc. ; bottomline technologies , inc. ; broadridge financial solutions , inc. ; cardtronics plc ; corelogic , inc. ; euronet worldwide , inc. ; exlservice holdings , inc. ; fair isaac corp. ; fidelity national information services , inc. ; fiserv , inc. ; fleetcor technologies , inc. ; global payments , inc. ; square , inc. ; ss&c technologies holdings , inc. ; total system services , inc. ; tyler technologies , inc. ; verint systems , inc. ; and wex , inc .
[text_9] companies in the 2018 peer group were aci worldwide , inc. ; bottomline technology , inc. ; broadridge financial solutions ; cardtronics , inc. ; corelogic , inc. ; euronet worldwide , inc. ; fair isaac corp. ; fidelity national information services , inc. ; fiserv , inc. ; global payments , inc. ; moneygram international , inc. ; ss&c technologies holdings , inc. ; total systems services , inc. ; tyler technologies , inc. ; verifone .
[table_0]  | 2014 | 2015 | 2016 | 2017 | 2018 | 2019
[table_1] : jkhy | 2014: 100.00 | 2015: 110.51 | 2016: 151.12 | 2017: 182.15 | 2018: 231.36 | 2019: 240.29
[table_2] : 2019 peer group | 2014: 100.00 | 2015: 126.23 | 2016: 142.94 | 2017: 166.15 | 2018: 224.73 | 2019: 281.09
[table_3] : 2018 peer group | 2014: 100.00 | 2015: 127.40 | 2016: 151.16 | 2017: 177.26 | 2018: 228.97 | 2019: 286.22
[table_4] : s&p 500 | 2014: 100.00 | 2015: 107.42 | 2016: 111.71 | 2017: 131.70 | 2018: 150.64 | 2019: 166.33

Question: what was the 5 year total return for jkhy?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"240.29"},{"source":"table_1","value":"100.00"}]}],"answer":140.29}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"240.29"},{"source":"table_1","value":"100.00"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100.00"}]}],"answer":1.4029}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"240.29"},{"source":"table_1","value":"100.00"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100.00"}]}],"answer":1.4029}
```

## 72. ETR/2016/page_343.pdf-1

Evidence:
[text_0] entergy louisiana , llc and subsidiaries management 2019s financial discussion and analysis in industrial usage is primarily due to increased demand from new customers and expansion projects , primarily in the chemicals industry .
[text_1] the louisiana act 55 financing savings obligation variance results from a regulatory charge for tax savings to be shared with customers per an agreement approved by the lpsc .
[text_2] the tax savings resulted from the 2010-2011 irs audit settlement on the treatment of the louisiana act 55 financing of storm costs for hurricane gustav and hurricane ike .
[text_3] see note 3 to the financial statements for additional discussion of the settlement and benefit sharing .
[text_4] included in other is a provision of $ 23 million recorded in 2016 related to the settlement of the waterford 3 replacement steam generator prudence review proceeding , offset by a provision of $ 32 million recorded in 2015 related to the uncertainty at that time associated with the resolution of the waterford 3 replacement steam generator prudence review proceeding .
[text_5] see note 2 to the financial statements for a discussion of the waterford 3 replacement steam generator prudence review proceeding .
[text_6] 2015 compared to 2014 net revenue consists of operating revenues net of : 1 ) fuel , fuel-related expenses , and gas purchased for resale , 2 ) purchased power expenses , and 3 ) other regulatory charges ( credits ) .
[text_7] following is an analysis of the change in net revenue comparing 2015 to 2014 .
[text_8] amount ( in millions ) .
[text_9] the retail electric price variance is primarily due to formula rate plan increases , as approved by the lpsc , effective december 2014 and january 2015 .
[text_10] entergy louisiana 2019s formula rate plan increases are discussed in note 2 to the financial statements .
[text_11] the volume/weather variance is primarily due to an increase of 841 gwh , or 2% ( 2 % ) , in billed electricity usage , as a result of increased industrial usage primarily due to increased demand for existing large refinery customers , new customers , and expansion projects primarily in the chemicals industry , partially offset by a decrease in demand in the chemicals industry as a result of a seasonal outage for an existing customer .
[text_12] the waterford 3 replacement steam generator provision is due to a regulatory charge of approximately $ 32 million recorded in 2015 related to the uncertainty associated with the resolution of the waterford 3 replacement steam generator project .
[text_13] see note 2 to the financial statements for a discussion of the waterford 3 replacement steam generator prudence review proceeding .
[text_14] the miso deferral variance is due to the deferral in 2014 of non-fuel miso-related charges , as approved by the lpsc .
[text_15] the deferral of non-fuel miso-related charges is partially offset in other operation and maintenance expenses .
[text_16] see note 2 to the financial statements for further discussion of the recovery of non-fuel miso-related charges. .
[table_0]  | amount ( in millions )
[table_1] : 2014 net revenue | amount ( in millions ): $ 2246.1
[table_2] : retail electric price | amount ( in millions ): 180.0
[table_3] : volume/weather | amount ( in millions ): 39.5
[table_4] : waterford 3 replacement steam generator provision | amount ( in millions ): -32.0 ( 32.0 )
[table_5] : miso deferral | amount ( in millions ): -32.0 ( 32.0 )
[table_6] : other | amount ( in millions ): 7.2
[table_7] : 2015 net revenue | amount ( in millions ): $ 2408.8

Question: without the benefit of the retail electric price and volume/weather adjustments , what would the 2015 net revenue be , in millions?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"180.0"},{"source":"table_3","value":"39.5"}]},{"op":"subtract","args":[{"source":"table_7","value":"2408.8"},"#0"]}],"answer":2189.3}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_7","value":"2408.8"},{"source":"table_2","value":"180.0"}]}],"answer":2228.8}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_7","value":"2408.8"},{"source":"table_2","value":"180.0"}]}],"answer":2228.8}
```

## 73. SNA/2013/page_33.pdf-1

Evidence:
[text_0] other purchases or sales of equity securities the following chart discloses information regarding shares of snap-on 2019s common stock that were sold by citibank , n.a .
[text_1] ( 201ccitibank 201d ) during the fourth quarter of 2013 pursuant to a prepaid equity forward transaction agreement ( the 201cagreement 201d ) with citibank that is intended to reduce the impact of market risk associated with the stock-based portion of the company 2019s deferred compensation plans .
[text_2] the company 2019s stock-based deferred compensation liabilities , which are impacted by changes in the company 2019s stock price , increase as the company 2019s stock price rises and decrease as the company 2019s stock price declines .
[text_3] pursuant to the agreement , citibank may purchase or sell shares of the company 2019s common stock ( for citibank 2019s account ) in the market or in privately negotiated transactions .
[text_4] the agreement has no stated expiration date , but the parties expect that each transaction under the agreement will have a term of approximately one year .
[text_5] the agreement does not provide for snap-on to purchase or repurchase shares .
[text_6] the following chart discloses information regarding citibank 2019s sales of snap-on common stock during the fourth quarter of 2013 pursuant to the agreement : period shares sold average per share .
[text_7] 2013 annual report 23 .
[table_0] period | shares sold | averagepriceper share
[table_1] period: 09/29/13 to 10/26/13 | shares sold: 2013 | averagepriceper share: 2013
[table_2] period: 10/27/13 to 11/23/13 | shares sold: 2013 | averagepriceper share: 2013
[table_3] period: 11/24/13 to 12/28/13 | shares sold: 5000 | averagepriceper share: $ 106.32
[table_4] period: total/average | shares sold: 5000 | averagepriceper share: $ 106.32

Question: how is the cash flow statement from financing activities affected by the sales of commons stock during the 4th quarter of 2013?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"table_3","value":"5000"},{"source":"table_3","value":"106.32"}]}],"answer":531600.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_3","value":"5000"},{"source":"table_3","value":"106.32"}]},{"op":"add","args":["#0",{"source":"table_3","value":"106.32"}]}],"answer":5212.64}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_3","value":"5000"},{"source":"table_3","value":"106.32"}]},{"op":"add","args":["#0",{"source":"table_3","value":"106.32"}]}],"answer":5106.32}
```

## 74. UPS/2013/page_34.pdf-2

Evidence:
[text_0] shareowner return performance graph the following performance graph and related information shall not be deemed 201csoliciting material 201d or to be 201cfiled 201d with the sec , nor shall such information be incorporated by reference into any future filing under the securities act of 1933 or securities exchange act of 1934 , each as amended , except to the extent that the company specifically incorporates such information by reference into such filing .
[text_1] the following graph shows a five year comparison of cumulative total shareowners 2019 returns for our class b common stock , the standard & poor 2019s 500 index , and the dow jones transportation average .
[text_2] the comparison of the total cumulative return on investment , which is the change in the quarterly stock price plus reinvested dividends for each of the quarterly periods , assumes that $ 100 was invested on december 31 , 2008 in the standard & poor 2019s 500 index , the dow jones transportation average , and our class b common stock. .
[text_3] .
[table_0]  | 12/31/2008 | 12/31/2009 | 12/31/2010 | 12/31/2011 | 12/31/2012 | 12/31/2013
[table_1] : united parcel service inc . | 12/31/2008: $ 100.00 | 12/31/2009: $ 107.75 | 12/31/2010: $ 140.39 | 12/31/2011: $ 145.84 | 12/31/2012: $ 151.44 | 12/31/2013: $ 221.91
[table_2] : standard & poor 2019s 500 index | 12/31/2008: $ 100.00 | 12/31/2009: $ 126.45 | 12/31/2010: $ 145.49 | 12/31/2011: $ 148.55 | 12/31/2012: $ 172.30 | 12/31/2013: $ 228.09
[table_3] : dow jones transportation average | 12/31/2008: $ 100.00 | 12/31/2009: $ 118.59 | 12/31/2010: $ 150.30 | 12/31/2011: $ 150.31 | 12/31/2012: $ 161.56 | 12/31/2013: $ 228.42

Question: what was the difference in percentage total cumulative return on investment for united parcel service inc . compared to the dow jones transportation average for the five years ended 12/31/2013?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"221.91"},"const_100"]},{"op":"divide","args":["#0","const_100"]},{"op":"subtract","args":[{"source":"table_3","value":"228.42"},"const_100"]},{"op":"divide","args":["#2","const_100"]},{"op":"subtract","args":["#1","#3"]}],"answer":-0.0651}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"221.91"},"const_100"]},{"op":"divide","args":["#0","const_100"]}],"answer":1.2191}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"221.91"},"const_100"]},{"op":"divide","args":["#0","const_100"]}],"answer":0.2191}
```

## 75. FRT/2009/page_124.pdf-1

Evidence:
[text_0] federal realty investment trust schedule iii summary of real estate and accumulated depreciation 2014continued three years ended december 31 , 2009 reconciliation of accumulated depreciation and amortization ( in thousands ) .
[text_1] .
[table_0] balance december 31 2006 | $ 740507
[table_1] balance december 31 2006: additions during period 2014depreciation and amortization expense | $ 740507: 96454
[table_2] balance december 31 2006: deductions during period 2014disposition and retirements of property | $ 740507: -80258 ( 80258 )
[table_3] balance december 31 2006: balance december 31 2007 | $ 740507: 756703
[table_4] balance december 31 2006: additions during period 2014depreciation and amortization expense | $ 740507: 101321
[table_5] balance december 31 2006: deductions during period 2014disposition and retirements of property | $ 740507: -11766 ( 11766 )
[table_6] balance december 31 2006: balance december 31 2008 | $ 740507: 846258
[table_7] balance december 31 2006: additions during period 2014depreciation and amortization expense | $ 740507: 103.698
[table_8] balance december 31 2006: deductions during period 2014disposition and retirements of property | $ 740507: -11869 ( 11869 )
[table_9] balance december 31 2006: balance december 31 2009 | $ 740507: $ 938087

Question: considering the years 2006-2009 , what is the value of the average additions?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"96454"},{"source":"table_4","value":"101321"}]},{"op":"multiply","args":["const_1000",{"source":"table_7","value":"103.698"}]},{"op":"add","args":["#0","#1"]},{"op":"divide","args":["#2","const_3"]}],"answer":100491.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_4","value":"101321"},{"source":"table_7","value":"103.698"}]},{"op":"divide","args":["#0",{"source":"table_4","value":"740507"}]}],"answer":0.13696656209867022}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_4","value":"101321"},{"source":"table_7","value":"103.698"}]},{"op":"divide","args":["#0",{"source":"table_4","value":"740507"}]}],"answer":0.1414141414141414}
```

## 76. BLL/2011/page_29.pdf-4

Evidence:
[text_0] shareholder return performance the line graph below compares the annual percentage change in ball corporation fffds cumulative total shareholder return on its common stock with the cumulative total return of the dow jones containers & packaging index and the s&p composite 500 stock index for the five-year period ended december 31 , 2011 .
[text_1] it assumes $ 100 was invested on december 31 , 2006 , and that all dividends were reinvested .
[text_2] the dow jones containers & packaging index total return has been weighted by market capitalization .
[text_3] total return to stockholders ( assumes $ 100 investment on 12/31/06 ) total return analysis .
[text_4] copyright a9 2012 standard & poor fffds , a division of the mcgraw-hill companies inc .
[text_5] all rights reserved .
[text_6] ( www.researchdatagroup.com/s&p.htm ) copyright a9 2012 dow jones & company .
[text_7] all rights reserved. .
[table_0]  | 12/31/2006 | 12/31/2007 | 12/31/2008 | 12/31/2009 | 12/31/2010 | 12/31/2011
[table_1] : ball corporation | 12/31/2006: $ 100.00 | 12/31/2007: $ 104.05 | 12/31/2008: $ 97.04 | 12/31/2009: $ 121.73 | 12/31/2010: $ 161.39 | 12/31/2011: $ 170.70
[table_2] : dj us containers & packaging | 12/31/2006: $ 100.00 | 12/31/2007: $ 106.73 | 12/31/2008: $ 66.91 | 12/31/2009: $ 93.98 | 12/31/2010: $ 110.23 | 12/31/2011: $ 110.39
[table_3] : s&p 500 | 12/31/2006: $ 100.00 | 12/31/2007: $ 105.49 | 12/31/2008: $ 66.46 | 12/31/2009: $ 84.05 | 12/31/2010: $ 96.71 | 12/31/2011: $ 98.75

Question: what was the five year percentage return on ball corporation stock?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"170.70"},{"source":"table_1","value":"100.00"}]}],"answer":1.707}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"170.70"},"const_100"]},{"op":"divide","args":["#0","const_100"]}],"answer":0.707}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"170.70"},"const_100"]},{"op":"divide","args":["#0","const_100"]}],"answer":0.707}
```

## 77. AMAT/2018/page_31.pdf-3

Evidence:
[text_0] item 2 : properties information concerning applied 2019s properties is set forth below: .
[text_1] because of the interrelation of applied 2019s operations , properties within a country may be shared by the segments operating within that country .
[text_2] the company 2019s headquarters offices are in santa clara , california .
[text_3] products in semiconductor systems are manufactured in santa clara , california ; austin , texas ; gloucester , massachusetts ; kalispell , montana ; rehovot , israel ; and singapore .
[text_4] remanufactured equipment products in the applied global services segment are produced primarily in austin , texas .
[text_5] products in the display and adjacent markets segment are manufactured in alzenau , germany and tainan , taiwan .
[text_6] other products are manufactured in treviso , italy .
[text_7] applied also owns and leases offices , plants and warehouse locations in many locations throughout the world , including in europe , japan , north america ( principally the united states ) , israel , china , india , korea , southeast asia and taiwan .
[text_8] these facilities are principally used for manufacturing ; research , development and engineering ; and marketing , sales and customer support .
[text_9] applied also owns a total of approximately 269 acres of buildable land in montana , texas , california , israel and italy that could accommodate additional building space .
[text_10] applied considers the properties that it owns or leases as adequate to meet its current and future requirements .
[text_11] applied regularly assesses the size , capability and location of its global infrastructure and periodically makes adjustments based on these assessments. .
[table_0] ( square feet in thousands ) | united states | other countries | total
[table_1] ( square feet in thousands ): owned | united states: 4530 | other countries: 2417 | total: 6947
[table_2] ( square feet in thousands ): leased | united states: 1037 | other countries: 1341 | total: 2378
[table_3] ( square feet in thousands ): total | united states: 5567 | other countries: 3758 | total: 9325

Question: what portion of company's property is located in united states?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_3","value":"5567"},{"source":"table_3","value":"9325"}]}],"answer":0.5969973190348525}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"4530"},{"source":"table_3","value":"9325"}]}],"answer":0.4857908847184987}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"4530"},{"source":"table_3","value":"9325"}]}],"answer":0.4841149012345679}
```

## 78. JKHY/2017/page_26.pdf-2

Evidence:
[text_0] 24 2017 annual report performance graph the following chart presents a comparison for the five-year period ended june 30 , 2017 , of the market performance of the company 2019s common stock with the s&p 500 index and an index of peer companies selected by the company : comparison of 5 year cumulative total return among jack henry & associates , inc. , the s&p 500 index , and a peer group the following information depicts a line graph with the following values: .
[text_1] this comparison assumes $ 100 was invested on june 30 , 2012 , and assumes reinvestments of dividends .
[text_2] total returns are calculated according to market capitalization of peer group members at the beginning of each period .
[text_3] peer companies selected are in the business of providing specialized computer software , hardware and related services to financial institutions and other businesses .
[text_4] companies in the peer group are aci worldwide , inc. ; bottomline technology , inc. ; broadridge financial solutions ; cardtronics , inc. ; convergys corp. ; corelogic , inc. ; dst systems , inc. ; euronet worldwide , inc. ; fair isaac corp. ; fidelity national information services , inc. ; fiserv , inc. ; global payments , inc. ; moneygram international , inc. ; ss&c technologies holdings , inc. ; total systems services , inc. ; tyler technologies , inc. ; verifone systems , inc. ; and wex , inc.. .
[table_0]  | 2012 | 2013 | 2014 | 2015 | 2016 | 2017
[table_1] : jkhy | 2012: 100.00 | 2013: 138.34 | 2014: 177.10 | 2015: 195.72 | 2016: 267.64 | 2017: 322.60
[table_2] : peer group | 2012: 100.00 | 2013: 117.87 | 2014: 161.90 | 2015: 203.87 | 2016: 233.39 | 2017: 271.10
[table_3] : s&p 500 | 2012: 100.00 | 2013: 120.60 | 2014: 150.27 | 2015: 161.43 | 2016: 167.87 | 2017: 197.92

Question: jkhy's total 5 year return was what percent of the peer group?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"322.60"},{"source":"table_2","value":"271.10"}]}],"answer":1.1899668019181113}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"322.60"},{"source":"table_2","value":"233.39"}]}],"answer":1.3822357427481897}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"322.60"},{"source":"table_2","value":"233.39"}]}],"answer":1.3611111111111112}
```

## 79. AON/2010/page_61.pdf-1

Evidence:
[text_0] holding other assumptions constant , the following table reflects what a one hundred basis point increase and decrease in our estimated long-term rate of return on plan assets would have on our estimated 2011 pension expense ( in millions ) : change in long-term rate of return on plan assets .
[text_1] estimated future contributions we estimate contributions of approximately $ 403 million in 2011 as compared with $ 288 million in goodwill and other intangible assets goodwill represents the excess of cost over the fair market value of the net assets acquired .
[text_2] we classify our intangible assets acquired as either trademarks , customer relationships , technology , non-compete agreements , or other purchased intangibles .
[text_3] our goodwill and other intangible balances at december 31 , 2010 increased to $ 8.6 billion and $ 3.6 billion , respectively , compared to $ 6.1 billion and $ 791 million , respectively , at december 31 , 2009 , primarily as a result of the hewitt acquisition .
[text_4] although goodwill is not amortized , we test it for impairment at least annually in the fourth quarter .
[text_5] in the fourth quarter , we also test acquired trademarks ( which also are not amortized ) for impairment .
[text_6] we test more frequently if there are indicators of impairment or whenever business circumstances suggest that the carrying value of goodwill or trademarks may not be recoverable .
[text_7] these indicators may include a sustained significant decline in our share price and market capitalization , a decline in our expected future cash flows , or a significant adverse change in legal factors or in the business climate , among others .
[text_8] no events occurred during 2010 or 2009 that indicate the existence of an impairment with respect to our reported goodwill or trademarks .
[text_9] we perform impairment reviews at the reporting unit level .
[text_10] a reporting unit is an operating segment or one level below an operating segment ( referred to as a 2018 2018component 2019 2019 ) .
[text_11] a component of an operating segment is a reporting unit if the component constitutes a business for which discrete financial information is available and segment management regularly reviews the operating results of that component .
[text_12] an operating segment shall be deemed to be a reporting unit if all of its components are similar , if none of its components is a reporting unit , or if the segment comprises only a single component .
[text_13] the goodwill impairment test is a two step analysis .
[text_14] step one requires the fair value of each reporting unit to be compared to its book value .
[text_15] management must apply judgment in determining the estimated fair value of the reporting units .
[text_16] if the fair value of a reporting unit is determined to be greater than the carrying value of the reporting unit , goodwill and trademarks are deemed not to be impaired and no further testing is necessary .
[text_17] if the fair value of a reporting unit is less than the carrying value , we perform step two .
[text_18] step two uses the calculated fair value of the reporting unit to perform a hypothetical purchase price allocation to the fair value of the assets and liabilities of the reporting unit .
[text_19] the difference between the fair value of the reporting unit calculated in step one and the fair value of the underlying assets and liabilities of the reporting unit is the implied fair value of the reporting unit 2019s goodwill .
[text_20] a charge is recorded in the financial statements if the carrying value of the reporting unit 2019s goodwill is greater than its implied fair value. .
[table_0] increase ( decrease ) in expense | change in long-term rateof return on plan assets increase | change in long-term rateof return on plan assets decrease
[table_1] increase ( decrease ) in expense: u.s . plans | change in long-term rateof return on plan assets increase: $ -14 ( 14 ) | change in long-term rateof return on plan assets decrease: $ 14
[table_2] increase ( decrease ) in expense: u.k . plans | change in long-term rateof return on plan assets increase: -35 ( 35 ) | change in long-term rateof return on plan assets decrease: 35
[table_3] increase ( decrease ) in expense: the netherlands plan | change in long-term rateof return on plan assets increase: -5 ( 5 ) | change in long-term rateof return on plan assets decrease: 5
[table_4] increase ( decrease ) in expense: canada plans | change in long-term rateof return on plan assets increase: -2 ( 2 ) | change in long-term rateof return on plan assets decrease: 2

Question: what was the percentage change in the goodwill in 2010 as a result of the hewitt acquisition .

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_3","value":"8.6"},{"source":"text_3","value":"6.1"}]},{"op":"divide","args":["#0",{"source":"text_3","value":"6.1"}]}],"answer":0.4098360655737705}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_3","value":"8.6"},{"source":"text_3","value":"6.1"}]}],"answer":1.4098360655737705}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_3","value":"8.6"},{"source":"text_3","value":"6.1"}]}],"answer":1.4117647058823529}
```

## 80. ETR/2016/page_324.pdf-3

Evidence:
[text_0] entergy arkansas , inc .
[text_1] and subsidiaries management 2019s financial discussion and analysis stock restrict the amount of retained earnings available for the payment of cash dividends or other distributions on its common and preferred stock .
[text_2] sources of capital entergy arkansas 2019s sources to meet its capital requirements include : 2022 internally generated funds ; 2022 cash on hand ; 2022 debt or preferred stock issuances ; and 2022 bank financing under new or existing facilities .
[text_3] entergy arkansas may refinance , redeem , or otherwise retire debt and preferred stock prior to maturity , to the extent market conditions and interest and dividend rates are favorable .
[text_4] all debt and common and preferred stock issuances by entergy arkansas require prior regulatory approval .
[text_5] preferred stock and debt issuances are also subject to issuance tests set forth in entergy arkansas 2019s corporate charters , bond indentures , and other agreements .
[text_6] entergy arkansas has sufficient capacity under these tests to meet its foreseeable capital needs .
[text_7] entergy arkansas 2019s receivables from or ( payables to ) the money pool were as follows as of december 31 for each of the following years. .
[text_8] see note 4 to the financial statements for a description of the money pool .
[text_9] entergy arkansas has a credit facility in the amount of $ 150 million scheduled to expire in august 2021 .
[text_10] entergy arkansas also has a $ 20 million credit facility scheduled to expire in april 2017 .
[text_11] the $ 150 million credit facility allows entergy arkansas to issue letters of credit against 50% ( 50 % ) of the borrowing capacity of the facility .
[text_12] as of december 31 , 2016 , there were no cash borrowings and no letters of credit outstanding under the credit facilities .
[text_13] in addition , entergy arkansas is a party to an uncommitted letter of credit facility as a means to post collateral to support its obligations under miso .
[text_14] as of december 31 , 2016 , a $ 1 million letter of credit was outstanding under entergy arkansas 2019s uncommitted letter of credit facility .
[text_15] see note 4 to the financial statements for additional discussion of the credit facilities .
[text_16] the entergy arkansas nuclear fuel company variable interest entity has a credit facility in the amount of $ 80 million scheduled to expire in may 2019 .
[text_17] as of december 31 , 2016 , no letters of credit were outstanding under the credit facility to support commercial paper issued by the entergy arkansas nuclear fuel company variable interest entity .
[text_18] see note 4 to the financial statements for additional discussion of the nuclear fuel company variable interest entity credit facility .
[text_19] entergy arkansas obtained authorizations from the ferc through october 2017 for short-term borrowings not to exceed an aggregate amount of $ 250 million at any time outstanding and long-term borrowings by its nuclear fuel company variable interest entity .
[text_20] see note 4 to the financial statements for further discussion of entergy arkansas 2019s short-term borrowing limits .
[text_21] the long-term securities issuances of entergy arkansas are limited to amounts authorized by the apsc and the tennessee regulatory authority ; the current authorizations extend through december 2018. .
[table_0] 2016 | 2015 | 2014 | 2013
[table_1] 2016: ( in thousands ) | 2015: ( in thousands ) | 2014: ( in thousands ) | 2013: ( in thousands )
[table_2] 2016: ( $ 51232 ) | 2015: ( $ 52742 ) | 2014: $ 2218 | 2013: $ 17531

Question: how is cash flow of entergy arkansas affected by the change in balance of money pool from 2014 to 2015?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"52742"},{"source":"table_2","value":"2218"}]}],"answer":54960.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"52742"},{"source":"table_2","value":"2218"}]}],"answer":50524.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"52742"},{"source":"table_2","value":"2218"}]}],"answer":50524.0}
```

## 81. UPS/2017/page_31.pdf-3

Evidence:
[text_0] shareowner return performance graph the following performance graph and related information shall not be deemed 201csoliciting material 201d or to be 201cfiled 201d with the sec , nor shall such information be incorporated by reference into any future filing under the securities act of 1933 or securities exchange act of 1934 , each as amended , except to the extent that the company specifically incorporates such information by reference into such filing .
[text_1] the following graph shows a five-year comparison of cumulative total shareowners 2019 returns for our class b common stock , the standard & poor 2019s 500 index and the dow jones transportation average .
[text_2] the comparison of the total cumulative return on investment , which is the change in the quarterly stock price plus reinvested dividends for each of the quarterly periods , assumes that $ 100 was invested on december 31 , 2012 in the standard & poor 2019s 500 index , the dow jones transportation average and our class b common stock. .
[text_3] .
[table_0]  | 12/31/2012 | 12/31/2013 | 12/31/2014 | 12/31/2015 | 12/31/2016 | 12/31/2017
[table_1] : united parcel service inc . | 12/31/2012: $ 100.00 | 12/31/2013: $ 146.54 | 12/31/2014: $ 159.23 | 12/31/2015: $ 148.89 | 12/31/2016: $ 182.70 | 12/31/2017: $ 195.75
[table_2] : standard & poor 2019s 500 index | 12/31/2012: $ 100.00 | 12/31/2013: $ 132.38 | 12/31/2014: $ 150.49 | 12/31/2015: $ 152.55 | 12/31/2016: $ 170.79 | 12/31/2017: $ 208.06
[table_3] : dow jones transportation average | 12/31/2012: $ 100.00 | 12/31/2013: $ 141.38 | 12/31/2014: $ 176.83 | 12/31/2015: $ 147.19 | 12/31/2016: $ 179.37 | 12/31/2017: $ 213.49

Question: what is the difference in percentage cumulative total shareowners return for united parcel service inc . versus the dow jones transportation average for the five years ended 12/31/2017?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"195.75"},"const_100"]},{"op":"divide","args":["#0","const_100"]},{"op":"subtract","args":[{"source":"table_3","value":"213.49"},"const_100"]},{"op":"divide","args":["#2","const_100"]},{"op":"subtract","args":["#1","#3"]}],"answer":-0.1774}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"195.75"},{"source":"table_3","value":"213.49"}]},{"op":"divide","args":["#0",{"source":"table_3","value":"213.49"}]}],"answer":-0.08309522694271394}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"195.75"},{"source":"table_3","value":"213.49"}]},{"op":"divide","args":["#0",{"source":"table_3","value":"213.49"}]}],"answer":-0.1374000004300001}
```

## 82. DVN/2014/page_85.pdf-1

Evidence:
[text_0] devon energy corporation and subsidiaries notes to consolidated financial statements 2013 ( continued ) asset divestitures in conjunction with the asset divestitures in 2013 and 2014 , devon removed $ 26 million and $ 706 million of goodwill , respectively , which were allocated to these assets .
[text_1] impairment devon 2019s canadian goodwill was originally recognized in 2001 as a result of a business combination consisting almost entirely of conventional gas assets that devon no longer owns .
[text_2] as a result of performing the goodwill impairment test described in note 1 , devon concluded the implied fair value of its canadian goodwill was zero as of december 31 , 2014 .
[text_3] this conclusion was largely based on the significant decline in benchmark oil prices , particularly after opec 2019s decision not to reduce its production targets that was announced in late november 2014 .
[text_4] consequently , in the fourth quarter of 2014 , devon wrote off its remaining canadian goodwill and recognized a $ 1.9 billion impairment .
[text_5] other intangible assets as of december 31 , 2014 , intangible assets associated with customer relationships had a gross carrying amount of $ 569 million and $ 36 million of accumulated amortization .
[text_6] the weighted-average amortization period for the customer relationships is 13.7 years .
[text_7] amortization expense for intangibles was approximately $ 36 million for the year ended december 31 , 2014 .
[text_8] other intangible assets are reported in other long-term assets in the accompanying consolidated balance sheets .
[text_9] the following table summarizes the estimated aggregate amortization expense for the next five years .
[text_10] year amortization amount ( in millions ) .
[text_11] .
[table_0] year | amortization amount ( in millions )
[table_1] year: 2015 | amortization amount ( in millions ): $ 45
[table_2] year: 2016 | amortization amount ( in millions ): $ 45
[table_3] year: 2017 | amortization amount ( in millions ): $ 45
[table_4] year: 2018 | amortization amount ( in millions ): $ 45
[table_5] year: 2019 | amortization amount ( in millions ): $ 44

Question: what is the average amortization amount , in millions , from 2015-2019?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"table_1","value":"45"},"const_4"]},{"op":"add","args":["#0",{"source":"table_5","value":"44"}]},{"op":"divide","args":["#1","const_5"]}],"answer":44.8}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_5","value":"44"},{"source":"table_4","value":"45"}]},{"op":"divide","args":["#0",{"source":"table_4","value":"45"}]}],"answer":-0.022222222222222223}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_5","value":"44"},{"source":"table_4","value":"45"}]},{"op":"divide","args":["#0",{"source":"table_4","value":"45"}]}],"answer":0.9333333333333333}
```

## 83. AAPL/2013/page_27.pdf-2

Evidence:
[text_0] table of contents company stock performance the following graph shows a five-year comparison of cumulative total shareholder return , calculated on a dividend reinvested basis , for the company , the s&p 500 index , the s&p computer hardware index , and the dow jones u.s .
[text_1] technology supersector index .
[text_2] the graph assumes $ 100 was invested in each of the company 2019s common stock , the s&p 500 index , the s&p computer hardware index , and the dow jones u.s .
[text_3] technology supersector index as of the market close on september 30 , 2008 .
[text_4] data points on the graph are annual .
[text_5] note that historic stock price performance is not necessarily indicative of future stock price performance .
[text_6] fiscal year ending september 30 .
[text_7] copyright 2013 s&p , a division of the mcgraw-hill companies inc .
[text_8] all rights reserved .
[text_9] copyright 2013 dow jones & co .
[text_10] all rights reserved .
[text_11] *$ 100 invested on 9/30/08 in stock or index , including reinvestment of dividends .
[text_12] september 30 , september 30 , september 30 , september 30 , september 30 , september 30 .
[text_13] .
[table_0]  | september 30 2008 | september 30 2009 | september 30 2010 | september 30 2011 | september 30 2012 | september 30 2013
[table_1] : apple inc . | september 30 2008: $ 100 | september 30 2009: $ 163 | september 30 2010: $ 250 | september 30 2011: $ 335 | september 30 2012: $ 589 | september 30 2013: $ 431
[table_2] : s&p 500 index | september 30 2008: $ 100 | september 30 2009: $ 93 | september 30 2010: $ 103 | september 30 2011: $ 104 | september 30 2012: $ 135 | september 30 2013: $ 161
[table_3] : s&p computer hardware index | september 30 2008: $ 100 | september 30 2009: $ 118 | september 30 2010: $ 140 | september 30 2011: $ 159 | september 30 2012: $ 255 | september 30 2013: $ 197
[table_4] : dow jones us technology supersector index | september 30 2008: $ 100 | september 30 2009: $ 111 | september 30 2010: $ 124 | september 30 2011: $ 128 | september 30 2012: $ 166 | september 30 2013: $ 175

Question: by how much did apple inc . outperform the s&p computer hardware index over the above mentioned 6 year period?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"431"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100"}]},{"op":"subtract","args":[{"source":"table_3","value":"197"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#2",{"source":"table_1","value":"100"}]},{"op":"subtract","args":["#1","#3"]}],"answer":2.34}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"431"},{"source":"table_3","value":"197"}]}],"answer":234.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"431"},{"source":"table_3","value":"197"}]}],"answer":234.0}
```

## 84. DVN/2014/page_88.pdf-2

Evidence:
[text_0] devon energy corporation and subsidiaries notes to consolidated financial statements 2013 ( continued ) other debentures and notes following are descriptions of the various other debentures and notes outstanding at december 31 , 2014 and 2013 , as listed in the table presented at the beginning of this note .
[text_1] geosouthern debt in december 2013 , in conjunction with the planned geosouthern acquisition , devon issued $ 2.25 billion aggregate principal amount of fixed and floating rate senior notes resulting in cash proceeds of approximately $ 2.2 billion , net of discounts and issuance costs .
[text_2] the floating rate senior notes due in 2015 bear interest at a rate equal to three-month libor plus 0.45 percent , which rate will be reset quarterly .
[text_3] the floating rate senior notes due in 2016 bears interest at a rate equal to three-month libor plus 0.54 percent , which rate will be reset quarterly .
[text_4] the schedule below summarizes the key terms of these notes ( in millions ) . .
[text_5] ( 1 ) the 1.20% ( 1.20 % ) $ 650 million note due december 15 , 2016 was redeemed on november 13 , 2014 .
[text_6] the senior notes were classified as short-term debt on devon 2019s consolidated balance sheet as of december 31 , 2013 due to certain redemption features in the event that the geosouthern acquisition was not completed on or prior to june 30 , 2014 .
[text_7] on february 28 , 2014 , the geosouthern acquisition closed and thus the senior notes were subsequently classified as long-term debt .
[text_8] additionally , during december 2013 , devon entered into a term loan agreement with a group of major financial institutions pursuant to which devon could draw up to $ 2.0 billion to finance , in part , the geosouthern acquisition and to pay transaction costs .
[text_9] in february 2014 , devon drew the $ 2.0 billion of term loans for the geosouthern transaction , and the amount was subsequently repaid on june 30 , 2014 with the canadian divestiture proceeds that were repatriated to the u.s .
[text_10] in june 2014 , at which point the term loan was terminated. .
[table_0] floating rate due december 15 2015 | $ 500
[table_1] floating rate due december 15 2015: floating rate due december 15 2016 | $ 500: 350
[table_2] floating rate due december 15 2015: 1.20% ( 1.20 % ) due december 15 2016 ( 1 ) | $ 500: 650
[table_3] floating rate due december 15 2015: 2.25% ( 2.25 % ) due december 15 2018 | $ 500: 750
[table_4] floating rate due december 15 2015: discount and issuance costs | $ 500: -2 ( 2 )
[table_5] floating rate due december 15 2015: net proceeds | $ 500: $ 2248

Question: debt in december 2013 , what was the percent of the net of discounts and issuance costs associated with the issuance fixed and floating rate senior notes in conjunction with the planned geosouthern acquisition

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_1","value":"2.25"},{"source":"text_1","value":"2.2"}]},{"op":"divide","args":["#0",{"source":"text_1","value":"2.2"}]}],"answer":0.022727272727272728}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_1","value":"2.25"},"const_1000000000"]}],"answer":2.25e-09}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_1","value":"2.25"},"const_1000000000"]}],"answer":0.000000225}
```

## 85. C/2009/page_194.pdf-3

Evidence:
[text_0] in addition , included in the loan table are purchased distressed loans , which are loans that have evidenced significant credit deterioration subsequent to origination but prior to acquisition by citigroup .
[text_1] in accordance with sop 03-3 , the difference between the total expected cash flows for these loans and the initial recorded investments is recognized in income over the life of the loans using a level yield .
[text_2] accordingly , these loans have been excluded from the impaired loan information presented above .
[text_3] in addition , per sop 03-3 , subsequent decreases to the expected cash flows for a purchased distressed loan require a build of an allowance so the loan retains its level yield .
[text_4] however , increases in the expected cash flows are first recognized as a reduction of any previously established allowance and then recognized as income prospectively over the remaining life of the loan by increasing the loan 2019s level yield .
[text_5] where the expected cash flows cannot be reliably estimated , the purchased distressed loan is accounted for under the cost recovery method .
[text_6] the carrying amount of the purchased distressed loan portfolio at december 31 , 2009 was $ 825 million net of an allowance of $ 95 million .
[text_7] the changes in the accretable yield , related allowance and carrying amount net of accretable yield for 2009 are as follows : in millions of dollars accretable carrying amount of loan receivable allowance .
[text_8] ( 1 ) the balance reported in the column 201ccarrying amount of loan receivable 201d consists of $ 87 million of purchased loans accounted for under the level-yield method and $ 242 million under the cost-recovery method .
[text_9] these balances represent the fair value of these loans at their acquisition date .
[text_10] the related total expected cash flows for the level-yield loans were $ 101 million at their acquisition dates .
[text_11] ( 2 ) the balance reported in the column 201ccarrying amount of loan receivable 201d consists of $ 561 million of loans accounted for under the level-yield method and $ 359 million accounted for under the cost-recovery method. .
[table_0] in millions of dollars | accretable yield | carrying amount of loan receivable | allowance
[table_1] in millions of dollars: beginning balance | accretable yield: $ 92 | carrying amount of loan receivable: $ 1510 | allowance: $ 122
[table_2] in millions of dollars: purchases ( 1 ) | accretable yield: 14 | carrying amount of loan receivable: 329 | allowance: 2014
[table_3] in millions of dollars: disposals/payments received | accretable yield: -5 ( 5 ) | carrying amount of loan receivable: -967 ( 967 ) | allowance: 2014
[table_4] in millions of dollars: accretion | accretable yield: -52 ( 52 ) | carrying amount of loan receivable: 52 | allowance: 2014
[table_5] in millions of dollars: builds ( reductions ) to the allowance | accretable yield: -21 ( 21 ) | carrying amount of loan receivable: 1 | allowance: -27 ( 27 )
[table_6] in millions of dollars: increase to expected cash flows | accretable yield: 10 | carrying amount of loan receivable: 2 | allowance: 2014
[table_7] in millions of dollars: fx/other | accretable yield: -11 ( 11 ) | carrying amount of loan receivable: -7 ( 7 ) | allowance: 2014
[table_8] in millions of dollars: balance december 31 2009 ( 2 ) | accretable yield: $ 27 | carrying amount of loan receivable: $ 920 | allowance: $ 95

Question: what is the percent of the purchased loans accounted for under the level-yield method included in the carrying amount of loan receivable net of purchased loans accounted for under the under the cost-recovery method

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_8","value":"920"},{"source":"text_8","value":"242"}]},{"op":"divide","args":[{"source":"text_8","value":"87"},"#0"]}],"answer":0.12831858407079647}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_8","value":"920"},{"source":"table_8","value":"27"}]}],"answer":34.074074074074076}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_8","value":"920"},{"source":"table_8","value":"27"}]}],"answer":34.07407407407407}
```

## 86. ETR/2008/page_343.pdf-4

Evidence:
[text_0] entergy mississippi , inc .
[text_1] management's financial discussion and analysis sources of capital entergy mississippi's sources to meet its capital requirements include : internally generated funds ; cash on hand ; debt or preferred stock issuances ; and bank financing under new or existing facilities .
[text_2] entergy mississippi may refinance or redeem debt and preferred stock prior to maturity , to the extent market conditions and interest and dividend rates are favorable .
[text_3] all debt and common and preferred stock issuances by entergy mississippi require prior regulatory approval .
[text_4] preferred stock and debt issuances are also subject to issuance tests set forth in its corporate charter , bond indenture , and other agreements .
[text_5] entergy mississippi has sufficient capacity under these tests to meet its foreseeable capital needs .
[text_6] entergy mississippi has two separate credit facilities in the aggregate amount of $ 50 million and renewed both facilities through may 2009 .
[text_7] borrowings under the credit facilities may be secured by a security interest in entergy mississippi's accounts receivable .
[text_8] no borrowings were outstanding under either credit facility as of december 31 , 2008 .
[text_9] entergy mississippi has obtained short-term borrowing authorization from the ferc under which it may borrow through march 31 , 2010 , up to the aggregate amount , at any one time outstanding , of $ 175 million .
[text_10] see note 4 to the financial statements for further discussion of entergy mississippi's short-term borrowing limits .
[text_11] entergy mississippi has also obtained an order from the ferc authorizing long-term securities issuances .
[text_12] the current long-term authorization extends through june 30 , 2009 .
[text_13] entergy mississippi's receivables from or ( payables to ) the money pool were as follows as of december 31 for each of the following years: .
[text_14] in may 2007 , $ 6.6 million of entergy mississippi's receivable from the money pool was replaced by a note receivable from entergy new orleans .
[text_15] see note 4 to the financial statements for a description of the money pool .
[text_16] state and local rate regulation the rates that entergy mississippi charges for electricity significantly influence its financial position , results of operations , and liquidity .
[text_17] entergy mississippi is regulated and the rates charged to its customers are determined in regulatory proceedings .
[text_18] a governmental agency , the mpsc , is primarily responsible for approval of the rates charged to customers .
[text_19] formula rate plan in march 2008 , entergy mississippi made its annual scheduled formula rate plan filing for the 2007 test year with the mpsc .
[text_20] the filing showed that a $ 10.1 million increase in annual electric revenues is warranted .
[text_21] in june 2008 , entergy mississippi reached a settlement with the mississippi public utilities staff that would result in a $ 3.8 million rate increase .
[text_22] in january 2009 the mpsc rejected the settlement and left the current rates in effect .
[text_23] entergy mississippi appealed the mpsc's decision to the mississippi supreme court. .
[table_0] 2008 | 2007 | 2006 | 2005
[table_1] 2008: ( in thousands ) | 2007: ( in thousands ) | 2006: ( in thousands ) | 2005: ( in thousands )
[table_2] 2008: ( $ 66044 ) | 2007: $ 20997 | 2006: $ 39573 | 2005: ( $ 84066 )

Question: how is the cash flow of entergy mississippi affected by the balance in money pool from 2006 to 2007?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"39573"},{"source":"table_2","value":"20997"}]}],"answer":18576.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"20997"},{"source":"table_2","value":"39573"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"39573"}]}],"answer":-0.4694109620195588}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"20997"},{"source":"table_2","value":"39573"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"39573"}]}],"answer":-0.4094410256381094}
```

## 87. ETR/2004/page_261.pdf-4

Evidence:
[text_0] entergy new orleans , inc .
[text_1] management's financial discussion and analysis entergy new orleans' receivables from the money pool were as follows as of december 31 for each of the following years: .
[text_2] money pool activity provided $ 0.4 million of entergy new orleans' operating cash flow in 2004 , provided $ 1.7 million in 2003 , and provided $ 5.7 million in 2002 .
[text_3] see note 4 to the domestic utility companies and system energy financial statements for a description of the money pool .
[text_4] investing activities net cash used in investing activities decreased $ 15.5 million in 2004 primarily due to capital expenditures related to a turbine inspection project at a fossil plant in 2003 and decreased customer service spending .
[text_5] net cash used in investing activities increased $ 23.2 million in 2003 compared to 2002 primarily due to the maturity of $ 14.9 million of other temporary investments in 2002 and increased construction expenditures due to increased customer service spending .
[text_6] financing activities net cash used in financing activities increased $ 7.0 million in 2004 primarily due to the costs and expenses related to refinancing $ 75 million of long-term debt in 2004 and an increase of $ 2.2 million in common stock dividends paid .
[text_7] net cash used in financing activities increased $ 1.5 million in 2003 primarily due to additional common stock dividends paid of $ 2.2 million .
[text_8] in july 2003 , entergy new orleans issued $ 30 million of 3.875% ( 3.875 % ) series first mortgage bonds due august 2008 and $ 70 million of 5.25% ( 5.25 % ) series first mortgage bonds due august 2013 .
[text_9] the proceeds from these issuances were used to redeem , prior to maturity , $ 30 million of 7% ( 7 % ) series first mortgage bonds due july 2008 , $ 40 million of 8% ( 8 % ) series bonds due march 2006 , and $ 30 million of 6.65% ( 6.65 % ) series first mortgage bonds due march 2004 .
[text_10] the issuances and redemptions are not shown on the cash flow statement because the proceeds from the issuances were placed in a trust for use in the redemptions and never held as cash by entergy new orleans .
[text_11] see note 5 to the domestic utility companies and system energy financial statements for details on long- term debt .
[text_12] uses of capital entergy new orleans requires capital resources for : 2022 construction and other capital investments ; 2022 debt and preferred stock maturities ; 2022 working capital purposes , including the financing of fuel and purchased power costs ; and 2022 dividend and interest payments. .
[table_0] 2004 | 2003 | 2002 | 2001
[table_1] 2004: ( in thousands ) | 2003: ( in thousands ) | 2002: ( in thousands ) | 2001: ( in thousands )
[table_2] 2004: $ 1413 | 2003: $ 1783 | 2002: $ 3500 | 2001: $ 9208

Question: what are the receivables from the money pool as a percentage of additional common stock dividends paid in 2003?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"1783"},"const_1000"]},{"op":"divide","args":["#0",{"source":"text_6","value":"2.2"}]}],"answer":0.8104545454545454}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_2","value":"1.7"},{"source":"text_6","value":"2.2"}]}],"answer":0.7727272727272727}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_2","value":"1.7"},{"source":"text_6","value":"2.2"}]}],"answer":0.7727272727272727}
```

## 88. ETR/2017/page_373.pdf-1

Evidence:
[text_0] 2016 compared to 2015 net revenue consists of operating revenues net of : 1 ) fuel , fuel-related expenses , and gas purchased for resale , 2 ) purchased power expenses , and 3 ) other regulatory charges ( credits ) .
[text_1] following is an analysis of the change in net revenue comparing 2016 to 2015 .
[text_2] amount ( in millions ) .
[text_3] the retail electric price variance is primarily due to a $ 19.4 million net annual increase in revenues , as approved by the mpsc , effective with the first billing cycle of july 2016 , and an increase in revenues collected through the storm damage rider . a0 see note 2 to the financial statements for more discussion of the formula rate plan and the storm damage rider .
[text_4] the volume/weather variance is primarily due to an increase of 153 gwh , or 1% ( 1 % ) , in billed electricity usage , including an increase in industrial usage , partially offset by the effect of less favorable weather on residential and commercial sales .
[text_5] the increase in industrial usage is primarily due to expansion projects in the pulp and paper industry , increased demand for existing customers , primarily in the metals industry , and new customers in the wood products industry .
[text_6] the net wholesale revenue variance is primarily due to entergy mississippi 2019s exit from the system agreement in november 2015 .
[text_7] the reserve equalization revenue variance is primarily due to the absence of reserve equalization revenue as compared to the same period in 2015 resulting from entergy mississippi 2019s exit from the system agreement in november other income statement variances 2017 compared to 2016 other operation and maintenance expenses decreased primarily due to : 2022 a decrease of $ 12 million in fossil-fueled generation expenses primarily due to lower long-term service agreement costs and a lower scope of work done during plant outages in 2017 as compared to the same period in 2016 ; and 2022 a decrease of $ 3.6 million in storm damage provisions .
[text_8] see note 2 to the financial statements for a discussion on storm cost recovery .
[text_9] the decrease was partially offset by an increase of $ 4.8 million in energy efficiency costs and an increase of $ 2.7 million in compensation and benefits costs primarily due to higher incentive-based compensation accruals in 2017 as compared to the prior year .
[text_10] entergy mississippi , inc .
[text_11] management 2019s financial discussion and analysis .
[table_0]  | amount ( in millions )
[table_1] : 2015 net revenue | amount ( in millions ): $ 696.3
[table_2] : retail electric price | amount ( in millions ): 12.9
[table_3] : volume/weather | amount ( in millions ): 4.7
[table_4] : net wholesale revenue | amount ( in millions ): -2.4 ( 2.4 )
[table_5] : reserve equalization | amount ( in millions ): -2.8 ( 2.8 )
[table_6] : other | amount ( in millions ): -3.3 ( 3.3 )
[table_7] : 2016 net revenue | amount ( in millions ): $ 705.4

Question: the change in retail electric price accounts for what percent of revenue increase?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"12.9"},{"source":"text_3","value":"19.4"}]}],"answer":0.6649484536082474}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"12.9"},{"source":"table_1","value":"696.3"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"696.3"}]}],"answer":-0.981473502800517}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"12.9"},{"source":"table_1","value":"696.3"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"696.3"}]}],"answer":-0.1825410254102541}
```

## 89. AES/2011/page_270.pdf-2

Evidence:
[text_0] the aes corporation notes to consolidated financial statements 2014 ( continued ) december 31 , 2011 , 2010 , and 2009 the preliminary allocation of the purchase price to the fair value of assets acquired and liabilities assumed is as follows ( in millions ) : .
[text_1] at december 31 , 2011 , the assets acquired and liabilities assumed in the acquisition were recorded at provisional amounts based on the preliminary purchase price allocation .
[text_2] the company is in the process of obtaining additional information to identify and measure all assets acquired and liabilities assumed in the acquisition within the measurement period , which could be up to one year from the date of acquisition .
[text_3] such provisional amounts will be retrospectively adjusted to reflect any new information about facts and circumstances that existed at the acquisition date that , if known , would have affected the measurement of these amounts .
[text_4] additionally , key input assumptions and their sensitivity to the valuation of assets acquired and liabilities assumed are currently being reviewed by management .
[text_5] it is likely that the value of the generation business related property , plant and equipment , the intangible asset related to the electric security plan with its regulated customers and long-term coal contracts , the 4.9% ( 4.9 % ) equity ownership interest in the ohio valley electric corporation , and deferred taxes could change as the valuation process is finalized .
[text_6] dpler , dpl 2019s wholly-owned competitive retail electric service ( 201ccres 201d ) provider , will also likely have changes in its initial purchase price allocation for the valuation of its intangible assets for the trade name , and customer relationships and contracts .
[text_7] as noted in the table above , the preliminary purchase price allocation has resulted in the recognition of $ 2.5 billion of goodwill .
[text_8] factors primarily contributing to a price in excess of the fair value of the net tangible and intangible assets include , but are not limited to : the ability to expand the u.s .
[text_9] utility platform in the mid-west market , the ability to capitalize on utility management experience gained from ipl , enhanced ability to negotiate with suppliers of fuel and energy , the ability to capture value associated with aes 2019 u.s .
[text_10] tax position , a well- positioned generating fleet , the ability of dpl to leverage its assembled workforce to take advantage of growth opportunities , etc .
[text_11] our ability to realize the benefit of dpl 2019s goodwill depends on the realization of expected benefits resulting from a successful integration of dpl into aes 2019 existing operations and our ability to respond to the changes in the ohio utility market .
[text_12] for example , utilities in ohio continue to face downward pressure on operating margins due to the evolving regulatory environment , which is moving towards a market-based competitive pricing mechanism .
[text_13] at the same time , the declining energy prices are also reducing operating .
[table_0] cash | $ 116
[table_1] cash: accounts receivable | $ 116: 278
[table_2] cash: inventory | $ 116: 124
[table_3] cash: other current assets | $ 116: 41
[table_4] cash: property plant and equipment | $ 116: 2549
[table_5] cash: intangible assets subject to amortization | $ 116: 166
[table_6] cash: intangible assets 2014indefinite-lived | $ 116: 5
[table_7] cash: regulatory assets | $ 116: 201
[table_8] cash: other noncurrent assets | $ 116: 58
[table_9] cash: current liabilities | $ 116: -401 ( 401 )
[table_10] cash: non-recourse debt | $ 116: -1255 ( 1255 )
[table_11] cash: deferred taxes | $ 116: -558 ( 558 )
[table_12] cash: regulatory liabilities | $ 116: -117 ( 117 )
[table_13] cash: other noncurrent liabilities | $ 116: -195 ( 195 )
[table_14] cash: redeemable preferred stock | $ 116: -18 ( 18 )
[table_15] cash: net identifiable assets acquired | $ 116: 994
[table_16] cash: goodwill | $ 116: 2489
[table_17] cash: net assets acquired | $ 116: $ 3483

Question: what is the total in millions of current assets acquired?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"116"},{"source":"table_1","value":"278"}]},{"op":"add","args":["#0",{"source":"table_2","value":"124"}]},{"op":"add","args":["#1",{"source":"table_3","value":"41"}]}],"answer":559.0}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"116"},{"source":"table_2","value":"124"}]},{"op":"add","args":["#0",{"source":"table_3","value":"41"}]},{"op":"add","args":["#1",{"source":"table_4","value":"2549"}]}],"answer":2830.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"116"},{"source":"table_2","value":"124"}]},{"op":"add","args":["#0",{"source":"table_3","value":"41"}]},{"op":"add","args":["#1",{"source":"table_4","value":"2549"}]}],"answer":2716.0}
```

## 90. IPG/2008/page_62.pdf-1

Evidence:
[text_0] notes to consolidated financial statements 2014 ( continued ) ( amounts in millions , except per share amounts ) a summary of the remaining liability for the 2007 , 2003 and 2001 restructuring programs is as follows : program program program total .
[text_1] 1 includes amounts representing adjustments to the liability for changes in foreign currency exchange rates .
[text_2] other reorganization-related charges other reorganization-related charges relate to our realignment of our media businesses into a newly created management entity called mediabrands and the 2006 merger of draft worldwide and foote , cone and belding worldwide to create draftfcb .
[text_3] charges related to severance and terminations costs and lease termination and other exit costs .
[text_4] we expect charges associated with mediabrands to be completed during the first half of 2009 .
[text_5] charges related to the creation of draftfcb in 2006 are complete .
[text_6] the charges were separated from the rest of our operating expenses within the consolidated statements of operations because they did not result from charges that occurred in the normal course of business. .
[table_0]  | 2007 program | 2003 program | 2001 program | total
[table_1] : liability at december 31 2006 | 2007 program: $ 2014 | 2003 program: $ 12.6 | 2001 program: $ 19.2 | total: $ 31.8
[table_2] : net charges ( reversals ) and adjustments | 2007 program: 19.1 | 2003 program: -0.5 ( 0.5 ) | 2001 program: -5.2 ( 5.2 ) | total: 13.4
[table_3] : payments and other1 | 2007 program: -7.2 ( 7.2 ) | 2003 program: -3.1 ( 3.1 ) | 2001 program: -5.3 ( 5.3 ) | total: -15.6 ( 15.6 )
[table_4] : liability at december 31 2007 | 2007 program: $ 11.9 | 2003 program: $ 9.0 | 2001 program: $ 8.7 | total: $ 29.6
[table_5] : net charges and adjustments | 2007 program: 4.3 | 2003 program: 0.8 | 2001 program: 0.7 | total: 5.8
[table_6] : payments and other1 | 2007 program: -15.0 ( 15.0 ) | 2003 program: -4.1 ( 4.1 ) | 2001 program: -3.5 ( 3.5 ) | total: -22.6 ( 22.6 )
[table_7] : liability at december 31 2008 | 2007 program: $ 1.2 | 2003 program: $ 5.7 | 2001 program: $ 5.9 | total: $ 12.8

Question: what is the average liability for all three programs , as of december 31 , 2008 , in millions?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_7","value":"1.2"},{"source":"table_7","value":"5.7"}]},{"op":"add","args":["#0",{"source":"table_7","value":"5.9"}]},{"op":"divide","args":["#1","const_3"]}],"answer":4.266666666666667}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_7","value":"1.2"},{"source":"table_7","value":"5.7"}]},{"op":"add","args":["#0",{"source":"table_7","value":"5.9"}]}],"answer":12.8}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_7","value":"1.2"},{"source":"table_7","value":"5.7"}]},{"op":"add","args":["#0",{"source":"table_7","value":"5.9"}]}],"answer":12.8}
```

## 91. UA/2015/page_71.pdf-1

Evidence:
[text_0] simplify the presentation of deferred income taxes and reduce complexity without decreasing the usefulness of information provided to users of financial statements .
[text_1] the adoption of this pronouncement did not have a significant impact on the company 2019s financial position , results of operations and cash flows .
[text_2] 3 .
[text_3] acquisitions endomondo on january 5 , 2015 , the company acquired 100% ( 100 % ) of the outstanding equity of endomondo , a denmark- based digital connected fitness company , to expand the under armour connected fitness community .
[text_4] the purchase price was $ 85.0 million , adjusted for working capital .
[text_5] the company recognized $ 0.6 million and $ 0.8 million in acquisition related costs that were expensed during the three months ended march 31 , 2015 and december 31 , 2014 , respectively .
[text_6] these costs are included in the consolidated statements of income in the line item entitled 201cselling , general and administrative expenses . 201d pro forma results are not presented , as the acquisition was not considered material to the consolidated company .
[text_7] myfitnesspal on march 17 , 2015 , the company acquired 100% ( 100 % ) of the outstanding equity of mfp , a digital nutrition and connected fitness company , to expand the under armour connected fitness community .
[text_8] the final adjusted transaction value totaled $ 474.0 million .
[text_9] the total consideration of $ 463.9 million was adjusted to reflect the accelerated vesting of certain share awards of mfp , which are not conditioned upon continued employment , and transaction costs borne by the selling shareholders .
[text_10] the acquisition was funded with $ 400.0 million of increased term loan borrowings and a draw on the revolving credit facility , with the remaining amount funded by cash on the company recognized $ 5.7 million of acquisition related costs that were expensed during the three months ended march 31 , 2015 .
[text_11] these costs are included in the consolidated statement of income in the line item entitled 201cselling , general and administrative expenses . 201d the following represents the pro forma consolidated income statement as if mfp had been included in the consolidated results of the company for the year ended december 31 , 2015 and december 31 , 2014: .
[text_12] these amounts have been calculated after applying the company 2019s accounting policies and adjusting the results of mfp to reflect the acquisition as if it closed on january 1 , 2014 .
[text_13] pro forma net income for the year ended december 31 , 2014 includes $ 5.7 million in transaction expenses which were included in the consolidated statement of income for the year ended december 31 , 2015 , but excluded from the calculation of pro forma net income for december 31 , 2015. .
[table_0] ( in thousands ) | year ended december 31 , 2015 | year ended december 31 , 2014
[table_1] ( in thousands ): net revenues | year ended december 31 , 2015: $ 3967008 | year ended december 31 , 2014: $ 3098341
[table_2] ( in thousands ): net income | year ended december 31 , 2015: 231277 | year ended december 31 , 2014: 189659

Question: what was the profit margin in 2015

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"231277"},{"source":"table_1","value":"3967008"}]}],"answer":0.05830010930151893}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"231277"},{"source":"table_2","value":"189659"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"189659"}]}],"answer":0.2194359350202205}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"231277"},{"source":"table_2","value":"189659"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"189659"}]}],"answer":0.4345111111111111}
```

## 92. SLB/2009/page_65.pdf-3

Evidence:
[text_0] part ii , item 8 fourth quarter of 2007 : 0160 schlumberger sold certain workover rigs for $ 32 million , resulting in a pretax gain of $ 24 million ( $ 17 million after-tax ) which is classified in interest and other income , net in the consolidated statement of income .
[text_1] 4 .
[text_2] acquisitions acquisition of eastern echo holding plc on december 10 , 2007 , schlumberger completed the acquisition of eastern echo holding plc ( 201ceastern echo 201d ) for $ 838 million in cash .
[text_3] eastern echo was a dubai-based marine seismic company that did not have any operations at the time of acquisition , but had signed contracts for the construction of six seismic vessels .
[text_4] the purchase price has been allocated to the net assets acquired based upon their estimated fair values as follows : ( stated in millions ) .
[text_5] other acquisitions schlumberger has made other acquisitions and minority interest investments , none of which were significant on an individual basis , for cash payments , net of cash acquired , of $ 514 million during 2009 , $ 345 million during 2008 , and $ 281 million during 2007 .
[text_6] pro forma results pertaining to the above acquisitions are not presented as the impact was not significant .
[text_7] 5 .
[text_8] drilling fluids joint venture the mi-swaco drilling fluids joint venture is owned 40% ( 40 % ) by schlumberger and 60% ( 60 % ) by smith international , inc .
[text_9] schlumberger records income relating to this venture using the equity method of accounting .
[text_10] the carrying value of schlumberger 2019s investment in the joint venture on december 31 , 2009 and 2008 was $ 1.4 billion and $ 1.3 billion , respectively , and is included within investments in affiliated companies on the consolidated balance sheet .
[text_11] schlumberger 2019s equity income from this joint venture was $ 131 million in 2009 , $ 210 million in 2008 and $ 178 million in 2007 .
[text_12] schlumberger received cash distributions from the joint venture of $ 106 million in 2009 , $ 57 million in 2008 and $ 46 million in 2007 .
[text_13] the joint venture agreement contains a provision under which either party to the joint venture may offer to sell its entire interest in the venture to the other party at a cash purchase price per percentage interest specified in an offer notice .
[text_14] if the offer to sell is not accepted , the offering party will be obligated to purchase the entire interest of the other party at the same price per percentage interest as the prices specified in the offer notice. .
[table_0] cash and short-term investments | $ 266
[table_1] cash and short-term investments: other current assets | $ 266: 23
[table_2] cash and short-term investments: fixed income investments held to maturity | $ 266: 54
[table_3] cash and short-term investments: vessels under construction | $ 266: 694
[table_4] cash and short-term investments: accounts payable and accrued liabilities | $ 266: -17 ( 17 )
[table_5] cash and short-term investments: long-term debt | $ 266: -182 ( 182 )
[table_6] cash and short-term investments: total purchase price | $ 266: $ 838

Question: what was the growth rate of the equity income in drilling fluids joint venture the mi-swaco from 2007 to 2007 for schlumberger

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_11","value":"210"},{"source":"text_11","value":"178"}]},{"op":"divide","args":["#0",{"source":"text_11","value":"178"}]}],"answer":0.1797752808988764}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_11","value":"131"},{"source":"text_11","value":"178"}]},{"op":"divide","args":["#0",{"source":"text_11","value":"178"}]}],"answer":-0.2640449438202247}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_11","value":"131"},{"source":"text_11","value":"178"}]},{"op":"divide","args":["#0",{"source":"text_11","value":"178"}]}],"answer":0.06551724137931034}
```

## 93. RSG/2017/page_142.pdf-1

Evidence:
[text_0] republic services , inc .
[text_1] notes to consolidated financial statements 2014 ( continued ) employee stock purchase plan republic employees are eligible to participate in an employee stock purchase plan .
[text_2] the plan allows participants to purchase our common stock for 95% ( 95 % ) of its quoted market price on the last day of each calendar quarter .
[text_3] for the years ended december 31 , 2017 , 2016 and 2015 , issuances under this plan totaled 113941 shares , 130085 shares and 141055 shares , respectively .
[text_4] as of december 31 , 2017 , shares reserved for issuance to employees under this plan totaled 0.4 million and republic held employee contributions of approximately $ 1.8 million for the purchase of common stock .
[text_5] 12 .
[text_6] stock repurchases and dividends stock repurchases stock repurchase activity during the years ended december 31 , 2017 and 2016 follows ( in millions except per share amounts ) : .
[text_7] as of december 31 , 2017 , there were 0.5 million repurchased shares pending settlement and $ 33.8 million was unpaid and included within other accrued liabilities .
[text_8] in october 2017 , our board of directors added $ 2.0 billion to the existing share repurchase authorization that now extends through december 31 , 2020 .
[text_9] before this , $ 98.4 million remained under a prior authorization .
[text_10] share repurchases under the program may be made through open market purchases or privately negotiated transactions in accordance with applicable federal securities laws .
[text_11] while the board of directors has approved the program , the timing of any purchases , the prices and the number of shares of common stock to be purchased will be determined by our management , at its discretion , and will depend upon market conditions and other factors .
[text_12] the share repurchase program may be extended , suspended or discontinued at any time .
[text_13] as of december 31 , 2017 , the remaining authorized purchase capacity under our october 2017 repurchase program was $ 1.8 billion .
[text_14] in december 2015 , our board of directors changed the status of 71272964 treasury shares to authorized and unissued .
[text_15] in doing so , the number of our issued shares was reduced by the stated amount .
[text_16] our accounting policy is to deduct the par value from common stock and to reflect the excess of cost over par value as a deduction from additional paid-in capital .
[text_17] the change in unissued shares resulted in a reduction of $ 2295.3 million in treasury stock , $ 0.6 million in common stock , and $ 2294.7 million in additional paid-in capital .
[text_18] there was no effect on our total stockholders 2019 equity position as a result of the change .
[text_19] dividends in october 2017 , our board of directors approved a quarterly dividend of $ 0.345 per share .
[text_20] cash dividends declared were $ 446.3 million , $ 423.8 million and $ 404.3 million for the years ended december 31 , 2017 , 2016 and 2015 , respectively .
[text_21] as of december 31 , 2017 , we recorded a quarterly dividend payable of $ 114.4 million to shareholders of record at the close of business on january 2 , 2018 .
[text_22] 13 .
[text_23] earnings per share basic earnings per share is computed by dividing net income attributable to republic services , inc .
[text_24] by the weighted average number of common shares ( including vested but unissued rsus ) outstanding during the .
[table_0]  | 2017 | 2016
[table_1] : number of shares repurchased | 2017: 9.6 | 2016: 8.4
[table_2] : amount paid | 2017: $ 610.7 | 2016: $ 403.8
[table_3] : weighted average cost per share | 2017: $ 63.84 | 2016: $ 48.56

Question: as part of the employee stock purchase plan what was the percent of the decline in issuance under this plan from 2016 to 2017

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_3","value":"113941"},{"source":"text_3","value":"130085"}]},{"op":"divide","args":["#0",{"source":"text_3","value":"130085"}]}],"answer":-0.12410347080754891}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"9.6"},{"source":"table_1","value":"8.4"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"8.4"}]}],"answer":0.14285714285714285}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"9.6"},{"source":"table_1","value":"8.4"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"8.4"}]}],"answer":0.14285714285714285}
```

## 94. ETR/2013/page_136.pdf-2

Evidence:
[text_0] entergy corporation and subsidiaries notes to financial statements this difference as a regulatory asset or liability on an ongoing basis , resulting in a zero net balance for the regulatory asset at the end of the lease term .
[text_1] the amount was a net regulatory liability of $ 61.6 million and $ 27.8 million as of december 31 , 2013 and 2012 , respectively .
[text_2] as of december 31 , 2013 , system energy had future minimum lease payments ( reflecting an implicit rate of 5.13% ( 5.13 % ) ) , which are recorded as long-term debt , as follows : amount ( in thousands ) .
[text_3] .
[table_0]  | amount ( in thousands )
[table_1] : 2014 | amount ( in thousands ): $ 51637
[table_2] : 2015 | amount ( in thousands ): 52253
[table_3] : 2016 | amount ( in thousands ): 13750
[table_4] : 2017 | amount ( in thousands ): 13750
[table_5] : 2018 | amount ( in thousands ): 13750
[table_6] : years thereafter | amount ( in thousands ): 247500
[table_7] : total | amount ( in thousands ): 392640
[table_8] : less : amount representing interest | amount ( in thousands ): 295226
[table_9] : present value of net minimum lease payments | amount ( in thousands ): $ 97414

Question: what portion of the total future minimum lease payments for system energy is due in the next 12 months?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"51637"},{"source":"table_7","value":"392640"}]}],"answer":0.13151232681336594}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_3","value":"13750"},{"source":"table_6","value":"247500"}]}],"answer":0.05555555555555555}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_3","value":"13750"},{"source":"table_6","value":"247500"}]}],"answer":0.05562903225806451}
```

## 95. AON/2009/page_54.pdf-1

Evidence:
[text_0] holding other assumptions constant , the following table reflects what a one hundred basis point increase and decrease in our estimated long-term rate of return on plan assets would have on our estimated 2010 pension expense ( in millions ) : change in long-term rate of return on plan assets .
[text_1] estimated future contributions we estimate contributions of approximately $ 381 million in 2010 as compared with $ 437 million in goodwill and other intangible assets goodwill represents the excess of cost over the fair market value of the net assets acquired .
[text_2] we classify our intangible assets acquired as either trademarks , client lists , non-compete agreements , or other purchased intangibles .
[text_3] our goodwill and other intangible balances at december 31 , 2009 were $ 6.1 billion and $ 791 million , respectively , compared to $ 5.6 billion and $ 779 million , respectively , at december 31 , 2008 .
[text_4] although goodwill is not amortized , we test it for impairment at least annually in the fourth quarter .
[text_5] beginning in 2009 , we also test trademarks ( which also are not amortized ) that were acquired in conjunction with the benfield merger for impairment .
[text_6] we test more frequently if there are indicators of impairment or whenever business circumstances suggest that the carrying value of goodwill or trademarks may not be recoverable .
[text_7] these indicators may include a sustained significant decline in our share price and market capitalization , a decline in our expected future cash flows , or a significant adverse change in legal factors or in the business climate , among others .
[text_8] no events occurred during 2009 or 2008 that indicate the existence of an impairment with respect to our reported goodwill or trademarks .
[text_9] we perform impairment reviews at the reporting unit level .
[text_10] a reporting unit is an operating segment or one level below an operating segment ( referred to as a 2018 2018component 2019 2019 ) .
[text_11] a component of an operating segment is a reporting unit if the component constitutes a business for which discrete financial information is available and segment management regularly reviews the operating results of that component .
[text_12] an operating segment shall be deemed to be a reporting unit if all of its components are similar , if none of its components is a reporting unit , or if the segment comprises only a single component .
[text_13] the goodwill impairment test is a two step analysis .
[text_14] step one requires the fair value of each reporting unit to be compared to its book value .
[text_15] management must apply judgment in determining the estimated fair value of the reporting units .
[text_16] if the fair value of a reporting unit is determined to be greater than the carrying value of the reporting unit , goodwill and trademarks are deemed not to be impaired and no further testing is necessary .
[text_17] if the fair value of a reporting unit is less than the carrying value , we perform step two .
[text_18] step two uses the calculated fair value of the reporting unit to perform a hypothetical purchase price allocation to the fair value of the assets and liabilities of the reporting unit .
[text_19] the difference between the fair value of the reporting unit calculated in step one and the fair value of the underlying assets and liabilities of the reporting unit is the implied fair value of .
[table_0] increase ( decrease ) in expense | change in long-term rateof return on plan assets increase | change in long-term rateof return on plan assets decrease
[table_1] increase ( decrease ) in expense: u.s . plans | change in long-term rateof return on plan assets increase: $ -13 ( 13 ) | change in long-term rateof return on plan assets decrease: $ 13
[table_2] increase ( decrease ) in expense: u.k . plans | change in long-term rateof return on plan assets increase: -32 ( 32 ) | change in long-term rateof return on plan assets decrease: 32
[table_3] increase ( decrease ) in expense: the netherlands plan | change in long-term rateof return on plan assets increase: -5 ( 5 ) | change in long-term rateof return on plan assets decrease: 5
[table_4] increase ( decrease ) in expense: canada plans | change in long-term rateof return on plan assets increase: -2 ( 2 ) | change in long-term rateof return on plan assets decrease: 2

Question: what is the increase in the value of goodwill balances during 2008 and 2009?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_3","value":"6.1"},{"source":"text_3","value":"5.6"}]},{"op":"subtract","args":["#0","const_1"]}],"answer":0.08928571428571429}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_3","value":"5.6"},{"source":"text_3","value":"5.6"}]}],"answer":0.0}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_3","value":"5.6"},{"source":"text_3","value":"5.6"}]}],"answer":0.0}
```

## 96. GRMN/2008/page_73.pdf-1

Evidence:
[text_0] contractual obligations and commercial commitments future commitments of garmin , as of december 27 , 2008 , aggregated by type of contractual obligation .
[text_1] operating leases describes lease obligations associated with garmin facilities located in the u.s. , taiwan , europe , and canada .
[text_2] purchase obligations are the aggregate of those purchase orders that were outstanding on december 27 , 2008 ; these obligations are created and then paid off within 3 months during the normal course of our manufacturing business .
[text_3] we may be required to make significant cash outlays related to unrecognized tax benefits .
[text_4] however , due to the uncertainty of the timing of future cash flows associated with our unrecognized tax benefits , we are unable to make reasonably reliable estimates of the period of cash settlement , if any , with the respective taxing authorities .
[text_5] accordingly , unrecognized tax benefits of $ 214.4 million as of december 27 , 2008 , have been excluded from the contractual obligations table above .
[text_6] for further information related to unrecognized tax benefits , see note 2 , 201cincome taxes 201d , to the consolidated financial statements included in this report .
[text_7] off-balance sheet arrangements we do not have any off-balance sheet arrangements .
[text_8] item 7a .
[text_9] quantitative and qualitative disclosures about market risk market sensitivity we have market risk primarily in connection with the pricing of our products and services and the purchase of raw materials .
[text_10] product pricing and raw materials costs are both significantly influenced by semiconductor market conditions .
[text_11] historically , during cyclical industry downturns , we have been able to offset pricing declines for our products through a combination of improved product mix and success in obtaining price reductions in raw materials costs .
[text_12] inflation we do not believe that inflation has had a material effect on our business , financial condition or results of operations .
[text_13] if our costs were to become subject to significant inflationary pressures , we may not be able to fully offset such higher costs through price increases .
[text_14] our inability or failure to do so could adversely affect our business , financial condition and results of operations .
[text_15] foreign currency exchange rate risk the operation of garmin 2019s subsidiaries in international markets results in exposure to movements in currency exchange rates .
[text_16] we have experienced significant foreign currency gains and losses due to the strengthening and weakening of the u.s .
[text_17] dollar .
[text_18] the potential of volatile foreign exchange rate fluctuations in the future could have a significant effect on our results of operations .
[text_19] the currencies that create a majority of the company 2019s exchange rate exposure are the taiwan dollar , the euro , and british pound sterling .
[text_20] garmin corporation , headquartered in shijr , taiwan , uses the local currency as the functional currency .
[text_21] the company translates all assets and liabilities at year-end exchange rates and income and .
[table_0] contractual obligations | payments due by period total | payments due by period less than 1 year | payments due by period 1-3 years | payments due by period 3-5 years | payments due by period more than 5 years
[table_1] contractual obligations: operating leases | payments due by period total: $ 44048 | payments due by period less than 1 year: $ 7957 | payments due by period 1-3 years: $ 13789 | payments due by period 3-5 years: $ 11061 | payments due by period more than 5 years: $ 11241
[table_2] contractual obligations: purchase obligations | payments due by period total: 51471 | payments due by period less than 1 year: 47966 | payments due by period 1-3 years: 2265 | payments due by period 3-5 years: 1240 | payments due by period more than 5 years: 0
[table_3] contractual obligations: total | payments due by period total: $ 95519 | payments due by period less than 1 year: $ 55923 | payments due by period 1-3 years: $ 16054 | payments due by period 3-5 years: $ 12301 | payments due by period more than 5 years: $ 11241

Question: considering the contractual obligations in which payments due by 1-3 years , what is the percentage of the operating leases in relation to the total obligations?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"13789"},{"source":"table_3","value":"16054"}]}],"answer":0.8589136663759811}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"13789"},{"source":"table_3","value":"95519"}]}],"answer":0.14435871397313624}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"13789"},{"source":"table_3","value":"95519"}]}],"answer":0.14412091209120912}
```

## 97. ADBE/1999/page_64.pdf-2

Evidence:
[text_0] adobe systems incorporated notes to consolidated financial statements ( in thousands , except share and per share data ) ( continued ) note 7 .
[text_1] restructuring and other charges ( continued ) previously announced restructuring programs the following table depicts the activity for previously announced restructuring programs through december 3 , 1999 : accrued accrued balance at balance at november 27 total cash december 3 1998 charges payments adjustments 1999 .
[text_2] as of december 3 , 1999 , approximately $ 0.8 million in accrued restructuring costs remain related to the company 2019s fiscal 1998 restructuring program .
[text_3] this balance is comprised of $ 0.3 million in severance and related charges , $ 0.1 million in lease termination costs , and $ 0.4 million in canceled contracts .
[text_4] the majority of the accrual is expected to be paid by the first quarter of fiscal 2000 .
[text_5] cash payments for the twelve months ended december 3 , 1999 related to the fiscal 1998 restructuring were $ 0.7 million , $ 3.6 million , and $ 0.4 million for severance and related charges , lease termination costs , and canceled contracts costs , respectively .
[text_6] in addition , adjustments related to the fiscal 1998 restructuring were made during the year , which consisted of $ 0.4 million related to estimated lease termination costs and $ 0.3 mil- lion related to other charges .
[text_7] included in the accrual balance as of november 27 , 1998 were lease termination costs related to previously announced restructuring programs in fiscal 1994 and 1995 .
[text_8] cash payments for the twelve months ended december 3 , 1999 related to both restructuring programs were $ 1.5 million .
[text_9] during the third and fourth quarters of fiscal 1999 , the company recorded adjustments to the accrual balance of approximately $ 1.2 million related to these programs .
[text_10] an adjustment of $ 0.6 million was made in the third quarter of fiscal 1999 due to the company 2019s success in terminating a lease agreement earlier than the contract term specified .
[text_11] in addition , $ 0.6 million was reduced from the restructuring accrual relating to expired lease termination costs for two facilities resulting from the merger with frame in fiscal 1995 .
[text_12] as of december 3 , 1999 no accrual balances remain related to the aldus and frame mergers .
[text_13] other charges during the third and fourth quarters of fiscal 1999 , the company recorded other charges of $ 8.4 million that were unusual in nature .
[text_14] these charges included $ 2.0 million associated with the cancellation of a contract and $ 2.2 million for accelerated depreciation related to the adjustment of the useful life of certain assets as a result of decisions made by management as part of the restructuring program .
[text_15] additionally , the company incurred a nonrecurring compensation charge totaling $ 2.6 million for a terminated employee and incurred consulting fees of $ 1.6 million to assist in the restructuring of the company 2019s operations. .
[table_0]  | accrued balance at november 27 1998 | total charges | cash payments | adjustments | accrued balance at december 3 1999
[table_1] : accrual related to previous restructurings | accrued balance at november 27 1998: $ 8867 | total charges: $ 2014 | cash payments: $ -6221 ( 6221 ) | adjustments: $ -1874 ( 1874 ) | accrued balance at december 3 1999: $ 772

Question: what portion of the 1999 accrual balance related to restructurings is comprised of canceled contracts?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_3","value":"0.4"},{"source":"text_2","value":"0.8"}]}],"answer":0.5}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_3","value":"0.4"},{"source":"text_3","value":"0.3"}]}],"answer":1.3333333333333333}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_3","value":"0.4"},{"source":"text_3","value":"0.3"}]}],"answer":1.3333333333333333}
```

## 98. DISCA/2008/page_141.pdf-1

Evidence:
[text_0] 2 0 0 8 a n n u a l r e p o r t stock performance graph the following graph sets forth the performance of our series a common , series b common stock , and series c common stock for the period september 18 , 2008 through december 31 , 2008 as compared with the performance of the standard and poor 2019s 500 index and a peer group index which consists of the walt disney company , time warner inc. , cbs corporation class b common stock , viacom , inc .
[text_1] class b common stock , news corporation class a common stock , and scripps network interactive , inc .
[text_2] the graph assumes $ 100 originally invested on september 18 , 2006 and that all subsequent dividends were reinvested in additional shares .
[text_3] september 18 , september 30 , december 31 , 2008 2008 2008 .
[text_4] s&p 500 peer group .
[table_0]  | september 18 2008 | september 30 2008 | december 31 2008
[table_1] : disca | september 18 2008: $ 100.00 | september 30 2008: $ 103.19 | december 31 2008: $ 102.53
[table_2] : discb | september 18 2008: $ 100.00 | september 30 2008: $ 105.54 | december 31 2008: $ 78.53
[table_3] : disck | september 18 2008: $ 100.00 | september 30 2008: $ 88.50 | december 31 2008: $ 83.69
[table_4] : s&p 500 | september 18 2008: $ 100.00 | september 30 2008: $ 96.54 | december 31 2008: $ 74.86
[table_5] : peer group | september 18 2008: $ 100.00 | september 30 2008: $ 92.67 | december 31 2008: $ 68.79

Question: how much did the s&p 500 index decline in the fourth quarter?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_4","value":"96.54"},{"source":"table_4","value":"74.86"}]},{"op":"divide","args":["#0",{"source":"table_4","value":"74.86"}]}],"answer":0.28960726689821}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_4","value":"74.86"},{"source":"table_4","value":"100.00"}]},{"op":"divide","args":["#0",{"source":"table_4","value":"100.00"}]}],"answer":-0.2514}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_4","value":"74.86"},{"source":"table_4","value":"100.00"}]},{"op":"divide","args":["#0",{"source":"table_4","value":"100.00"}]}],"answer":-0.2514}
```

## 99. HUM/2017/page_118.pdf-3

Evidence:
[text_0] humana inc .
[text_1] notes to consolidated financial statements 2014 ( continued ) amortization expense for other intangible assets was approximately $ 75 million in 2017 , $ 77 million in 2016 , and $ 93 million in 2015 .
[text_2] the following table presents our estimate of amortization expense for each of the five next succeeding fiscal years: .
[text_3] .
[table_0]  | ( in millions )
[table_1] : for the years ending december 31, | ( in millions ): 
[table_2] : 2018 | ( in millions ): $ 64
[table_3] : 2019 | ( in millions ): 54
[table_4] : 2020 | ( in millions ): 52
[table_5] : 2021 | ( in millions ): 19
[table_6] : 2022 | ( in millions ): 16

Question: in 2017 what was the percent of the total amortization expense that was due in 2019

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"64"},{"source":"table_3","value":"54"}]},{"op":"add","args":[{"source":"table_4","value":"52"},"#0"]},{"op":"add","args":["#1",{"source":"table_5","value":"19"}]},{"op":"add","args":["#2",{"source":"table_6","value":"16"}]},{"op":"divide","args":[{"source":"table_3","value":"54"},"#3"]}],"answer":0.2634146341463415}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_1","value":"75"},{"source":"table_6","value":"16"}]}],"answer":4.6875}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_1","value":"75"},{"source":"table_6","value":"16"}]}],"answer":4.6875}
```

## 100. GPN/2008/page_95.pdf-1

Evidence:
[text_0] notes to consolidated financial statements 2014 ( continued ) note 12 2014related party transactions in the course of settling money transfer transactions , we purchase foreign currency from consultoria internacional casa de cambio ( 201ccisa 201d ) , a mexican company partially owned by certain of our employees .
[text_1] as of march 31 , 2008 , mr .
[text_2] ra fal lim f3n cortes , a 10% ( 10 % ) shareholder of cisa , was no longer an employee , and we no longer considered cisa a related party .
[text_3] we purchased 6.1 billion mexican pesos for $ 560.3 million during the ten months ended march 31 , 2008 and 8.1 billion mexican pesos for $ 736.0 million during fiscal 2007 from cisa .
[text_4] we believe these currency transactions were executed at prevailing market exchange rates .
[text_5] also from time to time , money transfer transactions are settled at destination facilities owned by cisa .
[text_6] we incurred related settlement expenses , included in cost of service in the accompanying consolidated statements of income of $ 0.5 million in the ten months ended march 31 , 2008 .
[text_7] in fiscal 2007 and 2006 , we incurred related settlement expenses , included in cost of service in the accompanying consolidated statements of income of $ 0.7 and $ 0.6 million , respectively .
[text_8] in the normal course of business , we periodically utilize the services of contractors to provide software development services .
[text_9] one of our employees , hired in april 2005 , is also an employee , officer , and part owner of a firm that provides such services .
[text_10] the services provided by this firm primarily relate to software development in connection with our planned next generation front-end processing system in the united states .
[text_11] during fiscal 2008 , we capitalized fees paid to this firm of $ 0.3 million .
[text_12] as of may 31 , 2008 and 2007 , capitalized amounts paid to this firm of $ 4.9 million and $ 4.6 million , respectively , were included in property and equipment in the accompanying consolidated balance sheets .
[text_13] in addition , we expensed amounts paid to this firm of $ 0.3 million , $ 0.1 million and $ 0.5 million in the years ended may 31 , 2008 , 2007 and 2006 , respectively .
[text_14] note 13 2014commitments and contingencies leases we conduct a major part of our operations using leased facilities and equipment .
[text_15] many of these leases have renewal and purchase options and provide that we pay the cost of property taxes , insurance and maintenance .
[text_16] rent expense on all operating leases for fiscal 2008 , 2007 and 2006 was $ 30.4 million , $ 27.1 million , and $ 24.4 million , respectively .
[text_17] future minimum lease payments for all noncancelable leases at may 31 , 2008 were as follows : operating leases .
[text_18] we are party to a number of other claims and lawsuits incidental to our business .
[text_19] in the opinion of management , the reasonably possible outcome of such matters , individually or in the aggregate , will not have a material adverse impact on our financial position , liquidity or results of operations. .
[table_0]  | operating leases
[table_1] : 2009 | operating leases: $ 22883
[table_2] : 2010 | operating leases: 16359
[table_3] : 2011 | operating leases: 11746
[table_4] : 2012 | operating leases: 5277
[table_5] : 2013 | operating leases: 3365
[table_6] : thereafter | operating leases: 7816
[table_7] : total future minimum lease payments | operating leases: $ 67446

Question: what is the exchange rate pesos to dollar in 2008?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"text_3","value":"6.1"},"const_1000"]},{"op":"divide","args":["#0",{"source":"text_3","value":"560.3"}]}],"answer":10.887024808138497}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_3","value":"560.3"},{"source":"text_3","value":"6.1"}]}],"answer":91.85245901639344}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_3","value":"560.3"},{"source":"text_3","value":"6.1"}]}],"answer":92.08456039215686}
```

## 101. ETR/2008/page_154.pdf-2

Evidence:
[text_0] entergy corporation and subsidiaries notes to financial statements as of december 31 , 2008 , system energy had future minimum lease payments ( reflecting an implicit rate of 5.13% ( 5.13 % ) ) , which are recorded as long-term debt as follows : amount ( in thousands ) .
[text_1] .
[table_0]  | amount ( in thousands )
[table_1] : 2009 | amount ( in thousands ): $ 47760
[table_2] : 2010 | amount ( in thousands ): 48569
[table_3] : 2011 | amount ( in thousands ): 49437
[table_4] : 2012 | amount ( in thousands ): 49959
[table_5] : 2013 | amount ( in thousands ): 50546
[table_6] : years thereafter | amount ( in thousands ): 103890
[table_7] : total | amount ( in thousands ): 350161
[table_8] : less : amount representing interest | amount ( in thousands ): 54857
[table_9] : present value of net minimum lease payments | amount ( in thousands ): $ 295304

Question: what percent of lease payments are due after 2013?

Chosen（参考标签，仍需核对）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"103890"},{"source":"table_7","value":"350161"}]}],"answer":0.29669209306576116}
```

Rejected（模型错误程序，执行器重算 answer）：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_7","value":"350161"},{"source":"table_6","value":"103890"}]}],"answer":3.370497641736452}
```

模型原始输出：
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_7","value":"350161"},{"source":"table_6","value":"103890"}]}],"answer":33.99999999999999}
```
