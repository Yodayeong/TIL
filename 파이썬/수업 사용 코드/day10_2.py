import requests

order_currency = 'ALL'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
response = requests.get(URL).json()
coins = response.get('data')

#coins : 딕셔너리
#key : coin 이름
#value : 딕셔너리(coin의 정보)
for coin in coins:
    #coins.get(coin) <= coin의 정보인 딕셔저리
    #그 딕셔너리의 closing price
    if coin == 'date': #마지막에 string('date') 때문에 오류남.
        continue
    print(coin, coins.get(coin).get('closing_price'))