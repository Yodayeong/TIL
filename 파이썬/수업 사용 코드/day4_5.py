#기본 순회
#key가 기준이고, 직접 딕셔너리에 key로 접근하면 value를 얻을 수 있다!
my_dict = {'apple': '사과', 'banana': '바나나'}

for word in my_dict:
    print(word, my_dict[word]) #key값, value값 접근

#다양한 방법 => 일종의 리스트!
print(my_dict.keys())
#dict_keys(['apple', 'banana'])
print(my_dict.values())
#dict_values(['사과', '바나나'])
for value in my_dict.values():
    print(value)

#일종의 리스트 안에, tuple!
print(my_dict.items())
#dict_items([('apple', '사과'), ('banana', '바나나')])
for k, v in my_dict.items():
    print(k, v)