######################################################################
# df1是不复权数据，df2是后复权数据
######################################################################

import pandas as pd
import os
from collect_dataAkshare import *

def calculate_adjustment_factor(df_hfq, df):
    """
    计算后复权因子
    """
    
    df_hfq['close_bfq'] = df['close']
    #注意这个方法计算的是后复权因子：后复权因子 = 后复权价格 / 不复权价格
    df_hfq['factor'] = df_hfq['close']/df_hfq['close_bfq']
    
    stock_df = df_hfq[['date','symbol','open','close','high','low','volume','factor']]
    filename = f"{df_hfq.iloc[0,1]}.csv"
    csv_path = os.path.join('data', filename)
    stock_df.to_csv(csv_path,
                    index=False,
                    encoding='utf-8-sig')
    
    return stock_df


if __name__ == "__main__":
    df_houfuquan = collectfrom_Aksh_hfq('000402', '20200102', '20211230')
    df_bufuquan = collectfrom_Aksh('000402', '20200102', '20211230')
    print(calculate_adjustment_factor(df_houfuquan, df_bufuquan))
    