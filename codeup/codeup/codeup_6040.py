#정수 2개 입력받아 나눈 몫 계산하기

#2개의 정수(a, b)가 공백으로 구분되어 입력된다.
#a를 b로 나눈 몫을 출력한다.

a, b = map(int, input().split())

print(int(a/b))