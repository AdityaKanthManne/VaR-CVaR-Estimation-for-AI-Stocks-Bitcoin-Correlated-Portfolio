

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_price_data(tickers, start_date="2018-01-01", end_date=None):
    data = yf.download(tickers, start=start_date, end=end_date)["Close"]
    if data.empty:
        raise ValueError("No data fetched. You may be rate-limited by Yahoo Finance. Try again later.")
    return data.dropna()



def calculate_log_returns(price_df):
    """
    Calculates daily log returns from adjusted closing prices.

    Parameters:
    - price_df: DataFrame of prices

    Returns:
    - DataFrame of log returns
    """
    return (price_df / price_df.shift(1)).apply(lambda x: pd.Series(np.log(x))).dropna()


