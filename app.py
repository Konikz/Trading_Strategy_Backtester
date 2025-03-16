import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("📈 Trading Strategy Backtester")

# Sidebar Inputs
st.sidebar.header("Strategy Parameters")
ticker = st.sidebar.text_input("Enter Stock Ticker:", "AAPL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2023-01-01"))
short_window = st.sidebar.slider("Short Moving Average", 10, 100, 50)
long_window = st.sidebar.slider("Long Moving Average", 100, 300, 200)

# Fetch Data
st.subheader(f"Stock Data for {ticker}")
data = yf.download(ticker, start=start_date, end=end_date)
if data.empty:
    st.error("No data found. Check ticker symbol and dates.")
    st.stop()

# Calculate Moving Averages
data["Short_MA"] = data["Close"].rolling(window=short_window).mean()
data["Long_MA"] = data["Close"].rolling(window=long_window).mean()

# Plot Stock Price and Moving Averages
st.subheader("Stock Price and Moving Averages")
fig, ax = plt.subplots()
ax.plot(data["Close"], label="Stock Price", alpha=0.5)
ax.plot(data["Short_MA"], label=f"{short_window}-day SMA", linestyle="--", color="orange")
ax.plot(data["Long_MA"], label=f"{long_window}-day SMA", linestyle="--", color="green")
ax.set_title("Trading Strategy Backtest")
ax.legend()
st.pyplot(fig)

# Show Data Table
st.subheader("Raw Data")
st.write(data.tail())

# Simple Buy/Sell Strategy
st.subheader("Trading Signals (Buy/Sell)")
buy_signals = (data["Short_MA"] > data["Long_MA"]) & (data["Short_MA"].shift(1) <= data["Long_MA"].shift(1))
sell_signals = (data["Short_MA"] < data["Long_MA"]) & (data["Short_MA"].shift(1) >= data["Long_MA"].shift(1))

data["Buy Signal"] = buy_signals
data["Sell Signal"] = sell_signals

# Plot Buy/Sell Points
fig2, ax2 = plt.subplots()
ax2.plot(data["Close"], label="Stock Price", alpha=0.5)
ax2.scatter(data.index[buy_signals], data["Close"][buy_signals], marker="^", color="g", label="Buy Signal", alpha=1)
ax2.scatter(data.index[sell_signals], data["Close"][sell_signals], marker="v", color="r", label="Sell Signal", alpha=1)
ax2.set_title("Trading Signals")
ax2.legend()
st.pyplot(fig2)
