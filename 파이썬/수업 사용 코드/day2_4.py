num = -10

##조건문 코드
#1. 양수면 그대로
if num >= 0:
    value = num
#2. 음수면 -붙여서
else:
    value = -num
print(num, value)

#조건 표현식 코드
value = num if num >= 0 else -num