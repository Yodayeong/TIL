import random

#이것을 클래스로 정의하면
#n을 넣으면
#그 횟수만큼 출력해줌
def generate_lotto(n):
    result = []
    for i in range(n):
        numbers = range(1, 45)
        pick = random.sample(numbers, 6)
        pick.sort()
        result.append(pick)
    return result

def check(buy_numbers, result_numbers):
    return 0