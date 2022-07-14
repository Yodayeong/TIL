#수 나열하기3

#시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가
#공백을 두고 입력된다.(a, m, d는 -50 ~ +50, n은 10이하의 자연수)

#n번째 수를 출력한다.

a, m, d, n = map(int, input().split())

temp = a

for i in range(1, n):
    temp = (temp * m) + d
print(temp)