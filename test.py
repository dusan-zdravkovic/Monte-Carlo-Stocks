import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")


def fetch_stock_data(stock):
    """Fetch historical stock data from Tiingo."""
    headers = {"Content-Type": "application/json", "Authorization": f"Token {API_KEY}"}
    url = f"https://api.tiingo.com/tiingo/daily/{stock}/prices?startDate=2024-01-01&endDate=2025-01-01"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        print(df)
    else:
        print(f"Failed to fetch data for {stock}: {response.status_code}")


# Fetch and display data for one stock
fetch_stock_data("GOOGL")
