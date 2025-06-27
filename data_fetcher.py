import pandas as pd
import numpy as np

def fetch_stock_data(ticker, start_date, end_date):
    dates = pd.date_range(start=start_date, end=end_date)
    close_prices = np.random.rand(len(dates)) * 100 + 100
    rsi_values = np.clip(np.random.normal(50, 10, size=len(dates)), 0, 100)
    data = pd.DataFrame({'Close': close_prices, 'RSI': rsi_values}, index=dates)
    return data

