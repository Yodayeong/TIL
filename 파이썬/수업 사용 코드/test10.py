movie = {
    'title': '설국열차',
    'genres': ['SF', '액션', '드라마'], #list
    'open_date': '2013-08-01', #string
    'time': 126, #int
    'adult': False #boolean
}

print(movie['adult'])
print(movie['genres'])

movie.pop('genres') #key 삭제
print(movie['genres']) #key가 없는 경우는 keyError 발생