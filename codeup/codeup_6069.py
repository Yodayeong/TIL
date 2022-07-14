#평가 입력받아 다르게 출력하기

#영문자 1개가 입력된다.
#(A, B, C, D 등 문자 1개가 입력된다.)

#평가 내용
#평가 : 내용
#A : best!!!
#B : good!!
#C : run!
#D : slowly~
#나머지 문자들 : what?

item = input()

if item == 'A':
    print('best!!!')
elif item == 'B':
    print('good!!')
elif item == 'C':
    print('run!')
elif item == 'D':
    print('slowly~')
else:
    print('what?')