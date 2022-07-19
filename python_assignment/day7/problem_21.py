#숫자 뒤집기

#주어진 숫자를 뒤집은 결과를 출력하시오. 
#* 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

#input
#1234

#output
#4321

item = int(input())
reversed_item = []

while (item >= 1):
    reversed_item.append(int(item%10))
    item /= 10

for i in reversed_item:
    print(i, end = '')