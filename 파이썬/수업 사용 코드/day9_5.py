import requests

URL = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page=1&pageSize=20'

response = requests.get(URL).json()
print(response.get('stocks')[0].get('closePrice'))