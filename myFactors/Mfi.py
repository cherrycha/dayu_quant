# encoding: utf-8
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'ZhaYue' # 这里填下你的名字
default_params =  {'N': 10} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'N': "天数"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    资金流量指标（Money Flow Index），该指标是通过反映股价变动的四个元素：上涨的天数、下跌的天数、成交量增加幅度、成交量减少幅度来研判量能的趋势，预测市场供求关系和买卖力道。
    """
    N = 14
    dv.add_formula('TYP', "(close_adj+high_adj+low_adj)/3", is_quarterly=False,add_data=True)
    dv.add_formula('MF', "TYP*volume", is_quarterly=False,add_data=True)
    dv.add_formula('MR',
                   "Ts_Sum(If(Delta(TYP,1)>0,TYP*MF,0),%s)/Ts_Sum(If(Delta(TYP,1)<0,TYP*MF,0),%s)" % (params['N'], params['N']),
                   is_quarterly=False,add_data=True)
    Mfi = dv.add_formula('Mfi', "100-100/(1+MR)", is_quarterly=False)
    return Mfi