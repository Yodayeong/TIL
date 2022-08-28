# 제어문

- 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
- 제어문은 순서도(flow char)로 표현이 가능

## 조건문

- 참/거짓을 판단할 수 있는 조건식과 함께 사용

- 기본형식

  - expression에는 참/거짓에 대한 조건식

  - ```bash
    if <expression>:
        # Run this Code block
    else:
        # Run this Code block
    ```

- 조건문을 통해 변수 num의 값의 홀수/짝수 여부를 출력하시오.

  - 이때 num은 input을 통해 사용자로부터 입력을 받으시오.

  - ```bash
    num = int(input())
    if num % 2 == 1:
        print('홀수')
    else:
        print('짝수')
    ```

## 복수 조건문

- 복수의 조건식을 활용할 경우 elif를 활용하여 표현함

- 기본형식

  - ```bash
    if <expression>:
        # Code block
    elif <expression>:
    	# Code block
    elif <expression>:
    	# Code block
    else:
    	# Code block
    ```

- 다음은 미세먼지 농도에 따른 등급일 때, dust 값에 따라 등급을 출력하는 조건식을 작성하시오.

  ![KakaoTalk_20220712_094921784](python 제어문.assets/KakaoTalk_20220712_094921784-16575870350652.jpg)

  - ```bash
    dust = int(input())
    #dust가 150보다 크면, 매우 나쁨
    if dust > 150:
    	print('매우 나쁨')
    #80보다 크면, 나쁨
    elif dust > 80:
    	print('나쁨')
    #30보다 크면, 보통
    elif dust > 30:
    	print('보통')
    #좋음
    else:
    	print('좋음')
    ```

## 중첩 조건문

- 조건문은 다른 조건문에 중첩되어 사용될 수 있음

- 기본형식

  - ```bash
    if <expression>:
    	# Code block
    	if <expression>:
    		# Code block
    else:
    	# Code block
    ```

- 위의 미세먼저 문제의 코드에서 중첩조건문을 활용하여 미세먼지 농도(dust 값)이 300이 넘는 경우 '실외 활동을 자제하세요'를 추가적으로 출력하고 음수인 경우 '값이 잘못 되었습니다'를 출력하시오.

  - ```bash
    dust = int(input())
    
    if dust > 150:
        if dust > 300:
            print('실외 활동을 자제하세요')
        print('매우 나쁨')
    elif dust > 80:
        print('나쁨')
    elif dust > 30:
        print('보통')
    else:
        if dust < 0:
            print('값이 잘못 되었습니다')
        else:
            print('좋음')
    ```

## 조건 표현식

- num이 정수일 때, 아래의 코드는 무엇을 위한 코드일까요?

  - 절대값 계산기

  - ```bash
    num = -10
    
    ##조건문 코드
    #1. 양수면 그대로
    if num >= 0:
        value = num
    #2. 음수면 -붙여서
    else:
        value = -num
    print(num, value)
    
    ##조건 표현식 코드
    value = num if num >= 0 else -num
    ```

- 다음의 코드와 동일한 조건 표현식을 작성하시오.

  - ```bash
    num = 2
    if num % 2:
        result = '홀'
    else:
        result = '짝'
    print(result)
    ```

  - ```bash
    num = 2
    result = '홀' if num % 2 else '짝'
    print(result)
    ```

- 다음의 코드와 동일한 조건문을 작성하시오.

  - ```bash
    num = -5
    value = num if num >= 0 else 0
    print(value)
    ```

  - ```bash
    num = -5
    if num >= 0:
    	value = num
    else:
    	value = 0
    print(value)
    ```

## 반복문

- 특정 조건을 도달할 때까지, 계속 반복되는 일련의 문장

## while문

- 조건식이 참인 경우 반복적으로 코드를 실행

- 무한 루프를 하지 않도록 종료조건이 반드시 필요

- 기본형식

  - ```bash
    while <expression>:
    	# Code block
    ```

- 1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드를 작성하시오.

  - ```bash
    #값 초기화
    n = 0
    total = 0
    user_input = int(input())
    
    while n < user_input:
        n += 1
        total += n
    print(total)
    ```

## for문

- 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable) 요소를 모두 순회함

- 처음부터 끝까지 모두 훈회하므로 별도의 종료조건이 필요하지 않음

- 기본형식

  - ```bash
    for <변수명> in <iterable>:
    	# Code block
    ```

  - ```bash
    for fruit in ['apple', 'mango', 'banana']
    	print(fruit)
    print('끝')
    ```

- 사용자가 입력한 문자를 한 글자씩 세로로 출력하시오.

  - ```bash
    chars = input()
    for char in chars:
    	print(char)
    ```

- 사용자가 입력한 문자를 range를 활용하여 한 글자씩 출력하시오.

  - ```bash
    chars = input()
    for idx in range(len(chars))
    	print(chars[idx])
    ```

- 딕셔너리 순회

  : 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용

  - ```bash
    grades = {'john': 80, 'eric': 90}
    for name in grades:
    	print(name, grades[name])
    ```

    => john 80

     	 eric 90

## 반복문 제어

### 1. break

- break문을 만나면 반복문은 종료됨

  - ```bash
    n = 0
    while True:
    	if n == 3:
    		break
    	print(n)
    	n += 1
    ```

    => 0

    ​      1

    ​      2

  - ```bash
    for i in range(10):
    	if i > 1:
    		print('0과 1만 필요해!')
    		break
    	print(i)
    ```

    => 0

    ​	  1

    ​      0과 1만 필요해!

### 2. continue

- continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

  - ```bash
    for i in range(6)
    	if i % 2 == 0:
    		continue
    	print(i)
    ```

    => 1

    ​	  3

    ​	  5

### 3. for-else

- 끝까지 반복문을 실행한 이후에 else문 실행

  => else문은 break로 중단되었는지 여부에 따라 실행

  - ```bash
    for char in 'apple'
    	if char == 'b'
    		print('b!')
    		break
    else:
    	print('b가 없습니다.')
    ```

    => b가 없습니다.

  - ```bash
    for char in 'banana':
    	if char == 'b':
    		print('b!')
    		break
    else:
    	print('b가 없습니다.')
    ```

    => b!
