"""
Main Simulation file
May 25, 2025

"""

# Load in API key from TwelveData
from secrets1 import key1

# Other imports
import requests
import time
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

BASE_URL = "https://api.twelvedata.com/time_series"

# Selected 10 stock tickers
stock_symbols = [
    "AAPL",  # Apple
    "MSFT",  # Microsoft
    "GOOGL",  # Alphabet
    "TSLA",  # Tesla
    "NVDA",  # Nvidia
    "META",  # Meta (Facebook)
    "AMZN",  # Amazon
    "JPM",  # JPMorgan Chase
    "DIS",  # Disney
    "PFE",  # Pfizer
]

# Define time range for training (simulation inputs)
start_date = "2020-03-01"
end_date = "2021-03-01"

# Dictionary to store fetched price data
price_data = {}


# Defining function to fetch stock data
def fetch_prices(symbol, start_date, end_date, api_key):
    params = {
        "symbol": symbol,
        "interval": "1day",
        "start_date": start_date,
        "end_date": end_date,
        "apikey": api_key,
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "values" not in data:
        print(
            f"❌ Failed to fetch data for {symbol}: {data.get('message', 'Unknown error')}"
        )
        return None

    df = pd.DataFrame(data["values"])
    df["datetime"] = pd.to_datetime(df["datetime"])
    df["close"] = pd.to_numeric(df["close"])
    df = df.sort_values("datetime")
    return df[["datetime", "close"]]


# Fetch and store data for each stock
for symbol in stock_symbols:
    print(f"📦 Fetching data for {symbol}...")
    df = fetch_prices(symbol, start_date, end_date, key1)
    if df is not None:
        price_data[symbol] = df
        print(f"✅ {symbol} data loaded: {len(df)} rows")
    else:
        print(f"⚠️ Skipping {symbol} due to fetch error.")
