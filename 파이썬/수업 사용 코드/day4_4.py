#a라는 이름에 타입이 int, 1을 할당
a = 1

#print는 변수에 할당할 수 없음!
b = print(1 + 2)
c = print(3 * 3)
d = print(4 * 5)
print(b)
print(c)
print(d)

#한 단계
a = [1, 2, 3]
#sum(a)의 결과(int, 합 계산 결과)를 result에 할당
result = sum(a)

numbers = [1, 3, 2]
#None이 반환되고, numbers는 바뀌어 있음.
result = numbers.reverse()

print('1 2 3'.split().index('2') + 10)
#'1 2 3'.split() = ['1', '2', '3']
#['1', '2', '3'].index('2) = 1
#1 + 10 = 11