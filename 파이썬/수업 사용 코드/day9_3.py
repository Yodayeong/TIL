#3의 배수인 리스트로만 만들기
numbers = [1, 2, 5, 10, 3, 9, 12]

#기본 반복/조건 코드
result = []
for number in numbers:
    if number % 3 == 0:
        result.append(number)
print(result)

#lambda 활용
print(list(filter(lambda n: n%3==0, numbers)))

#어떤 느낌이냐면
def is_3(n):
    return n % 3 == 0
print(list(filter(is_3, numbers)))