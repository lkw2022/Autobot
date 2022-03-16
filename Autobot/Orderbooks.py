import pyupbit
import pprint #보기 좋게 출력

orderbooks = pyupbit.get_orderbook("KRW-BTC")
pprint.pprint(orderbooks)

