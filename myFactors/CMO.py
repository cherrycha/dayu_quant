def run_formula(dv, param = None):
    defult_param = {'N': 20}
    if not param:
        param = defult_param
    dv.add_formula('SU', "Ts_Sum(If(Delta(close_adj,1)>0,close_adj-Delay(close_adj, 1),0),%s)" % (param['N']), is_quarterly=False,add_data=True)
    dv.add_formula('SD', "Ts_Sum(If(Delta(close_adj,1)<0,Delay(close_adj, 1)-close_adj,0),%s)" % (param['N']), is_quarterly=False,add_data=True)
    CMO=dv.add_formula('CMO', "(SU-SD)/(SU+SD)*100", is_quarterly=False)
    return CMO