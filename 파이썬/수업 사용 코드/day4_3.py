#리스트는 mutable
a = [1, 2, 3]
a[0] = 100
print(a)

#문자열은 immutable
a = 'hi'
a[0] = 'c'
print(a)