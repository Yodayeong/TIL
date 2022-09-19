## ECMA Script



## 변수와 식별자

- 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함

- 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작

- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작

- 예약어(for, if, function ...) 사용 불가능 

- ```js
  let foo		//선언
  console.log(foo)	//undefined
  
  foo = 11		//할당
  console.log(foo)	//11
  
  let bar = 0		//선언 + 할당
  console.log(bar)	//0
  ```



### let, const

- **let**

- 재할당 가능

  ```js
  let number = 10	//1. 선언 및 초기값 할당
  number = 10	//2. 재할당
  
  console.log(number)	//10
  ```

- 재선언 불가능

  ```js
  let number = 10 //1. 선언 및 초기값 할당
  let number = 50 //2. 재선언 불가능
  
  //에러
  ```

  

- **const**

- 재할당 불가능

  ```js
  const number = 10 //1. 선언 및 초기값 할당
  number = 10	//2. 재할당 불가능
  
  //에러
  ```

- 재선언 불가능

  ```js
  const number = 10 //1. 선언 및 초기값 할당
  const number = 50 //2. 재선언 불가능
  
  //에러
  ```



- 블록 스코프(block scope) - **let, const 둘다 가지는 속성**

  - if, for, 함수 등의 중괄호 내부

  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

  - ```js
    let x = 1
    
    if(x === 1) {
        let x = 2
        console.log(x) //2
    }
    
    console.log(x) //1
    ```

    

### var

- var로 선언한 변수는 재선언 및 재할당 모두 가능

- ES6 이전에 변수를 선언할 때 사용되던 키워드

- 함수 스코프

  - 함수의 중괄호 내부를 가리킴

  - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

  - ```js
    function foo() {
        var x = 5
        console.log(x) //5
    }
    
    //ReferenceError: x is not defined
    console.log(x)
    ```

- 호이스팅

  - 변수를 선언 이전에 참조할 수 있는 현상

  - 변수 선언 이전의 위치에서 접근 시 undefined를 반환

  - 자바스크립트는 모든 선언을 호이스팅

  - 즉, var, let, const 모두 호이스팅이 발생하지만, var는 선언과  초기화가 동시에 발생하여 일시적 사각지대가 존재하지 않음

  - ```js
    console.log(username) //undefined
    var username = '홍길동'
    
    console.log(email) //error
    let email = 'gildong@gmail.com'
    
    console.log(age) //age
    const age = 50
    ```

  

### let, const, var 비교

| 키워드 | 재선언 | 재할당 | 스코프      | 비고         |
| ------ | ------ | ------ | ----------- | ------------ |
| let    | X      | O      | 블록 스코프 | ES6부터 도입 |
| const  | X      | X      | 블록 스코프 | ES6부터 도입 |
| var    | O      | O      | 함수 스코프 | 사용 X       |



## 데이터 타입

- 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐
- 크게 원시타입(primitive tye)과 참조타입(reference type)으로 분류됨



### 원시 타입(Primitive type)

- 객체(object)가 아닌 기본 타입

- 변수에 해당 타입의 값이 담김

- 다른 변수에 복사할 때 실제 값이 복사됨

- ```js
  let message = '안녕하세요!'
  
  let greeting = message
  console.log(greeting) //안녕하세요!
  
  message = 'Hello, world!'
  console.log(greeting) //안녕하세요!
  ```



### 참조 타입(Reference type)

- 객체(object) 타입의 자료형

- 변수에 해당 객체의 참조 값이 담김

- 다른 변수에 복사할 때 참조 값이 복사됨

- ```js
  const message = ['안녕하세요']
  
  const greeting = message
  console.log(greeting) //안녕하세요
  
  message[0] = 'Hello, world!'
  console.log(greeting) //Hello, world!
  ```



### 숫자 타입

- 정수, 실수 구분 없는 하나의 숫자 타입

- 부동소수점 형식을 따름

- ```js
  const a = 13	//양의 정수
  const b = -5	//음의 정수
  const c = 3.14	//실수
  const d = 2.998e8	//거듭제곱
  const e = Infinity	//양의 무한대
  const f = -Infinity	//음의 무한대
  const g = NaN	//산술 연산 불가
  ```



### 문자열 타입

- 텍스트 데이터를 나타내는 타입

- 16비트 유니코드 문자의 집합

- 작은따옴표 또는 큰따옴표 모두 가능

