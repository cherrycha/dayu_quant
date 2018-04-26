def run_formula(dv, param = None):
    defult_param = {'N': 10}
    if not param:
        param = defult_param
    N = 14
    dv.add_formula('TYP', "(close_adj+high_adj+low_adj)/3", is_quarterly=False,add_data=True)
    dv.add_formula('MF', "TYP*volume", is_quarterly=False,add_data=True)
    dv.add_formula('MR',
                   "Ts_Sum(If(Delta(TYP,1)>0,TYP*MF,0),%s)/Ts_Sum(If(Delta(TYP,1)<0,TYP*MF,0),%s)" % (param['N'], param['N']),
                   is_quarterly=False,add_data=True)
    Mfi = dv.add_formula('Mfi', "100-100/(1+MR)", is_quarterly=False)
    return Mfi