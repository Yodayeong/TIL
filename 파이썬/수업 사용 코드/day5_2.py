import random

numbers = random.sample([1, 2, 3], 2)
print(numbers, type(numbers))
#[1, 2] <class 'list'>


#1~45까지의 숫자!
#그 중에 6개
n = int(input('얼마 쓸래? '))
for i in range(n): #사용자가 입력한 수만큼 반복
    numbers = random.sample(range(1, 46), 6)
    numbers.sort() #정렬
    print(numbers)