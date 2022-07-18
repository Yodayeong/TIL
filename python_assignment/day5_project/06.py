#JSON 데이터 활용 - 영화 다중 정보 활용

#영화 데이터 movies.json 와 genres.json 을  활용하여 필요한 정보로만 구성된 리스트를 출력하시오.
#코드는 선언된 함수 내에 작성하며, 결과 리스트를 반환합니다. 
#JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.

#전체 영화 정보는 평점 높은 20개의 영화 데이터입니다.
#개별 영화 데이터는 id, title, vote_average, overview, genre_names로 구성된 딕셔너리입니다. 
#genre_names는 각 장르 정보를 값으로 가집니다.
#genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

import json
from pprint import pprint


def movie_info(movies, genres):

    my_movies = []

    for movie in movies:
        genre_ids = movie['genre_ids']

        genre_names = []
        for i in genres:
            if i['id'] in genre_ids:
                genre_names.append(i['name'])

        my_movie = dict()
        my_movie['genre_names'] = genre_names

        keys = ['id', 'overview', 'title', 'vote_average']
        for key in keys:
            my_movie[key] = movie[key]
        
        my_movies.append(my_movie)

    return my_movies


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))