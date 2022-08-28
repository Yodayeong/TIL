set_a = {1, 2, 3, 1, 1}
set_b = {'hi', 1, 2}

print(set_a)
print(set_b)

#활용 예시
#아래의 리스트에서 고유한 지역의 개수는?
locations = ['서울', '서울', '대구', '제주', '부산', '부산', '대구', '광주', '인천']
print(set(locations))
print(len(set(locations)))