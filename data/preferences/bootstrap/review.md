# Preference review

Review evidence, chosen and rejected. Fill review.csv decision=approve/reject.

## ETR/2011/page_146.pdf-2

Evidence:
[text_0] entergy corporation and subsidiaries notes to financial statements ferc audit report , system energy initially recorded as a net regulatory asset the difference between the recovery of the lease payments and the amounts expensed for interest and depreciation and continues to record this difference as a regulatory asset or liability on an ongoing basis , resulting in a zero net balance for the regulatory asset at the end of the lease term .
[text_1] the amount was a net regulatory asset ( liability ) of ( $ 2.0 ) million and $ 60.6 million as of december 31 , 2011 and 2010 , respectively .
[text_2] as of december 31 , 2011 , system energy had future minimum lease payments ( reflecting an implicit rate of 5.13% ( 5.13 % ) ) , which are recorded as long-term debt as follows : amount ( in thousands ) .
[text_3] .
[table_0]  | amount ( in thousands )
[table_1] : 2012 | amount ( in thousands ): $ 49959
[table_2] : 2013 | amount ( in thousands ): 50546
[table_3] : 2014 | amount ( in thousands ): 51637
[table_4] : 2015 | amount ( in thousands ): 52253
[table_5] : 2016 | amount ( in thousands ): -
[table_6] : years thereafter | amount ( in thousands ): -
[table_7] : total | amount ( in thousands ): 204395
[table_8] : less : amount representing interest | amount ( in thousands ): 25611
[table_9] : present value of net minimum lease payments | amount ( in thousands ): $ 178784

Question: in how many years will is the company expected to pay off all its future minimum lease payments?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_4","value":"2015"},{"source":"text_2","value":"2011"}]}],"answer":4.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_4","value":"2015"},{"source":"text_2","value":"2011"}]}],"answer":4026.0}
```

## DVN/2010/page_70.pdf-2

Evidence:
[text_0] likely than not that some portion or all of the deferred tax assets will not be realized .
[text_1] the accruals for deferred tax assets and liabilities are subject to a significant amount of judgment by management and are reviewed and adjusted routinely based on changes in facts and circumstances .
[text_2] material changes in these accruals may occur in the future , based on the progress of ongoing tax audits , changes in legislation and resolution of pending tax matters .
[text_3] forward-looking estimates we are providing our 2011 forward-looking estimates in this section .
[text_4] these estimates were based on our examination of historical operating trends , the information used to prepare our december 31 , 2010 , reserve reports and other data in our possession or available from third parties .
[text_5] the forward-looking estimates in this report were prepared assuming demand , curtailment , producibility and general market conditions for our oil , gas and ngls during 2011 will be similar to 2010 , unless otherwise noted .
[text_6] we make reference to the 201cdisclosure regarding forward-looking statements 201d at the beginning of this report .
[text_7] amounts related to our canadian operations have been converted to u.s .
[text_8] dollars using an estimated average 2011 exchange rate of $ 0.95 dollar to $ 1.00 canadian dollar .
[text_9] during 2011 , our operations are substantially comprised of our ongoing north america onshore operations .
[text_10] we also have international operations in brazil and angola that we are divesting .
[text_11] we have entered into agreements to sell our assets in brazil for $ 3.2 billion and our assets in angola for $ 70 million , plus contingent consideration .
[text_12] as a result of these divestitures , all revenues , expenses and capital related to our international operations are reported as discontinued operations in our financial statements .
[text_13] additionally , all forward-looking estimates in this document exclude amounts related to our international operations , unless otherwise noted .
[text_14] north america onshore operating items the following 2011 estimates relate only to our north america onshore assets .
[text_15] oil , gas and ngl production set forth below are our estimates of oil , gas and ngl production for 2011 .
[text_16] we estimate that our combined oil , gas and ngl production will total approximately 236 to 240 mmboe .
[text_17] ( mmbbls ) ( mmbbls ) ( mmboe ) .
[text_18] oil and gas prices we expect our 2011 average prices for the oil and gas production from each of our operating areas to differ from the nymex price as set forth in the following table .
[text_19] the expected ranges for prices are exclusive of the anticipated effects of the financial contracts presented in the 201ccommodity price risk management 201d section below .
[text_20] the nymex price for oil is determined using the monthly average of settled prices on each trading day for benchmark west texas intermediate crude oil delivered at cushing , oklahoma .
[text_21] the nymex price for gas is determined using the first-of-month south louisiana henry hub price index as published monthly in inside .
[table_0]  | oil ( mmbbls ) | gas ( bcf ) | ngls ( mmbbls ) | total ( mmboe )
[table_1] : u.s . onshore | oil ( mmbbls ): 17 | gas ( bcf ): 736 | ngls ( mmbbls ): 34 | total ( mmboe ): 174
[table_2] : canada | oil ( mmbbls ): 28 | gas ( bcf ): 199 | ngls ( mmbbls ): 3 | total ( mmboe ): 64
[table_3] : north america onshore | oil ( mmbbls ): 45 | gas ( bcf ): 935 | ngls ( mmbbls ): 37 | total ( mmboe ): 238

Question: what percentage of north america gas comes from us onshore?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"736"},{"source":"table_3","value":"935"}]},{"op":"multiply","args":["#0","const_100"]}],"answer":78.71657754010695}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"736"},{"source":"table_3","value":"935"}]},{"op":"multiply","args":["#0","const_100"]}],"answer":167100.0}
```

## BLL/2011/page_29.pdf-4

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"170.70"},{"source":"table_1","value":"100.00"}]}],"answer":1.707}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"170.70"},{"source":"table_1","value":"100.00"}]}],"answer":270.7}
```

## ETR/2017/page_316.pdf-3

Evidence:
[text_0] entergy arkansas , inc .
[text_1] and subsidiaries management 2019s financial discussion and analysis results of operations net income 2017 compared to 2016 net income decreased $ 27.4 million primarily due to higher nuclear refueling outage expenses , higher depreciation and amortization expenses , higher taxes other than income taxes , and higher interest expense , partially offset by higher other income .
[text_2] 2016 compared to 2015 net income increased $ 92.9 million primarily due to higher net revenue and lower other operation and maintenance expenses , partially offset by a higher effective income tax rate and higher depreciation and amortization expenses .
[text_3] net revenue 2017 compared to 2016 net revenue consists of operating revenues net of : 1 ) fuel , fuel-related expenses , and gas purchased for resale , 2 ) purchased power expenses , and 3 ) other regulatory charges ( credits ) . a0 a0following is an analysis of the change in net revenue comparing 2017 to 2016 .
[text_4] amount ( in millions ) .
[text_5] the retail electric price variance is primarily due to the implementation of formula rate plan rates effective with the first billing cycle of january 2017 and an increase in base rates effective february 24 , 2016 , each as approved by the apsc .
[text_6] a significant portion of the base rate increase was related to the purchase of power block 2 of the union power station in march 2016 .
[text_7] the increase was partially offset by decreases in the energy efficiency rider , as approved by the apsc , effective april 2016 and january 2017 .
[text_8] see note 2 to the financial statements for further discussion of the rate case and formula rate plan filings .
[text_9] see note 14 to the financial statements for further discussion of the union power station purchase .
[text_10] the opportunity sales variance results from the estimated net revenue effect of the 2017 and 2016 ferc orders in the opportunity sales proceeding attributable to wholesale customers .
[text_11] see note 2 to the financial statements for further discussion of the opportunity sales proceeding. .
[table_0]  | amount ( in millions )
[table_1] : 2016 net revenue | amount ( in millions ): $ 1520.5
[table_2] : retail electric price | amount ( in millions ): 33.8
[table_3] : opportunity sales | amount ( in millions ): 5.6
[table_4] : asset retirement obligation | amount ( in millions ): -14.8 ( 14.8 )
[table_5] : volume/weather | amount ( in millions ): -29.0 ( 29.0 )
[table_6] : other | amount ( in millions ): 6.5
[table_7] : 2017 net revenue | amount ( in millions ): $ 1522.6

Question: in 2016 what was the ratio of the net income increased to the net revenues

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_2","value":"92.9"},{"source":"table_1","value":"1520.5"}]}],"answer":0.061098322920092075}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_2","value":"92.9"},{"source":"table_1","value":"1520.5"}]}],"answer":1613.4}
```

## ETFC/2013/page_84.pdf-3

Evidence:
[text_0] individual loan before being modified as a tdr in the discounted cash flow analysis in order to determine that specific loan 2019s expected impairment .
[text_1] specifically , a loan that has a more severe delinquency history prior to modification will have a higher future default rate in the discounted cash flow analysis than a loan that was not as severely delinquent .
[text_2] for both of the one- to four-family and home equity loan portfolio segments , the pre- modification delinquency status , the borrower 2019s current credit score and other credit bureau attributes , in addition to each loan 2019s individual default experience and credit characteristics , are incorporated into the calculation of the specific allowance .
[text_3] a specific allowance is established to the extent that the recorded investment exceeds the discounted cash flows of a tdr with a corresponding charge to provision for loan losses .
[text_4] the specific allowance for these individually impaired loans represents the forecasted losses over the estimated remaining life of the loan , including the economic concession to the borrower .
[text_5] effects if actual results differ historic volatility in the credit markets has substantially increased the complexity and uncertainty involved in estimating the losses inherent in the loan portfolio .
[text_6] in the current market it is difficult to estimate how potential changes in the quantitative and qualitative factors , including the impact of home equity lines of credit converting from interest only to amortizing loans or requiring borrowers to repay the loan in full at the end of the draw period , might impact the allowance for loan losses .
[text_7] if our underlying assumptions and judgments prove to be inaccurate , the allowance for loan losses could be insufficient to cover actual losses .
[text_8] we may be required under such circumstances to further increase the provision for loan losses , which could have an adverse effect on the regulatory capital position and results of operations in future periods .
[text_9] during the normal course of conducting examinations , our banking regulators , the occ and federal reserve , continue to review our business and practices .
[text_10] this process is dynamic and ongoing and we cannot be certain that additional changes or actions will not result from their continuing review .
[text_11] valuation of goodwill and other intangible assets description goodwill and other intangible assets are evaluated for impairment on an annual basis as of november 30 and in interim periods when events or changes indicate the carrying value may not be recoverable , such as a significant deterioration in the operating environment or a decision to sell or dispose of a reporting unit .
[text_12] goodwill and other intangible assets net of amortization were $ 1.8 billion and $ 0.2 billion , respectively , at december 31 , 2013 .
[text_13] judgments goodwill is allocated to reporting units , which are components of the business that are one level below operating segments .
[text_14] reporting units are evaluated for impairment individually during the annual assessment .
[text_15] estimating the fair value of reporting units and the assets , liabilities and intangible assets of a reporting unit is a subjective process that involves the use of estimates and judgments , particularly related to cash flows , the appropriate discount rates and an applicable control premium .
[text_16] management judgment is required to assess whether the carrying value of the reporting unit can be supported by the fair value of the individual reporting unit .
[text_17] there are various valuation methodologies , such as the market approach or discounted cash flow methods , that may be used to estimate the fair value of reporting units .
[text_18] in applying these methodologies , we utilize a number of factors , including actual operating results , future business plans , economic projections , and market data .
[text_19] the following table shows the comparative data for the amount of goodwill allocated to our reporting units ( dollars in millions ) : .
[text_20] .
[table_0] reporting unit | december 31 , 2013 | december 31 , 2012
[table_1] reporting unit: retail brokerage | december 31 , 2013: $ 1791.8 | december 31 , 2012: $ 1791.8
[table_2] reporting unit: market making | december 31 , 2013: 2014 | december 31 , 2012: 142.4
[table_3] reporting unit: total goodwill | december 31 , 2013: $ 1791.8 | december 31 , 2012: $ 1934.2

Question: as of december 31 , 2013 what was the ratio of the goodwill to the other intangible assets net of amortization

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_12","value":"1.8"},{"source":"text_12","value":"0.2"}]}],"answer":9.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_12","value":"1.8"},{"source":"text_12","value":"0.2"}]}],"answer":2.0}
```

## ETR/2017/page_373.pdf-1

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"12.9"},{"source":"text_3","value":"19.4"}]}],"answer":0.6649484536082474}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"12.9"},{"source":"text_3","value":"19.4"}]}],"answer":32.3}
```

## DRE/2009/page_72.pdf-1

Evidence:
[text_0] 70| | duke realty corporation annual report 2009 the following table summarizes transactions for our rsus , excluding dividend equivalents , for 2009 : weighted average number of grant date restricted stock units rsus fair value .
[text_1] compensation cost recognized for rsus totaled $ 7.3 million , $ 4.9 million and $ 3.0 million for the years ended december 31 , 2009 , 2008 and 2007 , respectively .
[text_2] as of december 31 , 2009 , there was $ 6.7 million of total unrecognized compensation expense related to nonvested rsus granted under the plan , which is expected to be recognized over a weighted average period of 3.3 years .
[text_3] ( 14 ) financial instruments we are exposed to capital market risk , such as changes in interest rates .
[text_4] in an effort to manage interest rate risk , we may enter into interest rate hedging arrangements from time to time .
[text_5] we do not utilize derivative financial instruments for trading or speculative purposes .
[text_6] in november 2007 , we entered into forward starting interest swaps with notional amounts appropriate to hedge interest rates on $ 300.0 million of anticipated debt offerings in 2009 .
[text_7] the forward starting swaps were appropriately designated and tested for effectiveness as cash flow hedges .
[text_8] in march 2008 , we settled the forward starting swaps and made a cash payment of $ 14.6 million to the counterparties .
[text_9] an effectiveness test was performed as of the settlement date and it was concluded that a highly effective cash flow hedge was still in place for the expected debt offering .
[text_10] of the amount paid in settlement , approximately $ 700000 was immediately reclassified to interest expense , as the result of partial ineffectiveness calculated at the settlement date .
[text_11] the net amount of $ 13.9 million was recorded in other comprehensive income ( 201coci 201d ) and is being recognized through interest expense over the life of the hedged debt offering , which took place in may 2008 .
[text_12] the remaining unamortized amount included as a reduction to accumulated oci as of december 31 , 2009 is $ 9.3 million .
[text_13] in august 2005 , we entered into $ 300.0 million of cash flow hedges through forward starting interest rate swaps to hedge interest rates on $ 300.0 million of anticipated debt offerings in 2007 .
[text_14] the swaps qualified for hedge accounting , with any changes in fair value recorded in oci .
[text_15] in conjunction with the september 2007 issuance of $ 300.0 million of senior unsecured notes , we terminated these cash flow hedges as designated .
[text_16] the settlement amount received of $ 10.7 million is being recognized to earnings through a reduction of interest expense over the term of the hedged cash flows .
[text_17] the remaining unamortized amount included as an increase to accumulated oci as of december 31 , 2009 is $ 8.2 million .
[text_18] the ineffective portion of the hedge was insignificant .
[text_19] the effectiveness of our hedges is evaluated throughout their lives using the hypothetical derivative method under which the change in fair value of the actual swap designated as the hedging instrument is compared to the change in fair value of a hypothetical swap .
[text_20] we had no material interest rate derivatives , when considering both fair value and notional amount , at december 31 , 2009. .
[table_0] restricted stock units | number of rsus | weighted average grant date fair value
[table_1] restricted stock units: rsus at december 31 2008 | number of rsus: 401375 | weighted average grant date fair value: $ 29.03
[table_2] restricted stock units: granted | number of rsus: 1583616 | weighted average grant date fair value: $ 9.32
[table_3] restricted stock units: vested | number of rsus: -129352 ( 129352 ) | weighted average grant date fair value: $ 28.39
[table_4] restricted stock units: forfeited | number of rsus: -172033 ( 172033 ) | weighted average grant date fair value: $ 12.53
[table_5] restricted stock units: rsus at december 31 2009 | number of rsus: 1683606 | weighted average grant date fair value: $ 12.23

Question: what was the value of the rsu's granted

Chosen:
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"table_2","value":"1583616"},{"source":"table_2","value":"9.32"}]}],"answer":14759301.12}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"1583616"},{"source":"table_2","value":"9.32"}]}],"answer":1583625.32}
```

## GPN/2010/page_41.pdf-1

Evidence:
[text_0] the following details the impairment charge resulting from our review ( in thousands ) : .
[text_1] net income attributable to noncontrolling interests , net of tax noncontrolling interest , net of tax increased $ 28.9 million from $ 8.1 million fiscal 2008 .
[text_2] the increase was primarily related to our acquisition of a 51% ( 51 % ) majority interest in hsbc merchant services , llp on june 30 , net income attributable to global payments and diluted earnings per share during fiscal 2009 we reported net income of $ 37.2 million ( $ 0.46 diluted earnings per share ) .
[text_3] liquidity and capital resources a significant portion of our liquidity comes from operating cash flows , which are generally sufficient to fund operations , planned capital expenditures , debt service and various strategic investments in our business .
[text_4] cash flow from operations is used to make planned capital investments in our business , to pursue acquisitions that meet our corporate objectives , to pay dividends , and to pay off debt and repurchase our shares at the discretion of our board of directors .
[text_5] accumulated cash balances are invested in high-quality and marketable short term instruments .
[text_6] our capital plan objectives are to support the company 2019s operational needs and strategic plan for long term growth while maintaining a low cost of capital .
[text_7] lines of credit are used in certain of our markets to fund settlement and as a source of working capital and , along with other bank financing , to fund acquisitions .
[text_8] we regularly evaluate our liquidity and capital position relative to cash requirements , and we may elect to raise additional funds in the future , either through the issuance of debt , equity or otherwise .
[text_9] at may 31 , 2010 , we had cash and cash equivalents totaling $ 769.9 million .
[text_10] of this amount , we consider $ 268.1 million to be available cash , which generally excludes settlement related and merchant reserve cash balances .
[text_11] settlement related cash balances represent surplus funds that we hold on behalf of our member sponsors when the incoming amount from the card networks precedes the member sponsors 2019 funding obligation to the merchant .
[text_12] merchant reserve cash balances represent funds collected from our merchants that serve as collateral ( 201cmerchant reserves 201d ) to minimize contingent liabilities associated with any losses that may occur under the merchant agreement .
[text_13] at may 31 , 2010 , our cash and cash equivalents included $ 199.4 million related to merchant reserves .
[text_14] while this cash is not restricted in its use , we believe that designating this cash to collateralize merchant reserves strengthens our fiduciary standing with our member sponsors and is in accordance with the guidelines set by the card networks .
[text_15] see cash and cash equivalents and settlement processing assets and obligations under note 1 in the notes to the consolidated financial statements for additional details .
[text_16] net cash provided by operating activities increased $ 82.8 million to $ 465.8 million for fiscal 2010 from the prior year .
[text_17] income from continuing operations increased $ 16.0 million and we had cash provided by changes in working capital of $ 60.2 million .
[text_18] the working capital change was primarily due to the change in net settlement processing assets and obligations of $ 80.3 million and the change in accounts receivable of $ 13.4 million , partially offset by the change .
[table_0]  | year ended may 31 2009
[table_1] : goodwill | year ended may 31 2009: $ 136800
[table_2] : trademark | year ended may 31 2009: 10000
[table_3] : other long-lived assets | year ended may 31 2009: 864
[table_4] : total | year ended may 31 2009: $ 147664

Question: what portion of the impairment charge is related to goodwill?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"136800"},{"source":"table_4","value":"147664"}]}],"answer":0.926427565283346}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"136800"},{"source":"table_4","value":"147664"}]}],"answer":284464.0}
```

## ETR/2004/page_258.pdf-3

Evidence:
[text_0] entergy new orleans , inc .
[text_1] management's financial discussion and analysis results of operations net income ( loss ) 2004 compared to 2003 net income increased $ 20.2 million primarily due to higher net revenue .
[text_2] 2003 compared to 2002 entergy new orleans had net income of $ 7.9 million in 2003 compared to a net loss in 2002 .
[text_3] the increase was due to higher net revenue and lower interest expense , partially offset by higher other operation and maintenance expenses and depreciation and amortization expenses .
[text_4] net revenue 2004 compared to 2003 net revenue , which is entergy new orleans' measure of gross margin , consists of operating revenues net of : 1 ) fuel , fuel-related , and purchased power expenses and 2 ) other regulatory credits .
[text_5] following is an analysis of the change in net revenue comparing 2004 to 2003. .
[text_6] the increase in base rates was effective june 2003 .
[text_7] the rate increase is discussed in note 2 to the domestic utility companies and system energy financial statements .
[text_8] the volume/weather variance is primarily due to increased billed electric usage of 162 gwh in the industrial service sector .
[text_9] the increase was partially offset by milder weather in the residential and commercial sectors .
[text_10] the 2004 deferrals variance is due to the deferral of voluntary severance plan and fossil plant maintenance expenses in accordance with a stipulation approved by the city council in august 2004 .
[text_11] the stipulation allows for the recovery of these costs through amortization of a regulatory asset .
[text_12] the voluntary severance plan and fossil plant maintenance expenses are being amortized over a five-year period that became effective january 2004 and january 2003 , respectively .
[text_13] the formula rate plan is discussed in note 2 to the domestic utility companies and system energy financial statements .
[text_14] the price applied to unbilled electric sales variance is due to an increase in the fuel price applied to unbilled sales. .
[table_0]  | ( in millions )
[table_1] : 2003 net revenue | ( in millions ): $ 208.3
[table_2] : base rates | ( in millions ): 10.6
[table_3] : volume/weather | ( in millions ): 8.3
[table_4] : 2004 deferrals | ( in millions ): 7.5
[table_5] : price applied to unbilled electric sales | ( in millions ): 3.7
[table_6] : other | ( in millions ): 0.6
[table_7] : 2004 net revenue | ( in millions ): $ 239.0

Question: what is the growth rate in net revenue for entergy new orleans , inc . in 2004?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_7","value":"239.0"},{"source":"table_1","value":"208.3"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"208.3"}]}],"answer":0.14738358137301968}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_7","value":"239.0"},{"source":"table_1","value":"208.3"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"208.3"}]}],"answer":2.1473835813730195}
```

## ETR/2016/page_342.pdf-3

Evidence:
[text_0] entergy louisiana , llc and subsidiaries management 2019s financial discussion and analysis results of operations net income 2016 compared to 2015 net income increased $ 175.4 million primarily due to the effect of a settlement with the irs related to the 2010-2011 irs audit , which resulted in a $ 136.1 million reduction of income tax expense .
[text_1] also contributing to the increase were lower other operation and maintenance expenses , higher net revenue , and higher other income .
[text_2] the increase was partially offset by higher depreciation and amortization expenses , higher interest expense , and higher nuclear refueling outage expenses .
[text_3] 2015 compared to 2014 net income increased slightly , by $ 0.6 million , primarily due to higher net revenue and a lower effective income tax rate , offset by higher other operation and maintenance expenses , higher depreciation and amortization expenses , lower other income , and higher interest expense .
[text_4] net revenue 2016 compared to 2015 net revenue consists of operating revenues net of : 1 ) fuel , fuel-related expenses , and gas purchased for resale , 2 ) purchased power expenses , and 3 ) other regulatory charges .
[text_5] following is an analysis of the change in net revenue comparing 2016 to 2015 .
[text_6] amount ( in millions ) .
[text_7] the retail electric price variance is primarily due to an increase in formula rate plan revenues , implemented with the first billing cycle of march 2016 , to collect the estimated first-year revenue requirement related to the purchase of power blocks 3 and 4 of the union power station .
[text_8] see note 2 to the financial statements for further discussion .
[text_9] the transmission equalization variance is primarily due to changes in transmission investments , including entergy louisiana 2019s exit from the system agreement in august 2016 .
[text_10] the volume/weather variance is primarily due to the effect of less favorable weather on residential sales , partially offset by an increase in industrial usage and an increase in volume during the unbilled period .
[text_11] the increase .
[table_0]  | amount ( in millions )
[table_1] : 2015 net revenue | amount ( in millions ): $ 2408.8
[table_2] : retail electric price | amount ( in millions ): 69.0
[table_3] : transmission equalization | amount ( in millions ): -6.5 ( 6.5 )
[table_4] : volume/weather | amount ( in millions ): -6.7 ( 6.7 )
[table_5] : louisiana act 55 financing savings obligation | amount ( in millions ): -17.2 ( 17.2 )
[table_6] : other | amount ( in millions ): -9.0 ( 9.0 )
[table_7] : 2016 net revenue | amount ( in millions ): $ 2438.4

Question: assuming the retail electric price increase wouldn't have occured , what would 2016 net revenue have been , in millions?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_7","value":"2438.4"},{"source":"table_2","value":"69.0"}]}],"answer":2369.4}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_7","value":"2438.4"},{"source":"table_2","value":"69.0"}]}],"answer":2507.4}
```

## DVN/2014/page_85.pdf-1

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"table_1","value":"45"},"const_4"]},{"op":"add","args":["#0",{"source":"table_5","value":"44"}]},{"op":"divide","args":["#1","const_5"]}],"answer":44.8}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"45"},"const_4"]},{"op":"add","args":["#0",{"source":"table_5","value":"44"}]},{"op":"divide","args":["#1","const_5"]}],"answer":18.6}
```

## ETR/2004/page_281.pdf-2

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

Question: what is the money pool activity use of operating cash flows as a percentage of receivables from the money pool in 2003?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"19064"},"const_1000"]},{"op":"divide","args":[{"source":"text_14","value":"12.0"},"#0"]}],"answer":0.6294586655476291}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"19064"},"const_1000"]},{"op":"divide","args":[{"source":"text_14","value":"12.0"},"#0"]}],"answer":0.0005980861244019139}
```

## AAP/2016/page_26.pdf-1

Evidence:
[text_0] stock price performance the following graph shows a comparison of the cumulative total return on our common stock , the standard & poor 2019s 500 index and the standard & poor 2019s retail index .
[text_1] the graph assumes that the value of an investment in our common stock and in each such index was $ 100 on december 31 , 2011 , and that any dividends have been reinvested .
[text_2] the comparison in the graph below is based solely on historical data and is not intended to forecast the possible future performance of our common stock .
[text_3] comparison of cumulative total return among advance auto parts , inc. , s&p 500 index and s&p retail index company/index december 31 , december 29 , december 28 , january 3 , january 2 , december 31 .
[text_4] .
[table_0] company/index | december 31 2011 | december 29 2012 | december 28 2013 | january 3 2015 | january 2 2016 | december 31 2016
[table_1] company/index: advance auto parts | december 31 2011: $ 100.00 | december 29 2012: $ 102.87 | december 28 2013: $ 158.46 | january 3 2015: $ 228.88 | january 2 2016: $ 217.49 | december 31 2016: $ 244.64
[table_2] company/index: s&p 500 index | december 31 2011: 100.00 | december 29 2012: 114.07 | december 28 2013: 152.98 | january 3 2015: 174.56 | january 2 2016: 177.01 | december 31 2016: 198.18
[table_3] company/index: s&p retail index | december 31 2011: 100.00 | december 29 2012: 122.23 | december 28 2013: 178.55 | january 3 2015: 196.06 | january 2 2016: 245.31 | december 31 2016: 256.69

Question: what is the rate of return on an investment in advance auto parts from 2015 to 2016?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"217.49"},{"source":"table_1","value":"228.88"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"228.88"}]}],"answer":-0.04976406850751486}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"217.49"},{"source":"table_1","value":"228.88"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"228.88"}]}],"answer":1.950235931492485}
```

## ETR/2016/page_315.pdf-1

Evidence:
[text_0] entergy arkansas , inc .
[text_1] and subsidiaries management 2019s financial discussion and analysis results of operations net income 2016 compared to 2015 net income increased $ 92.9 million primarily due to higher net revenue and lower other operation and maintenance expenses , partially offset by a higher effective income tax rate and higher depreciation and amortization expenses .
[text_2] 2015 compared to 2014 net income decreased $ 47.1 million primarily due to higher other operation and maintenance expenses , partially offset by higher net revenue .
[text_3] net revenue 2016 compared to 2015 net revenue consists of operating revenues net of : 1 ) fuel , fuel-related expenses , and gas purchased for resale , 2 ) purchased power expenses , and 3 ) other regulatory charges ( credits ) .
[text_4] following is an analysis of the change in net revenue comparing 2016 to 2015 .
[text_5] amount ( in millions ) .
[text_6] the retail electric price variance is primarily due to an increase in base rates , as approved by the apsc .
[text_7] the new base rates were effective february 24 , 2016 and began billing with the first billing cycle of april 2016 .
[text_8] the increase includes an interim base rate adjustment surcharge , effective with the first billing cycle of april 2016 , to recover the incremental revenue requirement for the period february 24 , 2016 through march 31 , 2016 .
[text_9] a significant portion of the increase is related to the purchase of power block 2 of the union power station .
[text_10] see note 2 to the financial statements for further discussion of the rate case .
[text_11] see note 14 to the financial statements for further discussion of the union power station purchase. .
[table_0]  | amount ( in millions )
[table_1] : 2015 net revenue | amount ( in millions ): $ 1362.2
[table_2] : retail electric price | amount ( in millions ): 161.5
[table_3] : other | amount ( in millions ): -3.2 ( 3.2 )
[table_4] : 2016 net revenue | amount ( in millions ): $ 1520.5

Question: what is the growth rate in net revenue in 2016 for entergy arkansas , inc.?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_4","value":"1520.5"},{"source":"table_1","value":"1362.2"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"1362.2"}]}],"answer":0.11620907355748054}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_4","value":"1520.5"},{"source":"table_1","value":"1362.2"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"1362.2"}]}],"answer":2.1162090735574806}
```

## CME/2010/page_113.pdf-3

Evidence:
[text_0] the company granted 1020 performance shares .
[text_1] the vesting of these shares is contingent on meeting stated goals over a performance period .
[text_2] beginning with restricted stock grants in september 2010 , dividends are accrued on restricted class a common stock and restricted stock units and are paid once the restricted stock vests .
[text_3] the following table summarizes restricted stock and performance shares activity for 2010 : number of shares weighted average grant date fair value .
[text_4] the total fair value of restricted stock that vested during the years ended december 31 , 2010 , 2009 and 2008 , was $ 10.3 million , $ 6.2 million and $ 2.5 million , respectively .
[text_5] eligible employees may acquire shares of cme group 2019s class a common stock using after-tax payroll deductions made during consecutive offering periods of approximately six months in duration .
[text_6] shares are purchased at the end of each offering period at a price of 90% ( 90 % ) of the closing price of the class a common stock as reported on the nasdaq .
[text_7] compensation expense is recognized on the dates of purchase for the discount from the closing price .
[text_8] in 2010 , 2009 and 2008 , a total of 4371 , 4402 and 5600 shares , respectively , of class a common stock were issued to participating employees .
[text_9] these shares are subject to a six-month holding period .
[text_10] annual expense of $ 0.1 million for the purchase discount was recognized in 2010 , 2009 and 2008 , respectively .
[text_11] non-executive directors receive an annual award of class a common stock with a value equal to $ 75000 .
[text_12] non-executive directors may also elect to receive some or all of the cash portion of their annual stipend , up to $ 25000 , in shares of stock based on the closing price at the date of distribution .
[text_13] as a result , 7470 , 11674 and 5509 shares of class a common stock were issued to non-executive directors during 2010 , 2009 and 2008 , respectively .
[text_14] these shares are not subject to any vesting restrictions .
[text_15] expense of $ 2.4 million , $ 2.5 million and $ 2.4 million related to these stock-based payments was recognized for the years ended december 31 , 2010 , 2009 and 2008 , respectively. .
[table_0]  | number of shares | weighted average grant date fair value
[table_1] : outstanding at december 31 2009 | number of shares: 116677 | weighted average grant date fair value: $ 280
[table_2] : granted | number of shares: 134245 | weighted average grant date fair value: 275
[table_3] : vested | number of shares: -34630 ( 34630 ) | weighted average grant date fair value: 257
[table_4] : cancelled | number of shares: -19830 ( 19830 ) | weighted average grant date fair value: 260
[table_5] : outstanding at december 31 2010 | number of shares: 196462 | weighted average grant date fair value: 283

