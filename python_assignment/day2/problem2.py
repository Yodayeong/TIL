#문자열 word의 길이를 출력하는 코드를 for문(문자열 그대로) 으로 작성하시오.

#len() 함수 사용 금지

#for문
count = 0
word = input()

for char in word:
    count += 1
print(count)