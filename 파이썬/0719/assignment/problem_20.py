#각 자릿수의 합 구하기

#정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

#input
#123

#output
#6

number = int(input())
size = len(str(number))

init = 1
if size > 1:
    init *= 10**(size - 1)

total = 0
temp = number
while init >= 1:
    total += int(temp/init)
    temp = int(number%init)
    init /= 10
print(total)


#or (숫자를 문자로 형변환 해서 접근하기)
number = input()
size = len(number)

sum = 0
for i in range(size):
    sum += int(number[i])
print(sum)