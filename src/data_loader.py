import yfinance as yf
import pandas as pd

def load_stock_data(ticker="AAPL", start="2018-01-01", end="2024-01-01"):
    df = yf.download(ticker, start=start, end=end)
    df.to_csv("data/stock_data.csv")
    return df

if __name__ == "__main__":
    load_stock_data()
