#비트단위로 NOT 하여 출력하기

#정수 1개가 입력된다.
#-2147483648 ~ +2147483647

#비트 단위로 1 -> 0, 0 -> 1로 바꾼 후 그 값을 10진수로 출력한다.

#비트
#NOT: ~
#AND: &
#OR: |
#XOR: ^
#<<: left shift
#>>: right shift

item = int(input())

print(~item)