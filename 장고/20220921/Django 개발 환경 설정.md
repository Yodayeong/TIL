## Django 개발 환경 설정



### Web Framework

- 웹을 만드는 작업 중에 많은 부분이 공통적이다.

- 어떤 사이트들을 만들더라도 똑같은 작업이다.

- 이런 부분들을 미리 해둔 소프트웨어를 Web Framework라고 함.

- 공통적인 작업은 Web Framework에게 맡기고, 우리는 우리 웹만의 개성을 살리자.

  

### MTV 패턴

: Model + Template + View



### 가상 환경 설정

1. 가상 환경 만들기

   ```
   python -m venv myvenv
   ```

2. 가상 환경 실행

   ```
   source myvenv/Scripts/activate
   ```



### 장고 설치하기

1. 장고 설치하기

   ```
   pip install django
   ```

2. 장고 프로젝트 생성 및 해당 프로젝트로 이동

   ```
   #django-admin startproject <프로젝트명>
   #cd <프로젝트명>
   
   django-admin startproject blogproject
   cd blogproject
   ```



## MDN 문서



### 인터넷은 어떻게 동작하는가?

컴퓨터에 메세지를 보내려면 메세지를 받을 특정 컴퓨터를 지정해야 함.

=> **모든 컴퓨터에는 IP주소라는 고유한 주소가 있음** ex) 192.168.2.10

그러나, 사람들은 이러한 IP주소를 기억하기 어려움.

=> **'도메인 이름'이라고 하는, 사람이 읽을 수 있는 IP주소의 이름을 지정** ex) google.com



### 클라이언트와 서버는 무엇일까?

웹에 연결된 컴퓨터는 클라이언트와 서버라고 함.

- 클라이언트
  - 일반적인 웹 사용자의 인터넷이 연결된 장치들과(폰, 컴퓨터 ..), 이런 장치들에서 이용가능한 웹에 접근하는 소프트웨어(파이어폭스, 크롬 ..)
- 서버
  - 웹페이지, 사이트, 또는 앱을 저장하는 컴퓨터
  - 클라이언트의 장비가 웹페이지에 접근하길 원할 때, 서버로부터 클라이언트의 장치로, 사용자의 웹 브라우저에서 보여지기 위한 웹페이지의 사본이 다운로드 됨.



### 정적 웹사이트와 동적 웹사이트

- 정적 웹사이트
  - 사용자가 페이지를 탐색하거나, 브라우저가 지정된 URL에 HTTP "GET" 요청을 보낼 때, 서버는 파일 시스템에서 요청한 문서를 검색하고 문서와 success status를 포함한 HTTP 응답을 반환.
- 동적 웹사이트
  - 동적 웹사이트는 필요할 때, 동적으로 응답 콘텐츠가 생성됨.
  - 동적 웹사이트의 웹 페이지는 보통 HTML 템플릿에 있는 자리 표시자에 데이터베이스에서 가져온 데이터를 넣어 생성됨.
  - 동적 웹사이트는 사용자 또는 저장된 환경을 기반으로 URL에 대해 다른 데이터를 반환 할 수 있으며, 응답을 반환하는 과정에서 다른 작업을 수행 할 수 있음.