Question: what was the sum of the total fair value of restricted stock that vested during 2008 and 2010 in millions

Chosen:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_4","value":"10.3"},{"source":"text_4","value":"6.2"}]},{"op":"add","args":["#0",{"source":"text_4","value":"2.5"}]}],"answer":19.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_4","value":"10.3"},{"source":"text_4","value":"6.2"}]},{"op":"add","args":["#0",{"source":"text_4","value":"2.5"}]}],"answer":6.6}
```

## MRO/2009/page_32.pdf-4

Evidence:
[text_0] technical and research personnel and lab facilities , and significantly expanded the portfolio of patents available to us via license and through a cooperative development program .
[text_1] in addition , we have acquired a 20 percent interest in grt , inc .
[text_2] the gtftm technology is protected by an intellectual property protection program .
[text_3] the u.s .
[text_4] has granted 17 patents for the technology , with another 22 pending .
[text_5] worldwide , there are over 300 patents issued or pending , covering over 100 countries including regional and direct foreign filings .
[text_6] another innovative technology that we are developing focuses on reducing the processing and transportation costs of natural gas by artificially creating natural gas hydrates , which are more easily transportable than natural gas in its gaseous form .
[text_7] much like lng , gas hydrates would then be regasified upon delivery to the receiving market .
[text_8] we have an active pilot program in place to test and further develop a proprietary natural gas hydrates manufacturing system .
[text_9] the above discussion of the integrated gas segment contains forward-looking statements with respect to the possible expansion of the lng production facility .
[text_10] factors that could potentially affect the possible expansion of the lng production facility include partner and government approvals , access to sufficient natural gas volumes through exploration or commercial negotiations with other resource owners and access to sufficient regasification capacity .
[text_11] the foregoing factors ( among others ) could cause actual results to differ materially from those set forth in the forward-looking statements .
[text_12] refining , marketing and transportation we have refining , marketing and transportation operations concentrated primarily in the midwest , upper great plains , gulf coast and southeast regions of the u.s .
[text_13] we rank as the fifth largest crude oil refiner in the u.s .
[text_14] and the largest in the midwest .
[text_15] our operations include a seven-plant refining network and an integrated terminal and transportation system which supplies wholesale and marathon-brand customers as well as our own retail operations .
[text_16] our wholly-owned retail marketing subsidiary speedway superamerica llc ( 201cssa 201d ) is the third largest chain of company-owned and -operated retail gasoline and convenience stores in the u.s .
[text_17] and the largest in the midwest .
[text_18] refining we own and operate seven refineries with an aggregate refining capacity of 1.188 million barrels per day ( 201cmmbpd 201d ) of crude oil as of december 31 , 2009 .
[text_19] during 2009 , our refineries processed 957 mbpd of crude oil and 196 mbpd of other charge and blend stocks .
[text_20] the table below sets forth the location and daily crude oil refining capacity of each of our refineries as of december 31 , 2009 .
[text_21] crude oil refining capacity ( thousands of barrels per day ) 2009 .
[text_22] our refineries include crude oil atmospheric and vacuum distillation , fluid catalytic cracking , catalytic reforming , desulfurization and sulfur recovery units .
[text_23] the refineries process a wide variety of crude oils and produce numerous refined products , ranging from transportation fuels , such as reformulated gasolines , blend- grade gasolines intended for blending with fuel ethanol and ultra-low sulfur diesel fuel , to heavy fuel oil and asphalt .
[text_24] additionally , we manufacture aromatics , cumene , propane , propylene , sulfur and maleic anhydride .
[text_25] our garyville , louisiana , refinery is located along the mississippi river in southeastern louisiana between new orleans and baton rouge .
[text_26] the garyville refinery predominantly processes heavy sour crude oil into products .
[table_0] ( thousands of barrels per day ) | 2009
[table_1] ( thousands of barrels per day ): garyville louisiana | 2009: 436
[table_2] ( thousands of barrels per day ): catlettsburg kentucky | 2009: 212
[table_3] ( thousands of barrels per day ): robinson illinois | 2009: 206
[table_4] ( thousands of barrels per day ): detroit michigan | 2009: 106
[table_5] ( thousands of barrels per day ): canton ohio | 2009: 78
[table_6] ( thousands of barrels per day ): texas city texas | 2009: 76
[table_7] ( thousands of barrels per day ): st . paul park minnesota | 2009: 74
[table_8] ( thousands of barrels per day ): total | 2009: 1188

Question: what percentage of crude oil refining capacity is located in catlettsburg kentucky?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"212"},{"source":"table_8","value":"1188"}]}],"answer":0.17845117845117844}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"212"},{"source":"table_8","value":"1188"}]}],"answer":1400.0}
```

## AWK/2018/page_131.pdf-2

Evidence:
[text_0] investment tax credits have been deferred by the regulated utility subsidiaries and are being amortized to income over the average estimated service lives of the related assets .
[text_1] the company recognizes accrued interest and penalties related to tax positions as a component of income tax expense and accounts for sales tax collected from customers and remitted to taxing authorities on a net basis .
[text_2] see note 14 2014income taxes for additional information .
[text_3] allowance for funds used during construction afudc is a non-cash credit to income with a corresponding charge to utility plant that represents the cost of borrowed funds or a return on equity funds devoted to plant under construction .
[text_4] the regulated utility subsidiaries record afudc to the extent permitted by the pucs .
[text_5] the portion of afudc attributable to borrowed funds is shown as a reduction of interest , net on the consolidated statements of operations .
[text_6] any portion of afudc attributable to equity funds would be included in other , net on the consolidated statements of operations .
[text_7] afudc is provided in the following table for the years ended december 31: .
[text_8] environmental costs the company 2019s water and wastewater operations and the operations of its market-based businesses are subject to u.s .
[text_9] federal , state , local and foreign requirements relating to environmental protection , and as such , the company periodically becomes subject to environmental claims in the normal course of business .
[text_10] environmental expenditures that relate to current operations or provide a future benefit are expensed or capitalized as appropriate .
[text_11] remediation costs that relate to an existing condition caused by past operations are accrued , on an undiscounted basis , when it is probable that these costs will be incurred and can be reasonably estimated .
[text_12] a conservation agreement entered into by a subsidiary of the company with the national oceanic and atmospheric administration in 2010 and amended in 2017 required the subsidiary to , among other provisions , implement certain measures to protect the steelhead trout and its habitat in the carmel river watershed in the state of california .
[text_13] the subsidiary agreed to pay $ 1 million annually commencing in 2010 with the final payment being made in 2021 .
[text_14] remediation costs accrued amounted to $ 4 million and $ 6 million as of december 31 , 2018 and 2017 , respectively .
[text_15] derivative financial instruments the company uses derivative financial instruments for purposes of hedging exposures to fluctuations in interest rates .
[text_16] these derivative contracts are entered into for periods consistent with the related underlying exposures and do not constitute positions independent of those exposures .
[text_17] the company does not enter into derivative contracts for speculative purposes and does not use leveraged instruments .
[text_18] all derivatives are recognized on the balance sheet at fair value .
[text_19] on the date the derivative contract is entered into , the company may designate the derivative as a hedge of the fair value of a recognized asset or liability ( fair-value hedge ) or a hedge of a forecasted transaction or of the variability of cash flows to be received or paid related to a recognized asset or liability ( cash-flow hedge ) .
[text_20] changes in the fair value of a fair-value hedge , along with the gain or loss on the underlying hedged item , are recorded in current-period earnings .
[text_21] the gains and losses on the effective portion of cash-flow hedges are recorded in other comprehensive income , until earnings are affected by the variability of cash flows .
[text_22] any ineffective portion of designated cash-flow hedges is recognized in current-period earnings. .
[table_0]  | 2018 | 2017 | 2016
[table_1] : allowance for other funds used during construction | 2018: $ 24 | 2017: $ 19 | 2016: $ 15
[table_2] : allowance for borrowed funds used during construction | 2018: 13 | 2017: 8 | 2016: 6

Question: what was 2018 allowance for borrowed funds used during construction as a percentage of allowance for other funds used during construction?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"13"},{"source":"table_1","value":"24"}]}],"answer":0.5416666666666666}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"13"},{"source":"table_1","value":"24"}]}],"answer":37.0}
```

## FRT/2004/page_53.pdf-1

Evidence:
[text_0] the internal revenue code .
[text_1] therefore , cash needed to execute our strategy and invest in new properties , as well as to pay our debt at maturity , must come from one or more of the following sources : 2022 cash not distributed to shareholders , 2022 proceeds of property dispositions , or 2022 proceeds derived from the issuance of new debt or equity securities .
[text_2] it is management 2019s intention that we continually have access to the capital resources necessary to expand and develop our business .
[text_3] as a result , we intend to operate with and maintain a conservative capital structure that will allow us to maintain strong debt service coverage and fixed-charge coverage ratios as part of our commitment to investment-grade debt ratings .
[text_4] we may , from time to time , seek to obtain funds by the following means : 2022 additional equity offerings , 2022 unsecured debt financing and/or mortgage financings , and 2022 other debt and equity alternatives , including formation of joint ventures , in a manner consistent with our intention to operate with a conservative debt structure .
[text_5] cash and cash equivalents were $ 30.5 million and $ 35.0 million at december 31 , 2004 and december 31 , 2003 , respectively .
[text_6] summary of cash flows for the year ended december 31 , 2004 ( in thousands ) .
[text_7] the cash provided by operating activities is primarily attributable to the operation of our properties and the change in working capital related to our operations .
[text_8] we used cash of $ 154.3 million during the twelve months ended december 31 , 2004 in investing activities , including the following : 2022 $ 101.7 million for our acquisition of westgate mall , shaw 2019s plaza and several parcels of land , 2022 capital expenditures of $ 59.2 million for development and redevelopment of properties including santana row , 2022 maintenance capital expenditures of approximately $ 36.9 million , 2022 $ 9.4 million capital contribution to a real estate partnership , and 2022 an additional $ 3.2 million net advance under an existing mortgage note receivable ; offset by 2022 $ 41.8 million in net sale proceeds from the sale of properties , and .
[table_0]  | for the year ended december 31 2004 ( in thousands )
[table_1] : cash provided by operating activities | for the year ended december 31 2004 ( in thousands ): $ 161113
[table_2] : cash used in investing activities | for the year ended december 31 2004 ( in thousands ): -154273 ( 154273 )
[table_3] : cash used by financing activities | for the year ended december 31 2004 ( in thousands ): -11333 ( 11333 )
[table_4] : decrease in cash and cash equivalents | for the year ended december 31 2004 ( in thousands ): -4493 ( 4493 )
[table_5] : cash and cash equivalents beginning of period | for the year ended december 31 2004 ( in thousands ): 34968
[table_6] : cash and cash equivalents end of period | for the year ended december 31 2004 ( in thousands ): $ 30475

Question: what was the percentual decrease in the cash and cash equivalents during this period?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_4","value":"4493"},{"source":"table_5","value":"34968"}]}],"answer":0.12848890414092884}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_4","value":"4493"},{"source":"table_5","value":"34968"}]}],"answer":39461.0}
```

## AAPL/2007/page_70.pdf-1

Evidence:
[text_0] notes to consolidated financial statements ( continued ) note 2 2014financial instruments ( continued ) covered by collateral , third-party flooring arrangements , or credit insurance are outstanding with the company 2019s distribution and retail channel partners .
[text_1] one customer accounted for approximately 11% ( 11 % ) of trade receivables as of september 29 , 2007 , while no customers accounted for more than 10% ( 10 % ) of trade receivables as of september 30 , 2006 .
[text_2] the following table summarizes the activity in the allowance for doubtful accounts ( in millions ) : september 29 , september 30 , september 24 , 2007 2006 2005 .
[text_3] vendor non-trade receivables the company has non-trade receivables from certain of its manufacturing vendors resulting from the sale of raw material components to these manufacturing vendors who manufacture sub-assemblies or assemble final products for the company .
[text_4] the company purchases these raw material components directly from suppliers .
[text_5] these non-trade receivables , which are included in the consolidated balance sheets in other current assets , totaled $ 2.4 billion and $ 1.6 billion as of september 29 , 2007 and september 30 , 2006 , respectively .
[text_6] the company does not reflect the sale of these components in net sales and does not recognize any profits on these sales until the products are sold through to the end customer at which time the profit is recognized as a reduction of cost of sales .
[text_7] derivative financial instruments the company uses derivatives to partially offset its business exposure to foreign exchange risk .
[text_8] foreign currency forward and option contracts are used to offset the foreign exchange risk on certain existing assets and liabilities and to hedge the foreign exchange risk on expected future cash flows on certain forecasted revenue and cost of sales .
[text_9] the company 2019s accounting policies for these instruments are based on whether the instruments are designated as hedge or non-hedge instruments .
[text_10] the company records all derivatives on the balance sheet at fair value. .
[table_0]  | september 29 2007 | september 30 2006 | september 24 2005
[table_1] : beginning allowance balance | september 29 2007: $ 52 | september 30 2006: $ 46 | september 24 2005: $ 47
[table_2] : charged to costs and expenses | september 29 2007: 12 | september 30 2006: 17 | september 24 2005: 8
[table_3] : deductions | september 29 2007: -17 ( 17 ) | september 30 2006: -11 ( 11 ) | september 24 2005: -9 ( 9 )
[table_4] : ending allowance balance | september 29 2007: $ 47 | september 30 2006: $ 52 | september 24 2005: $ 46

Question: what was the percentage change in the allowance for doubtful accounts from 2005 to 2006?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_4","value":"52"},{"source":"table_4","value":"46"}]},{"op":"divide","args":["#0",{"source":"table_4","value":"46"}]}],"answer":0.13043478260869565}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_4","value":"52"},{"source":"table_4","value":"46"}]},{"op":"divide","args":["#0",{"source":"table_4","value":"46"}]}],"answer":2.130434782608696}
```

## AMAT/2016/page_30.pdf-2

Evidence:
[text_0] item 2 : properties information concerning applied 2019s properties at october 30 , 2016 is set forth below: .
[text_1] because of the interrelation of applied 2019s operations , properties within a country may be shared by the segments operating within that country .
[text_2] the company 2019s headquarters offices are in santa clara , california .
[text_3] products in semiconductor systems are manufactured in austin , texas ; gloucester , massachusetts ; kalispell , montana ; rehovot , israel ; and singapore .
[text_4] remanufactured equipment products in the applied global services segment are produced primarily in austin , texas .
[text_5] products in the display and adjacent markets segment are manufactured in alzenau , germany ; tainan , taiwan ; and santa clara , california .
[text_6] other products are manufactured in treviso , italy .
[text_7] applied also owns and leases offices , plants and warehouse locations in many locations throughout the world , including in europe , japan , north america ( principally the united states ) , israel , china , india , korea , southeast asia and taiwan .
[text_8] these facilities are principally used for manufacturing ; research , development and engineering ; and marketing , sales and customer support .
[text_9] applied also owns a total of approximately 280 acres of buildable land in montana , texas , california , massachusetts , israel and italy that could accommodate additional building space .
[text_10] applied considers the properties that it owns or leases as adequate to meet its current and future requirements .
[text_11] applied regularly assesses the size , capability and location of its global infrastructure and periodically makes adjustments based on these assessments. .
[table_0] ( square feet in thousands ) | united states | other countries | total
[table_1] ( square feet in thousands ): owned | united states: 3745 | other countries: 1629 | total: 5374
[table_2] ( square feet in thousands ): leased | united states: 564 | other countries: 1103 | total: 1667
[table_3] ( square feet in thousands ): total | united states: 4309 | other countries: 2732 | total: 7041

Question: what percentage of company's properties are leased?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"1667"},{"source":"table_3","value":"7041"}]}],"answer":0.23675614259338162}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"1667"},{"source":"table_3","value":"7041"}]}],"answer":8708.0}
```

## PKG/2006/page_68.pdf-2

Evidence:
[text_0] packaging corporation of america notes to consolidated financial statements ( continued ) december 31 , 2006 4 .
[text_1] stock-based compensation ( continued ) as of december 31 , 2006 , there was $ 8330000 of total unrecognized compensation costs related to the restricted stock awards .
[text_2] the company expects to recognize the cost of these stock awards over a weighted-average period of 2.5 years .
[text_3] 5 .
[text_4] accrued liabilities the components of accrued liabilities are as follows: .
[text_5] 6 .
[text_6] employee benefit plans and other postretirement benefits in connection with the acquisition from pactiv , pca and pactiv entered into a human resources agreement which , among other items , granted pca employees continued participation in the pactiv pension plan for a period of up to five years following the closing of the acquisition for an agreed upon fee .
[text_7] effective january 1 , 2003 , pca adopted a mirror-image pension plan for eligible hourly employees to succeed the pactiv pension plan in which pca hourly employees had participated though december 31 , 2002 .
[text_8] the pca pension plan for hourly employees recognizes service earned under both the pca plan and the prior pactiv plan .
[text_9] benefits earned under the pca plan are reduced by retirement benefits earned under the pactiv plan through december 31 , 2002 .
[text_10] all assets and liabilities associated with benefits earned through december 31 , 2002 for hourly employees and retirees of pca were retained by the pactiv plan .
[text_11] effective may 1 , 2004 , pca adopted a grandfathered pension plan for certain salaried employees who had previously participated in the pactiv pension plan pursuant to the above mentioned human resource agreement .
[text_12] the benefit formula for the new pca pension plan for salaried employees is comparable to that of the pactiv plan except that the pca plan uses career average base pay in the benefit formula in lieu of final average base pay .
[text_13] the pca pension plan for salaried employees recognizes service earned under both the pca plan and the prior pactiv plan .
[text_14] benefits earned under the pca plan are reduced by retirement benefits earned under the pactiv plan through april 30 , 2004 .
[text_15] all assets and liabilities associated with benefits earned through april 30 , 2004 for salaried employees and retirees of pca were retained by the pactiv plan .
[text_16] pca maintains a supplemental executive retirement plan ( 201cserp 201d ) , which augments pension benefits for eligible executives ( excluding the ceo ) earned under the pca pension plan for salaried employees .
[text_17] benefits are determined using the same formula as the pca pension plan but in addition to counting .
[table_0] ( in thousands ) | december 31 , 2006 | december 31 , 2005
[table_1] ( in thousands ): bonuses and incentives | december 31 , 2006: $ 29822 | december 31 , 2005: $ 21895
[table_2] ( in thousands ): medical insurance and workers 2019 compensation | december 31 , 2006: 18279 | december 31 , 2005: 18339
[table_3] ( in thousands ): vacation and holiday pay | december 31 , 2006: 14742 | december 31 , 2005: 14159
[table_4] ( in thousands ): customer volume discounts and rebates | december 31 , 2006: 13777 | december 31 , 2005: 13232
[table_5] ( in thousands ): franchise and property taxes | december 31 , 2006: 8432 | december 31 , 2005: 8539
[table_6] ( in thousands ): payroll and payroll taxes | december 31 , 2006: 5465 | december 31 , 2005: 4772
[table_7] ( in thousands ): other | december 31 , 2006: 9913 | december 31 , 2005: 5889
[table_8] ( in thousands ): total | december 31 , 2006: $ 100430 | december 31 , 2005: $ 86825

Question: what was the percent of the bonuses and incentives of the total accrued liabilities

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"29822"},{"source":"table_8","value":"100430"}]}],"answer":0.2969431444787414}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"29822"},{"source":"table_8","value":"100430"}]}],"answer":130252.0}
```

## UPS/2014/page_35.pdf-4

Evidence:
[text_0] shareowner return performance graph the following performance graph and related information shall not be deemed 201csoliciting material 201d or to be 201cfiled 201d with the sec , nor shall such information be incorporated by reference into any future filing under the securities act of 1933 or securities exchange act of 1934 , each as amended , except to the extent that the company specifically incorporates such information by reference into such filing .
[text_1] the following graph shows a five year comparison of cumulative total shareowners 2019 returns for our class b common stock , the standard & poor 2019s 500 index , and the dow jones transportation average .
[text_2] the comparison of the total cumulative return on investment , which is the change in the quarterly stock price plus reinvested dividends for each of the quarterly periods , assumes that $ 100 was invested on december 31 , 2009 in the standard & poor 2019s 500 index , the dow jones transportation average , and our class b common stock. .
[text_3] .
[table_0]  | 12/31/2009 | 12/31/2010 | 12/31/2011 | 12/31/2012 | 12/31/2013 | 12/31/2014
[table_1] : united parcel service inc . | 12/31/2009: $ 100.00 | 12/31/2010: $ 130.29 | 12/31/2011: $ 135.35 | 12/31/2012: $ 140.54 | 12/31/2013: $ 205.95 | 12/31/2014: $ 223.79
[table_2] : standard & poor 2019s 500 index | 12/31/2009: $ 100.00 | 12/31/2010: $ 115.06 | 12/31/2011: $ 117.48 | 12/31/2012: $ 136.26 | 12/31/2013: $ 180.38 | 12/31/2014: $ 205.05
[table_3] : dow jones transportation average | 12/31/2009: $ 100.00 | 12/31/2010: $ 126.74 | 12/31/2011: $ 126.75 | 12/31/2012: $ 136.24 | 12/31/2013: $ 192.61 | 12/31/2014: $ 240.91

Question: what was the percentage cumulative total shareowners 2019 returns for united parcel service inc . for the five years ended 12/31/2014?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"223.79"},"const_100"]},{"op":"divide","args":["#0","const_100"]}],"answer":1.2379}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"223.79"},"const_100"]},{"op":"divide","args":["#0","const_100"]}],"answer":3.2379}
```

## DISH/2010/page_117.pdf-2

Evidence:
[text_0] dish network corporation notes to consolidated financial statements - continued future minimum lease payments under the capital lease obligation , together with the present value of the net minimum lease payments as of december 31 , 2010 are as follows ( in thousands ) : for the years ended december 31 .
[text_1] the summary of future maturities of our outstanding long-term debt as of december 31 , 2010 is included in the commitments table in note 14 .
[text_2] 10 .
[text_3] income taxes and accounting for uncertainty in income taxes income taxes our income tax policy is to record the estimated future tax effects of temporary differences between the tax bases of assets and liabilities and amounts reported on our consolidated balance sheets , as well as probable operating loss , tax credit and other carryforwards .
[text_4] deferred tax assets are offset by valuation allowances when we believe it is more likely than not that net deferred tax assets will not be realized .
[text_5] we periodically evaluate our need for a valuation allowance .
[text_6] determining necessary valuation allowances requires us to make assessments about historical financial information as well as the timing of future events , including the probability of expected future taxable income and available tax planning opportunities .
[text_7] as of december 31 , 2010 , we had no net operating loss carryforwards ( 201cnols 201d ) for federal income tax purposes and $ 13 million of nol benefit for state income tax purposes .
[text_8] the state nols begin to expire in the year 2020 .
[text_9] in addition , there are $ 11 million of tax benefits related to credit carryforwards which are partially offset by a valuation allowance and $ 42 million of capital loss carryforwards which were fully offset by a valuation allowance .
[text_10] the credit carryforwards begin to expire in the year 2011. .
[table_0] 2011 | $ 82184
[table_1] 2011: 2012 | $ 82184: 77110
[table_2] 2011: 2013 | $ 82184: 75970
[table_3] 2011: 2014 | $ 82184: 75970
[table_4] 2011: 2015 | $ 82184: 75970
[table_5] 2011: thereafter | $ 82184: 390239
[table_6] 2011: total minimum lease payments | $ 82184: 777443
[table_7] 2011: less : amount representing lease of the orbital location and estimated executory costs ( primarily insurance and maintenance ) including profit thereon included in total minimum lease payments | $ 82184: -357982 ( 357982 )
[table_8] 2011: net minimum lease payments | $ 82184: 419461
[table_9] 2011: less : amount representing interest | $ 82184: -132490 ( 132490 )
[table_10] 2011: present value of net minimum lease payments | $ 82184: 286971
[table_11] 2011: less : current portion | $ 82184: -24801 ( 24801 )
[table_12] 2011: long-term portion of capital lease obligations | $ 82184: $ 262170

Question: what percentage of total minimum lease payments are due in 2015?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_4","value":"75970"},{"source":"table_6","value":"777443"}]}],"answer":0.09771777480792804}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_4","value":"75970"},{"source":"table_6","value":"777443"}]}],"answer":853413.0}
```

## AAPL/2017/page_23.pdf-2

Evidence:
[text_0] apple inc .
[text_1] | 2017 form 10-k | 20 company stock performance the following graph shows a comparison of cumulative total shareholder return , calculated on a dividend reinvested basis , for the company , the s&p 500 index , the s&p information technology index and the dow jones u.s .
[text_2] technology supersector index for the five years ended september 30 , 2017 .
[text_3] the graph assumes $ 100 was invested in each of the company 2019s common stock , the s&p 500 index , the s&p information technology index and the dow jones u.s .
[text_4] technology supersector index as of the market close on september 28 , 2012 .
[text_5] note that historic stock price performance is not necessarily indicative of future stock price performance .
[text_6] * $ 100 invested on 9/28/12 in stock or index , including reinvestment of dividends .
[text_7] data points are the last day of each fiscal year for the company 2019s common stock and september 30th for indexes .
[text_8] copyright a9 2017 s&p , a division of mcgraw hill financial .
[text_9] all rights reserved .
[text_10] copyright a9 2017 dow jones & co .
[text_11] all rights reserved .
[text_12] september september september september september september .
[text_13] .
[table_0]  | september2012 | september2013 | september2014 | september2015 | september2016 | september2017
[table_1] : apple inc . | september2012: $ 100 | september2013: $ 74 | september2014: $ 111 | september2015: $ 128 | september2016: $ 129 | september2017: $ 179
[table_2] : s&p 500 index | september2012: $ 100 | september2013: $ 119 | september2014: $ 143 | september2015: $ 142 | september2016: $ 164 | september2017: $ 194
[table_3] : s&p information technology index | september2012: $ 100 | september2013: $ 107 | september2014: $ 138 | september2015: $ 141 | september2016: $ 173 | september2017: $ 223
[table_4] : dow jones u.s . technology supersector index | september2012: $ 100 | september2013: $ 105 | september2014: $ 137 | september2015: $ 137 | september2016: $ 167 | september2017: $ 214

Question: what was the change in the apple stock return between 2016 and 2017?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"179"},{"source":"table_1","value":"129"}]}],"answer":50.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"179"},{"source":"table_1","value":"129"}]}],"answer":308.0}
```

## APD/2016/page_96.pdf-1

Evidence:
[text_0] 15 .
[text_1] debt the tables below summarize our outstanding debt at 30 september 2016 and 2015 : total debt .
[text_2] the weighted average interest rate of short-term borrowings outstanding at 30 september 2016 and 2015 was 1.1% ( 1.1 % ) and .8% ( .8 % ) , respectively .
[text_3] cash paid for interest , net of amounts capitalized , was $ 121.1 in 2016 , $ 97.5 in 2015 , and $ 132.4 in 2014. .
[table_0] 30 september | 2016 | 2015
[table_1] 30 september: short-term borrowings | 2016: $ 935.8 | 2015: $ 1494.3
[table_2] 30 september: current portion of long-term debt | 2016: 371.3 | 2015: 435.6
[table_3] 30 september: long-term debt | 2016: 4918.1 | 2015: 3949.1
[table_4] 30 september: total debt | 2016: $ 6225.2 | 2015: $ 5879.0
[table_5] 30 september: short-term borrowings | 2016:  | 2015: 
[table_6] 30 september: 30 september | 2016: 2016 | 2015: 2015
[table_7] 30 september: bank obligations | 2016: $ 133.1 | 2015: $ 234.3
[table_8] 30 september: commercial paper | 2016: 802.7 | 2015: 1260.0
[table_9] 30 september: total short-term borrowings | 2016: $ 935.8 | 2015: $ 1494.3

Question: considering the years 2014-2016 , what was the average cash paid for interest?

Chosen:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_3","value":"121.1"},{"source":"text_3","value":"97.5"}]},{"op":"add","args":[{"source":"text_3","value":"132.4"},"#0"]},{"op":"divide","args":["#1","const_3"]}],"answer":117.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_3","value":"121.1"},{"source":"text_3","value":"97.5"}]},{"op":"add","args":[{"source":"text_3","value":"132.4"},"#0"]},{"op":"divide","args":["#1","const_3"]}],"answer":52.0}
```

## STT/2008/page_109.pdf-3

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

Question: what portion of the balance of initial accrual is related to severances?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"250"},{"source":"table_1","value":"306"}]}],"answer":0.8169934640522876}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"250"},{"source":"table_1","value":"306"}]}],"answer":556.0}
```

## EOG/2017/page_85.pdf-1