- 템플릿 리터럴(Template Literal)

  - ES6부터 지원
  - 따옴표 대신 backtick(``)으로 표현
  - ${ expression } 형태로 표현식 삽입 가능

- ```js
  const firstName = 'Brandan'
  const lastName = 'Eich'
  const fullName = `${firstName} ${lastName}`
  
  console.log(fullName) //Brandan Eich
  ```



### null

- 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입

- ```js
  let firstName = null
  console.log(firstName) //null
  
  typeof null //object
  ```



### Boolean 타입

- 논리적 참 또는 거짓을 나타내는 타입

- true 또는 false로 표현

- 조건문 또는 반복문에서 유용하게 사용

- ```js
  let isAdmin = true
  console.log(Admin) //true
  
  isAdmin = false
  console.log(isAdmin) //false
  ```



## 연산자



### 할당 연산자

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자

- ```js
  let x = 0
  
  x += 10
  console.log(x) //10
  
  x -= 3
  console.log(x) //7
  
  x *= 10
  console.log(x) //70
  
  x /= 10
  console.log(x) //7
  ```



### 비교 연산자

- 피연산자를 비교하고 결과값을 boolean으로 반환하는 연산자

- 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교

- ```js
  const numOne = 1
  const numTwo = 100
  console.log(numOne < numTwo) //true
  
  const charOne = 'a'
  const charTwo = 'z'
  console.log(charOne > charTwo) //false
  ```



### 동등 비교 연산자

### 일치 비교 연산자(===)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환

- ```js
  const a = 1004
  const b = '1004'
  console.log(a === b) //false
  
  const c = 1
  const d = true
  console.log(c === d) //
  ```



### 논리 연산자

- 세가지 논리 연산자로 구성

  - and 연산은 '&&'
  - or 연산은 '||'
  - not 연산은 '!'

- ```js
  //and 연산
  console.log(true && false)	//false
  console.log(1 && 0)			//0
  console.log(4 && 7)			//7
  console.log('' && 5)		//''
  
  //or 연산
  console.log(true || false)	//true
  console.log(1 || 0)			//1
  console.log(4 || 7)			//4
  console.log('' || 5)		//5
  
  //not 연산
  console.log(!true)			//false
  console.log(!'Bonjour!')	//false
  ```



## 조건문



### 'if' statement

- 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단

- if, else if, else

- ```js
  const nation = 'Korea'
  
  if (nation === 'Korea') {
      console.log('안녕하세요!')
  } else if (nation === 'France') {
      console.log('Bonjour!')
  } else {
      console.log('Hello!')
  }
  ```



### 'switch' statement

- 주로 표현식의 결과값이 어느 값(case)에 해당하는지 판별
- 주로 특정 변수의 값에 따라 조건을 분기할 때 활용
  - 조건이 많아질 경우 if문보다 가독성이 나을 수 있음

- 표현식(expression)의 결과값을 이용한 조건문

- 표현식의 결과값과 case문의 오른쪽 값을 비교

- break 및 default문 선택적으로 사용 가능

- ```js
  const nation = 'Korea'
  
  switch(nation) {
      case 'Korea': {
          console.log('안녕하세요!')
      }
      case 'France': {
          console.log('Bonjour!')
      }
      default:
          console.log('Hello!')
  }
  
  //switch문은 몇 번 출력될까?
  //break문을 만나지 못해서 총 3번 출력('안녕하세요', 'Bonjour!', 'Hello!')
  //만약 nation = 'France'라면, 총 2번 출력('Bonjour!', 'Hello!')
  ```



## 반복문



### while

- 조건문이 참(true)인 동안 반복 시행

- ```js
  let i = 0
  
  while(i < 6) {
      console.log(i) //0, 1, 2, 3, 4, 5
      i += 1
  }
  ```



### for

- 세미콜론(;)으로 구분되는 세 부분으로 구성

- initialization

  - 최초 반복문 진입 시 1회만 실행되는 부분

- condition

  - 매 반복 시행 전 평가되는 부분

- expression

  - 매 반복 시행 이후 평가되는 부분

- ```js
  for (let i = 0; i < 6; i++) {
      console.log(i) //0, 1, 2, 3, 4, 5
  }
  ```



### for ... in

- 객체(object)와 속성(key)들을 순회할 때 사용

- 배열도 순회 가능하지만 권장하지 않음

- ```js
  //object(객체) => key-value로 이루어진 자료구조
  const capitals = {
      korea: 'seoul',
      france: 'paris',
      USA: 'washington D.C.'
  }
  
  for (let capital in capitals) {
      console.log(capital) //korea, france, USA
  }
  ```



