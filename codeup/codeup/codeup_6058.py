#둘 다 거짓일 경우만 참 출력하기

#2개의 정수가 공백을 두고 입력된다.
#두 값의 True / False 값이 모두 False 일 때만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.

a, b = map(int, input().split())

if a == 0 and b == 0:
    print('True')
else:
    print('False')