Evidence:
[text_0] the diluted earnings per share calculation excludes stock options , sars , restricted stock and units and performance units and stock that were anti-dilutive .
[text_1] shares underlying the excluded stock options and sars totaled 2.6 million , 10.3 million and 10.2 million for the years ended december 31 , 2017 , 2016 and 2015 , respectively .
[text_2] for the year ended december 31 , 2016 , 4.5 million shares of restricted stock and restricted stock units and performance units and performance stock were excluded .
[text_3] 10 .
[text_4] supplemental cash flow information net cash paid for interest and income taxes was as follows for the years ended december 31 , 2017 , 2016 and 2015 ( in thousands ) : .
[text_5] eog's accrued capital expenditures at december 31 , 2017 , 2016 and 2015 were $ 475 million , $ 388 million and $ 416 million , respectively .
[text_6] non-cash investing activities for the year ended december 31 , 2017 included non-cash additions of $ 282 million to eog's oil and gas properties as a result of property exchanges .
[text_7] non-cash investing activities for the year ended december 31 , 2016 included $ 3834 million in non-cash additions to eog's oil and gas properties related to the yates transaction ( see note 17 ) .
[text_8] 11 .
[text_9] business segment information eog's operations are all crude oil and natural gas exploration and production related .
[text_10] the segment reporting topic of the asc establishes standards for reporting information about operating segments in annual financial statements .
[text_11] operating segments are defined as components of an enterprise about which separate financial information is available and evaluated regularly by the chief operating decision maker , or decision-making group , in deciding how to allocate resources and in assessing performance .
[text_12] eog's chief operating decision-making process is informal and involves the chairman of the board and chief executive officer and other key officers .
[text_13] this group routinely reviews and makes operating decisions related to significant issues associated with each of eog's major producing areas in the united states , trinidad , the united kingdom and china .
[text_14] for segment reporting purposes , the chief operating decision maker considers the major united states producing areas to be one operating segment. .
[table_0]  | 2017 | 2016 | 2015
[table_1] : interest net of capitalized interest | 2017: $ 275305 | 2016: $ 252030 | 2015: $ 222088
[table_2] : income taxes net of refunds received | 2017: $ 188946 | 2016: $ -39293 ( 39293 ) | 2015: $ 41108

Question: what is the increase observed in the interest net of capitalized interest during 2016 and 2017?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"275305"},{"source":"table_1","value":"252030"}]},{"op":"subtract","args":["#0","const_1"]}],"answer":0.09235011704955759}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"275305"},{"source":"table_1","value":"252030"}]},{"op":"subtract","args":["#0","const_1"]}],"answer":527334.0}
```

## ETR/2004/page_160.pdf-3

Evidence:
[text_0] entergy arkansas , inc .
[text_1] management's financial discussion and analysis fuel and purchased power expenses increased primarily due to increased recovery of deferred fuel and purchased power costs primarily due to an increase in april 2004 in the energy cost recovery rider and the true-ups to the 2003 and 2002 energy cost recovery rider filings .
[text_2] other regulatory credits decreased primarily due to the over-recovery of grand gulf costs due to an increase in the grand gulf rider effective january 2004 .
[text_3] 2003 compared to 2002 net revenue , which is entergy arkansas' measure of gross margin , consists of operating revenues net of : 1 ) fuel , fuel-related , and purchased power expenses and 2 ) other regulatory credits .
[text_4] following is an analysis of the change in net revenue comparing 2003 to 2002. .
[text_5] the march 2002 settlement agreement resolved a request for recovery of ice storm costs incurred in december 2000 with an offset of those costs for funds contributed to pay for future stranded costs .
[text_6] a 1997 settlement provided for the collection of earnings in excess of an 11% ( 11 % ) return on equity in a transition cost account ( tca ) to offset stranded costs if retail open access were implemented .
[text_7] in mid- and late december 2000 , two separate ice storms left 226000 and 212500 entergy arkansas customers , respectively , without electric power in its service area .
[text_8] entergy arkansas filed a proposal to recover costs plus carrying charges associated with power restoration caused by the ice storms .
[text_9] entergy arkansas' final storm damage cost determination reflected costs of approximately $ 195 million .
[text_10] the apsc approved a settlement agreement submitted in march 2002 by entergy arkansas , the apsc staff , and the arkansas attorney general .
[text_11] in the march 2002 settlement , the parties agreed that $ 153 million of the ice storm costs would be classified as incremental ice storm expenses that can be offset against the tca on a rate class basis , and any excess of ice storm costs over the amount available in the tca would be deferred and amortized over 30 years , although such excess costs were not allowed to be included as a separate component of rate base .
[text_12] the allocated ice storm expenses exceeded the available tca funds by $ 15.8 million which was recorded as a regulatory asset in june 2002 .
[text_13] in accordance with the settlement agreement and following the apsc's approval of the 2001 earnings review related to the tca , entergy arkansas filed to return $ 18.1 million of the tca to certain large general service class customers that paid more into the tca than their allocation of storm costs .
[text_14] the apsc approved the return of funds to the large general service customer class in the form of refund checks in august 2002 .
[text_15] as part of the implementation of the march 2002 settlement agreement provisions , the tca procedure ceased with the 2001 earnings evaluation .
[text_16] of the remaining ice storm costs , $ 32.2 million was addressed through established ratemaking procedures , including $ 22.2 million classified as capital additions , while $ 3.8 million of the ice storm costs was not recovered through rates .
[text_17] the effect on net income of the march 2002 settlement agreement and 2001 earnings review was a $ 2.2 million increase in 2003 , because the decrease in net revenue was offset by the decrease in operation and maintenance expenses discussed below. .
[table_0]  | ( in millions )
[table_1] : 2002 net revenue | ( in millions ): $ 1095.9
[table_2] : march 2002 settlement agreement | ( in millions ): -154.0 ( 154.0 )
[table_3] : volume/weather | ( in millions ): -7.7 ( 7.7 )
[table_4] : asset retirement obligation | ( in millions ): 30.1
[table_5] : net wholesale revenue | ( in millions ): 16.6
[table_6] : deferred fuel cost revisions | ( in millions ): 10.2
[table_7] : other | ( in millions ): 7.6
[table_8] : 2003 net revenue | ( in millions ): $ 998.7

Question: what is the percent change in net revenue from 2002 to 2003?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"1095.9"},{"source":"table_8","value":"998.7"}]},{"op":"divide","args":["#0",{"source":"table_8","value":"998.7"}]}],"answer":0.09732652448182637}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"1095.9"},{"source":"table_8","value":"998.7"}]},{"op":"divide","args":["#0",{"source":"table_8","value":"998.7"}]}],"answer":2.097326524481826}
```

## PKG/2005/page_73.pdf-2

Evidence:
[text_0] packaging corporation of america notes to consolidated financial statements ( continued ) december 31 , 2005 9 .
[text_1] shareholders 2019 equity ( continued ) stockholder received proceeds , net of the underwriting discount , of $ 20.69 per share .
[text_2] the company did not sell any shares in , or receive any proceeds from , the secondary offering .
[text_3] concurrent with the closing of the secondary offering on december 21 , 2005 , the company entered into a common stock repurchase agreement with pca holdings llc .
[text_4] pursuant to the repurchase agreement , the company purchased 4500000 shares of common stock directly from pca holdings llc at the initial price to the public net of the underwriting discount or $ 20.69 per share , the same net price per share received by pca holdings llc in the secondary offering .
[text_5] these shares were retired on december 21 , 2005 .
[text_6] 10 .
[text_7] commitments and contingencies capital commitments the company had authorized capital expenditures of approximately $ 33.1 million and $ 55.2 million as of december 31 , 2005 and 2004 , respectively , in connection with the expansion and replacement of existing facilities and equipment .
[text_8] operating leases pca leases space for certain of its facilities and cutting rights to approximately 108000 acres of timberland under long-term leases .
[text_9] the company also leases equipment , primarily vehicles and rolling stock , and other assets under long-term leases of a duration generally of three years .
[text_10] the minimum lease payments under non-cancelable operating leases with lease terms in excess of one year are as follows : ( in thousands ) .
[text_11] capital lease obligations were not significant to the accompanying financial statements .
[text_12] total lease expense , including base rent on all leases and executory costs , such as insurance , taxes , and maintenance , for the years ended december 31 , 2005 , 2004 and 2003 was $ 35.8 million , $ 33.0 million and $ 31.6 million , respectively .
[text_13] these costs are included in cost of goods sold and selling and administrative expenses. .
[table_0] 2006 | $ 24569
[table_1] 2006: 2007 | $ 24569: 21086
[table_2] 2006: 2008 | $ 24569: 14716
[table_3] 2006: 2009 | $ 24569: 9801
[table_4] 2006: 2010 | $ 24569: 6670
[table_5] 2006: thereafter | $ 24569: 37130
[table_6] 2006: total | $ 24569: $ 113972

Question: pursuant to the repurchase agreement , what was the total purchase price of the 4500000 shares of common stock directly from pca holdings llc?

Chosen:
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"text_4","value":"4500000"},{"source":"text_4","value":"20.69"}]}],"answer":93105000.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_4","value":"4500000"},{"source":"text_4","value":"20.69"}]}],"answer":4500020.69}
```

## STT/2012/page_42.pdf-3

Evidence:
[text_0] shareholder return performance presentation the graph presented below compares the cumulative total shareholder return on state street's common stock to the cumulative total return of the s&p 500 index and the s&p financial index over a five-year period .
[text_1] the cumulative total shareholder return assumes the investment of $ 100 in state street common stock and in each index on december 31 , 2007 at the closing price on the last trading day of 2007 , and also assumes reinvestment of common stock dividends .
[text_2] the s&p financial index is a publicly available measure of 80 of the standard & poor's 500 companies , representing 26 diversified financial services companies , 22 insurance companies , 17 real estate companies and 15 banking companies .
[text_3] comparison of five-year cumulative total shareholder return .
[text_4] .
[table_0]  | 2007 | 2008 | 2009 | 2010 | 2011 | 2012
[table_1] : state street corporation | 2007: $ 100 | 2008: $ 49 | 2009: $ 55 | 2010: $ 58 | 2011: $ 52 | 2012: $ 61
[table_2] : s&p 500 index | 2007: 100 | 2008: 63 | 2009: 80 | 2010: 92 | 2011: 94 | 2012: 109
[table_3] : s&p financial index | 2007: 100 | 2008: 45 | 2009: 52 | 2010: 59 | 2011: 49 | 2012: 63

Question: what is the percent change in state street corporation's cumulative total shareholder return on common stock between 2008 and 2009?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"55"},{"source":"table_1","value":"49"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"49"}]}],"answer":0.12244897959183673}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"55"},{"source":"table_1","value":"49"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"49"}]}],"answer":2.122448979591837}
```

## ETR/2016/page_382.pdf-2

Evidence:
[text_0] entergy mississippi , inc .
[text_1] management 2019s financial discussion and analysis entergy mississippi 2019s receivables from or ( payables to ) the money pool were as follows as of december 31 for each of the following years. .
[text_2] see note 4 to the financial statements for a description of the money pool .
[text_3] entergy mississippi has four separate credit facilities in the aggregate amount of $ 102.5 million scheduled to expire may 2017 .
[text_4] no borrowings were outstanding under the credit facilities as of december 31 , 2016 .
[text_5] in addition , entergy mississippi is a party to an uncommitted letter of credit facility as a means to post collateral to support its obligations under miso .
[text_6] as of december 31 , 2016 , a $ 7.1 million letter of credit was outstanding under entergy mississippi 2019s uncommitted letter of credit facility .
[text_7] see note 4 to the financial statements for additional discussion of the credit facilities .
[text_8] entergy mississippi obtained authorizations from the ferc through october 2017 for short-term borrowings not to exceed an aggregate amount of $ 175 million at any time outstanding and long-term borrowings and security issuances .
[text_9] see note 4 to the financial statements for further discussion of entergy mississippi 2019s short-term borrowing limits .
[text_10] state and local rate regulation and fuel-cost recovery the rates that entergy mississippi charges for electricity significantly influence its financial position , results of operations , and liquidity .
[text_11] entergy mississippi is regulated and the rates charged to its customers are determined in regulatory proceedings .
[text_12] a governmental agency , the mpsc , is primarily responsible for approval of the rates charged to customers .
[text_13] formula rate plan in june 2014 , entergy mississippi filed its first general rate case before the mpsc in almost 12 years .
[text_14] the rate filing laid out entergy mississippi 2019s plans for improving reliability , modernizing the grid , maintaining its workforce , stabilizing rates , utilizing new technologies , and attracting new industry to its service territory .
[text_15] entergy mississippi requested a net increase in revenue of $ 49 million for bills rendered during calendar year 2015 , including $ 30 million resulting from new depreciation rates to update the estimated service life of assets .
[text_16] in addition , the filing proposed , among other things : 1 ) realigning cost recovery of the attala and hinds power plant acquisitions from the power management rider to base rates ; 2 ) including certain miso-related revenues and expenses in the power management rider ; 3 ) power management rider changes that reflect the changes in costs and revenues that will accompany entergy mississippi 2019s withdrawal from participation in the system agreement ; and 4 ) a formula rate plan forward test year to allow for known changes in expenses and revenues for the rate effective period .
[text_17] entergy mississippi proposed maintaining the current authorized return on common equity of 10.59% ( 10.59 % ) .
[text_18] in october 2014 , entergy mississippi and the mississippi public utilities staff entered into and filed joint stipulations that addressed the majority of issues in the proceeding .
[text_19] the stipulations provided for : 2022 an approximate $ 16 million net increase in revenues , which reflected an agreed upon 10.07% ( 10.07 % ) return on common equity ; 2022 revision of entergy mississippi 2019s formula rate plan by providing entergy mississippi with the ability to reflect known and measurable changes to historical rate base and certain expense amounts ; resolving uncertainty around and obviating the need for an additional rate filing in connection with entergy mississippi 2019s withdrawal from participation in the system agreement ; updating depreciation rates ; and moving costs associated with the attala and hinds generating plants from the power management rider to base rates; .
[table_0] 2016 | 2015 | 2014 | 2013
[table_1] 2016: ( in thousands ) | 2015: ( in thousands ) | 2014: ( in thousands ) | 2013: ( in thousands )
[table_2] 2016: $ 10595 | 2015: $ 25930 | 2014: $ 644 | 2013: ( $ 3536 )

Question: the company has four separate credit facilities expiring in may 2017 . what was the average amount in millions of those four facilties?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_3","value":"102.5"},"const_4"]}],"answer":25.625}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_3","value":"102.5"},"const_4"]}],"answer":106.5}
```

## AON/2015/page_96.pdf-1

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_5","value":"411636"},{"source":"text_5","value":"439000"}]}],"answer":850636.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_5","value":"411636"},{"source":"text_5","value":"439000"}]}],"answer":-27364.0}
```

## AON/2007/page_175.pdf-2

Evidence:
[text_0] notes to consolidated financial statements the following table sets forth the activity related to the 2005 restructuring plan liabilities .
[text_1] ( millions ) .
[text_2] aon 2019s unpaid restructuring liabilities are included in both accounts payable and accrued liabilities and other non-current liabilities in the consolidated statements of financial position .
[text_3] aon corporation .
[table_0] balance at january 1 2005 | $ 2014
[table_1] balance at january 1 2005: expensed in 2005 | $ 2014: 141
[table_2] balance at january 1 2005: cash payments in 2005 | $ 2014: -23 ( 23 )
[table_3] balance at january 1 2005: foreign currency revaluation | $ 2014: -2 ( 2 )
[table_4] balance at january 1 2005: balance at december 31 2005 | $ 2014: 116
[table_5] balance at january 1 2005: expensed in 2006 | $ 2014: 155
[table_6] balance at january 1 2005: cash payments in 2006 | $ 2014: -141 ( 141 )
[table_7] balance at january 1 2005: foreign currency revaluation | $ 2014: 4
[table_8] balance at january 1 2005: balance at december 31 2006 | $ 2014: 134
[table_9] balance at january 1 2005: expensed in 2007 | $ 2014: 38
[table_10] balance at january 1 2005: cash payments in 2007 | $ 2014: -110 ( 110 )
[table_11] balance at january 1 2005: foreign currency revaluation | $ 2014: 1
[table_12] balance at january 1 2005: balance at december 31 2007 | $ 2014: $ 63

Question: what is the net change in aon 2019s unpaid restructuring liabilities during 2006?

Chosen:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_5","value":"155"},{"source":"table_6","value":"-141"}]},{"op":"add","args":["#0",{"source":"table_7","value":"4"}]}],"answer":18.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_5","value":"155"},{"source":"table_6","value":"-141"}]},{"op":"add","args":["#0",{"source":"table_7","value":"4"}]}],"answer":300.0}
```

## ETR/2008/page_153.pdf-4

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

Question: what percent of total lease payments is in 'years thereafter'?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_6","value":"137858"},{"source":"table_7","value":"321237"}]}],"answer":0.4291473273626637}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_6","value":"137858"},{"source":"table_7","value":"321237"}]}],"answer":459095.0}
```

## LLY/2018/page_63.pdf-2

Evidence:
[text_0] note 6 : inventories we use the last-in , first-out ( lifo ) method for the majority of our inventories located in the continental u.s .
[text_1] other inventories are valued by the first-in , first-out ( fifo ) method .
[text_2] fifo cost approximates current replacement cost .
[text_3] inventories measured using lifo must be valued at the lower of cost or market .
[text_4] inventories measured using fifo must be valued at the lower of cost or net realizable value .
[text_5] inventories at december 31 consisted of the following: .
[text_6] inventories valued under the lifo method comprised $ 1.57 billion and $ 1.56 billion of total inventories at december 31 , 2018 and 2017 , respectively .
[text_7] note 7 : financial instruments financial instruments that potentially subject us to credit risk consist principally of trade receivables and interest- bearing investments .
[text_8] wholesale distributors of life-science products account for a substantial portion of our trade receivables ; collateral is generally not required .
[text_9] we seek to mitigate the risk associated with this concentration through our ongoing credit-review procedures and insurance .
[text_10] a large portion of our cash is held by a few major financial institutions .
[text_11] we monitor our exposures with these institutions and do not expect any of these institutions to fail to meet their obligations .
[text_12] major financial institutions represent the largest component of our investments in corporate debt securities .
[text_13] in accordance with documented corporate risk-management policies , we monitor the amount of credit exposure to any one financial institution or corporate issuer .
[text_14] we are exposed to credit-related losses in the event of nonperformance by counterparties to risk-management instruments but do not expect any counterparties to fail to meet their obligations given their high credit ratings .
[text_15] we consider all highly liquid investments with a maturity of three months or less from the date of purchase to be cash equivalents .
[text_16] the cost of these investments approximates fair value .
[text_17] our equity investments are accounted for using three different methods depending on the type of equity investment : 2022 investments in companies over which we have significant influence but not a controlling interest are accounted for using the equity method , with our share of earnings or losses reported in other-net , ( income ) expense .
[text_18] 2022 for equity investments that do not have readily determinable fair values , we measure these investments at cost , less any impairment , plus or minus changes resulting from observable price changes in orderly transactions for the identical or similar investment of the same issuer .
[text_19] any change in recorded value is recorded in other-net , ( income ) expense .
[text_20] 2022 our public equity investments are measured and carried at fair value .
[text_21] any change in fair value is recognized in other-net , ( income ) expense .
[text_22] we review equity investments other than public equity investments for indications of impairment on a regular basis .
[text_23] our derivative activities are initiated within the guidelines of documented corporate risk-management policies and are intended to offset losses and gains on the assets , liabilities , and transactions being hedged .
[text_24] management reviews the correlation and effectiveness of our derivatives on a quarterly basis. .
[table_0]  | 2018 | 2017
[table_1] : finished products | 2018: $ 988.1 | 2017: $ 1211.4
[table_2] : work in process | 2018: 2628.2 | 2017: 2697.7
[table_3] : raw materials and supplies | 2018: 506.5 | 2017: 488.8
[table_4] : total ( approximates replacement cost ) | 2018: 4122.8 | 2017: 4397.9
[table_5] : increase ( reduction ) to lifo cost | 2018: -11.0 ( 11.0 ) | 2017: 60.4
[table_6] : inventories | 2018: $ 4111.8 | 2017: $ 4458.3

Question: what was the percentage change in raw materials and supplies between 2017 and 2018?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_3","value":"506.5"},{"source":"table_3","value":"488.8"}]},{"op":"divide","args":["#0",{"source":"table_3","value":"488.8"}]}],"answer":0.036211129296235677}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_3","value":"506.5"},{"source":"table_3","value":"488.8"}]},{"op":"divide","args":["#0",{"source":"table_3","value":"488.8"}]}],"answer":2.0362111292962357}
```

## RSG/2013/page_69.pdf-1

Evidence:
[text_0] constitutes an event of default under our other debt instruments , including our senior notes , and , therefore , our senior notes would also be subject to acceleration of maturity .
[text_1] if such acceleration were to occur , we would not have sufficient liquidity available to repay the indebtedness .
[text_2] we would likely have to seek an amendment under our credit facilities for relief from the financial covenants or repay the debt with proceeds from the issuance of new debt or equity , or asset sales , if necessary .
[text_3] we may be unable to amend our credit facilities or raise sufficient capital to repay such obligations in the event the maturities are accelerated .
[text_4] financial assurance we must provide financial assurance to governmental agencies and a variety of other entities under applicable environmental regulations relating to our landfill operations for capping , closure and post-closure costs , and related to our performance under certain collection , landfill and transfer station contracts .
[text_5] we satisfy these financial assurance requirements by providing surety bonds , letters of credit , or insurance policies ( the financial assurance instruments ) , or trust deposits , which are included in restricted cash and marketable securities and other assets in our consolidated balance sheets .
[text_6] the amount of the financial assurance requirements for capping , closure and post-closure costs is determined by applicable state environmental regulations .
[text_7] the financial assurance requirements for capping , closure and post-closure costs may be associated with a portion of the landfill or the entire landfill .
[text_8] generally , states require a third-party engineering specialist to determine the estimated capping , closure and post-closure costs that are used to determine the required amount of financial assurance for a landfill .
[text_9] the amount of financial assurance required can , and generally will , differ from the obligation determined and recorded under u.s .
[text_10] gaap .
[text_11] the amount of the financial assurance requirements related to contract performance varies by contract .
[text_12] additionally , we must provide financial assurance for our insurance program and collateral for certain performance obligations .
[text_13] we do not expect a material increase in financial assurance requirements during 2014 , although the mix of financial assurance instruments may change .
[text_14] these financial instruments are issued in the normal course of business and are not considered indebtedness .
[text_15] because we currently have no liability for the financial assurance instruments , they are not reflected in our consolidated balance sheets ; however , we record capping , closure and post-closure liabilities and self-insurance liabilities as they are incurred .
[text_16] the underlying obligations of the financial assurance instruments , in excess of those already reflected in our consolidated balance sheets , would be recorded if it is probable that we would be unable to fulfill our related obligations .
[text_17] we do not expect this to occur .
[text_18] off-balance sheet arrangements we have no off-balance sheet debt or similar obligations , other than financial assurance instruments and operating leases , that are not classified as debt .
[text_19] we do not guarantee any third-party debt .
[text_20] free cash flow we define free cash flow , which is not a measure determined in accordance with u.s .
[text_21] gaap , as cash provided by operating activities less purchases of property and equipment , plus proceeds from sales of property and equipment as presented in our consolidated statements of cash flows .
[text_22] our free cash flow for the years ended december 31 , 2013 , 2012 and 2011 is calculated as follows ( in millions of dollars ) : .
[text_23] .
[table_0]  | 2013 | 2012 | 2011
[table_1] : cash provided by operating activities | 2013: $ 1548.2 | 2012: $ 1513.8 | 2011: $ 1766.7
[table_2] : purchases of property and equipment | 2013: -880.8 ( 880.8 ) | 2012: -903.5 ( 903.5 ) | 2011: -936.5 ( 936.5 )
[table_3] : proceeds from sales of property and equipment | 2013: 23.9 | 2012: 28.7 | 2011: 34.6
[table_4] : free cash flow | 2013: $ 691.3 | 2012: $ 639.0 | 2011: $ 864.8

Question: in 2013 what was the ratio of the cash provided by operating activities to the amount spent on purchases of property and the equipment

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"1548.2"},{"source":"table_2","value":"880.8"}]}],"answer":1.7577202543142598}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"1548.2"},{"source":"table_2","value":"880.8"}]}],"answer":2429.0}
```

## AAPL/2011/page_24.pdf-3

Evidence:
[text_0] company stock performance the following graph shows a five-year comparison of cumulative total shareholder return , calculated on a dividend reinvested basis , for the company , the s&p 500 composite index , the s&p computer hardware index , and the dow jones u.s .
[text_1] technology index .
[text_2] the graph assumes $ 100 was invested in each of the company 2019s common stock , the s&p 500 composite index , the s&p computer hardware index , and the dow jones u.s .
[text_3] technology index on september 30 , 2006 .
[text_4] data points on the graph are annual .
[text_5] note that historic stock price performance is not necessarily indicative of future stock price performance .
[text_6] comparison of 5 year cumulative total return* among apple inc. , the s&p 500 index , the s&p computer hardware index and the dow jones us technology index sep-10sep-09sep-08sep-07sep-06 sep-11 apple inc .
[text_7] s&p 500 s&p computer hardware dow jones us technology *$ 100 invested on 9/30/06 in stock or index , including reinvestment of dividends .
[text_8] fiscal year ending september 30 .
[text_9] copyright a9 2011 s&p , a division of the mcgraw-hill companies inc .
[text_10] all rights reserved .
[text_11] copyright a9 2011 dow jones & co .
[text_12] all rights reserved .
[text_13] september 30 , september 30 , september 30 , september 30 , september 30 , september 30 .
[text_14] .
[table_0]  | september 30 2006 | september 30 2007 | september 30 2008 | september 30 2009 | september 30 2010 | september 30 2011
[table_1] : apple inc . | september 30 2006: $ 100 | september 30 2007: $ 199 | september 30 2008: $ 148 | september 30 2009: $ 241 | september 30 2010: $ 369 | september 30 2011: $ 495
[table_2] : s&p 500 | september 30 2006: $ 100 | september 30 2007: $ 116 | september 30 2008: $ 91 | september 30 2009: $ 85 | september 30 2010: $ 93 | september 30 2011: $ 94
[table_3] : s&p computer hardware | september 30 2006: $ 100 | september 30 2007: $ 148 | september 30 2008: $ 124 | september 30 2009: $ 147 | september 30 2010: $ 174 | september 30 2011: $ 197
[table_4] : dow jones us technology | september 30 2006: $ 100 | september 30 2007: $ 123 | september 30 2008: $ 94 | september 30 2009: $ 104 | september 30 2010: $ 117 | september 30 2011: $ 120

Question: what was the cumulative percentage return for the four years ended september 30 , 2010 for apple inc.?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"369"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100"}]}],"answer":2.69}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"369"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100"}]}],"answer":4.69}
```

## GIS/2018/page_82.pdf-2

Evidence:
[text_0] scheduled maturities of our marketable securities are as follows: .
[text_1] as of may 27 , 2018 , we did not any have cash and cash equivalents pledged as collateral for derivative contracts .
[text_2] as of may 27 , 2018 , $ 0.9 million of certain accounts receivable were pledged as collateral against a foreign uncommitted line of credit .
[text_3] the fair value and carrying amounts of long-term debt , including the current portion , were $ 14169.7 million and $ 14268.8 million , respectively , as of may 27 , 2018 .
[text_4] the fair value of long-term debt was estimated using market quotations and discounted cash flows based on our current incremental borrowing rates for similar types of instruments .
[text_5] long-term debt is a level 2 liability in the fair value hierarchy .
[text_6] risk management activities as a part of our ongoing operations , we are exposed to market risks such as changes in interest and foreign currency exchange rates and commodity and equity prices .
[text_7] to manage these risks , we may enter into various derivative transactions ( e.g. , futures , options , and swaps ) pursuant to our established policies .
[text_8] commodity price risk many commodities we use in the production and distribution of our products are exposed to market price risks .
[text_9] we utilize derivatives to manage price risk for our principal ingredients and energy costs , including grains ( oats , wheat , and corn ) , oils ( principally soybean ) , dairy products , natural gas , and diesel fuel .
[text_10] our primary objective when entering into these derivative contracts is to achieve certainty with regard to the future price of commodities purchased for use in our supply chain .
[text_11] we manage our exposures through a combination of purchase orders , long-term contracts with suppliers , exchange-traded futures and options , and over-the-counter options and swaps .
[text_12] we offset our exposures based on current and projected market conditions and generally seek to acquire the inputs at as close to our planned cost as possible .
[text_13] we use derivatives to manage our exposure to changes in commodity prices .
[text_14] we do not perform the assessments required to achieve hedge accounting for commodity derivative positions .
[text_15] accordingly , the changes in the values of these derivatives are recorded currently in cost of sales in our consolidated statements of earnings .
[text_16] although we do not meet the criteria for cash flow hedge accounting , we believe that these instruments are effective in achieving our objective of providing certainty in the future price of commodities purchased for use in our supply chain .
[text_17] accordingly , for purposes of measuring segment operating performance these gains and losses are reported in unallocated corporate items outside of segment operating results until such time that the exposure we are managing affects earnings .
[text_18] at that time we reclassify the gain or loss from unallocated corporate items to segment operating profit , allowing our operating segments to realize the economic effects of the derivative without experiencing any resulting mark-to-market volatility , which remains in unallocated corporate items. .
[table_0] in millions | available for sale cost | available for sale fair value
[table_1] in millions: under 1 year ( current ) | available for sale cost: $ 25.4 | available for sale fair value: $ 25.4
[table_2] in millions: equity securities | available for sale cost: 0.3 | available for sale fair value: 3.5
[table_3] in millions: total | available for sale cost: $ 25.7 | available for sale fair value: $ 28.9

Question: what is the difference between carrying amounts of long-term debt and fair value?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_3","value":"14268.8"},{"source":"text_3","value":"14169.7"}]}],"answer":99.1}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_3","value":"14268.8"},{"source":"text_3","value":"14169.7"}]}],"answer":28438.5}
```

## EW/2016/page_92.pdf-2

Evidence:
[text_0] edwards lifesciences corporation notes to consolidated financial statements ( continued ) 12 .
[text_1] employee benefit plans ( continued ) equity and debt securities are valued at fair value based on quoted market prices reported on the active markets on which the individual securities are traded .
[text_2] the insurance contracts are valued at the cash surrender value of the contracts , which is deemed to approximate its fair value .
[text_3] the following benefit payments , which reflect expected future service , as appropriate , at december 31 , 2016 , are expected to be paid ( in millions ) : .
[text_4] as of december 31 , 2016 , expected employer contributions for 2017 are $ 6.1 million .
[text_5] defined contribution plans the company 2019s employees in the united states and puerto rico are eligible to participate in a qualified defined contribution plan .
[text_6] in the united states , participants may contribute up to 25% ( 25 % ) of their eligible compensation ( subject to tax code limitation ) to the plan .
[text_7] edwards lifesciences matches the first 3% ( 3 % ) of the participant 2019s annual eligible compensation contributed to the plan on a dollar-for-dollar basis .
[text_8] edwards lifesciences matches the next 2% ( 2 % ) of the participant 2019s annual eligible compensation to the plan on a 50% ( 50 % ) basis .
[text_9] in puerto rico , participants may contribute up to 25% ( 25 % ) of their annual compensation ( subject to tax code limitation ) to the plan .
[text_10] edwards lifesciences matches the first 4% ( 4 % ) of participant 2019s annual eligible compensation contributed to the plan on a 50% ( 50 % ) basis .
[text_11] the company also provides a 2% ( 2 % ) profit sharing contribution calculated on eligible earnings for each employee .
[text_12] matching contributions relating to edwards lifesciences employees were $ 17.3 million , $ 15.3 million , and $ 12.8 million in 2016 , 2015 , and 2014 , respectively .
[text_13] the company also has nonqualified deferred compensation plans for a select group of employees .
[text_14] the plans provide eligible participants the opportunity to defer eligible compensation to future dates specified by the participant with a return based on investment alternatives selected by the participant .
[text_15] the amount accrued under these nonqualified plans was $ 46.7 million and $ 35.5 million at december 31 , 2016 and 2015 , respectively .
[text_16] 13 .
[text_17] common stock treasury stock in july 2014 , the board of directors approved a stock repurchase program authorizing the company to purchase up to $ 750.0 million of the company 2019s common stock .
[text_18] in november 2016 , the board of directors approved a new stock repurchase program providing for an additional $ 1.0 billion of repurchases of our common stock .
[text_19] the repurchase programs do not have an expiration date .
[text_20] stock repurchased under these programs may be used to offset obligations under the company 2019s employee stock-based benefit programs and stock-based business acquisitions , and will reduce the total shares outstanding .
[text_21] during 2016 , 2015 , and 2014 , the company repurchased 7.3 million , 2.6 million , and 4.4 million shares , respectively , at an aggregate cost of $ 662.3 million , $ 280.1 million , and $ 300.9 million , respectively , including .
[table_0] 2017 | $ 4.5
[table_1] 2017: 2018 | $ 4.5: 4.0
[table_2] 2017: 2019 | $ 4.5: 4.0
[table_3] 2017: 2020 | $ 4.5: 4.6
[table_4] 2017: 2021 | $ 4.5: 4.5
[table_5] 2017: 2021-2025 | $ 4.5: 44.6

