import yfinance as yf
import matplotlib.pyplot as plt

print("Welcome to nebulaQuant!")
ticker = input("Enter a stock ticker: ").upper()
print("You selected: ", ticker)

data = yf.download(ticker, period="5y")

print(data.head())
print(data.shape)

close_prices = data["Close"]
print(close_prices.head())

print("highest closing price:", close_prices.max())

print("lowest closing price:", close_prices.min())

print("mean of closing price:", close_prices.mean())

print("number of trading days:", len(close_prices))

#show the graph
close_prices.plot()
plt.show()
plt.title("stock price")
plt.xlabel("time")
plt.ylabel("closing price")