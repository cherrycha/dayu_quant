# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'ZhaYue' # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    成交量的20日方差，取相反数
    """
    cherrycha4 = dv.add_formula('cherrycha4', "-StdDev(turnover,20)*StdDev(turnover,20)"%(),
        is_quarterly=False, add_data=True)
    return cherrycha4
