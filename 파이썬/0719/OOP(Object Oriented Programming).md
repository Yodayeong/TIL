## OOP(Object Oriented Programming)

=> 객체 지향 프로그래밍



파이썬은 모든 것이 객체

S + V



타입(종류)과 실제 사례(값)

class와 instance



객체(컴퓨터 과학)

오브젝트는 클래스에서 정의한 것을 토대로 메모리

-----------------------------------------------------



파이썬은 모든 것이 객체로 이루어져 있다.

객체(object)는 특정 타입(class)의 인스턴스(instance)이다.

- 123, 900, 5는 모두 int의 인스턴스
- 'hello', 'bye'는 모두 string의 인스턴스
- [232, 89, 1], []은 모두 list의 인스턴스



객체의 특징

- 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
- 속성(attribute) : 어떤 상태(데이터)를 가지는가?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?



객제지향 프로그래밍이란?

프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법



절차지향 프로그래밍

```bash
#함수 활용
def area(x, y):
	return x * y
	
def circumference(x, y):
	return 2 * (x + y)
	
a = 10
b = 30
c = 300
d = 20
square1_area = area(a, b)
square1_circumference = curcumference(a, b)
square2_area = area(c, d)
square2_circumference = circumference(c, d)
```



객체지향 프로그래밍

```bash
#클래스 정의
class Rectangle:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
    #클래스가 가지는 메서드 정의
    #ex)문자열.리스트.. 각각이 가지는 메서드가 다름
	def area(self):
		return self.x * self.y
	
	def circumference(self):
		return 2 * (self.x + self.y)
		
r1 = Rectangle(10, 30)
r1.area()
r1.circumference()

r2 = Rectangle(300, 20)
r2.area()
r2.circumference()
```

- 사각형 : 클래스(class)
- 각 사각형(r1, r2) : 인스턴스(instance)
- 사각형의 정보(가로 길이, 세로 길이) : 속성(attribute)
- 사각형의 행동/기능(넓이를 구한다, 높이를 구한다) : 메소드(method)

-----------



## OOP 기초

### 기본 문법

```bash
#클래스 정의
class MyClass:
	pass
#인스턴스 생성
my_instance = MyClass()
#매서드 호출
my_instance.my_method()
#속성
my_instance.my_attribute
```



### 클래스와 인스턴스

- 클래스(class) : 객체들의 분류

- 인스턴스(instance) : 하나하나의 실체/예

  ```bash
  class Person:
  	pass
  
  print(type(Person))
  #type
  p1 = Person()
  type(p1)
  #__main__.Person
  isinstance(person1, person2)
  #True
  ```

- 속성 : 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미

- 메소드 : 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)   

  - 클래스의 내부에 정의된 함수

- 객체 비교하기

  - == : 변수가 참조하는 객체가 동등한(내용이 같은) 경우 TRUE

  - is : 두 변수가 동일한 객체를 가리키는 경우 TRUE

    ```bash
    a = [1, 2, 3]
    b = [1, 2, 3]
    
    print(a == b, a is b)
    #True False
    ```

    => 값은 같지만, 주소가 다름

    ```bash
    a = [1, 2, 3]
    b = a
    
    print(a == b, a is b)
    #True True
    ```

    => 값이 같고, 주소도 같음

    => 같은 객체를 가리킴

- 인스턴스 메서드 : 인스턴스 조작을 위한 메서드

  - 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

- 생성자 메서드 : 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드

- 소멸자 메서드 : 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메서드