Question: what is the percent change of benefits expected to be paid between 2017 and 2018?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"4.0"},{"source":"table_2","value":"4.5"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"4.5"}]}],"answer":-0.1111111111111111}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"4.0"},{"source":"table_2","value":"4.5"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"4.5"}]}],"answer":1.8888888888888888}
```

## IQV/2016/page_65.pdf-1

Evidence:
[text_0] 2015 compared to 2014 when compared to 2014 , costs of revenue in 2015 increased $ 41 million .
[text_1] this increase included a constant currency increase in expenses of approximately $ 238 million , or 8.9% ( 8.9 % ) , partially offset by a positive impact of approximately $ 197 million from the effects of foreign currency fluctuations .
[text_2] the constant currency growth was comprised of a $ 71 million increase in commercial solutions , which included the impact from the encore acquisition which closed in july 2014 , a $ 146 million increase in research & development solutions , which included the incremental impact from the businesses that quest contributed to q2 solutions , and a $ 21 million increase in integrated engagement services .
[text_3] the decrease in costs of revenue as a percent of revenues for 2015 was primarily as a result of an improvement in constant currency profit margin in the commercial solutions , research & development solutions and integrated engagement services segments ( as more fully described in the segment discussion later in this section ) .
[text_4] for 2015 , this constant currency profit margin expansion was partially offset by the effect from a higher proportion of consolidated revenues being contributed by our lower margin integrated engagement services segment when compared to 2014 as well as a negative impact from foreign currency fluctuations .
[text_5] selling , general and administrative expenses , exclusive of depreciation and amortization .
[text_6] 2016 compared to 2015 the $ 196 million increase in selling , general and administrative expenses in 2016 included a constant currency increase of $ 215 million , or 26.4% ( 26.4 % ) , partially offset by a positive impact of approximately $ 19 million from the effects of foreign currency fluctuations .
[text_7] the constant currency growth was comprised of a $ 151 million increase in commercial solutions , which includes $ 158 million from the merger with ims health , partially offset by a decline in the legacy service offerings , a $ 32 million increase in research & development solutions , which includes the incremental impact from the businesses that quest contributed to q2 solutions , a $ 3 million increase in integrated engagement services , and a $ 29 million increase in general corporate and unallocated expenses , which includes $ 37 million from the merger with ims health .
[text_8] the constant currency increase in general corporate and unallocated expenses in 2016 was primarily due to higher stock-based compensation expense .
[text_9] 2015 compared to 2014 the $ 34 million increase in selling , general and administrative expenses in 2015 included a constant currency increase of $ 74 million , or 9.5% ( 9.5 % ) , partially offset by a positive impact of approximately $ 42 million from the effects of foreign currency fluctuations .
[text_10] the constant currency growth was comprised of a $ 14 million increase in commercial solutions , which included the impact from the encore acquisition which closed in july 2014 , a $ 40 million increase in research & development solutions , which included the incremental impact from the businesses that quest contributed to q2 solutions , a $ 4 million increase in integrated engagement services , and a $ 14 million increase in general corporate and unallocated expenses .
[text_11] the constant currency increase in general corporate and unallocated expenses in 2015 was primarily due to higher stock-based compensation expense and costs associated with the q2 solutions transaction. .
[table_0] ( dollars in millions ) | year ended december 31 , 2016 | year ended december 31 , 2015 | year ended december 31 , 2014
[table_1] ( dollars in millions ): selling general and administrative expenses | year ended december 31 , 2016: $ 1011 | year ended december 31 , 2015: $ 815 | year ended december 31 , 2014: $ 781
[table_2] ( dollars in millions ): % (  % ) of revenues | year ended december 31 , 2016: 18.8% ( 18.8 % ) | year ended december 31 , 2015: 18.8% ( 18.8 % ) | year ended december 31 , 2014: 18.8% ( 18.8 % )

Question: what was the gross revenues in 2016 based on the percent of the selling general and administrative expenses

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"1011"},{"source":"table_2","value":"18.8%"}]}],"answer":5377.659574468085}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"1011"},{"source":"table_2","value":"18.8%"}]}],"answer":1011.188}
```

## APTV/2013/page_48.pdf-1

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_6","value":"0.25"},{"source":"text_5","value":"0.17"}]},{"op":"multiply","args":["#0","const_4"]}],"answer":0.32}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_6","value":"0.25"},{"source":"text_5","value":"0.17"}]},{"op":"multiply","args":["#0","const_4"]}],"answer":1.68}
```

## HUM/2007/page_96.pdf-2

Evidence:
[text_0] humana inc .
[text_1] notes to consolidated financial statements 2014 ( continued ) the total intrinsic value of stock options exercised during 2007 was $ 133.9 million , compared with $ 133.7 million during 2006 and $ 57.8 million during 2005 .
[text_2] cash received from stock option exercises for the years ended december 31 , 2007 , 2006 , and 2005 totaled $ 62.7 million , $ 49.2 million , and $ 36.4 million , respectively .
[text_3] total compensation expense related to nonvested options not yet recognized was $ 23.6 million at december 31 , 2007 .
[text_4] we expect to recognize this compensation expense over a weighted average period of approximately 1.6 years .
[text_5] restricted stock awards restricted stock awards are granted with a fair value equal to the market price of our common stock on the date of grant .
[text_6] compensation expense is recorded straight-line over the vesting period , generally three years from the date of grant .
[text_7] the weighted average grant date fair value of our restricted stock awards was $ 63.59 , $ 54.36 , and $ 32.81 for the years ended december 31 , 2007 , 2006 , and 2005 , respectively .
[text_8] activity for our restricted stock awards was as follows for the year ended december 31 , 2007 : shares weighted average grant-date fair value .
[text_9] the fair value of shares vested during the years ended december 31 , 2007 , 2006 , and 2005 was $ 3.4 million , $ 2.3 million , and $ 0.6 million , respectively .
[text_10] total compensation expense related to nonvested restricted stock awards not yet recognized was $ 44.7 million at december 31 , 2007 .
[text_11] we expect to recognize this compensation expense over a weighted average period of approximately 1.4 years .
[text_12] there are no other contractual terms covering restricted stock awards once vested. .
[table_0]  | shares | weighted average grant-date fair value
[table_1] : nonvested restricted stock at december 31 2006 | shares: 1107455 | weighted average grant-date fair value: $ 45.86
[table_2] : granted | shares: 852353 | weighted average grant-date fair value: 63.59
[table_3] : vested | shares: -51206 ( 51206 ) | weighted average grant-date fair value: 56.93
[table_4] : forfeited | shares: -63624 ( 63624 ) | weighted average grant-date fair value: 49.65
[table_5] : nonvested restricted stock at december 31 2007 | shares: 1844978 | weighted average grant-date fair value: $ 53.61

Question: considering the years 2005-2007 , what is the average fair value of shares vested , in millions?

Chosen:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_9","value":"3.4"},{"source":"text_9","value":"0.6"}]},{"op":"add","args":["#0",{"source":"text_9","value":"2.3"}]},{"op":"divide","args":["#1","const_3"]}],"answer":2.1}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_9","value":"3.4"},{"source":"text_9","value":"0.6"}]},{"op":"add","args":["#0",{"source":"text_9","value":"2.3"}]},{"op":"divide","args":["#1","const_3"]}],"answer":1.7}
```

## SWKS/2012/page_116.pdf-2

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_6","value":"52380"},{"source":"table_1","value":"32136"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"32136"}]}],"answer":0.6299477221807319}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_6","value":"52380"},{"source":"table_1","value":"32136"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"32136"}]}],"answer":2.6299477221807317}
```

## TSCO/2017/page_73.pdf-1

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"84159"},{"source":"table_5","value":"94417"}]}],"answer":0.8913543111939587}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"84159"},{"source":"table_5","value":"94417"}]}],"answer":178576.0}
```

## AON/2009/page_102.pdf-1

Evidence:
[text_0] 14 .
[text_1] stock compensation plans the following table summarizes stock-based compensation expense recognized in continuing operations in the consolidated statements of income in compensation and benefits ( in millions ) : .
[text_2] during 2009 , the company converted its stock administration system to a new service provider .
[text_3] in connection with this conversion , a reconciliation of the methodologies and estimates utilized was performed , which resulted in a $ 12 million reduction of expense for the year ended december 31 , 2009 .
[text_4] stock awards stock awards , in the form of rsus , are granted to certain employees and consist of both performance-based and service-based rsus .
[text_5] service-based awards generally vest between three and ten years from the date of grant .
[text_6] the fair value of service-based awards is based upon the market price of the underlying common stock at the date of grant .
[text_7] with certain limited exceptions , any break in continuous employment will cause the forfeiture of all unvested awards .
[text_8] compensation expense associated with stock awards is recognized over the service period using the straight-line method .
[text_9] dividend equivalents are paid on certain service-based rsus , based on the initial grant amount .
[text_10] at december 31 , 2009 , 2008 and 2007 , the number of shares available for stock awards is included with options available for grant .
[text_11] performance-based rsus have been granted to certain employees .
[text_12] vesting of these awards is contingent upon meeting various individual , divisional or company-wide performance conditions , including revenue generation or growth in revenue , pretax income or earnings per share over a one- to five-year period .
[text_13] the performance conditions are not considered in the determination of the grant date fair value for these awards .
[text_14] the fair value of performance-based awards is based upon the market price of the underlying common stock at the date of grant .
[text_15] compensation expense is recognized over the performance period , and in certain cases an additional vesting period , based on management 2019s estimate of the number of units expected to vest .
[text_16] compensation expense is adjusted to reflect the actual number of shares paid out at the end of the programs .
[text_17] the payout of shares under these performance-based plans may range from 0-200% ( 0-200 % ) of the number of units granted , based on the plan .
[text_18] dividend equivalents are generally not paid on the performance-based rsus .
[text_19] during 2009 , the company granted approximately 2 million shares in connection with the completion of the 2006 leadership performance plan ( 2018 2018lpp 2019 2019 ) cycle .
[text_20] during 2009 , 2008 and 2007 , the company granted approximately 3.7 million , 4.2 million and 4.3 million restricted shares , respectively , in connection with the company 2019s incentive compensation plans. .
[table_0] years ended december 31 | 2009 | 2008 | 2007
[table_1] years ended december 31: rsus | 2009: $ 124 | 2008: $ 132 | 2007: $ 109
[table_2] years ended december 31: performance plans | 2009: 60 | 2008: 67 | 2007: 54
[table_3] years ended december 31: stock options | 2009: 21 | 2008: 24 | 2007: 22
[table_4] years ended december 31: employee stock purchase plans | 2009: 4 | 2008: 3 | 2007: 3
[table_5] years ended december 31: total stock-based compensation expense | 2009: 209 | 2008: 226 | 2007: 188
[table_6] years ended december 31: tax benefit | 2009: 68 | 2008: 82 | 2007: 64
[table_7] years ended december 31: stock-based compensation expense net of tax | 2009: $ 141 | 2008: $ 144 | 2007: $ 124

Question: what was the change in the stock compensation plans rsu in millions from 2007 to 2008

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"132"},{"source":"table_1","value":"109"}]}],"answer":23.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"132"},{"source":"table_1","value":"109"}]}],"answer":241.0}
```

## SLB/2009/page_65.pdf-3

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_11","value":"210"},{"source":"text_11","value":"178"}]},{"op":"divide","args":["#0",{"source":"text_11","value":"178"}]}],"answer":0.1797752808988764}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_11","value":"210"},{"source":"text_11","value":"178"}]},{"op":"divide","args":["#0",{"source":"text_11","value":"178"}]}],"answer":2.1797752808988764}
```

## ETR/2011/page_250.pdf-2

Evidence:
[text_0] part i item 1 entergy corporation , utility operating companies , and system energy asbestos litigation ( entergy arkansas , entergy gulf states louisiana , entergy louisiana , entergy mississippi , entergy new orleans , and entergy texas ) numerous lawsuits have been filed in federal and state courts primarily in texas and louisiana , primarily by contractor employees who worked in the 1940-1980s timeframe , against entergy gulf states louisiana and entergy texas , and to a lesser extent the other utility operating companies , as premises owners of power plants , for damages caused by alleged exposure to asbestos .
[text_1] many other defendants are named in these lawsuits as well .
[text_2] currently , there are approximately 500 lawsuits involving approximately 5000 claimants .
[text_3] management believes that adequate provisions have been established to cover any exposure .
[text_4] additionally , negotiations continue with insurers to recover reimbursements .
[text_5] management believes that loss exposure has been and will continue to be handled so that the ultimate resolution of these matters will not be material , in the aggregate , to the financial position or results of operation of the utility operating companies .
[text_6] employment and labor-related proceedings ( entergy corporation , entergy arkansas , entergy gulf states louisiana , entergy louisiana , entergy mississippi , entergy new orleans , entergy texas , and system energy ) the registrant subsidiaries and other entergy subsidiaries are responding to various lawsuits in both state and federal courts and to other labor-related proceedings filed by current and former employees .
[text_7] generally , the amount of damages being sought is not specified in these proceedings .
[text_8] these actions include , but are not limited to , allegations of wrongful employment actions ; wage disputes and other claims under the fair labor standards act or its state counterparts ; claims of race , gender and disability discrimination ; disputes arising under collective bargaining agreements ; unfair labor practice proceedings and other administrative proceedings before the national labor relations board ; claims of retaliation ; and claims for or regarding benefits under various entergy corporation sponsored plans .
[text_9] entergy and the registrant subsidiaries are responding to these suits and proceedings and deny liability to the claimants .
[text_10] employees employees are an integral part of entergy 2019s commitment to serving customers .
[text_11] as of december 31 , 2011 , entergy subsidiaries employed 14682 people .
[text_12] utility: .
[text_13] approximately 5300 employees are represented by the international brotherhood of electrical workers , the utility workers union of america , the international brotherhood of teamsters , the united government security officers of america , and the international union , security , police , fire professionals of america. .
[table_0] entergy arkansas | 1357
[table_1] entergy arkansas: entergy gulf states louisiana | 1357: 805
[table_2] entergy arkansas: entergy louisiana | 1357: 937
[table_3] entergy arkansas: entergy mississippi | 1357: 736
[table_4] entergy arkansas: entergy new orleans | 1357: 342
[table_5] entergy arkansas: entergy texas | 1357: 674
[table_6] entergy arkansas: system energy | 1357: -
[table_7] entergy arkansas: entergy operations | 1357: 2867
[table_8] entergy arkansas: entergy services | 1357: 3138
[table_9] entergy arkansas: entergy nuclear operations | 1357: 3709
[table_10] entergy arkansas: other subsidiaries | 1357: 117
[table_11] entergy arkansas: total entergy | 1357: 14682

Question: what percentage of total entergy's employees are part of entergy texas?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_5","value":"674"},{"source":"table_11","value":"14682"}]}],"answer":0.04590655224083912}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_5","value":"674"},{"source":"table_11","value":"14682"}]}],"answer":15356.0}
```

## LKQ/2010/page_84.pdf-3

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_3","value":"37660"},{"source":"table_6","value":"310643"}]}],"answer":0.12123241148199058}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_3","value":"37660"},{"source":"table_6","value":"310643"}]}],"answer":348303.0}
```

## SNPS/2012/page_62.pdf-1

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_4","value":"316263"},{"source":"table_5","value":"184300"}]},{"op":"divide","args":["#0",{"source":"table_3","value":"550234"}]}],"answer":0.9097274977555004}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_4","value":"316263"},{"source":"table_5","value":"184300"}]},{"op":"divide","args":["#0",{"source":"table_3","value":"550234"}]}],"answer":0.23983069021543563}
```

## RE/2014/page_125.pdf-2

Evidence:
[text_0] 9 .
[text_1] junior subordinated debt securities payable in accordance with the provisions of the junior subordinated debt securities which were issued on march 29 , 2004 , holdings elected to redeem the $ 329897 thousand of 6.2% ( 6.2 % ) junior subordinated debt securities outstanding on may 24 , 2013 .
[text_2] as a result of the early redemption , the company incurred pre-tax expense of $ 7282 thousand related to the immediate amortization of the remaining capitalized issuance costs on the trust preferred securities .
[text_3] interest expense incurred in connection with these junior subordinated debt securities is as follows for the periods indicated: .
[text_4] holdings considered the mechanisms and obligations relating to the trust preferred securities , taken together , constituted a full and unconditional guarantee by holdings of capital trust ii 2019s payment obligations with respect to their trust preferred securities .
[text_5] 10 .
[text_6] reinsurance and trust agreements certain subsidiaries of group have established trust agreements , which effectively use the company 2019s investments as collateral , as security for assumed losses payable to certain non-affiliated ceding companies .
[text_7] at december 31 , 2014 , the total amount on deposit in trust accounts was $ 322285 thousand .
[text_8] on april 24 , 2014 , the company entered into two collateralized reinsurance agreements with kilimanjaro re limited ( 201ckilimanjaro 201d ) , a bermuda based special purpose reinsurer , to provide the company with catastrophe reinsurance coverage .
[text_9] these agreements are multi-year reinsurance contracts which cover specified named storm and earthquake events .
[text_10] the first agreement provides up to $ 250000 thousand of reinsurance coverage from named storms in specified states of the southeastern united states .
[text_11] the second agreement provides up to $ 200000 thousand of reinsurance coverage from named storms in specified states of the southeast , mid-atlantic and northeast regions of the united states and puerto rico as well as reinsurance coverage from earthquakes in specified states of the southeast , mid-atlantic , northeast and west regions of the united states , puerto rico and british columbia .
[text_12] on november 18 , 2014 , the company entered into a collateralized reinsurance agreement with kilimanjaro re to provide the company with catastrophe reinsurance coverage .
[text_13] this agreement is a multi-year reinsurance contract which covers specified earthquake events .
[text_14] the agreement provides up to $ 500000 thousand of reinsurance coverage from earthquakes in the united states , puerto rico and canada .
[text_15] kilimanjaro has financed the various property catastrophe reinsurance coverage by issuing catastrophe bonds to unrelated , external investors .
[text_16] on april 24 , 2014 , kilimanjaro issued $ 450000 thousand of variable rate notes ( 201cseries 2014-1 notes 201d ) .
[text_17] on november 18 , 2014 , kilimanjaro issued $ 500000 thousand of variable rate notes ( 201cseries 2014-2 notes 201d ) .
[text_18] the proceeds from the issuance of the series 2014-1 notes and the series 2014-2 notes are held in reinsurance trust throughout the duration of the applicable reinsurance agreements and invested solely in us government money market funds with a rating of at least 201caaam 201d by standard & poor 2019s. .
[table_0] ( dollars in thousands ) | years ended december 31 , 2014 | years ended december 31 , 2013 | years ended december 31 , 2012
[table_1] ( dollars in thousands ): interest expense incurred | years ended december 31 , 2014: $ - | years ended december 31 , 2013: $ 8181 | years ended december 31 , 2012: $ 20454

Question: what was the total reinsurance coverage secured in 2014 in thousands

Chosen:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_11","value":"200000"},{"source":"text_10","value":"250000"}]}],"answer":450000.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_11","value":"200000"},{"source":"text_10","value":"250000"}]}],"answer":-50000.0}
```

## JKHY/2019/page_17.pdf-1

Evidence:
[text_0] j a c k h e n r y .
[text_1] c o m 1 5 market for registrant 2019s common equity , related stockholder matters and issuer purchases of equity securities the company 2019s common stock is quoted on the nasdaq global select market ( 201cnasdaq 201d ) under the symbol 201cjkhy 201d .
[text_2] the company established a practice of paying quarterly dividends at the end of fiscal 1990 and has paid dividends with respect to every quarter since that time .
[text_3] the declaration and payment of any future dividends will continue to be at the discretion of our board of directors and will depend upon , among other factors , our earnings , capital requirements , contractual restrictions , and operating and financial condition .
[text_4] the company does not currently foresee any changes in its dividend practices .
[text_5] on august 15 , 2019 , there were approximately 145300 holders of the company 2019s common stock , including individual participants in security position listings .
[text_6] on that same date the last sale price of the common shares as reported on nasdaq was $ 141.94 per share .
[text_7] issuer purchases of equity securities the following shares of the company were repurchased during the quarter ended june 30 , 2019 : total number of shares purchased ( 1 ) average price of total number of shares purchased as part of publicly announced plans ( 1 ) maximum number of shares that may yet be purchased under the plans ( 2 ) .
[text_8] ( 1 ) 250000 shares were purchased through a publicly announced repurchase plan .
[text_9] there were no shares surrendered to the company to satisfy tax withholding obligations in connection with employee restricted stock awards .
[text_10] ( 2 ) total stock repurchase authorizations approved by the company 2019s board of directors as of february 17 , 2015 were for 30.0 million shares .
[text_11] these authorizations have no specific dollar or share price targets and no expiration dates. .
[table_0]  | total number of shares purchased ( 1 ) | average price of share | total number of shares purchased as part of publicly announced plans ( 1 ) | maximum number of shares that may yet be purchased under the plans ( 2 )
[table_1] : april 1- april 30 2019 | total number of shares purchased ( 1 ): 2014 | average price of share: $ 2014 | total number of shares purchased as part of publicly announced plans ( 1 ): 2014 | maximum number of shares that may yet be purchased under the plans ( 2 ): 3732713
[table_2] : may 1- may 31 2019 | total number of shares purchased ( 1 ): 250000 | average price of share: $ 134.35 | total number of shares purchased as part of publicly announced plans ( 1 ): 250000 | maximum number of shares that may yet be purchased under the plans ( 2 ): 3482713
[table_3] : june 1- june 30 2019 | total number of shares purchased ( 1 ): 2014 | average price of share: $ 2014 | total number of shares purchased as part of publicly announced plans ( 1 ): 2014 | maximum number of shares that may yet be purchased under the plans ( 2 ): 3482713
[table_4] : total | total number of shares purchased ( 1 ): 250000 | average price of share: $ 134.35 | total number of shares purchased as part of publicly announced plans ( 1 ): 250000 | maximum number of shares that may yet be purchased under the plans ( 2 ): 3482713

Question: what was the company market capitalization on august 15 , 2019,

Chosen:
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"text_5","value":"145300"},{"source":"text_6","value":"141.94"}]}],"answer":20623882.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_5","value":"145300"},{"source":"text_6","value":"141.94"}]}],"answer":145441.94}
```

## ETR/2008/page_187.pdf-3

Evidence:
[text_0] entergy corporation and subsidiaries notes to financial statements ouachita in september 2008 , entergy arkansas purchased the ouachita plant , a 789 mw three-train gas-fired combined cycle generating turbine ( ccgt ) electric power plant located 20 miles south of the arkansas state line near sterlington , louisiana , for approximately $ 210 million from a subsidiary of cogentrix energy , inc .
[text_1] entergy arkansas received the plant , materials and supplies , and related real estate in the transaction .
[text_2] the ferc and the apsc approved the acquisition .
[text_3] the apsc also approved the recovery of the acquisition and ownership costs through a rate rider and the planned sale of one-third of the capacity and energy to entergy gulf states louisiana .
[text_4] the lpsc also approved the purchase of one-third of the capacity and energy by entergy gulf states louisiana , subject to certain conditions , including a study to determine the costs and benefits of entergy gulf states louisiana exercising an option to purchase one-third of the plant ( unit 3 ) from entergy arkansas .
[text_5] entergy gulf states louisiana is scheduled to report the results of that study by march 30 , 2009 .
[text_6] palisades in april 2007 , entergy's non-utility nuclear business purchased the 798 mw palisades nuclear energy plant located near south haven , michigan from consumers energy company for a net cash payment of $ 336 million .
[text_7] entergy received the plant , nuclear fuel , inventories , and other assets .
[text_8] the liability to decommission the plant , as well as related decommissioning trust funds , was also transferred to entergy's non-utility nuclear business .
[text_9] entergy's non-utility nuclear business executed a unit-contingent , 15-year purchased power agreement ( ppa ) with consumers energy for 100% ( 100 % ) of the plant's output , excluding any future uprates .
[text_10] prices under the ppa range from $ 43.50/mwh in 2007 to $ 61.50/mwh in 2022 , and the average price under the ppa is $ 51/mwh .
[text_11] in the first quarter 2007 , the nrc renewed palisades' operating license until 2031 .
[text_12] as part of the transaction , entergy's non- utility nuclear business assumed responsibility for spent fuel at the decommissioned big rock point nuclear plant , which is located near charlevoix , michigan .
[text_13] palisades' financial results since april 2007 are included in entergy's non-utility nuclear business segment .
[text_14] the following table summarizes the assets acquired and liabilities assumed at the date of acquisition .
[text_15] amount ( in millions ) .
[text_16] subsequent to the closing , entergy received approximately $ 6 million from consumers energy company as part of the post-closing adjustment defined in the asset sale agreement .
[text_17] the post-closing adjustment amount resulted in an approximately $ 6 million reduction in plant and a corresponding reduction in other liabilities .
[text_18] for the ppa , which was at below-market prices at the time of the acquisition , non-utility nuclear will amortize a liability to revenue over the life of the agreement .
[text_19] the amount that will be amortized each period is based upon the difference between the present value calculated at the date of acquisition of each year's difference between revenue under the agreement and revenue based on estimated market prices .
[text_20] amounts amortized to revenue were $ 76 .
[table_0]  | amount ( in millions )
[table_1] : plant ( including nuclear fuel ) | amount ( in millions ): $ 727
[table_2] : decommissioning trust funds | amount ( in millions ): 252
[table_3] : other assets | amount ( in millions ): 41
[table_4] : total assets acquired | amount ( in millions ): 1020
[table_5] : purchased power agreement ( below market ) | amount ( in millions ): 420
[table_6] : decommissioning liability | amount ( in millions ): 220
[table_7] : other liabilities | amount ( in millions ): 44
[table_8] : total liabilities assumed | amount ( in millions ): 684
[table_9] : net assets acquired | amount ( in millions ): $ 336

Question: what portion of the total acquired asset is composed of decommissioning trust funds?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"252"},{"source":"table_4","value":"1020"}]}],"answer":0.24705882352941178}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"252"},{"source":"table_4","value":"1020"}]}],"answer":1272.0}
```

## SLB/2009/page_65.pdf-4

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

Question: what was vessels under construction as a percentage of total purchase price?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_3","value":"694"},{"source":"table_6","value":"838"}]}],"answer":0.8281622911694511}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_3","value":"694"},{"source":"table_6","value":"838"}]}],"answer":1532.0}
```

## PKG/2009/page_63.pdf-4

Evidence:
[text_0] there were no changes in the company 2019s valuation techniques used to measure fair values on a recurring basis as a result of adopting asc 820 .
[text_1] pca had no assets or liabilities that were measured on a nonrecurring basis .
[text_2] 11 .
[text_3] stockholders 2019 equity on october 17 , 2007 , pca announced that its board of directors authorized a $ 150.0 million common stock repurchase program .
[text_4] there is no expiration date for the common stock repurchase program .
[text_5] through december 31 , 2008 , the company repurchased 3818729 shares of common stock , with 3142600 shares repurchased during 2008 and 676129 shares repurchased during 2007 .
[text_6] all repurchased shares were retired prior to december 31 , 2008 .
[text_7] there were no shares repurchased in 2009 .
[text_8] as of december 31 , 2009 , $ 65.0 million of the $ 150.0 million authorization remained available for repurchase of the company 2019s common stock .
[text_9] 12 .
[text_10] commitments and contingencies capital commitments the company had authorized capital commitments of approximately $ 41.7 million and $ 43.0 million as of december 31 , 2009 and 2008 , respectively , in connection with the expansion and replacement of existing facilities and equipment .
[text_11] in addition , commitments at december 31 , 2009 for the major energy optimization projects at its counce and valdosta mills totaled $ 156.3 million .
[text_12] lease obligations pca leases space for certain of its facilities and cutting rights to approximately 91000 acres of timberland under long-term leases .
[text_13] the company also leases equipment , primarily vehicles and rolling stock , and other assets under long-term leases with a duration of two to seven years .
[text_14] the minimum lease payments under non-cancelable operating leases with lease terms in excess of one year are as follows: .
[text_15] total lease expense , including base rent on all leases and executory costs , such as insurance , taxes , and maintenance , for the years ended december 31 , 2009 , 2008 and 2007 was $ 41.3 million , $ 41.6 million and $ 39.8 million , respectively .
[text_16] these costs are included in cost of goods sold and selling and administrative expenses .
[text_17] pca was obligated under capital leases covering buildings and machinery and equipment in the amount of $ 23.1 million and $ 23.7 million at december 31 , 2009 and 2008 , respectively .
[text_18] during the fourth quarter of 2008 , the company entered into a capital lease relating to buildings and machinery , totaling $ 23.9 million , payable over 20 years .
[text_19] this capital lease amount is a non-cash transaction and , accordingly , has been excluded packaging corporation of america notes to consolidated financial statements ( continued ) december 31 , 2009 .
[table_0]  | ( in thousands )
[table_1] : 2010 | ( in thousands ): $ 28162
[table_2] : 2011 | ( in thousands ): 25181
[table_3] : 2012 | ( in thousands ): 17338
[table_4] : 2013 | ( in thousands ): 11557
[table_5] : 2014 | ( in thousands ): 7742
[table_6] : thereafter | ( in thousands ): 18072
[table_7] : total | ( in thousands ): $ 108052

Question: as of december 31 , 2009 , what percentage of the $ 150.0 million authorization remained available for repurchase of the company 2019s common stock?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_8","value":"65.0"},{"source":"text_3","value":"150.0"}]}],"answer":0.43333333333333335}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_8","value":"65.0"},{"source":"text_3","value":"150.0"}]}],"answer":215.0}
```

