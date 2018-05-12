# encoding: utf-8
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'ZhaYue' # 这里填下你的名字
default_params ={'N': 10} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'N': "天数，默认为10"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    动量指标（Momentom Index）。动量指数以分析股价波动的速度为目的，研究股价在波动过程中各种加速，减速，惯性作用以及股价由静到动或由动转静的现象。
    """

    MTM = dv.add_formula('MTM', "Delta(close_adj,%s)"%(params['N']), is_quarterly=False)
    return MTM