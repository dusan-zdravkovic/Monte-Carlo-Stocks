"""
Learning how to use TwelveData Finance API
"""

import requests
import time
from secrets1 import key1
from datetime import datetime

ticker = "MSFT"


def get_stock_price(ticker_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    price = response["price"][:-3]
    print(price)
    return price


def get_stock_quote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response


stockdata = get_stock_quote(ticker, key1)
stock_price = get_stock_price(ticker, key1)

exchange = stockdata["exchange"]
currency = stockdata["currency"]
open_price = stockdata["open"]
high_price = stockdata["high"]
low_price = stockdata["low"]
close_price = stockdata["close"]
volume = stockdata["volume"]
name = stockdata["name"]

print(name, stock_price)


now = datetime.now().strftime("%H:%M:%S")
print(f"As of {now}, {name} is trading at ${stock_price}.")

high_price = float(stockdata["high"])
low_price = float(stockdata["low"])
price_float = float(stock_price)

if price_float == high_price:
    print("The stock is currently at the day's high.")
elif price_float == low_price:
    print("The stock is currently at the day's low.")
else:
    range_pos = (price_float - low_price) / (high_price - low_price)
    print(f"The stock is trading at {range_pos:.1%} of today’s range.")