## AAPL/2015/page_24.pdf-3

Evidence:
[text_0] table of contents company stock performance the following graph shows a comparison of cumulative total shareholder return , calculated on a dividend reinvested basis , for the company , the s&p 500 index , the s&p information technology index and the dow jones u.s .
[text_1] technology supersector index for the five years ended september 26 , 2015 .
[text_2] the graph assumes $ 100 was invested in each of the company 2019s common stock , the s&p 500 index , the s&p information technology index and the dow jones u.s .
[text_3] technology supersector index as of the market close on september 24 , 2010 .
[text_4] note that historic stock price performance is not necessarily indicative of future stock price performance .
[text_5] * $ 100 invested on 9/25/10 in stock or index , including reinvestment of dividends .
[text_6] data points are the last day of each fiscal year for the company 2019scommon stock and september 30th for indexes .
[text_7] copyright a9 2015 s&p , a division of mcgraw hill financial .
[text_8] all rights reserved .
[text_9] copyright a9 2015 dow jones & co .
[text_10] all rights reserved .
[text_11] september september september september september september .
[text_12] apple inc .
[text_13] | 2015 form 10-k | 21 .
[table_0]  | september 2010 | september 2011 | september 2012 | september 2013 | september 2014 | september 2015
[table_1] : apple inc . | september 2010: $ 100 | september 2011: $ 138 | september 2012: $ 229 | september 2013: $ 170 | september 2014: $ 254 | september 2015: $ 294
[table_2] : s&p 500 index | september 2010: $ 100 | september 2011: $ 101 | september 2012: $ 132 | september 2013: $ 157 | september 2014: $ 188 | september 2015: $ 187
[table_3] : s&p information technology index | september 2010: $ 100 | september 2011: $ 104 | september 2012: $ 137 | september 2013: $ 147 | september 2014: $ 190 | september 2015: $ 194
[table_4] : dow jones u.s . technology supersector index | september 2010: $ 100 | september 2011: $ 103 | september 2012: $ 134 | september 2013: $ 141 | september 2014: $ 183 | september 2015: $ 183

Question: what was the percentage cumulative total shareholder return for the four years ended 2014?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"254"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100"}]}],"answer":1.54}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"254"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100"}]}],"answer":3.54}
```

## WELL/2016/page_61.pdf-3

Evidence:
[text_0] item 7 .
[text_1] management 2019s discussion and analysis of financial condition and results of operations the following discussion and analysis is based primarily on the consolidated financial statements of welltower inc .
[text_2] for the periods presented and should be read together with the notes thereto contained in this annual report on form 10-k .
[text_3] other important factors are identified in 201citem 1 2014 business 201d and 201citem 1a 2014 risk factors 201d above .
[text_4] executive summary company overview welltower inc .
[text_5] ( nyse : hcn ) , an s&p 500 company headquartered in toledo , ohio , is driving the transformation of health care infrastructure .
[text_6] the company invests with leading seniors housing operators , post- acute providers and health systems to fund the real estate and infrastructure needed to scale innovative care delivery models and improve people 2019s wellness and overall health care experience .
[text_7] welltowertm , a real estate investment trust ( 201creit 201d ) , owns interests in properties concentrated in major , high-growth markets in the united states , canada and the united kingdom , consisting of seniors housing and post-acute communities and outpatient medical properties .
[text_8] our capital programs , when combined with comprehensive planning , development and property management services , make us a single-source solution for acquiring , planning , developing , managing , repositioning and monetizing real estate assets .
[text_9] the following table summarizes our consolidated portfolio for the year ended december 31 , 2016 ( dollars in thousands ) : type of property net operating income ( noi ) ( 1 ) percentage of number of properties .
[text_10] ( 1 ) excludes our share of investments in unconsolidated entities and non-segment/corporate noi .
[text_11] entities in which we have a joint venture with a minority partner are shown at 100% ( 100 % ) of the joint venture amount .
[text_12] business strategy our primary objectives are to protect stockholder capital and enhance stockholder value .
[text_13] we seek to pay consistent cash dividends to stockholders and create opportunities to increase dividend payments to stockholders as a result of annual increases in net operating income and portfolio growth .
[text_14] to meet these objectives , we invest across the full spectrum of seniors housing and health care real estate and diversify our investment portfolio by property type , relationship and geographic location .
[text_15] substantially all of our revenues are derived from operating lease rentals , resident fees and services , and interest earned on outstanding loans receivable .
[text_16] these items represent our primary sources of liquidity to fund distributions and depend upon the continued ability of our obligors to make contractual rent and interest payments to us and the profitability of our operating properties .
[text_17] to the extent that our customers/partners experience operating difficulties and become unable to generate sufficient cash to make payments to us , there could be a material adverse impact on our consolidated results of operations , liquidity and/or financial condition .
[text_18] to mitigate this risk , we monitor our investments through a variety of methods determined by the type of property .
[text_19] our proactive and comprehensive asset management process for seniors housing properties generally includes review of monthly financial statements and other operating data for each property , review of obligor/ partner creditworthiness , property inspections , and review of covenant compliance relating to licensure , real estate taxes , letters of credit and other collateral .
[text_20] our internal property management division actively manages and monitors the outpatient medical portfolio with a comprehensive process including review of tenant relations , lease expirations , the mix of health service providers , hospital/health system relationships , property performance .
[table_0] type of property | net operating income ( noi ) ( 1 ) | percentage of noi | number of properties
[table_1] type of property: triple-net | net operating income ( noi ) ( 1 ): $ 1208860 | percentage of noi: 50.3% ( 50.3 % ) | number of properties: 631
[table_2] type of property: seniors housing operating | net operating income ( noi ) ( 1 ): 814114 | percentage of noi: 33.9% ( 33.9 % ) | number of properties: 420
[table_3] type of property: outpatient medical | net operating income ( noi ) ( 1 ): 380264 | percentage of noi: 15.8% ( 15.8 % ) | number of properties: 262
[table_4] type of property: totals | net operating income ( noi ) ( 1 ): $ 2403238 | percentage of noi: 100.0% ( 100.0 % ) | number of properties: 1313

Question: what was net operating income in millions attributable to triple-net and seniors housing?

Chosen:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"1208860"},{"source":"table_2","value":"814114"}]}],"answer":2022974.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"1208860"},{"source":"table_2","value":"814114"}]}],"answer":394746.0}
```

## ETR/2011/page_281.pdf-2

Evidence:
[text_0] entergy arkansas , inc .
[text_1] and subsidiaries management 2019s financial discussion and analysis entergy arkansas 2019s receivables from the money pool were as follows as of december 31 for each of the following years: .
[text_2] in april 2011 , entergy arkansas entered into a new $ 78 million credit facility that expires in april 2012 .
[text_3] there were no outstanding borrowings under the entergy arkansas credit facility as of december 31 , 2011 .
[text_4] entergy arkansas has obtained short-term borrowing authorization from the ferc under which it may borrow through october 2013 , up to the aggregate amount , at any one time outstanding , of $ 250 million .
[text_5] see note 4 to the financial statements for further discussion of entergy arkansas 2019s short-term borrowing limits .
[text_6] entergy arkansas has also obtained an order from the apsc authorizing long-term securities issuances through december state and local rate regulation and fuel-cost recovery retail rates 2009 base rate filing in september 2009 , entergy arkansas filed with the apsc for a general change in rates , charges , and tariffs .
[text_7] in june 2010 the apsc approved a settlement and subsequent compliance tariffs that provide for a $ 63.7 million rate increase , effective for bills rendered for the first billing cycle of july 2010 .
[text_8] the settlement provides for a 10.2% ( 10.2 % ) return on common equity .
[text_9] production cost allocation rider the apsc approved a production cost allocation rider for recovery from customers of the retail portion of the costs allocated to entergy arkansas as a result of the system agreement proceedings .
[text_10] these costs cause an increase in entergy arkansas 2019s deferred fuel cost balance , because entergy arkansas pays the costs over seven months but collects them from customers over twelve months .
[text_11] see note 2 to the financial statements and entergy corporation and subsidiaries 201cmanagement 2019s financial discussion and analysis - system agreement 201d for discussions of the system agreement proceedings .
[text_12] energy cost recovery rider entergy arkansas 2019s retail rates include an energy cost recovery rider to recover fuel and purchased energy costs in monthly bills .
[text_13] the rider utilizes prior calendar year energy costs and projected energy sales for the twelve- month period commencing on april 1 of each year to develop an energy cost rate , which is redetermined annually and includes a true-up adjustment reflecting the over-recovery or under-recovery , including carrying charges , of the energy cost for the prior calendar year .
[text_14] the energy cost recovery rider tariff also allows an interim rate request depending upon the level of over- or under-recovery of fuel and purchased energy costs .
[text_15] in early october 2005 , the apsc initiated an investigation into entergy arkansas's interim energy cost recovery rate .
[text_16] the investigation focused on entergy arkansas's 1 ) gas contracting , portfolio , and hedging practices ; 2 ) wholesale purchases during the period ; 3 ) management of the coal inventory at its coal generation plants ; and 4 ) response to the contractual failure of the railroads to provide coal deliveries .
[text_17] in march 2006 , the apsc extended its investigation to cover the costs included in entergy arkansas's march 2006 annual energy cost rate filing , and a hearing was held in the apsc energy cost recovery investigation in october 2006. .
[table_0] 2011 | 2010 | 2009 | 2008
[table_1] 2011: ( in thousands ) | 2010: ( in thousands ) | 2009: ( in thousands ) | 2008: ( in thousands )
[table_2] 2011: $ 17362 | 2010: $ 41463 | 2009: $ 28859 | 2008: $ 15991

Question: what was the percent of the new entergy arkansas credit facility to the accounts receivables in 2011

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"text_2","value":"78"},{"source":"table_2","value":"17362"}]}],"answer":0.004492569980417003}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_2","value":"78"},{"source":"table_2","value":"17362"}]}],"answer":17440.0}
```

## GPN/2017/page_77.pdf-3

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

Question: what are the total amount of net tangible assets obtained through the acquisition?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_9","value":"265982"},{"source":"table_8","value":"203828"}]}],"answer":62154.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_9","value":"265982"},{"source":"table_8","value":"203828"}]}],"answer":469810.0}
```

## ADBE/2008/page_74.pdf-1

Evidence:
[text_0] our intangible assets are amortized over their estimated useful lives of 1 to 13 years as shown in the table below .
[text_1] amortization is based on the pattern in which the economic benefits of the intangible asset will be consumed .
[text_2] weighted average useful life ( years ) .
[text_3] software development costs capitalization of software development costs for software to be sold , leased , or otherwise marketed begins upon the establishment of technological feasibility , which is generally the completion of a working prototype that has been certified as having no critical bugs and is a release candidate .
[text_4] amortization begins once the software is ready for its intended use , generally based on the pattern in which the economic benefits will be consumed .
[text_5] to date , software development costs incurred between completion of a working prototype and general availability of the related product have not been material .
[text_6] revenue recognition our revenue is derived from the licensing of software products , consulting and maintenance and support .
[text_7] primarily , we recognize revenue pursuant to the requirements of aicpa statement of position 97-2 , 201csoftware revenue recognition 201d and any applicable amendments , when persuasive evidence of an arrangement exists , we have delivered the product or performed the service , the fee is fixed or determinable and collection is probable .
[text_8] multiple element arrangements we enter into multiple element revenue arrangements in which a customer may purchase a combination of software , upgrades , maintenance and support , and consulting ( multiple-element arrangements ) .
[text_9] when vsoe of fair value does not exist for all delivered elements , we allocate and defer revenue for the undelivered items based on vsoe of fair value of the undelivered elements and recognize the difference between the total arrangement fee and the amount deferred for the undelivered items as license revenue .
[text_10] vsoe of fair value for each element is based on the price for which the element is sold separately .
[text_11] we determine the vsoe of fair value of each element based on historical evidence of our stand-alone sales of these elements to third parties or from the stated renewal rate for the elements contained in the initial software license arrangement .
[text_12] when vsoe of fair value does not exist for any undelivered element , revenue is deferred until the earlier of the point at which such vsoe of fair value exists or until all elements of the arrangement have been delivered .
[text_13] the only exception to this guidance is when the only undelivered element is maintenance and support or other services , then the entire arrangement fee is recognized ratably over the performance period .
[text_14] product revenue we recognize our product revenue upon shipment , provided all other revenue recognition criteria have been met .
[text_15] our desktop application products 2019 revenue from distributors is subject to agreements allowing limited rights of return , rebates and price protection .
[text_16] our direct sales and oem sales are also subject to limited rights of return .
[text_17] accordingly , we reduce revenue recognized for estimated future returns , price protection and rebates at the time the related revenue is recorded .
[text_18] the estimates for returns are adjusted periodically based upon historical rates of returns , inventory levels in the distribution channel and other related factors .
[text_19] we record the estimated costs of providing free technical phone support to customers for our software products .
[text_20] we recognize oem licensing revenue , primarily royalties , when oem partners ship products incorporating our software , provided collection of such revenue is deemed probable .
[text_21] for certain oem customers , we must estimate royalty .
[table_0]  | weighted average useful life ( years )
[table_1] : purchased technology | weighted average useful life ( years ): 4
[table_2] : localization | weighted average useful life ( years ): 1
[table_3] : trademarks | weighted average useful life ( years ): 5
[table_4] : customer contracts and relationships | weighted average useful life ( years ): 6
[table_5] : other intangibles | weighted average useful life ( years ): 3

Question: what is the yearly amortization rate for the purchased technology?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":["const_100",{"source":"table_1","value":"4"}]}],"answer":25.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":["const_100",{"source":"table_1","value":"4"}]}],"answer":104.0}
```

## UPS/2014/page_35.pdf-2

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"136.26"},{"source":"table_2","value":"115.06"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"115.06"}]}],"answer":0.18425169476794717}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"136.26"},{"source":"table_2","value":"115.06"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"115.06"}]}],"answer":2.1842516947679473}
```

## AES/2002/page_128.pdf-3

Evidence:
[text_0] the contracts were valued as of april 1 , 2002 , and an asset and a corresponding gain of $ 127 million , net of income taxes , was recorded as a cumulative effect of a change in accounting principle in the second quarter of 2002 .
[text_1] the majority of the gain recorded relates to the warrior run contract , as the asset value of the deepwater contract on april 1 , 2002 , was less than $ 1 million .
[text_2] the warrior run contract qualifies and was designated as a cash flow hedge as defined by sfas no .
[text_3] 133 and hedge accounting is applied for this contract subsequent to april 1 , 2002 .
[text_4] the contract valuations were performed using current forward electricity and gas price quotes and current market data for other contract variables .
[text_5] the forward curves used to value the contracts include certain assumptions , including projections of future electricity and gas prices in periods where future prices are not quoted .
[text_6] fluctuations in market prices and their impact on the assumptions will cause the value of these contracts to change .
[text_7] such fluctuations will increase the volatility of the company 2019s reported results of operations .
[text_8] 11 .
[text_9] commitments , contingencies and risks operating leases 2014as of december 31 , 2002 , the company was obligated under long-term non-cancelable operating leases , primarily for office rental and site leases .
[text_10] rental expense for operating leases , excluding amounts related to the sale/leaseback discussed below , was $ 31 million $ 32 million and $ 13 million in the years ended december 31 , 2002 , 2001and 2000 , respectively , including commitments of businesses classified as discontinued amounting to $ 6 million in 2002 , $ 16 million in 2001 and $ 6 million in 2000 .
[text_11] the future minimum lease commitments under these leases are as follows ( in millions ) : discontinued total operations .
[text_12] sale/leaseback 2014in may 1999 , a subsidiary of the company acquired six electric generating stations from new york state electric and gas ( 2018 2018nyseg 2019 2019 ) .
[text_13] concurrently , the subsidiary sold two of the plants to an unrelated third party for $ 666 million and simultaneously entered into a leasing arrangement with the unrelated party .
[text_14] this transaction has been accounted for as a sale/leaseback with operating lease treatment .
[text_15] rental expense was $ 54 million , $ 58 million and $ 54 million in 2002 , 2001 and 2000 , respectively .
[text_16] future minimum lease commitments are as follows ( in millions ) : in connection with the lease of the two power plants , the subsidiary is required to maintain a rent reserve account equal to the maximum semi-annual payment with respect to the sum of the basic rent ( other then deferrable basic rent ) and fixed charges expected to become due in the immediately succeeding three-year period .
[text_17] at december 31 , 2002 , 2001 and 2000 , the amount deposited in the rent reserve account approximated .
[table_0]  | total | discontinued operations
[table_1] : 2003 | total: $ 30 | discontinued operations: $ 4
[table_2] : 2004 | total: 20 | discontinued operations: 4
[table_3] : 2005 | total: 15 | discontinued operations: 3
[table_4] : 2006 | total: 11 | discontinued operations: 1
[table_5] : 2007 | total: 9 | discontinued operations: 1
[table_6] : thereafter | total: 84 | discontinued operations: 1
[table_7] : total | total: $ 169 | discontinued operations: $ 14

Question: what percentage of total future minimum lease commitments is due in 2003?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"30"},{"source":"table_7","value":"169"}]}],"answer":0.17751479289940827}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"30"},{"source":"table_7","value":"169"}]}],"answer":199.0}
```

## GS/2012/page_83.pdf-2

Evidence:
[text_0] management 2019s discussion and analysis liquidity risk management liquidity is of critical importance to financial institutions .
[text_1] most of the recent failures of financial institutions have occurred in large part due to insufficient liquidity .
[text_2] accordingly , the firm has in place a comprehensive and conservative set of liquidity and funding policies to address both firm-specific and broader industry or market liquidity events .
[text_3] our principal objective is to be able to fund the firm and to enable our core businesses to continue to serve clients and generate revenues , even under adverse circumstances .
[text_4] we manage liquidity risk according to the following principles : excess liquidity .
[text_5] we maintain substantial excess liquidity to meet a broad range of potential cash outflows and collateral needs in a stressed environment .
[text_6] asset-liability management .
[text_7] we assess anticipated holding periods for our assets and their expected liquidity in a stressed environment .
[text_8] we manage the maturities and diversity of our funding across markets , products and counterparties , and seek to maintain liabilities of appropriate tenor relative to our asset base .
[text_9] contingency funding plan .
[text_10] we maintain a contingency funding plan to provide a framework for analyzing and responding to a liquidity crisis situation or periods of market stress .
[text_11] this framework sets forth the plan of action to fund normal business activity in emergency and stress situations .
[text_12] these principles are discussed in more detail below .
[text_13] excess liquidity our most important liquidity policy is to pre-fund our estimated potential cash and collateral needs during a liquidity crisis and hold this excess liquidity in the form of unencumbered , highly liquid securities and cash .
[text_14] we believe that the securities held in our global core excess would be readily convertible to cash in a matter of days , through liquidation , by entering into repurchase agreements or from maturities of reverse repurchase agreements , and that this cash would allow us to meet immediate obligations without needing to sell other assets or depend on additional funding from credit-sensitive markets .
[text_15] as of december 2012 and december 2011 , the fair value of the securities and certain overnight cash deposits included in our gce totaled $ 174.62 billion and $ 171.58 billion , respectively .
[text_16] based on the results of our internal liquidity risk model , discussed below , as well as our consideration of other factors including , but not limited to , a qualitative assessment of the condition of the financial markets and the firm , we believe our liquidity position as of december 2012 was appropriate .
[text_17] the table below presents the fair value of the securities and certain overnight cash deposits that are included in our gce .
[text_18] average for the year ended december in millions 2012 2011 .
[text_19] the u.s .
[text_20] dollar-denominated excess is composed of ( i ) unencumbered u.s .
[text_21] government and federal agency obligations ( including highly liquid u.s .
[text_22] federal agency mortgage-backed obligations ) , all of which are eligible as collateral in federal reserve open market operations and ( ii ) certain overnight u.s .
[text_23] dollar cash deposits .
[text_24] the non-u.s .
[text_25] dollar-denominated excess is composed of only unencumbered german , french , japanese and united kingdom government obligations and certain overnight cash deposits in highly liquid currencies .
[text_26] we strictly limit our excess liquidity to this narrowly defined list of securities and cash because they are highly liquid , even in a difficult funding environment .
[text_27] we do not include other potential sources of excess liquidity , such as less liquid unencumbered securities or committed credit facilities , in our gce .
[text_28] goldman sachs 2012 annual report 81 .
[table_0] in millions | average for theyear ended december 2012 | average for theyear ended december 2011
[table_1] in millions: u.s . dollar-denominated | average for theyear ended december 2012: $ 125111 | average for theyear ended december 2011: $ 125668
[table_2] in millions: non-u.s . dollar-denominated | average for theyear ended december 2012: 46984 | average for theyear ended december 2011: 40291
[table_3] in millions: total | average for theyear ended december 2012: $ 172095 | average for theyear ended december 2011: $ 165959

Question: what percentage of gce in 2011 is in non-u.s . dollar-denominated assets?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"40291"},{"source":"table_3","value":"165959"}]}],"answer":0.24277683042197168}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"40291"},{"source":"table_3","value":"165959"}]}],"answer":206250.0}
```

## AWK/2017/page_172.pdf-2

Evidence:
[text_0] deposits 2014deposits include escrow funds and certain other deposits held in trust .
[text_1] the company includes cash deposits in other current assets .
[text_2] deferred compensation obligations 2014the company 2019s deferred compensation plans allow participants to defer certain cash compensation into notional investment accounts .
[text_3] the company includes such plans in other long-term liabilities .
[text_4] the value of the company 2019s deferred compensation obligations is based on the market value of the participants 2019 notional investment accounts .
[text_5] the notional investments are comprised primarily of mutual funds , which are based on observable market prices .
[text_6] mark-to-market derivative asset and liability 2014the company utilizes fixed-to-floating interest-rate swaps , typically designated as fair-value hedges , to achieve a targeted level of variable-rate debt as a percentage of total debt .
[text_7] the company also employs derivative financial instruments in the form of variable-to-fixed interest rate swaps and forward starting interest rate swaps , classified as economic hedges and cash flow hedges , respectively , in order to fix the interest cost on existing or forecasted debt .
[text_8] the company uses a calculation of future cash inflows and estimated future outflows , which are discounted , to determine the current fair value .
[text_9] additional inputs to the present value calculation include the contract terms , counterparty credit risk , interest rates and market volatility .
[text_10] other investments 2014other investments primarily represent money market funds used for active employee benefits .
[text_11] the company includes other investments in other current assets .
[text_12] note 18 : leases the company has entered into operating leases involving certain facilities and equipment .
[text_13] rental expenses under operating leases were $ 29 million , $ 24 million and $ 21 million for the years ended december 31 , 2017 , 2016 and 2015 , respectively .
[text_14] the operating leases for facilities will expire over the next 25 years and the operating leases for equipment will expire over the next 5 years .
[text_15] certain operating leases have renewal options ranging from one to five years .
[text_16] the minimum annual future rental commitment under operating leases that have initial or remaining non-cancelable lease terms over the next 5 years and thereafter are as follows: .
[text_17] the company has a series of agreements with various public entities ( the 201cpartners 201d ) to establish certain joint ventures , commonly referred to as 201cpublic-private partnerships . 201d under the public-private partnerships , the company constructed utility plant , financed by the company and the partners constructed utility plant ( connected to the company 2019s property ) , financed by the partners .
[text_18] the company agreed to transfer and convey some of its real and personal property to the partners in exchange for an equal principal amount of industrial development bonds ( 201cidbs 201d ) , issued by the partners under a state industrial development bond and commercial development act .
[text_19] the company leased back the total facilities , including portions funded by both the company and the partners , under leases for a period of 40 years .
[text_20] the leases related to the portion of the facilities funded by the company have required payments from the company to the partners that approximate the payments required by the terms of the idbs from the partners to the company ( as the holder of the idbs ) .
[text_21] as the ownership of the portion of the facilities constructed by the .
[table_0]  | amount
[table_1] : 2018 | amount: $ 15
[table_2] : 2019 | amount: 14
[table_3] : 2020 | amount: 12
[table_4] : 2021 | amount: 9
[table_5] : 2022 | amount: 8
[table_6] : thereafter | amount: 65

Question: what were the average operating rental expenses from 2015 to 2017 in millions

Chosen:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_13","value":"29"},{"source":"text_13","value":"24"}]},{"op":"add","args":["#0",{"source":"text_13","value":"21"}]},{"op":"divide","args":["#1","const_3"]}],"answer":24.666666666666668}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_13","value":"29"},{"source":"text_13","value":"24"}]},{"op":"add","args":["#0",{"source":"text_13","value":"21"}]},{"op":"divide","args":["#1","const_3"]}],"answer":8.666666666666666}
```

## STT/2001/page_74.pdf-3

Evidence:
[text_0] a black-scholes option-pricing model was used for purposes of estimating the fair value of state street 2019s employee stock options at the grant date .
[text_1] the following were the weighted average assumptions for the years ended december 31 , 2001 , 2000 and 1999 , respectively : risk-free interest rates of 3.99% ( 3.99 % ) , 5.75% ( 5.75 % ) and 5.90% ( 5.90 % ) ; dividend yields of 1.08% ( 1.08 % ) , .73% ( .73 % ) and .92% ( .92 % ) ; and volatility factors of the expected market price of state street common stock of .30 , .30 and .30 .
[text_2] the estimated weighted average life of the stock options granted was 4.1 years for the years ended december 31 , 2001 , 2000 and 1999 .
[text_3] o t h e r u n r e a l i z e d c o m p r e h e n s i v e i n c o m e ( l o s s ) at december 31 , the components of other unrealized comprehensive income ( loss ) , net of related taxes , were as follows: .
[text_4] note j shareholders 2019 rights plan in 1988 , state street declared a dividend of one preferred share purchase right for each outstanding share of common stock .
[text_5] in 1998 , the rights agreement was amended and restated , and in 2001 , the rights plan was impacted by the 2-for-1 stock split .
[text_6] accordingly , a right may be exercised , under certain conditions , to purchase one eight-hundredths share of a series of participating preferred stock at an exercise price of $ 132.50 , subject to adjustment .
[text_7] the rights become exercisable if a party acquires or obtains the right to acquire 10% ( 10 % ) or more of state street 2019s common stock or after commencement or public announcement of an offer for 10% ( 10 % ) or more of state street 2019s common stock .
[text_8] when exercisable , under certain conditions , each right entitles the holder thereof to purchase shares of common stock , of either state street or of the acquirer , having a market value of two times the then-current exercise price of that right .
[text_9] the rights expire in september 2008 , and may be redeemed at a price of $ .00125 per right , subject to adjustment , at any time prior to expiration or the acquisition of 10% ( 10 % ) of state street 2019s common stock .
[text_10] under certain circumstances , the rights may be redeemed after they become exercisable and may be subject to automatic redemption .
[text_11] note k regulatory matters r e g u l a t o r y c a p i t a l state street is subject to various regulatory capital requirements administered by federal banking agencies .
[text_12] failure to meet minimum capital requirements can initiate certain mandatory and discretionary actions by regulators that , if undertaken , could have a direct material effect on state street 2019s financial condition .
[text_13] under capital adequacy guidelines , state street must meet specific capital guidelines that involve quantitative measures of state street 2019s assets , liabilities and off-balance sheet items as calculated under regulatory accounting practices .
[text_14] state street 2019s capital amounts and classification are subject to qualitative judgments by the regulators about components , risk weightings and other factors .
[text_15] 42 state street corporation .
[table_0] ( dollars in millions ) | 2001 | 2000
[table_1] ( dollars in millions ): unrealized gain on available-for-sale securities | 2001: $ 96 | 2000: $ 19
[table_2] ( dollars in millions ): foreign currency translation | 2001: -27 ( 27 ) | 2000: -20 ( 20 )
[table_3] ( dollars in millions ): other | 2001: 1 | 2000: 
[table_4] ( dollars in millions ): total | 2001: $ 70 | 2000: $ -1 ( 1 )

Question: between 2000 and 2001 , what was the percent increase of unrealized gains?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"96"},{"source":"table_1","value":"19"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"19"}]}],"answer":4.052631578947368}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"96"},{"source":"table_1","value":"19"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"19"}]}],"answer":6.052631578947368}
```

## AMAT/2018/page_33.pdf-2

Evidence:
[text_0] 10/27/13 10/26/14 10/25/15 10/30/16 10/29/17 10/28/18 applied materials , inc .
[text_1] s&p 500 rdg semiconductor composite part ii item 5 : market for registrant 2019s common equity , related stockholder matters and issuer purchases of equity securities market information applied 2019s common stock is traded on the nasdaq global select market under the symbol amat .
[text_2] as of december 7 , 2018 , there were 2854 registered holders of applied common stock .
[text_3] performance graph the performance graph below shows the five-year cumulative total stockholder return on applied common stock during the period from october 27 , 2013 through october 28 , 2018 .
[text_4] this is compared with the cumulative total return of the standard & poor 2019s 500 stock index and the rdg semiconductor composite index over the same period .
[text_5] the comparison assumes $ 100 was invested on october 27 , 2013 in applied common stock and in each of the foregoing indices and assumes reinvestment of dividends , if any .
[text_6] dollar amounts in the graph are rounded to the nearest whole dollar .
[text_7] the performance shown in the graph represents past performance and should not be considered an indication of future performance .
[text_8] comparison of 5 year cumulative total return* among applied materials , inc. , the s&p 500 index and the rdg semiconductor composite index *assumes $ 100 invested on 10/27/13 in stock or 10/31/13 in index , including reinvestment of dividends .
[text_9] indexes calculated on month-end basis .
[text_10] copyright a9 2018 standard & poor 2019s , a division of s&p global .
[text_11] all rights reserved. .
[text_12] .
[table_0]  | 10/27/2013 | 10/26/2014 | 10/25/2015 | 10/30/2016 | 10/29/2017 | 10/28/2018
[table_1] : applied materials | 10/27/2013: 100.00 | 10/26/2014: 121.04 | 10/25/2015: 96.67 | 10/30/2016: 171.69 | 10/29/2017: 343.16 | 10/28/2018: 198.27
[table_2] : s&p 500 index | 10/27/2013: 100.00 | 10/26/2014: 117.27 | 10/25/2015: 123.37 | 10/30/2016: 128.93 | 10/29/2017: 159.40 | 10/28/2018: 171.11
[table_3] : rdg semiconductor composite index | 10/27/2013: 100.00 | 10/26/2014: 128.42 | 10/25/2015: 126.26 | 10/30/2016: 154.41 | 10/29/2017: 232.29 | 10/28/2018: 221.61

