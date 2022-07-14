#이상한 출석 번호 부르기1

#첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
#두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

#1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.

n = int(input())
numbers = input().split()
my_dict = {}

for i in numbers:
    if i in my_dict:
        my_dict[i] += 1
        print('1')
    else:
        my_dict[i] = 1
        print('2')

print(my_dict.items())