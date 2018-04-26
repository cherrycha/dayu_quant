def run_formula(dv):
    alpha171 = dv.add_formula('alpha171',
                              "((-1 * ((low_adj - close_adj) * (open_adj^5))) / ((close_adj - high_adj) * (close_adj^5)))",
                              is_quarterly=False)
    return alpha171