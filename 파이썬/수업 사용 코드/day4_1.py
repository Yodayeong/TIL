#리스트 메서드 활용
a = [10, 1, 100]
#정렬(sort)
new_a = a.sort()
print(a, new_a)
#[1, 10, 100] None
#리스트 메서드를 활용하면, 그 메서드를 정렬된 상태로 변경(원본 변경)
#return되는 것은 None

#리스트에 sorted 함수를 활용
b = [10, 1, 100]
#정렬(sort)
new_b = sorted(b)
print(b, new_b)
#[10, 1, 100] [1, 10, 100]
#sorted 함수를 활용하면, 원본을 변경하지 않음
#return 되는 것은 정렬된 리스트
#input을 받고 output을 내놓음

#실제 활용 코드
a = [10, 1, 100]
a.sort()
#a를 정렬된 상태로 활용

b = [10, 1, 100]
b = sorted(b)
#b를 정렬된 상태로 활용