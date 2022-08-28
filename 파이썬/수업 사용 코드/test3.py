a = 5  
b = '5'  
print(a, type(a))
print(b, type(b))

#길이
fruit = 'abcde'
print(len(fruit))

#접근/인덱싱
print(fruit[1])

#슬라이싱
print(fruit[1:3])
#인덱스 1이상, 3미만
#a b c d e
#0 1 2 3 4

#마지막 값은?
#파이썬은 음의 인덱스도 가지고 있다!
print(fruit[-1])

#step
print(fruit[2:5:2])
#2부터 5까지 중에 step이 2

print(fruit[:3])
#처음부터 3까지

print(fruit[3:])
#5부터 끝까지