Question: what is the roi for applied materials if the investment made on october 2013 was sold 5 years later?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"198.27"},"const_100"]},{"op":"divide","args":["#0","const_100"]}],"answer":0.9827}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"198.27"},"const_100"]},{"op":"divide","args":["#0","const_100"]}],"answer":2.9827}
```

## UPS/2016/page_114.pdf-2

Evidence:
[text_0] united parcel service , inc .
[text_1] and subsidiaries notes to consolidated financial statements 8.375% ( 8.375 % ) debentures the 8.375% ( 8.375 % ) debentures consist of two separate tranches , as follows : 2022 $ 276 million of the debentures have a maturity of april 1 , 2030 .
[text_2] these debentures have an 8.375% ( 8.375 % ) interest rate until april 1 , 2020 , and , thereafter , the interest rate will be 7.62% ( 7.62 % ) for the final 10 years .
[text_3] these debentures are redeemable in whole or in part at our option at any time .
[text_4] the redemption price is equal to the greater of 100% ( 100 % ) of the principal amount and accrued interest , or the sum of the present values of the remaining scheduled payout of principal and interest thereon discounted to the date of redemption ( at a benchmark treasury yield plus five basis points ) plus accrued interest .
[text_5] 2022 $ 424 million of the debentures have a maturity of april 1 , 2020 .
[text_6] these debentures are not subject to redemption prior to maturity .
[text_7] interest is payable semiannually in april and october for both tranches and neither tranche is subject to sinking fund requirements .
[text_8] we subsequently entered into interest rate swaps on the 2020 debentures , which effectively converted the fixed interest rates on the debentures to variable libor-based interest rates .
[text_9] the average interest rate payable on the 2020 debentures , including the impact of the interest rate swaps , for 2016 and 2015 was 5.43% ( 5.43 % ) and 5.04% ( 5.04 % ) , respectively .
[text_10] floating rate senior notes the floating rate senior notes bear interest at either one or three-month libor , less a spread ranging from 30 to 45 basis points .
[text_11] the average interest rate for 2016 and 2015 was 0.21% ( 0.21 % ) and 0.01% ( 0.01 % ) , respectively .
[text_12] these notes are callable at various times after 30 years at a stated percentage of par value , and putable by the note holders at various times after 10 years at a stated percentage of par value .
[text_13] the notes have maturities ranging from 2049 through 2066 .
[text_14] in march , june and august 2016 , we issued floating rate senior notes in principal balances of $ 118 , $ 74 and $ 35 million , respectively .
[text_15] these notes bear interest at three-month libor less 30 basis points and mature in 2066 .
[text_16] capital lease obligations we have certain property , plant and equipment subject to capital leases .
[text_17] some of the obligations associated with these capital leases have been legally defeased .
[text_18] the recorded value of our property , plant and equipment subject to capital leases is as follows as of december 31 ( in millions ) : .
[text_19] these capital lease obligations have principal payments due at various dates from 2017 through 3005. .
[table_0]  | 2016 | 2015
[table_1] : vehicles | 2016: $ 68 | 2015: $ 74
[table_2] : aircraft | 2016: 2291 | 2015: 2289
[table_3] : buildings | 2016: 190 | 2015: 207
[table_4] : accumulated amortization | 2016: -896 ( 896 ) | 2015: -849 ( 849 )
[table_5] : property plant and equipment subject to capital leases | 2016: $ 1653 | 2015: $ 1721

Question: what was the change in millions of buildings from 2015 to 2016?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_3","value":"190"},{"source":"table_3","value":"207"}]}],"answer":-17.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_3","value":"190"},{"source":"table_3","value":"207"}]}],"answer":397.0}
```

## HOLX/2008/page_132.pdf-2

Evidence:
[text_0] hologic , inc .
[text_1] notes to consolidated financial statements ( continued ) ( in thousands , except per share data ) 3 .
[text_2] business combinations fiscal 2008 acquisitions : acquisition of third wave technologies , inc .
[text_3] on july 24 , 2008 the company completed its acquisition of third wave technologies , inc .
[text_4] ( 201cthird wave 201d ) pursuant to a definitive agreement dated june 8 , 2008 .
[text_5] the company has concluded that the acquisition of third wave does not represent a material business combination and therefore no pro forma financial information has been provided herein .
[text_6] subsequent to the acquisition date , the company 2019s results of operations include the results of third wave , which has been reported as a component of the company 2019s diagnostics reporting segment .
[text_7] third wave , located in madison , wisconsin , develops and markets molecular diagnostic reagents for a wide variety of dna and rna analysis applications based on its proprietary invader chemistry .
[text_8] third wave 2019s current clinical diagnostic offerings consist of products for conditions such as cystic fibrosis , hepatitis c , cardiovascular risk and other diseases .
[text_9] third wave recently submitted to the u.s .
[text_10] food and drug administration ( 201cfda 201d ) pre-market approval ( 201cpma 201d ) applications for two human papillomavirus ( 201chpv 201d ) tests .
[text_11] the company paid $ 11.25 per share of third wave , for an aggregate purchase price of approximately $ 591200 ( subject to adjustment ) consisting of approximately $ 575400 in cash in exchange for stock and warrants ; approximately 668 of fully vested stock options granted to third wave employees in exchange for their vested third wave stock options , with an estimated fair value of approximately $ 8100 ; and approximately $ 7700 for acquisition related fees and expenses .
[text_12] there are no potential contingent consideration arrangements payable to the former shareholders in connection with this transaction .
[text_13] additionally , the company granted approximately 315 unvested stock options in exchange for unvested third wave stock options , with an estimated fair value of approximately $ 5100 , which will be recognized as compensation expense over the vesting period .
[text_14] the company determined the fair value of the options issued in connection with the acquisition in accordance with eitf issue no .
[text_15] 99-12 , determination of the measurement date for the market price of acquirer securities issued in a purchase business combination 201d ) .
[text_16] the company determined the measurement date to be july 24 , 2008 , the date the transaction was completed , as the number of shares to be issued according to the exchange ratio was not fixed until this date .
[text_17] the company valued the securities based on the average market price for two days before the measurement date and the measurement date itself .
[text_18] the weighted average stock price was determined to be approximately $ 23.54 .
[text_19] the preliminary purchase price is as follows: .
[text_20] .
[table_0] cash portion of consideration | $ 575400
[table_1] cash portion of consideration: fair value of vested options exchanged | $ 575400: 8100
[table_2] cash portion of consideration: direct acquisition costs | $ 575400: 7700
[table_3] cash portion of consideration: total estimated purchase price | $ 575400: $ 591200

Question: what portion of the estimated purchase price is recorded as acquisition cost?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"7700"},{"source":"table_3","value":"591200"}]}],"answer":0.013024357239512856}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"7700"},{"source":"table_3","value":"591200"}]}],"answer":598900.0}
```

## MS/2013/page_240.pdf-3

Evidence:
[text_0] morgan stanley notes to consolidated financial statements 2014 ( continued ) lending commitments .
[text_1] primary lending commitments are those that are originated by the company whereas secondary lending commitments are purchased from third parties in the market .
[text_2] the commitments include lending commitments that are made to investment grade and non-investment grade companies in connection with corporate lending and other business activities .
[text_3] commitments for secured lending transactions .
[text_4] secured lending commitments are extended by the company to companies and are secured by real estate or other physical assets of the borrower .
[text_5] loans made under these arrangements typically are at variable rates and generally provide for over-collateralization based upon the creditworthiness of the borrower .
[text_6] forward starting reverse repurchase agreements .
[text_7] the company has entered into forward starting securities purchased under agreements to resell ( agreements that have a trade date at or prior to december 31 , 2013 and settle subsequent to period-end ) that are primarily secured by collateral from u.s .
[text_8] government agency securities and other sovereign government obligations .
[text_9] commercial and residential mortgage-related commitments .
[text_10] the company enters into forward purchase contracts involving residential mortgage loans , residential mortgage lending commitments to individuals and residential home equity lines of credit .
[text_11] in addition , the company enters into commitments to originate commercial and residential mortgage loans .
[text_12] underwriting commitments .
[text_13] the company provides underwriting commitments in connection with its capital raising sources to a diverse group of corporate and other institutional clients .
[text_14] other lending commitments .
[text_15] other commitments generally include commercial lending commitments to small businesses and commitments related to securities-based lending activities in connection with the company 2019s wealth management business segment .
[text_16] the company sponsors several non-consolidated investment funds for third-party investors where the company typically acts as general partner of , and investment advisor to , these funds and typically commits to invest a minority of the capital of such funds , with subscribing third-party investors contributing the majority .
[text_17] the company 2019s employees , including its senior officers , as well as the company 2019s directors , may participate on the same terms and conditions as other investors in certain of these funds that the company forms primarily for client investment , except that the company may waive or lower applicable fees and charges for its employees .
[text_18] the company has contractual capital commitments , guarantees , lending facilities and counterparty arrangements with respect to these investment funds .
[text_19] premises and equipment .
[text_20] the company has non-cancelable operating leases covering premises and equipment ( excluding commodities operating leases , shown separately ) .
[text_21] at december 31 , 2013 , future minimum rental commitments under such leases ( net of subleases , principally on office rentals ) were as follows ( dollars in millions ) : year ended operating premises leases .
[text_22] .
[table_0] year ended | operating premises leases
[table_1] year ended: 2014 | operating premises leases: $ 672
[table_2] year ended: 2015 | operating premises leases: 656
[table_3] year ended: 2016 | operating premises leases: 621
[table_4] year ended: 2017 | operating premises leases: 554
[table_5] year ended: 2018 | operating premises leases: 481
[table_6] year ended: thereafter | operating premises leases: 2712

Question: what is the percentage difference in future minimum rental commitments as of december 31 , 2013 between 2015 and 2016?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_3","value":"621"},{"source":"table_2","value":"656"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"656"}]}],"answer":-0.053353658536585365}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_3","value":"621"},{"source":"table_2","value":"656"}]},{"op":"divide","args":["#0",{"source":"table_2","value":"656"}]}],"answer":1.9466463414634145}
```

## AES/2012/page_223.pdf-2

Evidence:
[text_0] the aes corporation notes to consolidated financial statements 2014 ( continued ) december 31 , 2012 , 2011 , and 2010 ( 1 ) a u.s .
[text_1] subsidiary of the company has a defined benefit obligation of $ 764 million and $ 679 million as of december 31 , 2012 and 2011 , respectively , and uses salary bands to determine future benefit costs rather than rates of compensation increases .
[text_2] rates of compensation increases in the table above do not include amounts related to this specific defined benefit plan .
[text_3] ( 2 ) includes an inflation factor that is used to calculate future periodic benefit cost , but is not used to calculate the benefit obligation .
[text_4] the company establishes its estimated long-term return on plan assets considering various factors , which include the targeted asset allocation percentages , historic returns and expected future returns .
[text_5] the measurement of pension obligations , costs and liabilities is dependent on a variety of assumptions .
[text_6] these assumptions include estimates of the present value of projected future pension payments to all plan participants , taking into consideration the likelihood of potential future events such as salary increases and demographic experience .
[text_7] these assumptions may have an effect on the amount and timing of future contributions .
[text_8] the assumptions used in developing the required estimates include the following key factors : 2022 discount rates ; 2022 salary growth ; 2022 retirement rates ; 2022 inflation ; 2022 expected return on plan assets ; and 2022 mortality rates .
[text_9] the effects of actual results differing from the company 2019s assumptions are accumulated and amortized over future periods and , therefore , generally affect the company 2019s recognized expense in such future periods .
[text_10] sensitivity of the company 2019s pension funded status to the indicated increase or decrease in the discount rate and long-term rate of return on plan assets assumptions is shown below .
[text_11] note that these sensitivities may be asymmetric and are specific to the base conditions at year-end 2012 .
[text_12] they also may not be additive , so the impact of changing multiple factors simultaneously cannot be calculated by combining the individual sensitivities shown .
[text_13] the funded status as of december 31 , 2012 is affected by the assumptions as of that date .
[text_14] pension expense for 2012 is affected by the december 31 , 2011 assumptions .
[text_15] the impact on pension expense from a one percentage point change in these assumptions is shown in the table below ( in millions ) : .
[text_16] .
[table_0] increase of 1% ( 1 % ) in the discount rate | $ -48 ( 48 )
[table_1] increase of 1% ( 1 % ) in the discount rate: decrease of 1% ( 1 % ) in the discount rate | $ -48 ( 48 ): 38
[table_2] increase of 1% ( 1 % ) in the discount rate: increase of 1% ( 1 % ) in the long-term rate of return on plan assets | $ -48 ( 48 ): -47 ( 47 )
[table_3] increase of 1% ( 1 % ) in the discount rate: decrease of 1% ( 1 % ) in the long-term rate of return on plan assets | $ -48 ( 48 ): 47

Question: what was the net reduction in defined benefit obligations between december 31 , 2012 and 2011 , in millions?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_1","value":"764"},{"source":"text_1","value":"679"}]}],"answer":85.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_1","value":"764"},{"source":"text_1","value":"679"}]}],"answer":1443.0}
```

## HST/2018/page_135.pdf-1

Evidence:
[text_0] host hotels & resorts , inc. , host hotels & resorts , l.p. , and subsidiaries notes to consolidated financial statements 2014 ( continued ) a reconciliation of the beginning and ending balances of our unrecognized tax benefits is as follows ( in millions ) : .
[text_1] all of such uncertain tax position amounts , if recognized , would impact our reconciliation between the income tax provision calculated at the statutory u.s .
[text_2] federal income tax rate of 21% ( 21 % ) ( 35% ( 35 % ) in 2017 ) and the actual income tax provision recorded each year .
[text_3] we expect a decrease to the balance of unrecognized tax benefits within 12 months of the reporting date of approximately $ 3 million .
[text_4] as of december 31 , 2018 , the tax years that remain subject to examination by major tax jurisdictions generally include 2015-2018 .
[text_5] there were no material interest or penalties recorded for the years ended december 31 , 2018 , 2017 , and 2016 .
[text_6] 8 .
[text_7] leases taxable reit subsidiaries leases we lease substantially all of our hotels to a wholly owned subsidiary that qualifies as a taxable reit subsidiary due to federal income tax restrictions on a reit 2019s ability to derive revenue directly from the operation and management of a hotel .
[text_8] ground leases as of december 31 , 2018 , all or a portion of 25 of our hotels are subject to ground leases , generally with multiple renewal options , all of which are accounted for as operating leases .
[text_9] for lease agreements with scheduled rent increases , we recognize the fixed portion of the lease expense ratably over the term of the lease .
[text_10] certain of these leases contain provisions for the payment of contingent rentals based on a percentage of sales in excess of stipulated amounts .
[text_11] other lease information we also have leases on facilities used in our former restaurant business , all of which we subsequently subleased .
[text_12] these leases and subleases contain one or more renewal options , generally for five- or ten-year periods .
[text_13] the restaurant leases are accounted for as operating leases .
[text_14] our contingent liability related to these leases is $ 7 million as of december 31 , 2018 .
[text_15] we , however , consider the likelihood of any material funding related to these leases to be remote .
[text_16] our leasing activity also includes those entered into by our hotels for various types of equipment , such as computer equipment , vehicles and telephone systems .
[text_17] equipment leases are accounted for either as operating or capital leases , depending upon the characteristics of the particular lease arrangement .
[text_18] equipment leases that are characterized as capital leases are classified as furniture and equipment and are depreciated over the life of the lease .
[text_19] the amortization expense applicable to capitalized leases is included in depreciation expense. .
[table_0]  | 2018 | 2017
[table_1] : balance at january 1 | 2018: $ 11 | 2017: $ 11
[table_2] : balance at december 31 | 2018: $ 11 | 2017: $ 11

Question: what was the change in million of the unrecognized tax benefits between 2017 and 2018?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"11"},{"source":"table_2","value":"11"}]}],"answer":0.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"11"},{"source":"table_2","value":"11"}]}],"answer":22.0}
```

## ETR/2008/page_401.pdf-1

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"53620"},{"source":"table_2","value":"42915"}]}],"answer":10705.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"53620"},{"source":"table_2","value":"42915"}]}],"answer":96535.0}
```

## ETR/2016/page_418.pdf-2

Evidence:
[text_0] entergy texas , inc .
[text_1] and subsidiaries management 2019s financial discussion and analysis results of operations net income 2016 compared to 2015 net income increased $ 37.9 million primarily due to lower other operation and maintenance expenses , the asset write-off of its receivable associated with the spindletop gas storage facility in 2015 , and higher net revenue .
[text_2] 2015 compared to 2014 net income decreased $ 5.2 million primarily due to the asset write-off of its receivable associated with the spindletop gas storage facility and higher other operation and maintenance expenses , partially offset by higher net revenue and a lower effective tax rate .
[text_3] net revenue 2016 compared to 2015 net revenue consists of operating revenues net of : 1 ) fuel , fuel-related expenses , and gas purchased for resale , 2 ) purchased power expenses , and 3 ) other regulatory charges .
[text_4] following is an analysis of the change in net revenue comparing 2016 to 2015 .
[text_5] amount ( in millions ) .
[text_6] the reserve equalization variance is primarily due to a reduction in reserve equalization expense primarily due to changes in the entergy system generation mix compared to the same period in 2015 as a result of the execution of a new purchased power agreement and entergy mississippi 2019s exit from the system agreement , each in november 2015 , and entergy texas 2019s exit from the system agreement in august 2016 .
[text_7] see note 2 to the financial statements for a discussion of the system agreement .
[text_8] the purchased power capacity variance is primarily due to decreased expenses due to the termination of the purchased power agreements between entergy louisiana and entergy texas in august 2016 , as well as capacity cost changes for ongoing purchased power capacity contracts .
[text_9] the transmission revenue variance is primarily due to an increase in attachment o rates charged by miso to transmission customers and a settlement of attachment o rates previously billed to transmission customers by miso. .
[table_0]  | amount ( in millions )
[table_1] : 2015 net revenue | amount ( in millions ): $ 637.2
[table_2] : reserve equalization | amount ( in millions ): 14.3
[table_3] : purchased power capacity | amount ( in millions ): 12.4
[table_4] : transmission revenue | amount ( in millions ): 7.0
[table_5] : retail electric price | amount ( in millions ): 5.4
[table_6] : net wholesale | amount ( in millions ): -27.8 ( 27.8 )
[table_7] : other | amount ( in millions ): -4.3 ( 4.3 )
[table_8] : 2016 net revenue | amount ( in millions ): $ 644.2

Question: what is the net change in net revenue during 2016 for entergy texas , inc.?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_8","value":"644.2"},{"source":"table_1","value":"637.2"}]}],"answer":7.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_8","value":"644.2"},{"source":"table_1","value":"637.2"}]}],"answer":1281.4}
```

## AES/2001/page_33.pdf-4

Evidence:
[text_0] part ii item 5 2014market for registrant 2019s common equity and related stockholder matters ( a ) market information .
[text_1] the common stock of the company is currently traded on the new york stock exchange ( nyse ) under the symbol 2018 2018aes 2019 2019 .
[text_2] the following tables set forth the high and low sale prices for the common stock as reported by the nyse for the periods indicated .
[text_3] price range of common stock .
[text_4] ( b ) holders .
[text_5] as of march 2 , 2002 , there were 9967 record holders of the company 2019s common stock , par value $ 0.01 per share .
[text_6] ( c ) dividends .
[text_7] under the terms of the company 2019s corporate revolving loan and letters of credit facility of $ 850 million entered into with a commercial bank syndicate and other bank agreements , the company is currently limited in the amount of cash dividends it is allowed to pay .
[text_8] in addition , the company is precluded from paying cash dividends on its common stock under the terms of a guaranty to the utility customer in connection with the aes thames project in the event certain net worth and liquidity tests of the company are not met .
[text_9] the company has met these tests at all times since making the guaranty .
[text_10] the ability of the company 2019s project subsidiaries to declare and pay cash dividends to the company is subject to certain limitations in the project loans , governmental provisions and other agreements entered into by such project subsidiaries .
[text_11] such limitations permit the payment of cash dividends out of current cash flow for quarterly , semiannual or annual periods only at the end of such periods and only after payment of principal and interest on project loans due at the end of such periods , and in certain cases after providing for debt service reserves. .
[table_0] 2001 first quarter | high $ 60.15 | low $ 41.30 | 2000 first quarter | high $ 44.72 | low $ 34.25
[table_1] 2001 first quarter: second quarter | high $ 60.15: 52.25 | low $ 41.30: 39.95 | 2000 first quarter: second quarter | high $ 44.72: 49.63 | low $ 34.25: 35.56
[table_2] 2001 first quarter: third quarter | high $ 60.15: 44.50 | low $ 41.30: 12.00 | 2000 first quarter: third quarter | high $ 44.72: 70.25 | low $ 34.25: 45.13
[table_3] 2001 first quarter: fourth quarter | high $ 60.15: 17.80 | low $ 41.30: 11.60 | 2000 first quarter: fourth quarter | high $ 44.72: 72.81 | low $ 34.25: 45.00

Question: what was average of high and low stock prices for the first quarter of 2000?

Chosen:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_0","value":"44.72"},{"source":"table_0","value":"34.25"}]},{"op":"divide","args":["#0","const_2"]}],"answer":39.485}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_0","value":"44.72"},{"source":"table_0","value":"34.25"}]},{"op":"divide","args":["#0","const_2"]}],"answer":5.235}
```

## DG/2008/page_86.pdf-3

Evidence:
[text_0] for intangible assets subject to amortization , the estimated aggregate amortization expense for each of the five succeeding fiscal years is as follows : 2009 - $ 41.1 million , 2010 - $ 27.3 million , 2011 - $ 20.9 million , 2012 - $ 17.0 million , and 2013 - $ 12.0 million .
[text_1] fees and expenses related to the merger totaled $ 102.6 million , principally consisting of investment banking fees , legal fees and stock compensation ( $ 39.4 million as further discussed in note 10 ) , and are reflected in the 2007 results of operations .
[text_2] capitalized debt issuance costs as of the merger date of $ 87.4 million for merger-related financing were reflected in other long- term assets in the consolidated balance sheet .
[text_3] the following represents the unaudited pro forma results of the company 2019s consolidated operations as if the merger had occurred on february 3 , 2007 and february 4 , 2006 , respectively , after giving effect to certain adjustments , including the depreciation and amortization of the assets acquired based on their estimated fair values and changes in interest expense resulting from changes in consolidated debt ( in thousands ) : ( in thousands ) year ended february 1 , year ended february 2 .
[text_4] the pro forma information does not purport to be indicative of what the company 2019s results of operations would have been if the acquisition had in fact occurred at the beginning of the periods presented , and is not intended to be a projection of the company 2019s future results of operations .
[text_5] subsequent to the announcement of the merger agreement , the company and its directors , along with other parties , were named in seven putative class actions filed in tennessee state courts alleging claims for breach of fiduciary duty arising out of the proposed merger , all as described more fully under 201clegal proceedings 201d in note 8 below .
[text_6] 3 .
[text_7] strategic initiatives during 2006 , the company began implementing certain strategic initiatives related to its historical inventory management and real estate strategies , as more fully described below .
[text_8] inventory management in november 2006 , the company undertook an initiative to discontinue its historical inventory packaway model for virtually all merchandise by the end of fiscal 2007 .
[text_9] under the packaway model , certain unsold inventory items ( primarily seasonal merchandise ) were stored on-site and returned to the sales floor until the items were eventually sold , damaged or discarded .
[text_10] through end-of-season and other markdowns , this initiative resulted in the elimination of seasonal , home products and basic clothing packaway merchandise to allow for increased levels of newer , current-season merchandise .
[text_11] in connection with this strategic change , in the third quarter of 2006 the company recorded a reserve for lower of cost or market inventory .
[table_0] ( in thousands ) | year endedfebruary 12008 | year endedfebruary 22007
[table_1] ( in thousands ): revenue | year endedfebruary 12008: $ 9495246 | year endedfebruary 22007: $ 9169822
[table_2] ( in thousands ): net loss | year endedfebruary 12008: -57939 ( 57939 ) | year endedfebruary 22007: ( 156188 )

Question: what is the net income margin in 2008?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"57939"},{"source":"table_1","value":"9495246"}]}],"answer":0.006101895622293514}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"57939"},{"source":"table_1","value":"9495246"}]}],"answer":9553185.0}
```

## ETR/2011/page_398.pdf-3

Evidence:
[text_0] system energy resources , inc .
[text_1] management 2019s financial discussion and analysis sources of capital system energy 2019s sources to meet its capital requirements include : internally generated funds ; cash on hand ; debt issuances ; and bank financing under new or existing facilities .
[text_2] system energy may refinance , redeem , or otherwise retire debt prior to maturity , to the extent market conditions and interest and dividend rates are favorable .
[text_3] all debt and common stock issuances by system energy require prior regulatory approval .
[text_4] debt issuances are also subject to issuance tests set forth in its bond indentures and other agreements .
[text_5] system energy has sufficient capacity under these tests to meet its foreseeable capital needs .
[text_6] in february 2012 , system energy vie issued $ 50 million of 4.02% ( 4.02 % ) series h notes due february 2017 .
[text_7] system energy used the proceeds to purchase additional nuclear fuel .
[text_8] system energy has obtained a short-term borrowing authorization from the ferc under which it may borrow , through october 2013 , up to the aggregate amount , at any one time outstanding , of $ 200 million .
[text_9] see note 4 to the financial statements for further discussion of system energy 2019s short-term borrowing limits .
[text_10] system energy has also obtained an order from the ferc authorizing long-term securities issuances .
[text_11] the current long-term authorization extends through july 2013 .
[text_12] system energy 2019s receivables from the money pool were as follows as of december 31 for each of the following years: .
[text_13] see note 4 to the financial statements for a description of the money pool .
[text_14] nuclear matters system energy owns and operates grand gulf .
[text_15] system energy is , therefore , subject to the risks related to owning and operating a nuclear plant .
[text_16] these include risks from the use , storage , handling and disposal of high- level and low-level radioactive materials , regulatory requirement changes , including changes resulting from events at other plants , limitations on the amounts and types of insurance commercially available for losses in connection with nuclear operations , and technological and financial uncertainties related to decommissioning nuclear plants at the end of their licensed lives , including the sufficiency of funds in decommissioning trusts .
[text_17] in the event of an unanticipated early shutdown of grand gulf , system energy may be required to provide additional funds or credit support to satisfy regulatory requirements for decommissioning .
[text_18] after the nuclear incident in japan resulting from the march 2011 earthquake and tsunami , the nrc established a task force to conduct a review of processes and regulations relating to nuclear facilities in the united states .
[text_19] the task force issued a near term ( 90-day ) report in july 2011 that has made recommendations , which are currently being evaluated by the nrc .
[text_20] it is anticipated that the nrc will issue certain orders and requests for information to nuclear plant licensees by the end of the first quarter 2012 that will begin to implement the task force 2019s recommendations .
[text_21] these orders may require u.s .
[text_22] nuclear operators , including entergy , to undertake plant modifications or perform additional analyses that could , among other things , result in increased costs and capital requirements associated with operating entergy 2019s nuclear plants. .
[table_0] 2011 | 2010 | 2009 | 2008
[table_1] 2011: ( in thousands ) | 2010: ( in thousands ) | 2009: ( in thousands ) | 2008: ( in thousands )
[table_2] 2011: $ 120424 | 2010: $ 97948 | 2009: $ 90507 | 2008: $ 42915

Question: what is the total system energy 2019s receivables from the money pool in the last three years?

Chosen:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"120424"},{"source":"table_2","value":"97948"}]},{"op":"add","args":["#0",{"source":"table_2","value":"90507"}]}],"answer":308879.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"120424"},{"source":"table_2","value":"97948"}]},{"op":"add","args":["#0",{"source":"table_2","value":"90507"}]}],"answer":112983.0}
```

## AAP/2016/page_96.pdf-1

Evidence:
[text_0] advance auto parts , inc .
[text_1] schedule ii - valuation and qualifying accounts ( in thousands ) allowance for doubtful accounts receivable : balance at beginning of period charges to expenses deductions balance at end of period january 3 , 2015 $ 13295 $ 17182 $ ( 14325 ) ( 1 ) $ 16152 january 2 , 2016 16152 22067 ( 12461 ) ( 1 ) 25758 december 31 , 2016 25758 24597 ( 21191 ) ( 1 ) 29164 ( 1 ) accounts written off during the period .
[text_2] these amounts did not impact the company 2019s statement of operations for any year presented .
[text_3] note : other valuation and qualifying accounts have not been reported in this schedule because they are either not applicable or because the information has been included elsewhere in this report. .
[text_4] advance auto parts , inc .
[text_5] schedule ii - valuation and qualifying accounts ( in thousands ) allowance for doubtful accounts receivable : balance at beginning of period charges to expenses deductions balance at end of period january 3 , 2015 $ 13295 $ 17182 $ ( 14325 ) ( 1 ) $ 16152 january 2 , 2016 16152 22067 ( 12461 ) ( 1 ) 25758 december 31 , 2016 25758 24597 ( 21191 ) ( 1 ) 29164 ( 1 ) accounts written off during the period .
[text_6] these amounts did not impact the company 2019s statement of operations for any year presented .
[text_7] note : other valuation and qualifying accounts have not been reported in this schedule because they are either not applicable or because the information has been included elsewhere in this report. .
[table_0] allowance for doubtful accounts receivable: | balance atbeginningof period | charges toexpenses | deductions |  | balance atend ofperiod
[table_1] allowance for doubtful accounts receivable:: january 3 2015 | balance atbeginningof period: $ 13295 | charges toexpenses: $ 17182 | deductions: $ -14325 ( 14325 ) | : -1 ( 1 ) | balance atend ofperiod: $ 16152
[table_2] allowance for doubtful accounts receivable:: january 2 2016 | balance atbeginningof period: 16152 | charges toexpenses: 22067 | deductions: -12461 ( 12461 ) | : -1 ( 1 ) | balance atend ofperiod: 25758
[table_3] allowance for doubtful accounts receivable:: december 31 2016 | balance atbeginningof period: 25758 | charges toexpenses: 24597 | deductions: -21191 ( 21191 ) | : -1 ( 1 ) | balance atend ofperiod: 29164

Question: what is the net increase in the balance of allowance for doubtful accounts receivable during 2015?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"16152"},{"source":"table_1","value":"13295"}]}],"answer":2857.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"16152"},{"source":"table_1","value":"13295"}]}],"answer":29447.0}
```

