#숫자 입력을 받아서 출력
numbers = input('숫자를 입력해주세요: ')
print(numbers)

try:
    if int(numbers) == 5:
        print('오오~')
    else:
        print('오가 아닙니다.')
except:
    print('숫자를 입력하지 않았습니다.')