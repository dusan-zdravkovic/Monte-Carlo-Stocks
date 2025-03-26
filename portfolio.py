"""
Monte Carlo Stock Simulation
- Implement the Monte Carlo Method to simulate a stock portfolio
March 23, 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import os
import requests
from dotenv import load_dotenv
import time  # Added import for time

# Load environment variables
load_dotenv()
API_KEY = os.getenv("TIINGO_API_KEY")


def fetch_stock_data_tiingo(stock):
    """Fetch historical stock data from Tiingo."""
    headers = {"Content-Type": "application/json", "Authorization": f"Token {API_KEY}"}
    end_date = dt.datetime.now().strftime("%Y-%m-%d")
    start_date = (dt.datetime.now() - dt.timedelta(days=300)).strftime("%Y-%m-%d")
    url = f"https://api.tiingo.com/tiingo/daily/{stock}/prices?startDate={start_date}&endDate={end_date}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df.set_index("date", inplace=True)
        df.index = pd.to_datetime(df.index)
        return df["close"]
    else:
        print(f"Failed to fetch data for {stock}: {response.status_code}")
        return None


def get_stock_data(stocks):
    """Fetch and compile stock data into a DataFrame."""
    stock_data = {stock: fetch_stock_data_tiingo(stock) for stock in stocks}
    stock_df = pd.DataFrame({k: v for k, v in stock_data.items() if v is not None})

    returns = stock_df.pct_change()
    return returns.mean(), returns.cov()


# Stock symbols
stockList = ["CBA", "BHP", "TLS", "NAB", "WBC", "STO"]
stocks = [stock + ".AX" for stock in stockList]

# Date range
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)

# Fetch stock data
meanReturns, covMatrix = get_stock_data(stocks)

print(meanReturns)
