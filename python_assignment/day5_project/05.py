#JSON 데이터 활용 - 영화 단일 정보 응용

#영화 데이터 movie.json 와 genres.json 을  활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오.
#코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다. 
#JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.

#id, title, vote_average, overview, genre_names로 결과를 만듭니다.
#genre_names는 각 장르 정보를 값으로 가집니다.
#genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

import json
from pprint import pprint


def movie_info(movie, genres):
    genre_ids = movie['genre_ids']
    genre_names = []
    for i in genres:
        if i['id'] in genre_ids:
            genre_names.append(i['name'])
    
    my_movie = dict()
    my_movie['genre_names'] = genre_names

    keys = ['id', 'overview', 'title', 'vote_average']
    for i in keys:
        my_movie[i] = movie[i]

    return my_movie
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))