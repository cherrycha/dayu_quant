# dayu_quant


## 要实现的因子
| 因子         |                    公式                    |   描述 | 类型    |
| ---------- | :--------------------------------------: | ---: | ----- |
| alpha171   | ((-1 * ((LOW - CLOSE) * (OPEN^5))) / ((CLOSE - HIGH) * (CLOSE^5))) |      |       |
| alpha145   | (MEAN(VOLUME,9)-MEAN(VOLUME,26))/MEAN(VOLUME,12)*100 |      |       |
| alpha140   | MIN(RANK(DECAYLINEAR(((RANK(OPEN)+RANK(LOW))-RANK(HIGH)+RANK(CLOSE))),8)),TSRANK(DECAYLINEAR(CORR(TSRANK(CLOSE, 8), TSRANK(MEAN(VOLUME,60), 20), 8), 7), 3)) |      |       |
| DilutedEPS | 稀释每股收益（Diluted earnings per share）。属于每股指标类因子。数据更新时间：T日21点30分。 |      | 每股指标  |
| MTM        | 动量指标（Momentom Index），动量指数以分析股价波动的速度为目的，研究股价在波动过程中各种加速，减速，惯性作用以及股价由静到动或由动转静的现象。属于常用技术指标类因子。数据更新时间：T日17点00分。 |      | 趋势型   |
| Mfi        | 资金流量指标（Money Flow Index），该指标是通过反映股价变动的四个元素：上涨的天数、下跌的天数、成交量增加幅度、成交量减少幅度来研判量能的趋势，预测市场供求关系和买卖力道。属于常用技术指标类因子。数据更新时间：T日17点00分。 |      | 超买超卖型 |
| CMO        | 钱德动量摆动指标（Chande Momentum Osciliator），与其他动量指标摆动指标如相对强弱指标（RSI）和随机指标（KDJ）不同，钱德动量指标在计算公式的分子中采用上涨日和下跌日的数据。属于动量类因子。数据更新时间：T日17点00分。 |      | 动量    |
| SUOI       | 未预期毛利（Standardized unexpected gross income）。属于成长类因子。数据更新时间：T日21点30分。 |      | 历史成长  |