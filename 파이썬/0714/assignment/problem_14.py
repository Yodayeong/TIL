#문자의 갯수 구하기

#문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
#count() 메서드 사용 금지

cnt = 0
word = input()

for i in word:
    if i == 'a':
        cnt += 1
print(cnt)