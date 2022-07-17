#텍스트 데이터 활용 - 등장 횟수

#과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.

with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    temp = f.read()
    fruits = temp.split('\n')

    cnt = 0
    fruit_list = dict()
    for fruit in fruits:
        if fruit in fruit_list:
            fruit_list[fruit] += 1
        else:
            fruit_list[fruit] = 1

with open('03.txt', 'w', encoding='utf-8') as f:
    for i in fruit_list:
        f.write(i)
        f.write(' ')
        f.write(str(fruit_list[i]))
        f.write('\n')