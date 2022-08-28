#절차 지향 프로그래밍
#함수화 해서 그 결과값을 다시 저장해서 활용.
#word 각각은 흘러다니는 data에 불과함.
word_list = ['abc', 'banana', 'apple']

def transform_uppercase(word):
    result = ''
    for char in word:
        number = ord(char)
        number = number-32
        result += chr(number)
    return result

for word in word_list:
    print(transform_uppercase(word))

#객체 지향 프로그래밍은
#메소드를 활용해서 S+V 형태로.
#word 자체가 주가 됨.(주어)
#그리고 동작함.(동사)
word = 'Hello!'
print(word.upper())





my_list = [1, 2, 3]
#리스트.sort()
#리스트의 데이터를 직접 정렬
my_list.sort()


my_list = [1, 2, 3]
#리스트는 sorted 함수의 인자로 전달될 뿐.
sorted(my_list)