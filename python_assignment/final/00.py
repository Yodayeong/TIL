#텍스트 데이터 출력

#아래의 내용을  00.txt에 기록하시오.

#N회차 홍길동
#Hello, Python!
#1일차 파이썬 공부 중
#2일차 파이썬 공부 중
#3일차 파이썬 공부 중
#4일차 파이썬 공부 중
#5일차 파이썬 공부 중

with open('00.txt', 'w', encoding='utf-8') as f:
    f.write('N회차 홍길동\n')
    f.write('Hello, Python!\n')
    for i in range(1, 6):
        f.write(f'{1}일차 파이썬 공부 중\n')