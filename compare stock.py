import yfinance as yf
import matplotlib.pyplot as plt
from yfinance.const import ordered_keys

tickers = input("enter stock tickers: ").split()
time_period = input("enter timer period: ")

fig, ax = plt.subplots()

stock_returns = {}

for ticker in tickers:
    data = yf.download(ticker, period = time_period, progress = False)
    close_prices = data["Close"].squeeze().dropna()
    normalized_prices = close_prices / close_prices.iloc[0] * 100
    ax.plot(close_prices.index, normalized_prices, label=ticker)
    percentage_return = round(normalized_prices.iloc[-1] - 100, 2)
    stock_returns[ticker] = percentage_return
    print(f"{ticker}: {percentage_return:+}%")

best_stock = max(stock_returns, key=stock_returns.get)
print(f"\nBest performer: {best_stock} (+{stock_returns[best_stock]}%)")

ax.set_title("normalized prices")
ax.set_xlabel("time")
ax.set_ylabel("normalized prices")
ax.legend()
plt.show()

