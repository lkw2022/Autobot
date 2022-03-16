import requests #rest api의 데이터를 스크래핑

url = "https://api.upbit.com/v1/market/all" #마켓 코드 조회
resp = requests.get(url) #requests 모듈의 get 함수에 url 삽입
data = resp.json() #resp 객체를 json 메소드를 사용하여 키와 값을 가지는 파이썬 딕셔너리 데이터 타입으로 변경
print(data)
print(len(data)) #업비트에서 거래되고 있는 암호화폐의 개수

 