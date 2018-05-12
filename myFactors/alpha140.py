# encoding: utf-8
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'ZhaYue' # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    MIN(RANK(DECAYLINEAR(((RANK(OPEN)+RANK(LOW))-RANK(HIGH)+RANK(CLOSE))),8)),TSRANK(DECAYLINEAR(CORR(TSRANK(CLOSE, 8), TSRANK(MEAN(VOLUME,60), 20), 8), 7), 3))
    """
    alpha140 = dv.add_formula('alpha140',
                              "Min(Rank(Decay_linear(((Rank(open_adj)+Rank(low_adj))-Rank(high_adj)+Rank(close_adj),8))),Ts_Rank(Decay_linear(Correlation(Ts_Rank(close_adj, 8), Ts_Rank(Ts_Mean(volume,60), 20), 8), 7), 3))",
                              is_quarterly=False)
    return alpha140