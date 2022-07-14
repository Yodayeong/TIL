#참/거짓이 서로 다를 때에만 참 출력하기

#2개의 정수가 공백을 두고 입력된다.
#두 값의 True / False 값이 서로 다를 경우만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.

a, b = map(int, input().split())

if (a == 0 and b == 0) or (a != 0 and b != 0):
    print('False')
else:
    print('True')