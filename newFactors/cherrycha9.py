# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'ZhaYue' # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    威廉变异离散量的20日均值
    """
    cherrycha9 = dv.add_formula('cherrycha9', "-Ts_Mean((close_adj-open_adj)/(high_adj-low_adj)*volume,20)"%(),
        is_quarterly=False, add_data=True)
    return cherrycha9