### for ... of

- 반복 가능한(iterable) 객체를 순회하며 값을 꺼낼 때 사용

- ```js
  const fruits = ['딸기', '바나나', '멜론']
  
  for (let fruit of fruits) {
      fruit = fruit + '!'
      console.log(fruit) //딸기!, 바나나!, 멜론!
  }
  ```



## 함수

- 매개변수와 인자의 개수 불일치 허용

  - 매개변수보다 인자의 개수가 많은 경우

    ```js
    const noArgs = function() {
        return 0
    }
    
    noArgs(1, 2, 3) //0
    
    const twoArgs = function(arg1, arg2) {
        return [arg1, arg2]
    }
    
    twoargs(1, 2, 3) //[1, 2]
    ```

  - 매개변수보다 인자의 개수가 적은 경우

    ```js
    const threeArgs = function (arg1, arg2, arg3) {
        return [arg1, arg2, arg3]
    }
    
    threeArgs()		//[undefined, undefined, undefined]
    threeArgs(1)	//[1, undefined, undefined]
    threeArgs(1, 2)	//[1, 2, undefined]
    ```

  

### Rest Parameter

- rest parameter(...)를 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받음

  ```js
  const restOpr = function (arg1, arg2, ...restArgs) {
      return [arg1, arg2, restArgs]
  }
  
  restArgs(1, 2, 3, 4, 5) //[1, 2, [3, 4, 5]]
  restArgs(1, 2) [1, 2, []]
  ```

  

### Spread operator

- spread operator(...)를 사용하면 배열 인자를 전개하여 전달 가능

  ```js
  const spreadOpr = function (arg1, arg2, arg3) {
      return arg1 + arg2 + arg3
  }
  
  const numbers = [1, 2, 3]
  spreadOpr(...numbers) //6
  ```

  

### 함수의 타입

- 함수 선언식과  함수 표현식 모두 타입은 function으로 동일

  ```js
  //함수 표현식
  const add = function (args) {}
  
  //함수 선언식
  function sub(args) {}
  
  console.log(typeof add) //fuction
  console.log(typeof sub) //fuction
  ```

- 함수 선언식은 hoisting 발생

  ```js
  add(2, 7) //9
  
  function add(num1, num2) {
      return num1 + num2
  }
  ```

- 함수 표현식 hoising 불가

  ```js
  sub(7, 2) //Uncaught ReferenceError
  
  const sub = function (num1, num2) {
      return num1 - num2
  }
  ```

  

### Arrow Function(화살표 함수)

- 함수를 비교적 간결하게 정의할 수 있는 문법

- ```js
  const arrow1 = function (name) {
      return `hello, ${name}`
  }
  
  //1. funciton 키워드 삭제
  const arrow2 = (name) => { return `hello, ${name}` }
  
  //2. 매개변수가 1개일 경우에만 () 생략 가능
  const arrow3 = name => { return `hello, ${name}` }
  
  //3. 함수 바디가 return을 포함한 표현식 1개일 경우에 {} & return 삭제 가능
  const arrow4 = name => `hello, ${name}`
  ```



## 문자열



### 문자열 관련 주요 메서드

- **string.includes(value)**

  - 문자열에 value가 존재하는지 판별 후 참 또는 거짓 반환

  - ```js
    const str = 'a santa at nasa'
    
    str.includes('santa')	//true
    str.includes('asan')	//false
    ```

- **string.split(value)**

  - value가 없을 경우, 기존 문자열을 배열에 담아 반환

  - value가 빈 문자열일 경우 각 문자로 나눈 배열을 반환

  - value가 기타 문자열일 경우, 해당 문자열로 나눈 배열을 반환

  - ```js
    const str = 'a cup'
    
    str.split()		//['a cup']
    str.split('')	//['a', '', 'c', 'u', 'p']
    str.split(' ')	//['a', 'cup']
    ```

- **string.replace(from, to)**

  - 문자열에 from 값이 존재할 경우, 1개만 to 값으로 교체하여 반환

- **string.replaceAll(from, to)**

  - 문자열에 from 값이 존재할 경우, 모두 to 값으로 교체하여 반환

```js
const str = 'a b c d'

str.replace(' ', '-')		//a-b c d
str.replaceAll(' ', '-')	//a-b-c-d
```

- **string.trim()**
  - 문자열 시작과 끝의 모든 공백문자를 제거한 문자열 반환
