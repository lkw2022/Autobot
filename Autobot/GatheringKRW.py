import requests

url = "https://api.upbit.com/v1/market/all"
resp = requests.get(url)
data = resp.json()

krw_tickers = [] # KRW fiat를 갖는 ticker들을 저장할 list 생성

for coin in data:
    ticker = coin['market'] #coin 딕셔너리 타입에서 market 키를 통해 인덱싱
    
    if ticker.startswith("KRW"):
        krw_tickers.append(ticker)

print(krw_tickers)
print(len(krw_tickers))