def run_formula(dv):
    alpha145 = dv.add_formula('alpha145', "(Ts_Mean(volume,9)-Ts_Mean(volume,26))/Ts_Mean(volume,12)*100",
                              is_quarterly=False)
    return alpha145