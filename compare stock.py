import yfinance as yf
import matplotlib.pyplot as plt

tickers = input("enter stock tickers: ").split()
time_period = input("enter timer period: ")
fig, ax = plt.subplots()
for ticker in tickers:
    data = yf.download(ticker, period = time_period)
    close_prices = data["Close"].squeeze()
    ax.plot(close_prices.index, close_prices, label=ticker)
ax.set_title("stock price")
ax.set_xlabel("time")
ax.set_ylabel("closing price")
ax.legend()
plt.show()