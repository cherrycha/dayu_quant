# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'ZhaYue' # 这里填下你的名字
default_params = {'t1': 20} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    收盘价的20日均值除以收盘价
    """
    cherrycha5 = dv.add_formula('cherrycha5', "Ts_Mean(close_adj,%s)/close_adj"%(params['t1']),
        is_quarterly=False, add_data=True)
    return cherrycha5
