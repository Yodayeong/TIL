#정수 1개 입력받아 카운트다운 출력하기2

#정수 1개가 입력된다.
#(1 ~ 100)

#1만큼씩 줄이면서 카운트다운 수가 0이 될 때까지 한 줄에 1개씩 출력한다.

item = int(input())

while item > 0:
    item -= 1
    print(item)