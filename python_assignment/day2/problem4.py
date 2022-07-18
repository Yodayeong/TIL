#1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

n = int(input())

#while문
temp = 0
total = 1 #곱하기 이므로, 초기화를 1로 해줘야함.

while temp < n:
    temp += 1
    total *= temp
print(total)

#for문
temp = 0
total = 1

for idx in range(n):
    temp += 1
    total *= temp
print(total)