import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", "week")
print(df)
