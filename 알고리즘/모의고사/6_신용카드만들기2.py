#신용카드 만들기 2

#신용 카드를 만들려면 아래 두 가지의 조건을 모두 만족해야 한다.

#1. 카드 번호는 3, 4, 5, 6, 9 로 시작해야 한다.
#2. 카드 번호에 "-"이 들어갈 수 있으며 "-" 를 제외한 숫자의 개수는 16개이다.
#EX) 6471-6836-9525-5276
#EX) 3029192045012901

#카드 번호가 주어졌을 때 해당 번호로 신용카드를 만들 수 있는지 판별하는 프로그램을 작성하시오.

#[입력]
#첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
#각 테스트 케이스는 한 개의 줄로 이루어지며, 각 줄에는 `자연수`와 `-`로 이루어진 길이가 1 이상인 문자열이 주어진다. 

#[출력]
#각 테스트 케이스마다, 주어진 카드 번호로 신용 카드를 만들 수 있으면 1 만들 수 없으면 0을 출력한다.

import sys
sys.stdin = open('6_신용카드만들기2.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    credit_nums = input()
    if credit_nums[0] == '3' or credit_nums[0] == '4' or credit_nums[0] == '5' or credit_nums[0] == '6' or credit_nums[0] == '9':
        #credit의 첫째자리 조건 충족 후,
        credit_nums = credit_nums.replace('-', '')
        #'-'기호를 빼고
        if len(credit_nums) == 16:
            #credit의 길이 조건까지 충족하면
            print(f'#{i}', 1)
            #1 출력
        else:
            print(f'#{i}', 0)
    else:
        print(f'#{i}', 0)