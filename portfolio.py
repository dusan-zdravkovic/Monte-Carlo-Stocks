"""
Monte Carlo Stock Simulation
- Implement the Monte Carlo Method to simulate a stock portfolio
March 23, 2025
"""

import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")

# from pandas_datareader import data as pdr - yahoo fianance no longer works directly
import yfinance as yf
from pandas_datareader import data as pdr

# yf.pdr_override()  # override pandas_datareader with yfinance
import requests

# Custom session with User-Agent to bypass blocking
session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

yf.pdr_override()  # Override pandas_datareader with yfinance
yf.shared._requests = session  # Force yfinance to use the custom session


# Import Data
def get_data(stocks, start, end):
    stockData = pdr.get_data_yahoo(stocks, start, end)
    print(stockData.head())  # Check if data is retrieved properly

    stockData = stockData["Close"]  # only interested in daily changes
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix


stockList = ["CBA", "BHP", "TLS", "NAB", "WBC", "STO"]
stocks = [stock + ".AX" for stock in stockList]
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)

meanReturns, covMatrix = get_data(stocks, startDate, endDate)

print(meanReturns)