## MRO/2008/page_99.pdf-2

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"20000"},{"source":"table_3","value":"15000"}]},{"op":"divide","args":["#0","const_2"]}],"answer":17500.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"20000"},{"source":"table_3","value":"15000"}]},{"op":"divide","args":["#0","const_2"]}],"answer":2500.0}
```

## ETR/2002/page_24.pdf-2

Evidence:
[text_0] entergy corporation and subsidiaries management's financial discussion and analysis the decrease in interest income in 2002 was primarily due to : fffd interest recognized in 2001 on grand gulf 1's decommissioning trust funds resulting from the final order addressing system energy's rate proceeding ; fffd interest recognized in 2001 at entergy mississippi and entergy new orleans on the deferred system energy costs that were not being recovered through rates ; and fffd lower interest earned on declining deferred fuel balances .
[text_1] the decrease in interest charges in 2002 is primarily due to : fffd a decrease of $ 31.9 million in interest on long-term debt primarily due to the retirement of long-term debt in late 2001 and early 2002 ; and fffd a decrease of $ 76.0 million in other interest expense primarily due to interest recorded on system energy's reserve for rate refund in 2001 .
[text_2] the refund was made in december 2001 .
[text_3] 2001 compared to 2000 results for the year ended december 31 , 2001 for u.s .
[text_4] utility were also affected by an increase in interest charges of $ 61.5 million primarily due to : fffd the final ferc order addressing the 1995 system energy rate filing ; fffd debt issued at entergy arkansas in july 2001 , at entergy gulf states in june 2000 and august 2001 , at entergy mississippi in january 2001 , and at entergy new orleans in july 2000 and february 2001 ; and fffd borrowings under credit facilities during 2001 , primarily at entergy arkansas .
[text_5] non-utility nuclear the increase in earnings in 2002 for non-utility nuclear from $ 128 million to $ 201 million was primarily due to the operation of indian point 2 and vermont yankee , which were purchased in september 2001 and july 2002 , respectively .
[text_6] the increase in earnings in 2001 for non-utility nuclear from $ 49 million to $ 128 million was primarily due to the operation of fitzpatrick and indian point 3 for a full year , as each was purchased in november 2000 , and the operation of indian point 2 , which was purchased in september 2001 .
[text_7] following are key performance measures for non-utility nuclear: .
[text_8] 2002 compared to 2001 the following fluctuations in the results of operations for non-utility nuclear in 2002 were primarily caused by the acquisitions of indian point 2 and vermont yankee ( except as otherwise noted ) : fffd operating revenues increased $ 411.0 million to $ 1.2 billion ; fffd other operation and maintenance expenses increased $ 201.8 million to $ 596.3 million ; fffd depreciation and amortization expenses increased $ 25.1 million to $ 42.8 million ; fffd fuel expenses increased $ 29.4 million to $ 105.2 million ; fffd nuclear refueling outage expenses increased $ 23.9 million to $ 46.8 million , which was due primarily to a .
[table_0]  | 2002 | 2001 | 2000
[table_1] : net mw in operation at december 31 | 2002: 3955 | 2001: 3445 | 2000: 2475
[table_2] : generation in gwh for the year | 2002: 29953 | 2001: 22614 | 2000: 7171
[table_3] : capacity factor for the year | 2002: 93% ( 93 % ) | 2001: 93% ( 93 % ) | 2000: 94% ( 94 % )

Question: in 2002 what was the ratio of the net mw in operation to the generation in gwh for the year

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"3955"},{"source":"table_2","value":"29953"}]}],"answer":0.13204019630754849}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"3955"},{"source":"table_2","value":"29953"}]}],"answer":33908.0}
```

## STT/2007/page_65.pdf-1

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

Question: what was the percent change in cross-border outstandings in the uk between 2006 and 2007?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"5951"},{"source":"table_1","value":"5531"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"5531"}]}],"answer":0.07593563550894955}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"5951"},{"source":"table_1","value":"5531"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"5531"}]}],"answer":2.0759356355089498}
```

## DISH/2002/page_94.pdf-1

Evidence:
[text_0] echostar communications corporation notes to consolidated financial statements - continued closing price of the class a common stock on the last business day of each calendar quarter in which such shares of class a common stock are deemed sold to an employee under the espp .
[text_1] the espp shall terminate upon the first to occur of ( i ) october 1 , 2007 or ( ii ) the date on which the espp is terminated by the board of directors .
[text_2] during 2000 , 2001 and 2002 employees purchased approximately 58000 ; 80000 and 108000 shares of class a common stock through the espp , respectively .
[text_3] 401 ( k ) employee savings plan echostar sponsors a 401 ( k ) employee savings plan ( the 201c401 ( k ) plan 201d ) for eligible employees .
[text_4] voluntary employee contributions to the 401 ( k ) plan may be matched 50% ( 50 % ) by echostar , subject to a maximum annual contribution by echostar of $ 1000 per employee .
[text_5] matching 401 ( k ) contributions totaled approximately $ 1.6 million , $ 2.1 million and $ 2.4 million during the years ended december 31 , 2000 , 2001 and 2002 , respectively .
[text_6] echostar also may make an annual discretionary contribution to the plan with approval by echostar 2019s board of directors , subject to the maximum deductible limit provided by the internal revenue code of 1986 , as amended .
[text_7] these contributions may be made in cash or in echostar stock .
[text_8] forfeitures of unvested participant balances which are retained by the 401 ( k ) plan may be used to fund matching and discretionary contributions .
[text_9] expense recognized relating to discretionary contributions was approximately $ 7 million , $ 225 thousand and $ 17 million during the years ended december 31 , 2000 , 2001 and 2002 , respectively .
[text_10] 9 .
[text_11] commitments and contingencies leases future minimum lease payments under noncancelable operating leases as of december 31 , 2002 , are as follows ( in thousands ) : year ending december 31 .
[text_12] total rent expense for operating leases approximated $ 9 million , $ 14 million and $ 16 million in 2000 , 2001 and 2002 , respectively .
[text_13] purchase commitments as of december 31 , 2002 , echostar 2019s purchase commitments totaled approximately $ 359 million .
[text_14] the majority of these commitments relate to echostar receiver systems and related components .
[text_15] all of the purchases related to these commitments are expected to be made during 2003 .
[text_16] echostar expects to finance these purchases from existing unrestricted cash balances and future cash flows generated from operations .
[text_17] patents and intellectual property many entities , including some of echostar 2019s competitors , now have and may in the future obtain patents and other intellectual property rights that cover or affect products or services directly or indirectly related to those that echostar offers .
[text_18] echostar may not be aware of all patents and other intellectual property rights that its products may potentially infringe .
[text_19] damages in patent infringement cases can include a tripling of actual damages in certain cases .
[text_20] further , echostar cannot estimate the extent to which it may be required in the future to obtain licenses with respect to .
[table_0] 2003 | $ 17274
[table_1] 2003: 2004 | $ 17274: 14424
[table_2] 2003: 2005 | $ 17274: 11285
[table_3] 2003: 2006 | $ 17274: 7698
[table_4] 2003: 2007 | $ 17274: 3668
[table_5] 2003: thereafter | $ 17274: 1650
[table_6] 2003: total minimum lease payments | $ 17274: 55999

Question: what is the percentage change in rent expense for operating leases from 2001 to 2002?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_12","value":"16"},{"source":"text_12","value":"14"}]},{"op":"divide","args":["#0",{"source":"text_12","value":"14"}]}],"answer":0.14285714285714285}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_12","value":"16"},{"source":"text_12","value":"14"}]},{"op":"divide","args":["#0",{"source":"text_12","value":"14"}]}],"answer":2.142857142857143}
```

## IPG/2008/page_21.pdf-4

Evidence:
[text_0] repurchase of equity securities the following table provides information regarding our purchases of equity securities during the fourth quarter of 2008 : number of shares purchased average paid per share2 total number of shares purchased as part of publicly announced plans or programs maximum number of shares that may yet be purchased under the plans or programs .
[text_1] total1 .
[text_2] .
[text_3] .
[text_4] .
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
[text_23] .
[text_24] .
[text_25] .
[text_26] .
[text_27] .
[text_28] .
[text_29] .
[text_30] .
[text_31] .
[text_32] .
[text_33] 47022 $ 5.18 2014 2014 1 consists of restricted shares of our common stock withheld under the terms of grants under employee stock compensation plans to offset tax withholding obligations that occurred upon vesting and release of restricted shares during each month of the fourth quarter of 2008 ( the 201cwithheld shares 201d ) .
[text_34] 2 the average price per month of the withheld shares was calculated by dividing the aggregate value of the tax withholding obligations for each month by the aggregate number of shares of our common stock withheld each month. .
[table_0]  | total number of shares purchased | average price paid per share2 | total number of shares purchased as part of publicly announced plans or programs | maximum number ofshares that may yet be purchased under the plans or programs
[table_1] : october 1-31 | total number of shares purchased: 29704 | average price paid per share2: $ 5.99 | total number of shares purchased as part of publicly announced plans or programs: 2014 | maximum number ofshares that may yet be purchased under the plans or programs: 2014
[table_2] : november 1-30 | total number of shares purchased: 4468 | average price paid per share2: $ 3.24 | total number of shares purchased as part of publicly announced plans or programs: 2014 | maximum number ofshares that may yet be purchased under the plans or programs: 2014
[table_3] : december 1-31 | total number of shares purchased: 12850 | average price paid per share2: $ 3.98 | total number of shares purchased as part of publicly announced plans or programs: 2014 | maximum number ofshares that may yet be purchased under the plans or programs: 2014
[table_4] : total1 | total number of shares purchased: 47022 | average price paid per share2: $ 5.18 | total number of shares purchased as part of publicly announced plans or programs: 2014 | maximum number ofshares that may yet be purchased under the plans or programs: 2014

Question: what is the cash outflow for the repurchase of shares during october 2008?

Chosen:
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"table_1","value":"29704"},{"source":"table_1","value":"5.99"}]}],"answer":177926.96}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"29704"},{"source":"table_1","value":"5.99"}]}],"answer":29709.99}
```

## STT/2008/page_139.pdf-1

Evidence:
[text_0] note 21 .
[text_1] expenses during the fourth quarter of 2008 , we elected to provide support to certain investment accounts managed by ssga through the purchase of asset- and mortgage-backed securities and a cash infusion , which resulted in a charge of $ 450 million .
[text_2] ssga manages certain investment accounts , offered to retirement plans , that allow participants to purchase and redeem units at a constant net asset value regardless of volatility in the underlying value of the assets held by the account .
[text_3] the accounts enter into contractual arrangements with independent third-party financial institutions that agree to make up any shortfall in the account if all the units are redeemed at the constant net asset value .
[text_4] the financial institutions have the right , under certain circumstances , to terminate this guarantee with respect to future investments in the account .
[text_5] during 2008 , the liquidity and pricing issues in the fixed-income markets adversely affected the market value of the securities in these accounts to the point that the third-party guarantors considered terminating their financial guarantees with the accounts .
[text_6] although we were not statutorily or contractually obligated to do so , we elected to purchase approximately $ 2.49 billion of asset- and mortgage-backed securities from these accounts that had been identified as presenting increased risk in the current market environment and to contribute an aggregate of $ 450 million to the accounts to improve the ratio of the market value of the accounts 2019 portfolio holdings to the book value of the accounts .
[text_7] we have no ongoing commitment or intent to provide support to these accounts .
[text_8] the securities are carried in investment securities available for sale in our consolidated statement of condition .
[text_9] the components of other expenses were as follows for the years ended december 31: .
[text_10] in september and october 2008 , lehman brothers holdings inc. , or lehman brothers , and certain of its affiliates filed for bankruptcy or other insolvency proceedings .
[text_11] while we had no unsecured financial exposure to lehman brothers or its affiliates , we indemnified certain customers in connection with these and other collateralized repurchase agreements with lehman brothers entities .
[text_12] in the then current market environment , the market value of the underlying collateral had declined .
[text_13] during the third quarter of 2008 , to the extent these declines resulted in collateral value falling below the indemnification obligation , we recorded a reserve to provide for our estimated net exposure .
[text_14] the reserve , which totaled $ 200 million , was based on the cost of satisfying the indemnification obligation net of the fair value of the collateral , which we purchased during the fourth quarter of 2008 .
[text_15] the collateral , composed of commercial real estate loans which are discussed in note 5 , is recorded in loans and leases in our consolidated statement of condition. .
[table_0] ( in millions ) | 2008 | 2007 | 2006
[table_1] ( in millions ): customer indemnification obligation | 2008: $ 200 | 2007:  | 2006: 
[table_2] ( in millions ): securities processing | 2008: 187 | 2007: $ 79 | 2006: $ 37
[table_3] ( in millions ): other | 2008: 505 | 2007: 399 | 2006: 281
[table_4] ( in millions ): total other expenses | 2008: $ 892 | 2007: $ 478 | 2006: $ 318

Question: what portion of the total other expenses is related to customer indemnification obligation in 2008?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"200"},{"source":"table_4","value":"892"}]}],"answer":0.2242152466367713}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"200"},{"source":"table_4","value":"892"}]}],"answer":1092.0}
```

## LKQ/2007/page_76.pdf-1

Evidence:
[text_0] lkq corporation and subsidiaries notes to consolidated financial statements ( continued ) note 5 .
[text_1] long-term obligations ( continued ) as part of the consideration for business acquisitions completed during 2007 , 2006 and 2005 , we issued promissory notes totaling approximately $ 1.7 million , $ 7.2 million and $ 6.4 million , respectively .
[text_2] the notes bear interest at annual rates of 3.0% ( 3.0 % ) to 6.0% ( 6.0 % ) , and interest is payable at maturity or in monthly installments .
[text_3] we also assumed certain liabilities in connection with a business acquisition during the second quarter of 2005 , including a promissory note with a remaining principle balance of approximately $ 0.2 million .
[text_4] the annual interest rate on the note , which was retired during 2006 , was note 6 .
[text_5] commitments and contingencies operating leases we are obligated under noncancelable operating leases for corporate office space , warehouse and distribution facilities , trucks and certain equipment .
[text_6] the future minimum lease commitments under these leases at december 31 , 2007 are as follows ( in thousands ) : years ending december 31: .
[text_7] rental expense for operating leases was approximately $ 27.4 million , $ 18.6 million and $ 12.2 million during the years ended december 31 , 2007 , 2006 and 2005 , respectively .
[text_8] we guaranty the residual values of the majority of our truck and equipment operating leases .
[text_9] the residual values decline over the lease terms to a defined percentage of original cost .
[text_10] in the event the lessor does not realize the residual value when a piece of equipment is sold , we would be responsible for a portion of the shortfall .
[text_11] similarly , if the lessor realizes more than the residual value when a piece of equipment is sold , we would be paid the amount realized over the residual value .
[text_12] had we terminated all of our operating leases subject to these guaranties at december 31 , 2007 , the guarantied residual value would have totaled approximately $ 24.0 million .
[text_13] litigation and related contingencies on december 2 , 2005 , ford global technologies , llc ( 2018 2018ford 2019 2019 ) filed a complaint with the united states international trade commission ( 2018 2018usitc 2019 2019 ) against keystone and five other named respondents , including four taiwan-based manufacturers .
[text_14] on december 12 , 2005 , ford filed an amended complaint .
[text_15] both the complaint and the amended complaint contended that keystone and the other respondents infringed 14 design patents that ford alleges cover eight parts on the 2004-2005 .
[table_0] 2008 | $ 42335
[table_1] 2008: 2009 | $ 42335: 33249
[table_2] 2008: 2010 | $ 42335: 25149
[table_3] 2008: 2011 | $ 42335: 17425
[table_4] 2008: 2012 | $ 42335: 11750
[table_5] 2008: thereafter | $ 42335: 28581
[table_6] 2008: future minimum lease payments | $ 42335: $ 158489

Question: what was the percentage change in rental expense from 2005 to 2006?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_7","value":"18.6"},{"source":"text_7","value":"12.2"}]},{"op":"divide","args":["#0",{"source":"text_7","value":"12.2"}]}],"answer":0.5245901639344263}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_7","value":"18.6"},{"source":"text_7","value":"12.2"}]},{"op":"divide","args":["#0",{"source":"text_7","value":"12.2"}]}],"answer":2.5245901639344264}
```

## ETR/2017/page_20.pdf-1

Evidence:
[text_0] the regulatory credit resulting from reduction of the federal corporate income tax rate variance is due to the reduction of the vidalia purchased power agreement regulatory liability by $ 30.5 million and the reduction of the louisiana act 55 financing savings obligation regulatory liabilities by $ 25 million as a result of the enactment of the tax cuts and jobs act , in december 2017 , which lowered the federal corporate income tax rate from 35% ( 35 % ) to 21% ( 21 % ) .
[text_1] the effects of the tax cuts and jobs act are discussed further in note 3 to the financial statements .
[text_2] the grand gulf recovery variance is primarily due to increased recovery of higher operating costs .
[text_3] the louisiana act 55 financing savings obligation variance results from a regulatory charge in 2016 for tax savings to be shared with customers per an agreement approved by the lpsc .
[text_4] the tax savings resulted from the 2010-2011 irs audit settlement on the treatment of the louisiana act 55 financing of storm costs for hurricane gustav and hurricane ike .
[text_5] see note 3 to the financial statements for additional discussion of the settlement and benefit sharing .
[text_6] the volume/weather variance is primarily due to the effect of less favorable weather on residential and commercial sales , partially offset by an increase in industrial usage .
[text_7] the increase in industrial usage is primarily due to new customers in the primary metals industry and expansion projects and an increase in demand for existing customers in the chlor-alkali industry .
[text_8] entergy wholesale commodities following is an analysis of the change in net revenue comparing 2017 to 2016 .
[text_9] amount ( in millions ) .
[text_10] as shown in the table above , net revenue for entergy wholesale commodities decreased by approximately $ 73 million in 2017 primarily due to the absence of net revenue from the fitzpatrick plant after it was sold to exelon in march 2017 and lower volume in the entergy wholesale commodities nuclear fleet resulting from more outage days in 2017 as compared to 2016 .
[text_11] the decrease was partially offset by an increase resulting from the reimbursement agreement with exelon pursuant to which exelon reimbursed entergy for specified out-of-pocket costs associated with preparing for the refueling and operation of fitzpatrick that otherwise would have been avoided had entergy shut down fitzpatrick in january 2017 and a decrease in nuclear fuel expenses primarily related to the impairments of the indian point 2 , indian point 3 , and palisades plants and related assets .
[text_12] revenues received from exelon in 2017 under the reimbursement agreement are offset by other operation and maintenance expenses and taxes other than income taxes and had no effect on net income .
[text_13] see note 14 to the financial statements for discussion of the sale of fitzpatrick , the reimbursement agreement with exelon , and the impairments and related charges .
[text_14] entergy corporation and subsidiaries management 2019s financial discussion and analysis .
[table_0]  | amount ( in millions )
[table_1] : 2016 net revenue | amount ( in millions ): $ 1542
[table_2] : fitzpatrick sale | amount ( in millions ): -158 ( 158 )
[table_3] : nuclear volume | amount ( in millions ): -89 ( 89 )
[table_4] : fitzpatrick reimbursement agreement | amount ( in millions ): 57
[table_5] : nuclear fuel expenses | amount ( in millions ): 108
[table_6] : other | amount ( in millions ): 9
[table_7] : 2017 net revenue | amount ( in millions ): $ 1469

Question: what is the percent change in net revenue from 2016 to 2017?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"1542"},{"source":"table_7","value":"1469"}]},{"op":"divide","args":["#0",{"source":"table_7","value":"1469"}]}],"answer":0.049693669162695714}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"1542"},{"source":"table_7","value":"1469"}]},{"op":"divide","args":["#0",{"source":"table_7","value":"1469"}]}],"answer":2.049693669162696}
```

## ETFC/2007/page_126.pdf-1

Evidence:
[text_0] before the purchase in november 2008 , the units will be reflected in diluted earnings per share calculations using the treasury stock method as defined by sfas no .
[text_1] 128 , earnings per share .
[text_2] under this method , the number of shares of common stock used in calculating diluted earnings per share ( based on the settlement formula applied at the end of the reporting period ) is deemed to be increased by the excess , if any , of the number of shares that would be issued upon settlement of the purchase contracts less the number of shares that could be purchased by the company in the market at the average market price during the period using the proceeds to be received upon settlement .
[text_3] therefore , dilution will occur for periods when the average market price of the company 2019s common stock for the reporting period is above $ 21.816 .
[text_4] senior secured revolving credit facility in september 2005 , the company entered into a $ 250 million , three-year senior secured revolving credit facility .
[text_5] as a result of the citadel investment in november 2007 , the facility was terminated and all unamortized debt issuance costs were expensed .
[text_6] corporate debt covenants certain of the company 2019s corporate debt described above have terms which include customary financial covenants .
[text_7] as of december 31 , 2007 , the company was in compliance with all such covenants .
[text_8] early extinguishment of debt in 2006 , the company called the entire remaining $ 185.2 million principal amount of its 6% ( 6 % ) notes for redemption .
[text_9] the company recorded a $ 0.7 million loss on early extinguishment of debt relating to the write-off of the unamortized debt offering costs .
[text_10] the company did not have any early extinguishments of debt in 2005 .
[text_11] other corporate debt the company also has multiple term loans from financial institutions .
[text_12] these loans are collateralized by equipment and are included within other borrowings on the consolidated balance sheet .
[text_13] see note 14 2014securities sold under agreement to repurchase and other borrowings .
[text_14] future maturities of corporate debt scheduled principal payments of corporate debt as of december 31 , 2007 are as follows ( dollars in thousands ) : years ending december 31 .
[text_15] .
[table_0] 2008 | $ 2014
[table_1] 2008: 2009 | $ 2014: 2014
[table_2] 2008: 2010 | $ 2014: 2014
[table_3] 2008: 2011 | $ 2014: 453815
[table_4] 2008: 2012 | $ 2014: 2014
[table_5] 2008: thereafter | $ 2014: 2996337
[table_6] 2008: total future principal payments of corporate debt | $ 2014: 3450152
[table_7] 2008: unamortized discount net | $ 2014: -427454 ( 427454 )
[table_8] 2008: total corporate debt | $ 2014: $ 3022698

Question: what percentage of total future principal payments of corporate debt are due in 2011?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_3","value":"453815"},{"source":"table_6","value":"3450152"}]}],"answer":0.13153478455441964}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_3","value":"453815"},{"source":"table_6","value":"3450152"}]}],"answer":3903967.0}
```

## RSG/2018/page_13.pdf-1

Evidence:
[text_0] organizational structure a key enabler of the republic way operating model is our organizational structure that fosters a high performance culture by maintaining 360-degree accountability and full profit and loss responsibility with local management , supported by a functional structure to provide subject matter expertise .
[text_1] this structure allows us to take advantage of our scale by coordinating functionally across all of our markets , while empowering local management to respond to unique market dynamics .
[text_2] our senior management evaluates , oversees and manages the financial performance of our operations through two field groups , referred to as group 1 and group 2 .
[text_3] group 1 primarily consists of geographic areas located in the western united states , and group 2 primarily consists of geographic areas located in the southeastern and mid-western united states , and the eastern seaboard of the united states .
[text_4] each field group is organized into several areas and each area contains multiple business units or operating locations .
[text_5] each of our field groups and all of our areas provide collection , transfer , recycling and landfill services .
[text_6] see note 14 , segment reporting , to our consolidated financial statements in item 8 of this form 10-k for further discussion of our operating segments .
[text_7] through this operating model , we have rolled out several productivity and cost control initiatives designed to deliver the best service possible to our customers in an efficient and environmentally sound way .
[text_8] fleet automation approximately 75% ( 75 % ) of our residential routes have been converted to automated single-driver trucks .
[text_9] by converting our residential routes to automated service , we reduce labor costs , improve driver productivity , decrease emissions and create a safer work environment for our employees .
[text_10] additionally , communities using automated vehicles have higher participation rates in recycling programs , thereby complementing our initiative to expand our recycling capabilities .
[text_11] fleet conversion to compressed natural gas ( cng ) approximately 20% ( 20 % ) of our fleet operates on natural gas .
[text_12] we expect to continue our gradual fleet conversion to cng as part of our ordinary annual fleet replacement process .
[text_13] we believe a gradual fleet conversion is the most prudent approach to realizing the full value of our previous fleet investments .
[text_14] approximately 13% ( 13 % ) of our replacement vehicle purchases during 2018 were cng vehicles .
[text_15] we believe using cng vehicles provides us a competitive advantage in communities with strict clean emission initiatives that focus on protecting the environment .
[text_16] although upfront capital costs are higher , using cng reduces our overall fleet operating costs through lower fuel expenses .
[text_17] as of december 31 , 2018 , we operated 37 cng fueling stations .
[text_18] standardized maintenance based on an industry trade publication , we operate the seventh largest vocational fleet in the united states .
[text_19] as of december 31 , 2018 , our average fleet age in years , by line of business , was as follows : approximate number of vehicles approximate average age .
[text_20] onefleet , our standardized vehicle maintenance program , enables us to use best practices for fleet management , truck care and maintenance .
[text_21] through standardization of core functions , we believe we can minimize variability .
[table_0]  | approximate number of vehicles | approximate average age
[table_1] : residential | approximate number of vehicles: 7000 | approximate average age: 7.5
[table_2] : small-container | approximate number of vehicles: 4700 | approximate average age: 7.0
[table_3] : large-container | approximate number of vehicles: 4300 | approximate average age: 8.8
[table_4] : total | approximate number of vehicles: 16000 | approximate average age: 7.7

Question: what is the ratio of the number of vehicles for the residential line of business to large-container

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"7000"},{"source":"table_3","value":"4300"}]}],"answer":1.627906976744186}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"7000"},{"source":"table_3","value":"4300"}]}],"answer":11300.0}
```

## PM/2018/page_24.pdf-1

Evidence:
[text_0] performance graph the graph below compares the cumulative total shareholder return on pmi's common stock with the cumulative total return for the same period of pmi's peer group and the s&p 500 index .
[text_1] the graph assumes the investment of $ 100 as of december 31 , 2013 , in pmi common stock ( at prices quoted on the new york stock exchange ) and each of the indices as of the market close and reinvestment of dividends on a quarterly basis .
[text_2] date pmi pmi peer group ( 1 ) s&p 500 index .
[text_3] ( 1 ) the pmi peer group presented in this graph is the same as that used in the prior year .
[text_4] the pmi peer group was established based on a review of four characteristics : global presence ; a focus on consumer products ; and net revenues and a market capitalization of a similar size to those of pmi .
[text_5] the review also considered the primary international tobacco companies .
[text_6] as a result of this review , the following companies constitute the pmi peer group : altria group , inc. , anheuser-busch inbev sa/nv , british american tobacco p.l.c. , the coca-cola company , colgate-palmolive co. , diageo plc , heineken n.v. , imperial brands plc , japan tobacco inc. , johnson & johnson , kimberly-clark corporation , the kraft-heinz company , mcdonald's corp. , mondel z international , inc. , nestl e9 s.a. , pepsico , inc. , the procter & gamble company , roche holding ag , and unilever nv and plc .
[text_7] note : figures are rounded to the nearest $ 0.10. .
[table_0] date | pmi | pmi peer group ( 1 ) | s&p 500 index
[table_1] date: december 31 2013 | pmi: $ 100.00 | pmi peer group ( 1 ): $ 100.00 | s&p 500 index: $ 100.00
[table_2] date: december 31 2014 | pmi: $ 97.90 | pmi peer group ( 1 ): $ 107.80 | s&p 500 index: $ 113.70
[table_3] date: december 31 2015 | pmi: $ 111.00 | pmi peer group ( 1 ): $ 116.80 | s&p 500 index: $ 115.30
[table_4] date: december 31 2016 | pmi: $ 120.50 | pmi peer group ( 1 ): $ 118.40 | s&p 500 index: $ 129.00
[table_5] date: december 31 2017 | pmi: $ 144.50 | pmi peer group ( 1 ): $ 140.50 | s&p 500 index: $ 157.20
[table_6] date: december 31 2018 | pmi: $ 96.50 | pmi peer group ( 1 ): $ 127.70 | s&p 500 index: $ 150.30

Question: what is the roi of an investment in pmi from 2013 to 2014?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"97.90"},"const_100"]},{"op":"divide","args":["#0","const_100"]}],"answer":-0.021}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"97.90"},"const_100"]},{"op":"divide","args":["#0","const_100"]}],"answer":1.979}
```

## RE/2010/page_42.pdf-4

Evidence:
[text_0] united kingdom .
[text_1] bermuda re 2019s uk branch conducts business in the uk and is subject to taxation in the uk .
[text_2] bermuda re believes that it has operated and will continue to operate its bermuda operation in a manner which will not cause them to be subject to uk taxation .
[text_3] if bermuda re 2019s bermuda operations were to become subject to uk income tax , there could be a material adverse impact on the company 2019s financial condition , results of operations and cash flow .
[text_4] ireland .
[text_5] holdings ireland and ireland re conduct business in ireland and are subject to taxation in ireland .
[text_6] available information .
[text_7] the company 2019s annual reports on form 10-k , quarterly reports on form 10-q , current reports on form 8- k , proxy statements and amendments to those reports are available free of charge through the company 2019s internet website at http://www.everestre.com as soon as reasonably practicable after such reports are electronically filed with the securities and exchange commission ( the 201csec 201d ) .
[text_8] item 1a .
[text_9] risk factors in addition to the other information provided in this report , the following risk factors should be considered when evaluating an investment in our securities .
[text_10] if the circumstances contemplated by the individual risk factors materialize , our business , financial condition and results of operations could be materially and adversely affected and the trading price of our common shares could decline significantly .
[text_11] risks relating to our business fluctuations in the financial markets could result in investment losses .
[text_12] prolonged and severe disruptions in the public debt and equity markets , such as occurred during 2008 , could result in significant realized and unrealized losses in our investment portfolio .
[text_13] for the year ended december 31 , 2008 , we incurred $ 695.8 million of realized investment gains and $ 310.4 million of unrealized investment losses .
[text_14] although financial markets significantly improved during 2009 and 2010 , they could deteriorate in the future and again result in substantial realized and unrealized losses , which could have a material adverse impact on our results of operations , equity , business and insurer financial strength and debt ratings .
[text_15] our results could be adversely affected by catastrophic events .
[text_16] we are exposed to unpredictable catastrophic events , including weather-related and other natural catastrophes , as well as acts of terrorism .
[text_17] any material reduction in our operating results caused by the occurrence of one or more catastrophes could inhibit our ability to pay dividends or to meet our interest and principal payment obligations .
[text_18] subsequent to april 1 , 2010 , we define a catastrophe as an event that causes a loss on property exposures before reinsurance of at least $ 10.0 million , before corporate level reinsurance and taxes .
[text_19] prior to april 1 , 2010 , we used a threshold of $ 5.0 million .
[text_20] by way of illustration , during the past five calendar years , pre-tax catastrophe losses , net of contract specific reinsurance but before cessions under corporate reinsurance programs , were as follows: .
[text_21] .
[table_0] calendar year: | pre-tax catastrophe losses
[table_1] calendar year:: ( dollars in millions ) | pre-tax catastrophe losses: 
[table_2] calendar year:: 2010 | pre-tax catastrophe losses: $ 571.1
[table_3] calendar year:: 2009 | pre-tax catastrophe losses: 67.4
[table_4] calendar year:: 2008 | pre-tax catastrophe losses: 364.3
[table_5] calendar year:: 2007 | pre-tax catastrophe losses: 160.0
[table_6] calendar year:: 2006 | pre-tax catastrophe losses: 287.9

Question: what is the percent change in pre tax catastrophe losses between 2007 and 2008?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_4","value":"364.3"},{"source":"table_5","value":"160.0"}]},{"op":"divide","args":["#0",{"source":"table_5","value":"160.0"}]}],"answer":1.276875}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_4","value":"364.3"},{"source":"table_5","value":"160.0"}]},{"op":"divide","args":["#0",{"source":"table_5","value":"160.0"}]}],"answer":3.276875}
```

