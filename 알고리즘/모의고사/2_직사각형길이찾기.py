#직사각형 길이 찾기

#직사각형의 네 변 중에서 세 변의 길이가 주어진다.
#나머지 한 변의 길이가 얼마인지 출력하는 프로그램을 작성하라.
#세 변의 길이는 상하좌우 어디든 될 수 있으므로 그 순서는 중요하지 않다.
#입력으로 직사각형이 불가능한 경우는 주어지지 않는다.

#[입력]
#첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
#각 테스트 케이스의 첫 번째 줄에는 세 자연수 a, b, c(1 ≤ a, b, c ≤ 100)가 공백으로 구분되어 주어진다.

#[출력]
#각 테스트 케이스마다 나머지 한 변의 길이를 출력한다.

import sys
sys.stdin = open('2_직사각형길이찾기.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    a, b, c = input().split()

    if a == b == c:
        #네 변의 길이가 모두 같은 경우
        print(f'#{i}', a)
    elif a == b:
        #여기서부터는 두 변씩 길이가 같은 경우
        print(f'#{i}', c)
    elif a == c:
        print(f'#{i}', b)
    else:
        print(f'#{i}', a)