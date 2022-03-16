import pyupbit
import pandas as pd

df = pyupbit.get_ohlcv("KRW-BTC", "minute1")
print(df)

df1 = df['open'].resample('3T').first() #open column에서 3분 단위로 리셈플링
df2 = df['high'].resample('3T').max()
df3 = df['low'].resample('3T').min()
df4 = df['close'].resample('3T').last()
df5 = df['volume'].resample('3T').sum()

df = pd.concat([df1, df2, df3, df4, df5], axis = 1) #concat 함수로 결합, axis=1은 행 단위 방향으로 적용
print(df)

#출처: https://gist.github.com/brayden-jo/d92dd67d3f3718f09c7dcb6fdefe6977