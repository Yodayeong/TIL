#소문자-대문자 변환하기

#소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
#.upper(), .swapcase() 사용 금지

#ord() : 특정 문자에 대응되는 유니코드 숫자로 반환하는 함수
#chr() : 해당 유니코드 숫자를 문자로 반환하는 함수

temp = ''
word = input()

for i in word:
    temp += chr(ord(i) - 32)
print(temp)