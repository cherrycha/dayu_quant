# encoding: utf-8
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'ZhaYue' # 这里填下你的名字
default_params =  {'N': 20}# 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'N': "天数"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    钱德动量摆动指标（Chande Momentum Osciliator），与其他动量指标摆动指标如相对强弱指标（RSI）和随机指标（KDJ）不同，钱德动量指标在计算公式的分子中采用上涨日和下跌日的数据。
    计算方法：
    SU是今日收盘价与昨日收盘价（上涨日）差值加总。若当日下跌，则增加值为0；
    SD是今日收盘价与昨日收盘价（下跌日）差值的绝对值加总。若当日上涨，则增加值为0。
    N取20。
    """
    dv.add_formula('SU', "Ts_Sum(If(Delta(close_adj,1)>0,close_adj-Delay(close_adj, 1),0),%s)" % (params['N']), is_quarterly=False,add_data=True)
    dv.add_formula('SD', "Ts_Sum(If(Delta(close_adj,1)<0,Delay(close_adj, 1)-close_adj,0),%s)" % (params['N']), is_quarterly=False,add_data=True)
    CMO=dv.add_formula('CMO', "(SU-SD)/(SU+SD)*100", is_quarterly=False)
    return CMO