#얕은 복사
a = [1, 2, 3]
b = a #변수에 메모리 주소값이 할당된 것.
b[0] = 'hi'

#a를 출력
print(a) #['hi', 2, 3]
#b를 출력
print(b) #['hi', 2, 3]

#list 형변환 결과 : 사실은 list고 사실은 값도 같지만 다른 메모리 주소 결과를 받아냄
c = [3, 4, 5]
d = list(c)
d[0] = 'hi'

#c를 출력
print(c) #[3, 4, 5]
#d를 출력
print(d) #['hi', 4, 5]

#슬라이싱
e = [4, 5, 6]
f = e[::]
f[0] = 'hi'

#깊은 복사
a = [[1, 2], 2, 3]
b = list(a) #list 안에 list의 주소가 담김
b[0][0] = 'hi'

#a를 출력
print(a) #[['hi', 2], 2, 3]
#b를 출력
print(b) #[['hi', 2], 2, 3]

import copy
a = [[1, 2], 2, 3]
b = copy.deepcopy(a)
b[0][0] = 'hi'
print(a)
print(b)

#얕은 복사
#리스트 주소가 123
#a = '12345'
