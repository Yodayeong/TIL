#정수 2개 입력받아 그대로 출력하기2
#공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

item = input()
splited_item = item.split() #splited_item = ['1', '2', ...]

#ex) splited_item = item.split(':')
#':'기호를 기준으로 item을 split

print(int(splited_item[0]))
print(int(splited_item[1]))


#or
a, b = input().split()

print(int(a))
print(int(b))