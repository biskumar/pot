import streamlit as st
import yfinance as yf
import pandas as pd

tickers = ["AAPL","MSFT","AMZN","GOOGL","NVDA","TSLA","META","AMD","MU"]

data = []

for t in tickers:
    stock = yf.Ticker(t)
    
    regular = stock.fast_info.get("lastPrice", None)
    post = stock.info.get("postMarketPrice", None)

    data.append({
        "Ticker": t,
        "Regular Price": regular,
        "After Market Price": post
    })

df = pd.DataFrame(data)

st.title("US Stocks After Market Prices")

st.dataframe(df)
