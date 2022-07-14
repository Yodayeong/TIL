#주민번호 입력받아 형태 바꿔 출력하기
#주민번호는 다음과 같이 구성된다.
#XXXXXX-XXXXXXX

#'-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.

id_first, id_last = input().split('-')

print(id_first + id_last)