#문장 1개 입력받아 3번 출력하기
#정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.

item = input()
print(item, item, item) #공백으로 구분해 한 줄로 출력

print(3*item) #공백 없이 한 줄로 출력

#실수의 경우, 3번 출력 말고 3을 곱한 값을 출력하고 싶다.
print(3*float(item))