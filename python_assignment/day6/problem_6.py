#[오류 해결] 1부터 N까지의 2의 곱 저장하기

#아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
#코드에서 오류를 찾아 원인을 적고, 수정하세요.

#N = 10
#answer = ()
#for number in range(N + 1):
#    answer.append(number * 2)
#print(answer)

#output
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



#튜플 자료형은 append 할 수 없다.
#answer를 list 자료형으로 두어야 한다.
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)
print(answer)