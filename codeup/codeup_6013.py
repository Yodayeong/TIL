#문자 2개 입력받아 순서 바꿔 출력하기1
#줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.

item_1 = input()
item_2 = input()

temp = item_1
item_1 = item_2
item_2 = temp

print(item_1)
print(item_2)