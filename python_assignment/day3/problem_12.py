#문자열 조작하기

#주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

#<string>.replace('x', '')
#string에서 x는 ''로 대체하여 준다.

word = input()

temp = word.replace('a', '')

print(temp)

#or
temp = ''
word = input()

for i in word:
    if i == 'a':
        continue
    temp += i
print(temp)