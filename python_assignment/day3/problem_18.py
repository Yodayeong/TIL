#알파벳 등장 갯수 구하기

#문자열 word가 주어질 때, 
#Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

#dictionary에 해당 알파벳 갯수가 있으면 (개수 + 1)
#없으면 dictionary에 새로 추가 및 개수는 1

my_dict = dict()
word = input()

for i in word:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

for i in my_dict:
    print(i, my_dict[i])