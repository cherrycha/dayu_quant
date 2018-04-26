def run_formula(dv, param = None):
    defult_param = {'N': 10}
    if not param:
        param = defult_param
    MTM = dv.add_formula('MTM', "Delta(close_adj,%s)"%(param['N']), is_quarterly=False)
    return MTM