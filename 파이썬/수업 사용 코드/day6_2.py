#100을 사용자가 입력한 숫자로 나눠서 결과를 출력
number = input()

try:
    print(100/int(number))
except ZeroDivisionError:
    print('0으로 나눌 수는 없습니다.')
except ValueError:
    print('숫자 형식을 입력해주세요.')
except Exception: #무슨 오류인지 모르겠지만, 모든 오류 (가장 상위의 오류)
    print('오류')