- **string.trimStart()**
  - 문자열 시작의 공백문자를 제거한 문자열 반환
- **string.trimEnd()**
  - 문자열 끝의 공백문자를 제거한 문자열 반환

```js
const str = '	hello	'

str.trim()			//'hello'
str.trimStart()		//'hello	'
str.trimEnd()		//'		hello'
```



## 배열

- 키와 속성들을 담고 있는 참조 타입의 객체

- 순서를 보장하는 특징이 있음

- 주로 대괄호를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능

- 배열의 길이는 array.length 형태로 접근 가능

- ```js
  const numbers = [1, 2, 3, 4, 5]
  
  console.log(numbers[0])			//1
  console.log(numbers[-1])		//undefined
  console.log(numbers.length)		//5
  ```



### 배열 관련 주요 메서드

- **array.reverse()**

  - 원본 배열 요소들의 순서를 반대로 정렬

  - ```js
    const numbers = [1, 2, 3, 4, 5]
    numbers.reverse()
    console.log(numbers)	//[5, 4, 3, 2, 1]
    ```

- **array.push()**

  - 배열의 가장 뒤에 요소 추가

- **array.pop()**

  - 배열의 마지막 요소 제거

```js
const numbers = [1, 2, 3, 4, 5]

numbers.push(100)
console.log(numbers)	//[1, 2, 3, 4, 5, 100]

numbers.pop()
console.log(numbers)	//[1, 2, 3, 4, 5]
```

- **array.unshift()**
  - 배열의 가장 앞에 요소 추가
- **array.shift()**
  - 배열의 첫번째 요소 제거

```js
const numbers = [1, 2, 3, 4, 5]

numbers.unshift(100)
console.log(numbers)	//[100, 1, 2, 3, 4, 5]

numbers.shift()
console.log(numbers)	//[1, 2, 3, 4, 5]
```

- **array.includes(value)**

  - 배열에 특정 값이 존재하는지 판별 후, 참 또는 거짓 반환

  - ```js
    const numbers = [1, 2, 3, 4, 5]
    
    console.log(numbers.includes(1))	//true
    console.log(numbers.includes(100))	//false
    ```

- **array.indexOf(value)**

  - 배열에 특정 값이 존재하는지 확인 후 가장 첫번째로 찾은 요소의 인덱스 반환

  - 만약 해당 값이 없을 경우 -1 반환

  - ```js
    const numbers = [1, 2, 3, 4, 5]
    let result
    
    result = numbers.indexOf(3)		//2
    console.log(result)
    
    result = numbers.indexOf(100)	//-1
    console.log(result)
    ```

- **array.join([separator])**

  - 배열의 모든 요소를 연결하여 반환

  - separator(구분자)는 선택적으로 지정가능하며, 생략 시 쉼표를 기본 값으로 사용

  - ```js
    const numbers = [1, 2, 3, 4, 5]
    let result
    
    result = numbers.join()		//1,2,3,4,5
    console.log(result)			
    
    result = numbers.join('')	//12345
    console.log(result)
    
    result = numbers.join(' ')	//1 2 3 4 5
    console.log(result)
    
    result = numbers.join('-')	//1-2-3-4-5
    console.log(result)
    ```
  
- **spread operator**

  - spread operator(...)를 사용하면 배열 내부에서 배열 전개 가능

  - 얕은 복사에 활용 가능

  - ```js
    const array = [1, 2, 3]
    const newArray = [0, ...array, 4]
    
    console.log(newArray)	//[0, 1, 2, 3, 4]
    ```




### Array Helper Methods

- 배열을 순회하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 callback 함수를 받는 것이 특징



- **array.forEach(callback(element[, index[,array]]))**

  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  - 콜백 함수는 3가지 매개변수로 구성

    - element: 배열의 요소
    - index: 배열 요소의 인덱스
    - array: 배열 자체

  - 반환 값이 없는 메서드

  - ```js
    const fruits = ['딸기', '당근', '수박', '참외', '메론']
    
    fruits.forEach(funcion(fruit) {
       console.log(fruit)
    })
    
    /*딸기
    당근
    수박
    참외
    메론*/
    
    fruits.forEach(function(fruit, i, array) {
        console.log(fruit, i, array)
    })
    
    /*딸기 0 ['딸기', '당근', '수박', '참외', '메론']
    당근 1 ['딸기', '당근', '수박', '참외', '메론']
    수박 2 ['딸기', '당근', '수박', '참외', '메론']
    참외 3 ['딸기', '당근', '수박', '참외', '메론']
    메론 4 ['딸기', '당근', '수박', '참외', '메론']*/
    
    //arrow function
    fruits.forEach(fruit => console.log(fruit))
    
    /*딸기
    당근
    수박
    참외
    메론*/
    ```

