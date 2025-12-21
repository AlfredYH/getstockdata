# 获取沪深京A股的当前数据

import akshare as ak
from datetime import datetime
import os


def get_all_stocklist_a():
    stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
    # print(stock_zh_a_spot_em_df)

    # 获取当前时间，格式化为YYYYMMDD_HHMMSS
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    # 输出合并后的所有财务数据到CSV
    # 生成动态文件名：时间+板块名称+FinanceData
    csv_filename = f"{current_time}_A_board_stocklist.csv"
    csv_path = os.path.join('data', csv_filename)
    stock_zh_a_spot_em_df.to_csv(csv_path, 
                              index=True,
                              encoding='utf-8-sig')

    print(f"\n所有沪深京A股当前数据已保存至: {csv_path}")
    return stock_zh_a_spot_em_df


if __name__ == "__main__":
    get_all_stocklist_a()