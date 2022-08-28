#키워드로 sep를 바꿔서 호출할 수 있음
print('hi', 'hello', sep='-')
print(1, 2, 3, 4, 5, 6, 7, 8)


#정해지지 않은 갯수의 인자
def my_add(*numbers):
    #내부적으로 numbers가 tuple
    return numbers

result = my_add(1, 2, 3)
print(result, type(result)) #(1, 2, 3) <class 'tuple'>

def my_func(**kwargs):
    return kwargs

result = my_func(name='홍길동', age='100', gender='M')
print(result, type(result)) #{'name': '홍길동', 'age': '100', 'gender': 'M'} => 딕셔너리