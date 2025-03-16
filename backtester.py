import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Load historical data
def get_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    return df

# Simple Moving Average (SMA) Crossover Strategy
def sma_strategy(df, short_window=50, long_window=200):
    df['SMA50'] = df['Close'].rolling(window=short_window).mean()
    df['SMA200'] = df['Close'].rolling(window=long_window).mean()
    df['Signal'] = 0
    df.loc[df['SMA50'] > df['SMA200'], 'Signal'] = 1  # Buy
    df.loc[df['SMA50'] <= df['SMA200'], 'Signal'] = -1  # Sell
    return df

# Backtest the strategy
def backtest(df, initial_cash=10000):
    cash = initial_cash
    position = 0
    for i in range(1, len(df)):
        if df['Signal'].iloc[i-1] == 1 and position == 0:
            position = cash / df['Close'].iloc[i]
            cash = 0  # Buy
        elif df['Signal'].iloc[i-1] == -1 and position > 0:
            cash = position * df['Close'].iloc[i]
            position = 0  # Sell
    final_value = cash + (position * df['Close'].iloc[-1])
    return float(final_value)  # Ensure it's a scalar number

# Visualization
def plot_results(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Stock Price', alpha=0.5)
    plt.plot(df['SMA50'], label='50-day SMA', linestyle='dashed')
    plt.plot(df['SMA200'], label='200-day SMA', linestyle='dashed')
    plt.legend()
    plt.title('Trading Strategy Backtest')
    plt.show()

# Run the backtester
def main():
    ticker = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2023-01-01'
    
    df = get_data(ticker, start_date, end_date)
    df = sma_strategy(df)
    final_balance = backtest(df)
    print(f"Final Portfolio Value: ${final_balance:.2f}")
    plot_results(df)

if __name__ == "__main__":
    main()
