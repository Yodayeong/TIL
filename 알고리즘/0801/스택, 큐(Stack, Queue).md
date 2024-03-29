## 스택, 큐(Stack, Queue)





(복습)

**프로그램 = 데이터 구조 + 알고리즘**

- 데이터 구조 : 리스트. 딕셔너리. 튜플. 문자열

  => 문제 상황에 따라 더 적합한 통이 필요하다!

  

  ![캡처](스택, 큐(Stack, Queue).assets/캡처.PNG)



## 스택(stack)

- 데이터를 한쪽에서만 넣고 빼는 자료구조
- 가장 마지막에 들어온 데이터가 가장 먼저 나가므로 LIFO(Last-in First-out, 후입선출) 방식

- 스택 자료구조 대표 동작
  - push : 스택에 새로운 데이터를 삽입하는 행위
  - pop : 스택의 가장 마지막 데이터를 가져오는 행위
- 스택이 필요한 이유
  - 뒤집기, 되돌리기, 되돌아가기
  - 마무리 되지 않은 일을 임시 저장
- 파이썬은 리스트(List)로 스택을 간편하게 사용할 수 있다!
  - .append(원소)
  - .pop()



## 큐(Queue)

- 한 쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺄 수 있는 자료구조

- 가장 먼저 들어온 데이터가 가장 먼저 나가므로 FIFO(First-in First-out, 선입선출) 방식

- 큐 자료구조 대표 동작

  - enqueue : 큐의 맨 뒤에 데이터를 삽입하는 행위
  - dequeue : 큐의 맨 앞 데이터를 가져오는 행위

- 큐 자료구조도 파이썬 리스트(List)로 간편하게 사용할 수 있다!

  - .append(원소)
  - pop(0)

- 리스트를 이용한 큐 자료구조의 단점

  - 데이터를 뺄 때 큐 안에 있는 데이터가 많은 경우 비효율적이다.

    맨 앞 데이터가 빠지면서, 리스트의 인덱스가 하나씩 당겨지기 때문이다.

    => **덱(Double - Ended Queue) 자료구조**

    ​	  : 양 방향으로 삽입과 삭제가 자유로운 큐

    ​		양 방향 삽입, 추출이 모두 큐보다 훨씬 빠르다.

     - 앞 쪽에서 넣고 뺄 때 : appendleft(), <u>popleft()</u>

     - 뒤 쪽에서 넣고 뺄 때 : <u>append()</u>, pop()

     - ```bash
       from collections import deque
       
       numbers = [1, 2, 3, 4, 5]
       
       queue = deque(numbers)
       
       queue.append(6)
       queue.popleft()
       
       print(queue) #deque([2, 3, 4, 5, 6])
       ```