def run_formula(dv):
    alpha140 = dv.add_formula('alpha140',
                              "Min(Rank(Decay_linear(((Rank(open_adj)+Rank(low_adj))-Rank(high_adj)+Rank(close_adj),8))),Ts_Rank(Decay_linear(Correlation(Ts_Rank(close_adj, 8), Ts_Rank(Ts_Mean(volume,60), 20), 8), 7), 3))",
                              is_quarterly=False)
    return alpha140
