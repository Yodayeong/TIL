|      | 구문   | 예시                                                         |
| ---- | ------ | ------------------------------------------------------------ |
| C    | INSERT | **INSERT INTO** 테이블이름 (컬럼1, 컬럼2 ..> ) **VALUES** (값1, 값2); |
| R    | SELECT | **SELECT** * **FROM** 테이블이름 **WHERE** 조건;             |
| U    | UPDATE | **UPDATE** 테이블이름 **SET** 컬럼1=값1, 컬럼2=값2 **WHERE** 조건; |
| D    | DELETE | **DELETE FROM** 테이블이름 **WHERE** 조건;                   |



### WHERE

- table users 생성

  ```sql
  CREATE TABLE users(
      first_name TEXT NOT NULL,
      last_name TEXT NOT NULL,
      age INTEGER NOT NULL,
      country TEXT NOT NULL,
      phone TEXT NOT NULL,
      balance INTEGER NOT NULL
  );
  ```

- 데이터 추가

  ```sql
  .mode csv
  ```

- 같은 디렉토리에 있는 users.csv 파일을 users 테이블로

  ```sql
  .import users.csv users
  ```

- users 테이블에서 age가 30 이상인 유저의 모든 컬럼 정보를 조회하려면?

  ```bash
  SELECT (*) FROM users WHERE age >= 30;
  ```

- users 테이블에서 age가 30 이상인 사람들의 이름 3명만

  ```bash
  SELECT first_name FROM users WHERE age >= 30 LIMIT 3;
  ```

- users 테이블에서 age가 30 이상, 성이 '김'인 사람의 나이와 이름만 조회하려면?

  ```bash
  SELECT age, first_name FROM users WHERE age >= 30 AND last_name = '김';
  ```

  

[WHERE절에서 사용할 수 있는 연산자]

- 논리 연산자

  - AND
    - 앞에 있는 조건과 뒤에 오는 조건이 모두 참인 경우
  - OR
    - 앞의 조건이나 뒤의 조건이 참인 경우
  - NOT
    - 뒤에 오는 조건의 결과를 반대로

- 주의!

  ```bash
  --1. 키가 175이거나, 키가 183이면서 몸무게가 80인 사람
  WHERE HEIGHT = 175 OR HEIGHT = 183 AND WEIGHT = 80
  --2. 키가 175 또는 183인 사람 중에서 몸무게가 80인 사람
  WHERE (HEIGHT = 175 OR HEIGHT = 183) AND WEIGHT = 80
  ```

  



### SQLite Aggregate Functions

- Aggregate function (집계 함수)

  - 값 집합에 대해 계산을 수행하고 단일 값을 반환

  - COUNT : 그룹의 항목 수를 가져옴

  - AVG : 모든 값의 평균을 계산

    ```bash
    -- 30세 이상인 사람들의 평균 나이
    SELECT AVG(age) FROM users WHERE age >= 30;
    ```

  - MAX : 그룹에 있는 모든 값의 최대값을 가져옴

    ```bash
    -- 계좌 잔액(balance)이 가장 높은 사람과 그 액수를 조회하려면?
    SELECT first_name, MAX(balance) FROM users;
    ```

  - MIN : 그룹에 있는 모든 값의 최소값을 가져옴

    ```bash
    -- 이씨 중에, 가장 작은 나이를 가진 사람의 이름과 계좌잔고
    SELECT MIN(age), first_name, balance FROM users WHERE last_name = '이';
    ```

  - SUM : 모든 값의 합을 계산



### LIKE

- query data based on pattern matching

- 패턴 일치를 기반으로 데이터를 조회하는 방법

- SQLite는 패턴 구성을 위한 2개의 wildcards 제공

  - % : 0개 이상의 문자

  - _ : 임의의 단일 문자

  - ```bash
    SELECT * FROM 테이블이름 WHERE 컬럼 LIKE '패턴';
    ```

    | 와일드카드패턴 | 의미                                          |
    | :------------- | :-------------------------------------------- |
    | 2%             | 2로 시작하는 값                               |
    | %2             | 2로 끝나는 값                                 |
    | %2%            | 2가 들어가는 값                               |
    | _2%            | 아무 값이 하나 있고 두 번째가 2로 시작하는 값 |
    | 1---           | 1로 시작하고 총 4자리인 값                    |
    | 2_%_% / 2__%   | 2로 시작하고 적어도 3자리인 값                |

  - users 테이블에서 지역 번호가 02인 사람만 조회한다면?

    ```bash
    SELECT * FROM users WHERE phone LIKE '02-%';
    ```

  - users 테이블에서 이름이 '준'으로 끝나는 사람만 조회한다면?

    ```bash
    SELECT * FROM users WHERE first_name LIKE '%준';
    ```

  - users 테이블에서 중간 번호가 5114인 사람만 조회한다면?

    ```bash
    SELECT * FROM users WHERE phone LIKE '%-5114-%';
    ```



### ORDER BY

- sort a result set of a query

- 조회 결과 집합을 정렬

- SELECT 문에 추가하여 사용

- 정렬 순서를 위한 2개의 keyword 제공

  - ASC - 오름차순 (default)

  - DESC - 내림차순

  - ```bash
    SELECT * FROM 테이블이름 ORDER BY 컬럼 ASC;
    SELECT * FROM 테이블이름 ORDER BY 컬럼 DESC;
    ```

  - users에서 나이 순으로 오름차순 정렬하여 상위 10개만 조회한다면?

    ```bash
    SELECT * FROM users ORDER BY age ASC LIMIT 10;
    ```

  - 나이 순, 성 순으로 오름차순 정렬하여 상위 10개만 조회한다면?

    ```bash
    SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
    ```

  - 계좌 잔액 순으로 내림차순 정렬하여 해당 유저의 성과 이름을 10개만 조회한다면?

    ```bash
    SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
    ```

  - 계좌 잔액 순으로 내림차순, 성 오름차순

    ```bash
    SELECT last_name, first_name, balance FROM users ORDER BY balance DESC, last_name ASC LIMIT 10;
    ```

    