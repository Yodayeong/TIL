#2의 거듭제곱 배로 곱해 출력하기

#정수 2개(a, b)가 공백을 두고 입력된다.
#0 <= a, b <= 10

#a 를 2b배 만큼 곱한 값을 출력한다.

a, b = map(int, input().split())

temp = 2**b

print(a*temp)