#숫자의 개수

#문제
#세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
#예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

#입력
#첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

#출력
#첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.

A = int(input())
B = int(input())
C = int(input())
#계산을 해야하므로, A,B,C 변수는 int형으로 주었다.

total = str(A * B * C)
#결과값의 각 자릿수에 도달해야하므로, total 변수는 str형으로 주었다.

cnt_0 = 0
cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0
cnt_5 = 0
cnt_6 = 0
cnt_7 = 0
cnt_8 = 0
cnt_9 = 0
#각 자릿수를 count해 줄 통을 생성한다.

for i in total:
    if i == '0':
        cnt_0 += 1
    elif i == '1':
        cnt_1 += 1
    elif i == '2':
        cnt_2 += 1
    elif i == '3':
        cnt_3 += 1
    elif i == '4':
        cnt_4 += 1
    elif i == '5':
        cnt_5 += 1
    elif i == '6':
        cnt_6 += 1
    elif i == '7':
        cnt_7 += 1
    elif i == '8':
        cnt_8 += 1
    else:
        cnt_9 += 1
#노가다....

print(cnt_0)
print(cnt_1)
print(cnt_2)
print(cnt_3)
print(cnt_4)
print(cnt_5)
print(cnt_6)
print(cnt_7)
print(cnt_8)
print(cnt_9)
#노가다....