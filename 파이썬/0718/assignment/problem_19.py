#숫자의 길이 구하기

#양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
#양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

#input
#123

#output
#3

number = int(input())

i = 1
output = 1
cnt = 0
while output != 0:
    i *= 10
    cnt += 1
    output = int(number / i)
print(cnt)
