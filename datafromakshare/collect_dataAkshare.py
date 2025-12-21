import akshare as ak

def collectfrom_Aksh(stock_code, start, end):
    if not isinstance(stock_code, str):
        stock_code = str(stock_code).zfill(6)
    if not isinstance(start, str):
        start = str(start)
    if not isinstance(end, str):
        end = str(end)
    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=stock_code, period="daily", start_date=start, end_date=end, adjust="")

# 添加交易所前缀
    if stock_code.startswith(('sz', 'sh')):
        stock_code = stock_code
    if stock_code.startswith(('0', '3')):
        stock_code = 'sz' + stock_code
    elif stock_code.startswith(('6', '9')):
        stock_code = 'sh' + stock_code

    code = stock_zh_a_hist_df.iloc[0,1]

    stock_zh_a_hist_df['股票代码'] = stock_zh_a_hist_df['股票代码'].replace(code,str(stock_code))

    stock_zh_a_hist_df.rename(columns={
        '日期':'date',
        '股票代码':'symbol',
        '开盘':'open',
        '收盘':'close',
        '最高':'high',
        '最低':'low',
        '成交量':'volume'
    }, inplace=True)
    return(stock_zh_a_hist_df)

def collectfrom_Aksh_hfq(stock_code, start, end):
    if not isinstance(stock_code, str):
        stock_code = str(stock_code).zfill(6)
    if not isinstance(start, str):
        start = str(start)
    if not isinstance(end, str):
        end = str(end)
    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=stock_code, period="daily", start_date=start, end_date=end, adjust="hfq")

# 添加交易所前缀
    if stock_code.startswith(('sz', 'sh')):
        stock_code = stock_code
    if stock_code.startswith(('0', '3')):
        stock_code = 'sz' + stock_code
    elif stock_code.startswith(('6', '9')):
        stock_code = 'sh' + stock_code

    code = stock_zh_a_hist_df.iloc[0,1]

    stock_zh_a_hist_df['股票代码'] = stock_zh_a_hist_df['股票代码'].replace(code,str(stock_code))

    stock_zh_a_hist_df.rename(columns={
        '日期':'date',
        '股票代码':'symbol',
        '开盘':'open',
        '收盘':'close',
        '最高':'high',
        '最低':'low',
        '成交量':'volume'
    }, inplace=True)
    return(stock_zh_a_hist_df)

def collectfrom_Aksh_qfq(stock_code, start, end):
    if not isinstance(stock_code, str):
        stock_code = str(stock_code).zfill(6)
    if not isinstance(start, str):
        start = str(start)
    if not isinstance(end, str):
        end = str(end)
    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=stock_code, period="daily", start_date=start, end_date=end, adjust="qfq")

# 添加交易所前缀
    if stock_code.startswith(('sz', 'sh')):
        stock_code = stock_code
    if stock_code.startswith(('0', '3')):
        stock_code = 'sz' + stock_code
    elif stock_code.startswith(('6', '9')):
        stock_code = 'sh' + stock_code

    code = stock_zh_a_hist_df.iloc[0,1]

    stock_zh_a_hist_df['股票代码'] = stock_zh_a_hist_df['股票代码'].replace(code,str(stock_code))

    stock_zh_a_hist_df.rename(columns={
        '日期':'date',
        '股票代码':'symbol',
        '开盘':'open',
        '收盘':'close',
        '最高':'high',
        '最低':'low',
        '成交量':'volume'
    }, inplace=True)
    return(stock_zh_a_hist_df)



if __name__ == "__main__":
    print(collectfrom_Aksh_hfq('000402', '20200102', '20211230'))

"""
          日期    股票代码     开盘     收盘     最高     最低      成交量           成交额    振幅   涨跌幅   涨跌额   换手率
0   2024-11-20  000001  11.67  11.64  11.75  11.61  1286572  1.498818e+09  1.20 -0.34 -0.04  0.66
1   2024-11-21  000001  11.62  11.59  11.65  11.56   883408  1.023998e+09  0.77 -0.43 -0.05  0.46
2   2024-11-22  000001  11.59  11.28  11.61  11.28  1625317  1.858072e+09  2.85 -2.67 -0.31  0.84
3   2024-11-25  000001  11.28  11.18  11.34  11.14  1166020  1.310131e+09  1.77 -0.89 -0.10  0.60

date    symbol     open    close     high      low   volume           成交额    振幅   涨跌幅    涨跌额   换手率
0   2024-11-20  sz000001  1773.73  1769.98  1783.73  1766.23  1286572  1.498818e+09  0.99 -0.28  -5.00  0.66
1   2024-11-21  sz000001  1767.48  1763.73  1771.23  1759.98   883408  1.023998e+09  0.64 -0.35  -6.25  0.46
2   2024-11-22  sz000001  1763.73  1724.97  1766.23  1724.97  1625317  1.858072e+09  2.34 -2.20 -38.76  0.84
3   2024-11-25  sz000001  1724.97  1712.47  1732.47  1707.47  1166020  1.310131e+09  1.45 -0.72 -12.50  0.60
4   2024-11-26  sz000001  1712.47  1723.72  1728.72  1707.47   831078  9.337339e+08  1.24  0.66  11.25  0.43
5   2024-11-27  sz000001  1719.97  1738.72  1738.72  1708.72   895178  1.010002e+09  1.74  0.87  15.00  0.46
"""