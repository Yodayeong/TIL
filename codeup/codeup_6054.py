#둘 다 참일 경우만 참 출력하기

#2개의 정수가 공백을 두고 입력된다.
#둘 다 True 일 경우에만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.

a, b = map(int, input().split())

if a == 0 or b == 0:
    print('False')
else:
    print('True')