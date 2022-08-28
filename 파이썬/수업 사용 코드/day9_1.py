#list comprehension
#홀짝 구분해서 짝수 리스트 만들기

even_list = [i for i in range(10) if i % 2 == 0]
print(even_list)

#짝수 제곱 리스트 만들기
even_list_2 = [i**2 for i in range(10) if i % 2 == 0]
#전체 합
print(sum(even_list_2))