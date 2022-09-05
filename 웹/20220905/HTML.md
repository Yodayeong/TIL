## HTML



### HTML 문서 구조화

- table의 각 영역을 명시하기 위해 <thead>, <tbody>, <tfoot> 요소를 활용
- <tr>으로 가로 줄을 구성하고 내부에는 <th> 혹은 <td>로 셀을 구성
- colspan, rowspan 속성을 활용하여 셀 병합
- <caption>을 통해 표 설명 또는 제목을 나타냄
- table 태그 기본 구성
  - thead
    - tr > th
  - tbody
    - tr > td
  - tfoot
    - tr > td
  - caption



### form

- `<form>`은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그

- `<form>` 기본 속성
  - action : form을 처리할 서버의 URL(데이터를 보낼 곳)
  - method : form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
  - enctype : method가 post인 경우 데이터의 유형

- ex)

  ```html
  <form action="">
      username: <input type="text" name="username" disabled>
      <input type="submit" value="얍">
  </form>
  ```

  

### input label

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음

- <input>에 id 속성을, <label>에는 for 속성을 활용하여 상호 연관 시킴

- ```html
  <label for="agreement">개인정보 수집에 동의합니다.</label>
  <input type="checkbox" name="agreement" id="agreement">
  ```

- input유형 - 일반

  - text: 일반 텍스트 입력
  - password: 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
  - email: 이메일 형식이 아닌 경우 form 제출 불가
  - number: min, max, step 속성을 활용하여 숫자 범위 설정 가능
  - file: accept 속성을 활용하여 파일 타입 지정 가능

- input유형 - 항목 중 선택

  - 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value 지정
  - checkbox: 다중 선택
  - radio: 단일 선택



## Bootstrap



**spacing**

- m: margin

- p: madding

  - t: top
  - b: bottom
  - x: set both left and right
  - y: set both top and bottom

- ```html
  <p class="mt-3 mx-3">lorem</p>
  ```



### CDN

: Content Delivery(Distribution) Network

- 컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템