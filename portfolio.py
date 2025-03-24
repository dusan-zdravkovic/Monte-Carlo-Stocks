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

# from pandas_datareader import data as pdr - yahoo fianance no longer works directly
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()  # override pandas_datareader with yfinance


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
