import pyupbit
import pandas as pd

pd.options.display.float_format = "{:.1f}".format
df = pyupbit.get_ohlcv("KRW-BTC", "month")
print(df)
