## URL namespace

1. appname 지정

   ```python
   app_name = 'articles'
   ```

2. url pattern 바꿔주기

   ```python
   {% url 'articles:create' %}
   ```

   

## Django's Design Pattern

- Django는 MVC 패턴을 기반으로 한 MTV 패턴을 사용
  - Model : 데이터 관련
  - Template : 화면 관련
  - View : Model & Template 중간 처리 및 응답 반환



### Model

- CharField(max_length=None, **options)
- TextField(**options)



## Datbase

- PK(Primary Key)
  - 기본 키
  - 각 레코드의 고유한 값(식별자로 사용)