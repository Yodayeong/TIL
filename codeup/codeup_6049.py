#정수 2개 입력받아 비교하기2

#두 정수 a, b가 공백을 두고 입력된다.
#-2147483648 <= a, b <= +2147483647

#a와 b의 값이 같은 경우 True 를, 그렇지 않은 경우 False 를 출력한다.

a, b = map(int, input().split())

if a == b:
    print('True')
else:
    print('False')