import yfinance as yf
import pandas as pd

daily_returns_data = {}
tickers = input("enter stock tickers: ").split()
time_period = input("enter timer period: ")
for ticker in tickers:
    data = yf.download(ticker, period = time_period, progress = False)
    close_prices = data["Close"].squeeze().dropna()
    daily_returns = close_prices.pct_change().round(5).dropna()
    daily_returns_data[ticker] = daily_returns

returns_df = pd.DataFrame(daily_returns_data)
corr_matrix = returns_df.corr()  
print(corr_matrix)