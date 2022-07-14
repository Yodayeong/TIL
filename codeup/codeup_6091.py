#함께 문제 푸는 날

#같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는,
#방문 주기가 공백을 두고 입력된다. (단, 입력값은 100이하의 자연수이다.)

#3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)을 출력한다.

#최소공배수를 활용
#최소공배수는 주어진 세 수로 모두 나뉘어지는 가장 작은 수이다.

a, b, c = map(int, input().split())
x = 1

while (x % a != 0) or (x % b != 0) or (x % c != 0): #셋 다 나머지가 0이어야 종료
    x += 1
print(x)