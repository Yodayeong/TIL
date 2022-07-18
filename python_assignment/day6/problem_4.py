#[오류 해결] 입력 받기 - 2

#아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
#코드에서 오류를 찾아 원인을 적고, 수정하세요.

#words = list(map(int, input().split()))
#print(words)

#input
#I'm Tutor 6

#output
#["I'm", 'Tutor', '6']



#문자열을 map을 통해서 정수로 받아버렸다.
words = list(input().split())
print(words)