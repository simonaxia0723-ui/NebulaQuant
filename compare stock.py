import yfinance as yf
import matplotlib.pyplot as plt

tickers = input("enter stock tickers: ").split()
time_period = input("enter timer period: ")

fig, ax = plt.subplots()

for ticker in tickers:
    data = yf.download(ticker, period = time_period)
    close_prices = data["Close"].squeeze()
    normalized_prices = close_prices / close_prices.iloc[0] * 100
    ax.plot(close_prices.index, normalized_prices, label=ticker)

ax.set_title("normalized prices")
ax.set_xlabel("time")
ax.set_ylabel("normalized prices")
ax.legend()
plt.show()