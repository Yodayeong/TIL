#정수 2개 입력받아 비교하기4

#2개의 정수(a, b)가 공백을 두고 입력된다.
#-2147483647 <= a, b <= +2147483648

#a와 b가 다른 경우 True 를, 그렇지 않은 경우 False 를 출력한다.

a, b = map(int, input().split())

if a != b:
    print('True')
else:
    print('False')