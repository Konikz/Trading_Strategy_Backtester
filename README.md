# Trading Strategy Backtester

A simple web application that allows you to backtest a trading strategy using moving average crossovers. This project uses Python, Streamlit, and Yahoo Finance data.

## Features

- Fetches historical stock data from Yahoo Finance
- Implements a short and long moving average crossover strategy
- Displays buy and sell signals on an interactive chart
- Allows customization of parameters such as time range and moving average windows

## Installation

### Clone this repository:
```sh
git clone https://github.com/Konikz/Trading_Strategy_Backtester.git
```

### Navigate to the project folder:
```sh
cd Trading_Strategy_Backtester
```

### Install the required dependencies:
```sh
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, install dependencies manually:
```sh
pip install streamlit yfinance pandas matplotlib
```

## Usage

Run the Streamlit application:
```sh
streamlit run app.py
```

A new browser window will open. You can then:
- Enter the stock ticker symbol (e.g., AAPL).
- Specify the date range.
- Adjust the short and long moving average windows.
- Observe the plotted stock price and moving averages, along with buy and sell signals.

## Project Structure

```
Trading_Strategy_Backtester/
│
├── app.py             # Main Streamlit application
├── backtester.py      # Optional script for local backtesting
├── requirements.txt   # List of Python dependencies
└── README.md          # Project documentation
```

## Contributing

Contributions are welcome. To propose a change:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Open a pull request.
