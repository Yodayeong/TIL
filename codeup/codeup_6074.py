#문자 1개 입력받아 알파벳 출력하기

#영문자 1개가 입력된다.
#(a ~ z)

#a부터 입력한 문자까지 순서대로 공백을 두고 한 줄로 출력한다.

item = ord(input())
first = 97
temp = ''

while first <= item:
    temp += chr(first)
    temp += ' '
    first += 1
print(temp)