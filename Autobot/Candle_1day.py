import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", "day", 10)
print(df)
