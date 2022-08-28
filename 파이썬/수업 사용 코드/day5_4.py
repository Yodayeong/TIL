#파일명, 어떤 모드로 열지,
#인코딩을 설정
with open('students.txt', 'r', encoding='utf-8') as f:
    #텍스트는 string 타입
    text = f.read()
    print(text, type(text))
    #string.split() => list 타입
    names = text.split()
    #김씨인 사람의 수를 구하시오.
    cnt = 0
    for name in names:
        #name : 첫번째 시행 - 김세환
        #언제? 김씨?
        if name[0] == '김':
            cnt += 1
    print(cnt)