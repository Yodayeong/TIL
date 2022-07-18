#텍스트 데이터 입력

#과일 데이터 fruits.txt를 활용하여 총 과일의 갯수를 01.txt  에 기록하시오.
#과일은 하나당 한 줄에 기록되어 있습니다.

with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    temp = f.read()
    fruits = temp.split('\n')

    cnt = 0
    for fruit in fruits:
        cnt += 1

with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(cnt))