- **array.map(callback(element[, index[, array]]))**

  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  - 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환

  - 기존 배열 전체를 다른 형태로 바꿀 때 유용

  - ```js
    const numbers = [1, 2, 3, 4, 5]
    
    const doubleNums = numbers.map((num) => {
        return num *2
    })
    
    consloe.log(doubleNums) //[2, 4, 6, 8, 10]
    ```

- **array.filter(callback(element[, index[, array]]))**

  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  - 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환

  - 기존 배열의 요소들을 필터링할 때 유용

  - ```js
    const numbers = [1, 2, 3, 4, 5]
    
    const oddNums = numbers.filter((num, index) => {
        return num % 2
    })
    
    console.log(oddNums) //[1, 3, 5]
    ```

- **array.reduce(callback(acc, element, [index[, array]])[, initialValue])**

  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  - 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환

  - reduce 메서드의 주요 매개변수

    - acc
      - 이전 callback 함수의 반환 값이 누적되는 변수
    - initialValue(optional)
      - 최초 callback 함수 호출 시 acc에 할당되는 값. default 값은 배열의 첫 번째 값

  - 빈 배열의 경우, initialValue를 제공하지 않으면 에러 발생

  - ```js
    const numbers = [1, 2, 3]
    
    const result = numbers.reduce((acc, num) => {
        return acc + num
    }, 0)
    
    console.log(result) //6
    ```

- **array.find(callback(element[, index[, array]]))**

  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  - 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환

  - 찾는 값이 배열에 없으면 undefined 반환

  - ```js
    const avengers = [
        {name: 'Tony Stark', age: 45},
        {name: 'Steve Rogers', age: 32},
        {name: 'Thor', age: 40}
    ]
    
    const result = avengers.find((avenger) => {
        return avenger name === 'Tony Stark'
    })
    
    console.log(result) //{name: 'Tony Stark', age: 45}
    ```

- **array.some(callback(element[, index[, array]]]))**

  - 배열의 요소 중 하나라도, 주어진 판별 함수를 통과하면 참을 반환

  - 모든 요소가 통과하지 못하면 거짓 반환

  - 빈 배열은 항상 거짓 반환

  - ```js
    const numbers = [1, 3, 5, 7, 9]
    
    const hasEvenNumbers = numbers.some((num) => {
        return num % 2 === 0
    })
    console.log(hasEvenNumbers) //false
    
    const hasOddNumbers = numbers.some((num) => {
        return num % 2
    })
    console.log(hasOddNumbers) //true
    ```

- **array.every(callback(element[, index[, array]]))**

  - 배열의 모든 요소가 주어진 판별 함수를 통과하면 참을 반환

  - 하나의 요소라도 통과하지 못하면 거짓 반환

  - 빈 배열은 항상 참 반환

  - ```js
    const numbers = [2, 4, 6, 8, 10]
    
    const isEveryNumberEven = numbers.every((num) => {
        return num % 2 === 0
    })
    console.log(isEveryNumberEven) //true
    
    const isEveryNumberOdd = numbers.every((num) => {
        return num % 2
    })
    console.log(isEveryNumberOdd) //false
    ```



## 객체(Objects)

- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현

- key는 문자열 타입만 가능

- value는 모든 타입(함수 포함) 가능

- 객체 요소 접근은 점 또는 대괄호로 가능

- ```js
  const me = {
      name: 'Jack',
      phoneNumber: '01012345678',
      'samsung products': {
          buds: 'Galaxy Buds Pro',
          galaxy: 'Galaxy s20',
      },
  }
  
  console.log(me.name)
  console.log(me.phoneNumber)
  console.log(me['samsung products'])
  console.log(me['samsung products'].buds)
  ```

- 메서드는 객체의 속성이 참조하는 함수

- 객체.메서드명()으로 호출 가능

- 메서드 내부에서는 this 키워드가 객체를 의미함

- ```js
  const me = {
      firstName: 'John',
      lastName: 'Doe',
      getFullName: function() {
          return this.firstName + this.lastName
      }
  }
  
  me.getFullName() //John Doe
  ```
