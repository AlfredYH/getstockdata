import akshare as ak
import pandas as pd
from tqdm import tqdm  # 导入进度条库



def collectfrom_aksh(stock_code, start, end):
    """
    从 akshare 获取单只股票的历史日线数据。
    此版本已修正并完善，可正确处理沪、深、北三个交易所的股票代码。
    """
    # 1. 确保股票代码是6位字符串
    if not isinstance(stock_code, str):
        # .zfill(6) 可以确保代码是6位，不足的前面补0
        stock_code = str(stock_code).zfill(6)

    # 4. 调用 akshare 获取数据
    try:
        # 使用 'qfq' (前复权) 数据通常更适合技术分析
        stock_hist_df_old = ak.stock_zh_a_hist(
            symbol=stock_code,
            period='daily',
            start_date=start,
            end_date=end,
            adjust="" 
        )
        stock_hist_df = stock_hist_df_old.rename(columns={
            '日期': 'date',
            '股票代码': 'stock_code',
            '开盘': 'open',
            '最高': 'high',
            '最低': 'low',
            '收盘': 'close',
            '成交量': 'volume'
        })
        return stock_hist_df
        
    except Exception as e:
        # 捕获所有可能的异常，例如网络问题、API返回格式错误等
        tqdm.write(f"获取数据失败 for {stock_code}: {e}")
        return None

def collectfrom_aksh2(stock_code, start, end):
    """
    从 akshare 获取单只股票的历史日线数据。
    此版本已修正并完善，可正确处理沪、深、北三个交易所的股票代码。
    """
    # 1. 确保股票代码是6位字符串
    if not isinstance(stock_code, str):
        # .zfill(6) 可以确保代码是6位，不足的前面补0
        stock_code = str(stock_code).zfill(6)
    
    # 2. 如果代码已经带有前缀（如 'sz000001'），则直接使用
    if stock_code.startswith(('sz', 'sh', 'bj')):
        pass # 不做任何事，直接进入下一步
    # 3. 根据代码开头数字，添加正确的交易所前缀
    elif stock_code.startswith(('0', '3')):
        # 0, 3 开头 -> 深交所
        stock_code = 'sz' + stock_code
    elif stock_code.startswith('6'):
        # 6 开头 -> 上交所
        stock_code = 'sh' + stock_code
    elif stock_code.startswith(('8', '4')):
        # 8, 4 开头 -> 北交所
        stock_code = 'bj' + stock_code
    else:
        # 如果代码不符合任何已知规则，打印错误并返回None
        tqdm.write(f"无法识别的股票代码格式: {stock_code}")
        return None
    
    # 确保日期是字符串类型
    if not isinstance(start, str):
        start = str(start)
    if not isinstance(end, str):
        end = str(end)

    # 调用 akshare 获取数据
    try:
        # 使用 'qfq' (前复权) 数据通常更适合技术分析
        stock_hist_df = ak.stock_zh_a_daily(
            symbol=stock_code,
            start_date=start,
            end_date=end,
            adjust="" 
        )
        
        return stock_hist_df[['date','open','high','low','close','volume']]
        
    except Exception as e:
        # 捕获所有可能的异常，例如网络问题、API返回格式错误等
        tqdm.write(f"获取数据失败 for {stock_code}: {e}")
        return None



if __name__ == "__main__":
    print(collectfrom_aksh2('000026', '20241120', '20251231'))