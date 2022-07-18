#주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
#max() 함수 사용 금지

numbers = [0, 20, 100]

#초기화
if int(numbers[0]) > int(numbers[1]):
    max = int(numbers[0])
    second = int(numbers[1])
else:
    max = int(numbers[1])
    second = int(numbers[0])

for i in numbers:
    if(int(i) > max):
        second = max
        max = int(i)
    elif(int(i) > second):
        if int(i) == max: #중복되는 수 제거
            continue
        second = int(i) 
print(second)