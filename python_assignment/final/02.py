#텍스트 데이터 활용 - 특정 단어 추출

#과일 데이터 fruits.txt를 활용하여 berry로 끝나는 과일의 갯수와 목록을 02.txt에 기록하시오.
#과일은 하나당 한 줄에 기록되어 있습니다.

with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    temp = f.read()
    fruits = temp.split('\n')

    cnt = 0
    berry_list = dict()

    for fruit in fruits:
        if (fruit[-1] == 'y') and (fruit[-2] == 'r') and (fruit[-3] == 'r') and (fruit[-4] == 'e') and (fruit[-5] == 'b'):
            if fruit in berry_list:
                continue
            else:
                cnt += 1
                berry_list[fruit] = 1
    
with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(str(cnt))
    f.write('\n')
    for i in berry_list:
        f.write(str(i))
        f.write('\n')