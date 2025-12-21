# 用于输出个股的财务信息（雪球）,包含股息率
# 加上转置的数据处理

import akshare as ak

def get_finance_data(stock_code):
    stock_individual_spot_xq_df = ak.stock_individual_spot_xq(symbol=stock_code)

    # 转置
    stock_xq_df_T = stock_individual_spot_xq_df.T
    # 将一个Dataframe的第一行数据删除，将第二行的内容作为列标题
    #stock_xq_df_T = stock_xq_df_T.drop(stock_xq_df_T.columns[0], axis=1) ,不需要删第一列
    new_header = stock_xq_df_T.iloc[0]
    stock_xq_df_T = stock_xq_df_T[1:]
    stock_xq_df_T.columns = new_header
    stock_xq_df_T = stock_xq_df_T.reset_index(drop=True)
    #print(stock_xq_df_T)
    return stock_xq_df_T



if __name__ == "__main__":
    # 创建示例DataFrame
    #get_finance_data("SH600000")
    get_finance_data("SH600000").to_csv('bank_financial_data_transposed.csv', 
                          index=True,  # 保存行索引（原列名）
                          encoding='utf-8-sig')
    # print(type(stock_individual_spot_xq_df))