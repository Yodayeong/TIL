#정수 3개 입력받아 가장 작은 값 출력하기

#3개의 정수가 공백으로 구분되어 입력된다.
#-2147483648 ~ +2147483648

#가장 작은 값을 출력한다.

a, b, c = map(int, input().split())

if a >= b:
    if b >= c:
        print(c)
    else:
        print(b)
elif b >= a:
    if a >= c:
        print(c)
    else:
        print(a)
elif c >= a:
    if a >= b:
        print(b)
    else:
        print(a)