## DG/2008/page_86.pdf-1

Evidence:
[text_0] for intangible assets subject to amortization , the estimated aggregate amortization expense for each of the five succeeding fiscal years is as follows : 2009 - $ 41.1 million , 2010 - $ 27.3 million , 2011 - $ 20.9 million , 2012 - $ 17.0 million , and 2013 - $ 12.0 million .
[text_1] fees and expenses related to the merger totaled $ 102.6 million , principally consisting of investment banking fees , legal fees and stock compensation ( $ 39.4 million as further discussed in note 10 ) , and are reflected in the 2007 results of operations .
[text_2] capitalized debt issuance costs as of the merger date of $ 87.4 million for merger-related financing were reflected in other long- term assets in the consolidated balance sheet .
[text_3] the following represents the unaudited pro forma results of the company 2019s consolidated operations as if the merger had occurred on february 3 , 2007 and february 4 , 2006 , respectively , after giving effect to certain adjustments , including the depreciation and amortization of the assets acquired based on their estimated fair values and changes in interest expense resulting from changes in consolidated debt ( in thousands ) : ( in thousands ) year ended february 1 , year ended february 2 .
[text_4] the pro forma information does not purport to be indicative of what the company 2019s results of operations would have been if the acquisition had in fact occurred at the beginning of the periods presented , and is not intended to be a projection of the company 2019s future results of operations .
[text_5] subsequent to the announcement of the merger agreement , the company and its directors , along with other parties , were named in seven putative class actions filed in tennessee state courts alleging claims for breach of fiduciary duty arising out of the proposed merger , all as described more fully under 201clegal proceedings 201d in note 8 below .
[text_6] 3 .
[text_7] strategic initiatives during 2006 , the company began implementing certain strategic initiatives related to its historical inventory management and real estate strategies , as more fully described below .
[text_8] inventory management in november 2006 , the company undertook an initiative to discontinue its historical inventory packaway model for virtually all merchandise by the end of fiscal 2007 .
[text_9] under the packaway model , certain unsold inventory items ( primarily seasonal merchandise ) were stored on-site and returned to the sales floor until the items were eventually sold , damaged or discarded .
[text_10] through end-of-season and other markdowns , this initiative resulted in the elimination of seasonal , home products and basic clothing packaway merchandise to allow for increased levels of newer , current-season merchandise .
[text_11] in connection with this strategic change , in the third quarter of 2006 the company recorded a reserve for lower of cost or market inventory .
[table_0] ( in thousands ) | year endedfebruary 12008 | year endedfebruary 22007
[table_1] ( in thousands ): revenue | year endedfebruary 12008: $ 9495246 | year endedfebruary 22007: $ 9169822
[table_2] ( in thousands ): net loss | year endedfebruary 12008: -57939 ( 57939 ) | year endedfebruary 22007: ( 156188 )

Question: what is the growth rate of revenue from 2007 to 2008?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"9495246"},{"source":"table_1","value":"9169822"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"9169822"}]}],"answer":0.035488584184076855}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"9495246"},{"source":"table_1","value":"9169822"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"9169822"}]}],"answer":2.035488584184077}
```

## GS/2013/page_91.pdf-4

Evidence:
[text_0] management 2019s discussion and analysis we believe our credit ratings are primarily based on the credit rating agencies 2019 assessment of : 2030 our liquidity , market , credit and operational risk management practices ; 2030 the level and variability of our earnings ; 2030 our capital base ; 2030 our franchise , reputation and management ; 2030 our corporate governance ; and 2030 the external operating environment , including the assumed level of government support .
[text_1] certain of the firm 2019s derivatives have been transacted under bilateral agreements with counterparties who may require us to post collateral or terminate the transactions based on changes in our credit ratings .
[text_2] we assess the impact of these bilateral agreements by determining the collateral or termination payments that would occur assuming a downgrade by all rating agencies .
[text_3] a downgrade by any one rating agency , depending on the agency 2019s relative ratings of the firm at the time of the downgrade , may have an impact which is comparable to the impact of a downgrade by all rating agencies .
[text_4] we allocate a portion of our gce to ensure we would be able to make the additional collateral or termination payments that may be required in the event of a two-notch reduction in our long-term credit ratings , as well as collateral that has not been called by counterparties , but is available to them .
[text_5] the table below presents the additional collateral or termination payments related to our net derivative liabilities under bilateral agreements that could have been called at the reporting date by counterparties in the event of a one-notch and two-notch downgrade in our credit ratings. .
[text_6] in millions 2013 2012 additional collateral or termination payments for a one-notch downgrade $ 911 $ 1534 additional collateral or termination payments for a two-notch downgrade 2989 2500 cash flows as a global financial institution , our cash flows are complex and bear little relation to our net earnings and net assets .
[text_7] consequently , we believe that traditional cash flow analysis is less meaningful in evaluating our liquidity position than the excess liquidity and asset-liability management policies described above .
[text_8] cash flow analysis may , however , be helpful in highlighting certain macro trends and strategic initiatives in our businesses .
[text_9] year ended december 2013 .
[text_10] our cash and cash equivalents decreased by $ 11.54 billion to $ 61.13 billion at the end of 2013 .
[text_11] we generated $ 4.54 billion in net cash from operating activities .
[text_12] we used net cash of $ 16.08 billion for investing and financing activities , primarily to fund loans held for investment and repurchases of common stock .
[text_13] year ended december 2012 .
[text_14] our cash and cash equivalents increased by $ 16.66 billion to $ 72.67 billion at the end of 2012 .
[text_15] we generated $ 9.14 billion in net cash from operating and investing activities .
[text_16] we generated $ 7.52 billion in net cash from financing activities from an increase in bank deposits , partially offset by net repayments of unsecured and secured long-term borrowings .
[text_17] year ended december 2011 .
[text_18] our cash and cash equivalents increased by $ 16.22 billion to $ 56.01 billion at the end of 2011 .
[text_19] we generated $ 23.13 billion in net cash from operating and investing activities .
[text_20] we used net cash of $ 6.91 billion for financing activities , primarily for repurchases of our series g preferred stock and common stock , partially offset by an increase in bank deposits .
[text_21] goldman sachs 2013 annual report 89 .
[table_0] in millions | as of december 2013 | as of december 2012
[table_1] in millions: additional collateral or termination payments for a one-notch downgrade | as of december 2013: $ 911 | as of december 2012: $ 1534
[table_2] in millions: additional collateral or termination payments for a two-notch downgrade | as of december 2013: 2989 | as of december 2012: 2500

Question: what is the difference in millions , between additional collateral or termination payments for a two-notch downgrade and additional collateral or termination payments for a one-notch downgrade at the end of december 2013?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_2","value":"2989"},{"source":"table_1","value":"911"}]}],"answer":2078.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"2989"},{"source":"table_1","value":"911"}]}],"answer":3900.0}
```

## RSG/2014/page_22.pdf-1

Evidence:
[text_0] standardized maintenance based on an industry trade publication , we operate the eighth largest vocational fleet in the united states .
[text_1] as of december 31 , 2014 , our average fleet age in years , by line of business , was as follows : approximate number of vehicles approximate average age .
[text_2] through standardization of core functions , we believe we can minimize variability in our maintenance processes resulting in higher vehicle quality while extending the service life of our fleet .
[text_3] we believe operating a more reliable , safer and efficient fleet will lower our operating costs .
[text_4] we have implemented standardized maintenance programs for approximately 60% ( 60 % ) of our fleet maintenance operations as of december 31 , 2014 .
[text_5] cash utilization strategy key components of our cash utilization strategy include increasing free cash flow and improving our return on invested capital .
[text_6] our definition of free cash flow , which is not a measure determined in accordance with united states generally accepted accounting principles ( u.s .
[text_7] gaap ) , is cash provided by operating activities less purchases of property and equipment , plus proceeds from sales of property and equipment as presented in our consolidated statements of cash flows .
[text_8] for a discussion and reconciliation of free cash flow , you should read the 201cfree cash flow 201d section of our management 2019s discussion and analysis of financial condition and results of operations contained in item 7 of this form 10-k .
[text_9] we believe free cash flow drives shareholder value and provides useful information regarding the recurring cash provided by our operations .
[text_10] free cash flow also demonstrates our ability to execute our cash utilization strategy , which includes investments in acquisitions and returning a majority of free cash flow to our shareholders through dividends and share repurchases .
[text_11] we are committed to an efficient capital structure and maintaining our investment grade credit ratings .
[text_12] we manage our free cash flow by ensuring that capital expenditures and operating asset levels are appropriate in light of our existing business and growth opportunities , and by closely managing our working capital , which consists primarily of accounts receivable , accounts payable , and accrued landfill and environmental costs .
[text_13] dividends in july 2003 , our board of directors initiated a quarterly cash dividend of $ 0.04 per share .
[text_14] our quarterly dividend has increased from time to time thereafter , the latest increase occurring in july 2014 to $ 0.28 per share , representing a 7.7% ( 7.7 % ) increase over that of the prior year .
[text_15] over the last 5 years , our dividend has increased at a compounded annual growth rate of 8.1% ( 8.1 % ) .
[text_16] we expect to continue paying quarterly cash dividends and may consider additional dividend increases if we believe they will enhance shareholder value .
[text_17] share repurchases in october 2013 , our board of directors added $ 650 million to the existing share repurchase authorization originally approved in november 2010 .
[text_18] from november 2010 to december 31 , 2014 , we used $ 1439.5 million to repurchase 46.6 million shares of our common stock at a weighted average cost per share of $ 30.88 .
[text_19] as of december 31 , 2014 , there were $ 360.2 million remaining under our share repurchase authorization .
[text_20] during 2015 , we expect to use our remaining authorization to repurchase more of our outstanding common stock. .
[table_0]  | approximate number of vehicles | approximate average age
[table_1] : residential | approximate number of vehicles: 7600 | approximate average age: 7
[table_2] : commercial | approximate number of vehicles: 4300 | approximate average age: 7
[table_3] : industrial | approximate number of vehicles: 3900 | approximate average age: 9
[table_4] : total | approximate number of vehicles: 15800 | approximate average age: 7.5

Question: what is the percent of the residential vehicles as part of the fleet

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"7600"},{"source":"table_4","value":"15800"}]}],"answer":0.4810126582278481}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"7600"},{"source":"table_4","value":"15800"}]}],"answer":23400.0}
```

## AON/2015/page_96.pdf-4

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"multiply","args":[{"source":"text_6","value":"9"},"const_1000000"]},{"op":"divide","args":["#0",{"source":"text_5","value":"411636"}]}],"answer":21.863976911640382}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_6","value":"9"},"const_1000000"]},{"op":"divide","args":["#0",{"source":"text_5","value":"411636"}]}],"answer":2.429352631936954}
```

## TFX/2018/page_47.pdf-1

Evidence:
[text_0] part a0ii item a05 .
[text_1] market for registrant 2019s common equity , related stockholder matters and issuer purchases of equity securities our common stock is listed on the new york stock exchange under the symbol 201ctfx . 201d as of february 19 , 2019 , we had 473 holders of record of our common stock .
[text_2] a substantially greater number of holders of our common stock are beneficial owners whose shares are held by brokers and other financial institutions for the accounts of beneficial owners .
[text_3] stock performance graph the following graph provides a comparison of five year cumulative total stockholder returns of teleflex common stock , the standard a0& poor 2019s ( s&p ) 500 stock index and the s&p 500 healthcare equipment & supply index .
[text_4] the annual changes for the five-year period shown on the graph are based on the assumption that $ 100 had been invested in teleflex common stock and each index on december a031 , 2013 and that all dividends were reinvested .
[text_5] market performance .
[text_6] s&p 500 healthcare equipment & supply index 100 126 134 142 186 213 .
[table_0] company / index | 2013 | 2014 | 2015 | 2016 | 2017 | 2018
[table_1] company / index: teleflex incorporated | 2013: 100 | 2014: 124 | 2015: 143 | 2016: 177 | 2017: 275 | 2018: 288
[table_2] company / index: s&p 500 index | 2013: 100 | 2014: 114 | 2015: 115 | 2016: 129 | 2017: 157 | 2018: 150
[table_3] company / index: s&p 500 healthcare equipment & supply index | 2013: 100 | 2014: 126 | 2015: 134 | 2016: 142 | 2017: 186 | 2018: 213

Question: what is the roi of an investment in teleflex incorporated from 2013 to 2014?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"124"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100"}]}],"answer":0.24}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"124"},{"source":"table_1","value":"100"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"100"}]}],"answer":2.24}
```

## UPS/2009/page_84.pdf-1

Evidence:
[text_0] united parcel service , inc .
[text_1] and subsidiaries notes to consolidated financial statements 2014 ( continued ) a discount rate is used to determine the present value of our future benefit obligations .
[text_2] in 2008 and prior years , the discount rate for u.s .
[text_3] plans was determined by matching the expected cash flows to a yield curve based on long-term , high quality fixed income debt instruments available as of the measurement date .
[text_4] in 2008 , we reduced the population of bonds from which the yield curve was developed to better reflect bonds we would more likely consider to settle our obligations .
[text_5] in 2009 , we further enhanced this process for plans in the u.s .
[text_6] by using a bond matching approach to select specific bonds that would satisfy our projected benefit payments .
[text_7] we believe the bond matching approach more closely reflects the process we would employ to settle our pension and postretirement benefit obligations .
[text_8] these modifications had an impact of increasing the pension benefits and postretirement medical benefits discount rate on average 31 and 51 basis points for 2009 and 25 and 17 basis points for 2008 .
[text_9] for 2009 , each basis point increase in the discount rate decreases the projected benefit obligation by approximately $ 25 million and $ 3 million for pension and postretirement medical benefits , respectively .
[text_10] for our international plans , the discount rate is selected based on high quality fixed income indices available in the country in which the plan is domiciled .
[text_11] these assumptions are updated annually .
[text_12] an assumption for expected return on plan assets is used to determine a component of net periodic benefit cost for the fiscal year .
[text_13] this assumption for our u.s .
[text_14] plans was developed using a long-term projection of returns for each asset class , and taking into consideration our target asset allocation .
[text_15] the expected return for each asset class is a function of passive , long-term capital market assumptions and excess returns generated from active management .
[text_16] the capital market assumptions used are provided by independent investment advisors , while excess return assumptions are supported by historical performance , fund mandates and investment expectations .
[text_17] in addition , we compare the expected return on asset assumption with the average historical rate of return these plans have been able to generate .
[text_18] for the ups retirement plan , we use a market-related valuation method for recognizing investment gains or losses .
[text_19] investment gains or losses are the difference between the expected and actual return based on the market- related value of assets .
[text_20] this method recognizes investment gains or losses over a five year period from the year in which they occur , which reduces year-to-year volatility in pension expense .
[text_21] our expense in future periods will be impacted as gains or losses are recognized in the market-related value of assets .
[text_22] for plans outside the u.s. , consideration is given to local market expectations of long-term returns .
[text_23] strategic asset allocations are determined by country , based on the nature of liabilities and considering the demographic composition of the plan participants .
[text_24] health care cost trends are used to project future postretirement benefits payable from our plans .
[text_25] for year-end 2009 u.s .
[text_26] plan obligations , future postretirement medical benefit costs were forecasted assuming an initial annual increase of 8.0% ( 8.0 % ) , decreasing to 5.0% ( 5.0 % ) by the year 2016 and with consistent annual increases at those ultimate levels thereafter .
[text_27] assumed health care cost trends have a significant effect on the amounts reported for the u.s .
[text_28] postretirement medical plans .
[text_29] a one-percent change in assumed health care cost trend rates would have the following effects ( in millions ) : .
[text_30] .
[table_0]  | 1% ( 1 % ) increase | 1% ( 1 % ) decrease
[table_1] : effect on total of service cost and interest cost | 1% ( 1 % ) increase: $ 10 | 1% ( 1 % ) decrease: $ -10 ( 10 )
[table_2] : effect on postretirement benefit obligation | 1% ( 1 % ) increase: $ 83 | 1% ( 1 % ) decrease: $ -87 ( 87 )

Question: what is the current total of service cost and interest cost?

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"10"},{"source":"table_1","value":"1%"}]}],"answer":1000.0}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"10"},{"source":"table_1","value":"1%"}]}],"answer":10.01}
```

## RCL/2018/page_38.pdf-1

Evidence:
[text_0] table of contents performance graph the following graph compares the total return , assuming reinvestment of dividends , on an investment in the company , based on performance of the company's common stock , with the total return of the standard & poor's 500 composite stock index ( "s&p 500" ) and the dow jones united states travel and leisure index for a five year period by measuring the changes in common stock prices from december 31 , 2013 to december 31 , 2018. .
[text_1] the stock performance graph assumes for comparison that the value of the company's common stock and of each index was $ 100 on december 31 , 2013 and that all dividends were reinvested .
[text_2] past performance is not necessarily an indicator of future results. .
[table_0]  | 12/13 | 12/14 | 12/15 | 12/16 | 12/17 | 12/18
[table_1] : royal caribbean cruises ltd . | 12/13: 100.00 | 12/14: 176.94 | 12/15: 220.72 | 12/16: 182.99 | 12/17: 271.25 | 12/18: 227.46
[table_2] : s&p 500 | 12/13: 100.00 | 12/14: 113.69 | 12/15: 115.26 | 12/16: 129.05 | 12/17: 157.22 | 12/18: 150.33
[table_3] : dow jones u.s . travel & leisure | 12/13: 100.00 | 12/14: 116.37 | 12/15: 123.23 | 12/16: 132.56 | 12/17: 164.13 | 12/18: 154.95

Question: what was the percentage change in the royal caribbean cruises ltd . performance from 2014 to 2015

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"220.72"},{"source":"table_1","value":"176.94"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"176.94"}]}],"answer":0.2474285068384763}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"220.72"},{"source":"table_1","value":"176.94"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"176.94"}]}],"answer":2.2474285068384763}
```

## ETR/2016/page_17.pdf-3

Evidence:
[text_0] entergy corporation and subsidiaries management 2019s financial discussion and analysis palisades plants and related assets to their fair values .
[text_1] see note 14 to the financial statements for further discussion of the impairment and related charges .
[text_2] as a result of the entergy louisiana and entergy gulf states louisiana business combination , results of operations for 2015 also include two items that occurred in october 2015 : 1 ) a deferred tax asset and resulting net increase in tax basis of approximately $ 334 million and 2 ) a regulatory liability of $ 107 million ( $ 66 million net-of-tax ) as a result of customer credits to be realized by electric customers of entergy louisiana , consistent with the terms of the stipulated settlement in the business combination proceeding .
[text_3] see note 2 to the financial statements for further discussion of the business combination and customer credits .
[text_4] results of operations for 2015 also include the sale in december 2015 of the 583 mw rhode island state energy center for a realized gain of $ 154 million ( $ 100 million net-of-tax ) on the sale and the $ 77 million ( $ 47 million net-of-tax ) write-off and regulatory charges to recognize that a portion of the assets associated with the waterford 3 replacement steam generator project is no longer probable of recovery .
[text_5] see note 14 to the financial statements for further discussion of the rhode island state energy center sale .
[text_6] see note 2 to the financial statements for further discussion of the waterford 3 write-off .
[text_7] net revenue utility following is an analysis of the change in net revenue comparing 2016 to 2015 .
[text_8] amount ( in millions ) .
[text_9] the retail electric price variance is primarily due to : 2022 an increase in base rates at entergy arkansas , as approved by the apsc .
[text_10] the new rates were effective february 24 , 2016 and began billing with the first billing cycle of april 2016 .
[text_11] the increase includes an interim base rate adjustment surcharge , effective with the first billing cycle of april 2016 , to recover the incremental revenue requirement for the period february 24 , 2016 through march 31 , 2016 .
[text_12] a significant portion of the increase is related to the purchase of power block 2 of the union power station ; 2022 an increase in the purchased power and capacity acquisition cost recovery rider for entergy new orleans , as approved by the city council , effective with the first billing cycle of march 2016 , primarily related to the purchase of power block 1 of the union power station ; 2022 an increase in formula rate plan revenues for entergy louisiana , implemented with the first billing cycle of march 2016 , to collect the estimated first-year revenue requirement related to the purchase of power blocks 3 and 4 of the union power station ; and 2022 an increase in revenues at entergy mississippi , as approved by the mpsc , effective with the first billing cycle of july 2016 , and an increase in revenues collected through the storm damage rider .
[text_13] see note 2 to the financial statements for further discussion of the rate proceedings .
[text_14] see note 14 to the financial statements for discussion of the union power station purchase .
[text_15] the louisiana business combination customer credits variance is due to a regulatory liability of $ 107 million recorded by entergy in october 2015 as a result of the entergy gulf states louisiana and entergy louisiana business .
[table_0]  | amount ( in millions )
[table_1] : 2015 net revenue | amount ( in millions ): $ 5829
[table_2] : retail electric price | amount ( in millions ): 289
[table_3] : louisiana business combination customer credits | amount ( in millions ): 107
[table_4] : volume/weather | amount ( in millions ): 14
[table_5] : louisiana act 55 financing savings obligation | amount ( in millions ): -17 ( 17 )
[table_6] : other | amount ( in millions ): -43 ( 43 )
[table_7] : 2016 net revenue | amount ( in millions ): $ 6179

Question: what is the percent change in net revenue from 2015 to 2016?

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_7","value":"6179"},{"source":"table_1","value":"5829"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"5829"}]}],"answer":0.06004460456338995}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_7","value":"6179"},{"source":"table_1","value":"5829"}]},{"op":"divide","args":["#0",{"source":"table_1","value":"5829"}]}],"answer":2.06004460456339}
```

## C/2010/page_223.pdf-3

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

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"table_1","value":"920"},{"source":"table_1","value":"95"}]},{"op":"subtract","args":[{"source":"table_8","value":"469"},{"source":"table_8","value":"77"}]},{"op":"subtract","args":["#1","#0"]},{"op":"divide","args":["#2","#0"]}],"answer":-0.5248484848484849}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"920"},{"source":"table_1","value":"95"}]},{"op":"subtract","args":[{"source":"table_8","value":"469"},{"source":"table_8","value":"77"}]},{"op":"subtract","args":["#1","#0"]},{"op":"divide","args":["#2","#0"]}],"answer":-0.6137931034482759}
```

## DVN/2014/page_88.pdf-3

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

Question: what is the ratio of the floating rate due december 2015 compared to 2016

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_1","value":"500"},{"source":"table_1","value":"350"}]}],"answer":1.4285714285714286}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_1","value":"500"},{"source":"table_1","value":"350"}]}],"answer":850.0}
```

## VLO/2016/page_23.pdf-1

Evidence:
[text_0] table of contents the following table discloses purchases of shares of our common stock made by us or on our behalf during the fourth quarter of 2016 .
[text_1] period total number of shares purchased average price paid per share total number of shares not purchased as part of publicly announced plans or programs ( a ) total number of shares purchased as part of publicly announced plans or programs approximate dollar value of shares that may yet be purchased under the plans or programs ( b ) .
[text_2] ( a ) the shares reported in this column represent purchases settled in the fourth quarter of 2016 relating to ( i ) our purchases of shares in open-market transactions to meet our obligations under stock-based compensation plans , and ( ii ) our purchases of shares from our employees and non-employee directors in connection with the exercise of stock options , the vesting of restricted stock , and other stock compensation transactions in accordance with the terms of our stock-based compensation plans .
[text_3] ( b ) on july 13 , 2015 , we announced that our board of directors authorized our purchase of up to $ 2.5 billion of our outstanding common stock .
[text_4] this authorization has no expiration date .
[text_5] as of december 31 , 2016 , the approximate dollar value of shares that may yet be purchased under the 2015 authorization is $ 40 million .
[text_6] on september 21 , 2016 , we announced that our board of directors authorized our purchase of up to an additional $ 2.5 billion of our outstanding common stock with no expiration date .
[text_7] as of december 31 , 2016 , no purchases have been made under the 2016 authorization. .
[table_0] period | total numberof sharespurchased | averageprice paidper share | total number ofshares notpurchased as part ofpublicly announcedplans or programs ( a ) | total number ofshares purchased aspart of publiclyannounced plans orprograms | approximate dollarvalue of shares thatmay yet be purchasedunder the plans orprograms ( b )
[table_1] period: october 2016 | total numberof sharespurchased: 433272 | averageprice paidper share: $ 52.69 | total number ofshares notpurchased as part ofpublicly announcedplans or programs ( a ): 50337 | total number ofshares purchased aspart of publiclyannounced plans orprograms: 382935 | approximate dollarvalue of shares thatmay yet be purchasedunder the plans orprograms ( b ): $ 2.7 billion
[table_2] period: november 2016 | total numberof sharespurchased: 667644 | averageprice paidper share: $ 62.25 | total number ofshares notpurchased as part ofpublicly announcedplans or programs ( a ): 248349 | total number ofshares purchased aspart of publiclyannounced plans orprograms: 419295 | approximate dollarvalue of shares thatmay yet be purchasedunder the plans orprograms ( b ): $ 2.6 billion
[table_3] period: december 2016 | total numberof sharespurchased: 1559569 | averageprice paidper share: $ 66.09 | total number ofshares notpurchased as part ofpublicly announcedplans or programs ( a ): 688 | total number ofshares purchased aspart of publiclyannounced plans orprograms: 1558881 | approximate dollarvalue of shares thatmay yet be purchasedunder the plans orprograms ( b ): $ 2.5 billion
[table_4] period: total | total numberof sharespurchased: 2660485 | averageprice paidper share: $ 62.95 | total number ofshares notpurchased as part ofpublicly announcedplans or programs ( a ): 299374 | total number ofshares purchased aspart of publiclyannounced plans orprograms: 2361111 | approximate dollarvalue of shares thatmay yet be purchasedunder the plans orprograms ( b ): $ 2.5 billion

Question: for the quarter ended december 31 , 2016 what was the percent of the total number of shares purchased in november

Chosen:
```json
{"abstain":false,"steps":[{"op":"divide","args":[{"source":"table_2","value":"667644"},{"source":"table_4","value":"2660485"}]}],"answer":0.25094822936419486}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"table_2","value":"667644"},{"source":"table_4","value":"2660485"}]}],"answer":3328129.0}
```

## RSG/2015/page_142.pdf-2

Evidence:
[text_0] republic services , inc .
[text_1] notes to consolidated financial statements 2014 ( continued ) 16 .
[text_2] financial instruments fuel hedges we have entered into multiple swap agreements designated as cash flow hedges to mitigate some of our exposure related to changes in diesel fuel prices .
[text_3] these swaps qualified for , and were designated as , effective hedges of changes in the prices of forecasted diesel fuel purchases ( fuel hedges ) .
[text_4] the following table summarizes our outstanding fuel hedges as of december 31 , 2015 : year gallons hedged weighted average contract price per gallon .
[text_5] if the national u.s .
[text_6] on-highway average price for a gallon of diesel fuel as published by the department of energy exceeds the contract price per gallon , we receive the difference between the average price and the contract price ( multiplied by the notional gallons ) from the counterparty .
[text_7] if the average price is less than the contract price per gallon , we pay the difference to the counterparty .
[text_8] the fair values of our fuel hedges are determined using standard option valuation models with assumptions about commodity prices based on those observed in underlying markets ( level 2 in the fair value hierarchy ) .
[text_9] the aggregate fair values of our outstanding fuel hedges as of december 31 , 2015 and 2014 were current liabilities of $ 37.8 million and $ 34.4 million , respectively , and have been recorded in other accrued liabilities in our consolidated balance sheets .
[text_10] the ineffective portions of the changes in fair values resulted in a loss of $ 0.4 million and $ 0.5 million for the years ended december 31 , 2015 and 2014 respectively , and a gain of less than $ 0.1 million for the year ended december 31 , 2013 , and have been recorded in other income , net in our consolidated statements of income .
[text_11] total ( loss ) gain recognized in other comprehensive ( loss ) income for fuel hedges ( the effective portion ) was $ ( 2.0 ) million , $ ( 24.2 ) million and $ 2.4 million , for the years ended december 31 , 2015 , 2014 and 2013 , respectively .
[text_12] recycling commodity hedges revenue from the sale of recycled commodities is primarily from sales of old corrugated cardboard and old newspaper .
[text_13] from time to time we use derivative instruments such as swaps and costless collars designated as cash flow hedges to manage our exposure to changes in prices of these commodities .
[text_14] we had no outstanding recycling commodity hedges as of december 31 , 2015 and 2014 .
[text_15] no amounts were recognized in other income , net in our consolidated statements of income for the ineffective portion of the changes in fair values during the years ended december 31 , 2015 , 2014 and 2013 .
[text_16] total gain ( loss ) recognized in other comprehensive income for recycling commodity hedges ( the effective portion ) was $ 0.1 million and $ ( 0.1 ) million for the years ended december 31 , 2014 and 2013 , respectively .
[text_17] no amount was recognized in other comprehensive income for 2015 .
[text_18] fair value measurements in measuring fair values of assets and liabilities , we use valuation techniques that maximize the use of observable inputs ( level 1 ) and minimize the use of unobservable inputs ( level 3 ) .
[text_19] we also use market data or assumptions that we believe market participants would use in pricing an asset or liability , including assumptions about risk when appropriate. .
[table_0] year | gallons hedged | weighted average contractprice per gallon
[table_1] year: 2016 | gallons hedged: 27000000 | weighted average contractprice per gallon: $ 3.57
[table_2] year: 2017 | gallons hedged: 12000000 | weighted average contractprice per gallon: 2.92

Question: what is the percentage growth of the aggregate fair values of our outstanding fuel hedge for 2014 to 2015

Chosen:
```json
{"abstain":false,"steps":[{"op":"subtract","args":[{"source":"text_9","value":"37.8"},{"source":"text_9","value":"34.4"}]},{"op":"divide","args":["#0",{"source":"text_9","value":"34.4"}]}],"answer":0.09883720930232558}
```
Rejected:
```json
{"abstain":false,"steps":[{"op":"add","args":[{"source":"text_9","value":"37.8"},{"source":"text_9","value":"34.4"}]},{"op":"divide","args":["#0",{"source":"text_9","value":"34.4"}]}],"answer":2.0988372093023258}
```
