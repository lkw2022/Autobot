import pyupbit

tickers = ["KRW-BTC", "KRW-ETH"]
price = pyupbit.get_current_price(tickers)
print(price)
