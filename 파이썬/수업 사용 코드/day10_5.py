#https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>

import requests

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/now_playing'
params = {
    'api_key': '{내 api key}',
    'language': 'ko_KR'
}

response = requests.get(BASE_URL+path, params = params).json()
print(response)