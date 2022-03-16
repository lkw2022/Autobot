import pyupbit

krw_tickers = pyupbit.get_tickers(fiat="KRW")

prices = pyupbit.get_current_price(krw_tickers)

for k, v in prices.items(): #prices 딕셔너리의 키값을 얻어와서 보기 좋게 바인딩
    print(k, v)
