#연월일 입력받아 나누어 출력하기
#6자리 숫자로 이루어진 연월일(YYMMDD)이 입력된다.
#년도(YY) 월(MM) 일(DD)을 공백으로 구분해 한 줄로 출력한다.

item = input()

print(item[0] + item[1], item[2] + item[3], item[4] + item[5])

#or
print(item[0:2], item[2:4], item[4:6])