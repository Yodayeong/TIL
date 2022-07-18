#[오류 해결] 과일 개수 구하기

#아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
#코드에서 오류를 찾아 원인을 적고, 수정하세요.

#from pprint import pprint

#fruits = [
#    "Soursop",
#    "Grapefruit",
#    "Apricot",
#    "Juniper berry",
#    "Feijoa",
#    "Blackcurrant",
#    "Cantaloupe",
#    "Salal berry",
#]

#fruit_count = {}

#for fruit in fruits:
#    if fruit not in fruit_count:
#        fruit_count = {fruit: 1}
#    else:
#        fruit_count[fruit] += 1

#pprint(fruit_count)

#output
#{'Apricot': 1,
# 'Blackcurrant': 1,
# 'Cantaloupe': 1,
# 'Feijoa': 1,
# 'Grapefruit': 1,
# 'Juniper berry': 1,
# 'Salal berry': 1,
# 'Soursop': 1}



#fruit_count = {fruit: 1}라고 해버리면 fruit라는 key에 1이 추가되는 것이 아니라
#dic에 추가된 이전의 값들은 사라지고, {'fruit': 1}만 추가가 된다.

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)