#하나라도 참이면 참 출력하기

#2개의 정수가 공백을 두고 입력된다.
#하나라도 참일 경우 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.

a, b = map(int, input().split())

if a == 0 and b == 0:
    print('False')
else:
    print('True')