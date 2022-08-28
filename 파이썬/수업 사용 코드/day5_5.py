with open('students.txt', 'r', encoding='utf-8') as f:
    #한 줄씩 출력됨
    #lines = f.readline()
    #print(lines)

    #전체 출력
    for line in f:
        print(line, end = '') #개행이 기본 들어가있기 때문에 없애줌