## Variable Routing

- URL 주소를 변수로 사용하는 것을 의미
- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
- 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음



## Sending and Retrieving from data

- 데이터를 보내고 가져오기



### Client

- HTML <form> element

  - 데이터가 전송되는 방법을 정의
  - 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit ...)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당
  - "데이터를 어디(action)로 어떤 방식(method)으로 보낼지"

- **action**

  - 입력 데이터가 전송될 URL 지정
  - 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL 이어야 함
  - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐

- **method**

  - 데이터를 어떻게 보낼 것인지 정의
  - 입력 데이터의 HTTP request methods를 지정
  - HTML form 데이터는 GET 방식과 POST 방식으로만 전송 가능

- fake 네이버 앱

  - https://search.naver.com/search.naver?

    => form의 action에 정의한 내용

  - query=아이유

    => input으로 정의한 데이터



## 템플릿 상속

1. base라는 이름의 skeleton 템플릿 작성

   ```html
   <!--base.html-->
   
   <!--body-->
   {% block content %}
   {% endblock content %}
   ```

2. 상속받을 템플릿에 적용

   ```html
   <!--index.html-->
   {% extends 'base.html' %}
   
   {% block content %}
   내용
   {% endblock %}
   ```

   