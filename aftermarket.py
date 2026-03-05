import streamlit as st
import yfinance as yf
import pandas as pd

tickers = ["AAPL","MSFT","AMZN","GOOGL","NVDA","TSLA","META","AMD","MU"]

@st.cache_data(ttl=300)
def load_prices():
    return yf.download(tickers, period="1d")

data = load_prices()

rows = []

for t in tickers:
    try:
        price = data["Close"][t].iloc[-1]
    except:
        price = None

    rows.append({"Ticker": t, "Price": price})

df = pd.DataFrame(rows)

st.title("US Market Prices")
st.dataframe(df)
