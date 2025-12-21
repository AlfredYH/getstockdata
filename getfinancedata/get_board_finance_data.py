# 每次运行脚本时，都会生成一个唯一的、包含时间戳和板块信息的 CSV 文件，避免文件覆盖问题。
# 从指定板块中，获取板块内股票的finance数据

import akshare as ak
import pandas as pd
import finance_data_xq
import add_prefix
from datetime import datetime
import os

def get_board_all_finance_data(industry_name):

    indus_name = industry_name  # 板块名称，可根据需要修改或从参数传入

    industry_stock_df = ak.stock_board_industry_cons_em(symbol=indus_name)
    print(industry_stock_df)

    # 创建空的DataFrame用于存储所有财务数据
    all_financial_data = pd.DataFrame()

    for i in range(len(industry_stock_df)):
        stock = industry_stock_df.iloc[i]['代码']
        stock_prefix = add_prefix.add_exchange_prefix(stock)
        name = industry_stock_df.iloc[i]['名称']
        print(f"正在获取 {name}({stock_prefix}) 的财务数据...")

        try:
            # 获取单只股票的财务数据，这里是雪球的数据格式，未转置
            stock_df = finance_data_xq.get_finance_data(stock_prefix)

            # 添加股票名称和代码列
            stock_df['名称'] = name
            stock_df['代码'] = stock_prefix
            # 将当前股票数据添加到总DataFrame中
            all_financial_data = pd.concat([all_financial_data, stock_df], 
                                        ignore_index=True)
        except Exception as e:
            print(f"获取 {name} 的数据失败: {e}")
            continue
    
    # 获取当前时间，格式化为YYYYMMDD_HHMMSS
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    # 输出合并后的所有财务数据到CSV
    # 生成动态文件名：时间+板块名称+FinanceData
    csv_filename = f"{current_time}_{indus_name}FinanceData.csv"
    csv_path = os.path.join('data', csv_filename)
    all_financial_data.to_csv(csv_path, 
                              index=True,
                              encoding='utf-8-sig')

    # 保存合并后的所有财务数据
    print(f"\n所有{indus_name}股财务数据已保存至: {csv_path}")
    return all_financial_data




if __name__ == "__main__":
    get_board_all_finance_data("银行")
