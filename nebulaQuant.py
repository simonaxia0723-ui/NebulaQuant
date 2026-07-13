import yfinance as yf
import matplotlib.pyplot as plt

print("Welcome to nebulaQuant!")
ticker = input("Enter a stock ticker: ").upper()
print("You selected: ", ticker)

data = yf.download(ticker, period="5y")

close_prices = data["Close"]
print(close_prices.head())
print("highest closing price:", close_prices.max())
print("lowest closing price:", close_prices.min())
print("mean of closing price:", close_prices.mean())
print("number of trading days:", len(close_prices))

#show the graph
close_prices.plot()
plt.title("stock price")
plt.xlabel("time")
plt.ylabel("closing price")
plt.show()

daily_returns = close_prices.pct_change().round(5).dropna()
print(daily_returns.head())
daily_returns.plot()
plt.title("daily returns")
plt.xlabel("time")
plt.ylabel("daily returns")
plt.show()

print("volatility:", daily_returns.std())

#3 stocks on one graph
tickers = ["NVDA", "MSFT", "GOOGL"]
fig, ax = plt.subplots()
for ticker in tickers:
    data = yf.download(ticker, period="5y")
    close_prices = data["Close"].squeeze()
    ax.plot(close_prices.index, close_prices, label=ticker)
ax.set_title("stock price")
ax.set_xlabel("time")
ax.set_ylabel("closing price")
ax.legend()
plt.show()