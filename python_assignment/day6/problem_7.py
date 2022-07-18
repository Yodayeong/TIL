#[오류 해결] 평균 구하기

#아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
#코드에서 오류를 찾아 원인을 적고, 수정하세요.

#number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#total = 0
#count = 0
#for number in number_list:
#    total += number
#count += 1
#print(total // count)

#output
#5.5



#count 계산에서 indent 오류가 있고, 
#맨마지막 줄 평균 계산에서 나누기 기호가 하나만 있어야 한다.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)