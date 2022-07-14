#짝수 합 구하기

#정수 1개가 입력된다.
#(0 ~ 100)

#1부터 그 수까지 짝수만 합해 출력한다.

item = int(input())
total = 0
cnt = 0

while cnt <= item:
    if cnt % 2 == 0:
        total += cnt
    cnt += 1
print(total)