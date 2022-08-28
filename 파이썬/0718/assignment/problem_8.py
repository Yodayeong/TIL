#[오류 해결] 모음의 개수 찾기

#아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
#코드에서 오류를 찾아 원인을 적고, 수정하세요.

#word = "HappyHacking"
#count = 0
#for char in word:
#    if char == "a" or "e" or "i" or "o" or "u":
#        count += 1
#print(count)

#output
#3



#조건을 명시할 때 각 조건을 정확하게 명시해야 한다.
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)