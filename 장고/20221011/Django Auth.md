## Django Auth

Django authentication system은 인증(Authentication)과 권한(Authorization) 부여를 함께 제공(처리) 하고 있음

- **Authentication**
  - 신원 확인
  - 사용자가 자신이 누구인지 확인하는 것
- **Authorization**
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정



### User 모델 생성하기

- accounts app 생성 및 등록

- auth의 user 모델을 가져와서 사용하기

  => 클래스 상속

  => Django는 User Model을 제공하지만, 대부분의 개발 환경에서는 기본 User Model을 Custom User Model로 대체함

  ```python
  #pjt/settings.py
  
  #accounts의 User 모델을 AUTH_USER_MODEL로 씀
  AUTH_USER_MODEL = 'accounts.User'
  ```

  ```python
  #accounts/models.py
  #django.contrib.auth의 모델 중, AbstractUser를 그대로 상속
  
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser):
      pass
  ```

- 모델을 새로 만들었으니, db를 지우고 migrate & createsuperuser

  => db에 auth_user가 아니라, accounts_user가 생성됨



### Django shell_plus 실행

```bash
pip install django-extensions
```

```python
#pjt/settings.py

INSTALLED_APPS = [
    'django.contrib.admin', #관리자
    'django.contrib.auth', #유저/인증
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles',
    'accounts',
    #django_extensions 추가
    'django_extensions'
]
```

```bash
pip freeze > requirements.txt
```

```bash
pip install ipython
```

```bash
pip freeze > requirements.txt
```

```bash
python manage.py shell_plus
```

- user 객체 생성하기

```bash
User.objects.create(username='sun', password='12345')
```

=> 비밀번호가 12345 로 저장됨.

=> 암호화가 필요함.

```bash
User.objects.create_user('hong', 'hong@gmail.com', '12345')
```

=> 암호화가 되어서 저장됨.

- user 인증(비밀번호 확인)

```bash
from django.contrib.auth import authenticate
authenticate(username='sun', password='12345')
```

=> 일치하면 뜨고, 아니면 안뜸



### User 모델을 바탕으로 CRUD

- 회원가입 form 생성**(UserCreationForm 활용)**

  ```python
  #accounts/views.py
  
  from django.contrib.auth.forms import UserCreationForm
  
  def index(request):
      form = UserCreationForm()
      context = {
          'form': form
      }
      return render(request, 'accounts/index.html', context)
  ```

  ```html
  <!-- accounts/templates/accounts/index.html -->
  
  {% extends 'base.html' %}
  
  {% load static %}
  
  {% block css %}
  <link rel="stylesheet" href="{% static 'accounts/css/index.css' %}">
  {% endblock css %}
  
  {% block content %}
  
  <h1 class="register-title">회원가입</h1>
  
  <!-- form 태그 -->
  <form class="register-form" action="./index.html" method="POST">
      
      <!-- 넘겨받은 form을 p 형식으로 표현 -->
      {{ form.as_p }}
  
      <div style="height:2rem;"></div>
      <!-- submit 버튼 -->
      <input class="btn btn-outline-dark" type="submit" value="제출">
      <div style="height:1rem;"></div>
      <a class="btn btn-outline-dark" href="{% url 'articles:index' %}">홈으로</a>
  </form>
  
  {% endblock content %}
  ```

  ```python
  #accounts/views.py
  
  from django.shrotcuts import redirect
  
  def index(request):
      #POST 방식이라면,
      if request.method == 'POST':
          form = UserCreationFOrm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      #GET 방식이라면,
      else:
          form = UserCreationForm()
      context = {
          'form': form
      }
      return render(request, 'accounts/index.html', context)
  ```

  => **Manager isn't available; 'auth.User' has been swapped for 'accounts.User'** 오류 발생

  => UserCreationForm은 현재 장고에서 제공하는 User를 쓰고 있어서, **내가 만든 accounts 앱의 모델 User**로 바꾸어줘야 함.

  => Django 내장 회원가입 폼 UserCreationForm을 **상속**받은 CustomUserCreationForm 생성하고 이를 활용

  ```python
  #accounts/forms.py
  
  #django에 내장된 UserCreationForm 과 accounts의 모델에서 정의한 User를 가져옴
  from django.contrib.auth.forms import UserCreationForm
  from .models import User
  
  #CustomUserCreationForm은 UserCreationForm을 상속받음
  class CustomUserCreationForm(UserCreationForm):
      
      class Meta:
          #User의 model을 활용
          model = User
          fields = ['username', 'email', 'password1', 'password2']
  ```

  ```python
  #accounts/views.py
  
  #forms.py에서 직접 정의한 CustomUserCreationForm 가져오기
  from .forms import CustomUserCreationForm
  
  def index(request):
      #POST 방식일 때,
      if request.method == 'POST':
          #form을 CustomUserCreationForm으로 변경
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      #GET 방식일 때,
      else:
          #form을 CustomUserCreationForm으로 변경
          form = CustomUserCreationForm()
      context = {
          'form': form
      }
      return render(request, 'accounts/index.html', context)
  ```



### admin 페이지에서 생성한 User들 보기

```python
#accounts/admin.py

#accounts 앱의 모델에서 User를 가져옴
from .models import User

admin.site.register(User)
```



### 현재 user model로 수정하기

```python
#accounts/admin.py

from django.contrib import admin
#현재 django.contrib.auth의 model을 가져옴
from django.contrib.auth import get_user_model
#django.contrib.auth.admin에서 UserAdmin을 가져옴
from django.contrib.auth.admin import UserAdmin

#get_user_model()호출
admin.site.register(get_user_model(), UserAdmin)
```

```python
#accounts/forms.py

#django에 내장된 UserCreationForm 과 accounts의 모델에서 정의한 User를 가져옴
from django.contrib.auth.forms import UserCreationForm
#from .models import User
from django.contrib.auth.forms import get_user_model

#CustomUserCreationForm은 UserCreationForm을 상속받음
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        #get_user_model 호출
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
```



### User Detail 만들기

```python
#accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup', views.index, name='index'),
    #pk값이 들어오면, 해당 detail 페이지로 연결
    path('<int:pk>/', views.detail, name='detail'),
]
```

```python
#accounts/views.py

from django.contrib.auth import get_user_model

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)
```

```html
<!-- accounts/templates/accounts/detail.html -->

{% extends 'base.html' %}

{% block content %}

<h1>{{ user.username }}님의 프로필</h1>

{% endblock content %}
```

