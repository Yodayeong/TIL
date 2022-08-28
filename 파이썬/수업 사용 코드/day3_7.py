#직사각형의 넒이를 구하시오.
#직사각형 세로는 n 가로는 m
#Input 예시
# 10 20

n, m = map(int, input().split())
#input() 은 항상 문자열(string) 입력받음
#문자열.split()
#map : 어떤 함수를 반복가능한 것들의 요소에 모두 적용시킴
# => int 함수를 input().split() 리스트의 모든 요소에 적용!
print(n*m)


#내장함수를 10을 다 더해주는 함수
def plus10(n):
    return n + 10

numbers = [10, 20, 30]
new_numbers = list(map(plus10, numbers))
print(new_numbers)