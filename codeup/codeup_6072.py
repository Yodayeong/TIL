#정수 1개 입력받아 카운트다운 출력하기1

#정수 1개가 입력된다.
#(1 ~ 100)

#1만큼씩 줄이면서 한 줄에 1개씩 카운트다운 수를 출력한다.

item = int(input())

while item > 0:
    print(item)
    item -= 1