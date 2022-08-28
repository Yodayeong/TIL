#주어진 숫자의 평균을 구하는 코드를 작성하시오.
#sum(), len()  함수 사용 금지

n = 0
sum = 0
numbers = [3, 10, 20]

for char in numbers:
    sum += int(numbers[n])
    n += 1
print(int(sum/3))