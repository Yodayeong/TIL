#문자의 위치 구하기

#문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
#a 가 없는 경우에는 -1을 출력해주세요.
#find() index() 메서드 사용 금지

cnt = 0
word = input()

for i in word:
    if i == 'a':
        break
    cnt += 1
    
if cnt == len(word):
    print(-1)
else:
    print(cnt)