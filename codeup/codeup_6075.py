#정수 1개 입력받아 그 수까지 출력하기1

#정수 1개가 입력된다.
#(0 ~ 100)

#0부터 그 수까지 줄을 바꿔 한 개씩 출력한다.

item = int(input())
temp = 0

while temp <= item:
    print(temp)
    temp += 1