#점수 입력받아 평가 출력하기

#정수(0 ~ 100) 1개가 입력된다.

#평가 기준
#점수 범위 : 평가
#90 ~ 100 : A
#70 ~   89 : B
#40 ~   69 : C
#  0 ~   39 : D
#로 평가되어야 한다.

grade = int(input())

if grade >= 90:
    print('A')
elif grade >= 70:
    print('B')
elif grade >= 40:
    print('C')
else:
    print('D')