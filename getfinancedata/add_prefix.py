#雪球的股票代码前缀有交易所名称，比如SH600000，用一段脚本实现所有交易所的代码都添加上前缀

import pandas as pd

def add_exchange_prefix(stock_code):
    """根据股票代码判断交易所并添加前缀"""
    code = str(stock_code).strip()  # 转换为字符串并去除空格
    
    # 处理已包含前缀的情况
    if code.startswith(('SH', 'SZ', 'BJ', 'HK', 'NASDAQ', 'NYSE', 'LSE')):
        return code
    
    # A股判断逻辑
    if len(code) == 6:
        if code.startswith(('00', '30', '01', '02')):
            return f'SZ{code}'  # 深交所（创业板、中小板等）
        elif code.startswith(('60', '68', '69')):
            return f'SH{code}'  # 上交所（主板、科创板）
        elif code.startswith(('8', '4')):
            return f'BJ{code}'  # 北交所
        else:
            return f'UNKNOWN_{code}'  # 无法识别的A股代码
    
    # 港股判断逻辑（通常为5位数字）
    elif len(code) <= 5 and code.isdigit():
        return f'HK{code.zfill(5)}'  # 港股代码不足5位时左侧补零
    
    # 美股判断逻辑（通常为字母）
    elif code.isalpha() and len(code) <= 5:
        # 简单区分NASDAQ和NYSE（实际需更复杂的API查询）
        if len(code) == 4 or len(code) == 3:
            return f'NASDAQ:{code}'
        else:
            return f'NYSE:{code}'
    
    # 其他情况
    else:
        return f'UNKNOWN_{code}'

def process_dataframe(df, code_column='code'):
    """处理DataFrame中的股票代码列"""
    df[f'{code_column}_with_prefix'] = df[code_column].apply(add_exchange_prefix)
    return df

# 使用示例
if __name__ == "__main__":
    # 创建示例DataFrame
    data = {
        'code': ['600000', '000001', '831278', '00700', 'AAPL', 'MSFT', 'LSE:BARC']
    }
    df = pd.DataFrame(data)
    
    # 处理股票代码列
    processed_df = process_dataframe(df)
    
    # 输出结果
    print(processed_df)