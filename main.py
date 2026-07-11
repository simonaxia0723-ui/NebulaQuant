import yfinance as yf

print("Welcome to nebulaQuant!")
ticker = input("Enter a stock ticker: ").upper()
print("You selected: ", ticker)

data = yf.download(ticker, period="5y", )
print(data)