#정수 1개 입력받아 분류하기

#정수 1개가 입력된다.
#-2147483648 ~ +2147483647, 단 0은 입력되지 않는다.

#음수이면서 짝수이면, A
#음수이면서 홀수이면, B
#양수이면서 짝수이면, C
#양수이면서 홀수이면, D
#를 출력한다.

item = int(input())

if item < 0 and item % 2 == 0:
    print('A')
elif item < 0 and item % 2 != 0:
    print('B')
elif item >= 0 and item % 2 == 0:
    print('C')
else:
    print('D')