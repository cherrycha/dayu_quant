import pandas as pd


def get_dv(start = 20170101,end = 20180101): 
    import jaqs_fxdayu
    jaqs_fxdayu.patch_all()
    from jaqs.data import DataView
    from jaqs_fxdayu.data.dataservice import LocalDataService
    
    import warnings
    warnings.filterwarnings("ignore")
    
    #--------------------------------------------------------
    
    #define
    factor_list  = ['capital_stk','cash_cash_equ_end_period','oper_rev','acct_rcv','adv_from_cust','adv_from_cust','oper_profit',
               'less_oper_cost','inventories','ARTRate','ARTDays','InventoryTDays','AccountsPayablesTDays',
              'DAVOL5','AD']
    check_factor = ','.join(factor_list)
    
    dataview_folder = r'../data'
    ds = LocalDataService(fp = dataview_folder)
    
    ZZ800_id = ds.query_index_member("000906.SH", start, end)
    stock_symbol = list(set(ZZ800_id))
    
    dv_props = {'start_date': start, 'end_date': end, 'symbol':','.join(stock_symbol),
             'fields': check_factor,
             'freq': 1,
             "prepare_fields": True}
    
    dv = DataView()
    dv.init_from_config(dv_props, data_api=ds)
    dv.prepare_data()
    return dv


if 'dv' not in dir():
    dv = get_dv()
    
#--------------------------------------------------------- 
#test output
def test(factor,data):
    if not isinstance(data, pd.core.frame.DataFrame):
        raise TypeError('On factor {} ,output must be a pandas.DataFrame!'.format(factor))
    else:
        try:
            index_name = data.index.names[0]
            columns_name = data.index.names[0]
        except:
            if not (index_name in ['trade_date','report_date'] and columns_name == 'symbol'):
                raise NameError('''Error index name,index name must in ["trade_date","report_date"],columns name must be "symbol" ''')
                
        index_dtype = data.index.dtype_str
        columns_dtype = data.columns.dtype_str
        
        if columns_dtype not in ['object','str']:
            raise TypeError('error columns type')
            
        if index_dtype not in ['int32','int64','int']:
            raise TypeError('error index type')
        print ('{} OK!'.format(factor))

import leon1,leon2,leon3,leon4,leon5,leon6,leon7,leon8,leon9,leonA


for f in [ 'leon1','leon2' ,'leon3' ,'leon4', 'leon5', 'leon6' ,'leon7' ,'leon8','leon9','leonA']:
    test(f, globals()[f].run_formula(dv))