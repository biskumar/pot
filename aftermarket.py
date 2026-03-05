import streamlit as st
import yfinance as yf
import pandas as pd

tickers = ["AAPL","MSFT","AMZN","GOOGL","NVDA","TSLA","META","AMD","MU"]

data = []

for t in tickers:
    try:
        stock = yf.Ticker(t)

        hist = stock.history(period="1d")
        regular = hist["Close"].iloc[-1] if not hist.empty else None

        info = stock.info
        post = info.get("postMarketPrice", None)

        data.append({
            "Ticker": t,
            "Regular Price": regular,
            "After Market Price": post
        })

    except Exception as e:
        data.append({
            "Ticker": t,
            "Regular Price": None,
            "After Market Price": None
        })

df = pd.DataFrame(data)

st.title("US Stocks After Market Prices")
st.dataframe(df)
