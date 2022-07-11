#문자 2개 입력받아 순서 바꿔 출력하기2
#공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.

a, b = input().split()

temp = a
a = b
b = temp

print(a)
print(b)