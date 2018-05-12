
# encoding: utf-8
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'ZhaYue' # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    ((-1 * ((LOW - CLOSE) * (OPEN^5))) / ((CLOSE - HIGH) * (CLOSE^5)))
    """
    alpha171 = dv.add_formula('alpha171',
                              "((-1 * ((low_adj - close_adj) * (open_adj^5))) / ((close_adj - high_adj) * (close_adj^5)))",
                              is_quarterly=False)
    return alpha171