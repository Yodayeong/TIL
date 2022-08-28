numbers = ['1', '2', '3']

#숫자로 바꿔서 쓰고 싶다?
#리스트를 숫자로 형 변환은 불가능합니다.
#다만, 숫자 형태의 문자를 변환할 수는 있습니다.
# n = int(numbers)

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
new_numbers = [a, b, c]
print(new_numbers)

#반복문!
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

#map
#모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
numbers = ['1', '2', '3']
new_numbers_2 = map(int, numbers)
print(new_numbers_2)
print(list(new_numbers))