#[오류 해결] 입력 받기

#두 수를 Input으로 받아 합을 구하는 코드이다.
#코드에서 오류를 찾아 원인을 적고, 수정하세요.

#numbers = input().split()
#print(sum(numbers))

#input
#10 20

#output
#30



#numbers를 정수형으로 바꾸어 주어야 한다.
numbers = map(int, input().split())
print(sum(numbers))