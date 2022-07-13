#정수 2개 입력받아 자동 계산하기

#정수 2개가 공백을 두고 입력된다.
#첫 번째 줄에 합
#두 번째 줄에 차,
#세 번째 줄에 곱,
#네 번째 줄에 몫,
#다섯 번째 줄에 나머지,
#여섯 번째 줄에 나눈 값을 순서대로 출력한다.
#(실수, 소수점 이하 둘째 자리까지의 정확도로 출력)

a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(int(a/b))
print(int(a%b))
print(format(a/b, '.2f'))