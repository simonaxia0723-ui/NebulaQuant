import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

tickers = input("enter stock tickers: ").split()
time_period = input("enter timer period: ")

fig, ax = plt.subplots()

stock_returns = {}
volatility = {}

for ticker in tickers:
    data = yf.download(ticker, period = time_period, progress = False)
    close_prices = data["Close"].squeeze().dropna()
    normalized_prices = close_prices / close_prices.iloc[0] * 100
    ax.plot(close_prices.index, normalized_prices, label=ticker)
    percentage_return = round(normalized_prices.iloc[-1] - 100, 2)
    daily_returns = []
    for i in range(1, len(close_prices)):
        daily_return = ((close_prices.iloc[i] - close_prices.iloc[i-1])
                        / close_prices.iloc[i-1] * 100)
        daily_returns.append(daily_return)
    volatility[ticker] = round(np.std(daily_returns), 4)
    stock_returns[ticker] = percentage_return

least_risky = min(volatility, key=volatility.get)
print("Least risky:", least_risky, "(volatility:", volatility[least_risky], ")")

volatility_ranking = sorted(
    volatility.items(),
    key=lambda pair: pair[1],
    reverse=False
)

for rank, (ticker, volatility) in enumerate(volatility_ranking, start=1):
    print(f"{rank}. {ticker}: {volatility:+}%")
best_stock = max(stock_returns, key=stock_returns.get)
print(f"\nBest performer: {best_stock} (+{stock_returns[best_stock]}%)")

stock_returns_ranking = sorted(
    stock_returns.items(),
    key=lambda pair: pair[1],
    reverse=True
)
for rank, (ticker, percentage_return) in enumerate(stock_returns_ranking, start=1):
    print(f"{rank}. {ticker}: {percentage_return:+}%")

ax.set_title("normalized prices")
ax.set_xlabel("time")
ax.set_ylabel("normalized prices")
ax.legend()
plt.show()
