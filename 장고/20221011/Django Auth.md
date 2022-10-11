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



### User 모델을 바탕으로 CRUD













### 커스텀 모델 사용하기

- User 모델 설정

  ```python
  #pjt/settings.py
  
  #User Model
  AUTH_USER_MODEL = 'accounts.Uer'
  ```

- AbstractUser를 상속받는 커스텀 User 클래스 작성 (상속)

  ```python
  #accounts/models.py
  
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser):
      pass
  ```

- migrate 해주기

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- superuser 만들기

  ```bash
  python manage.py createsuperuser
  ```



### User 객체 활용

- User 생성

  ```python
  user = User.objects.create_user('john', 'john@google.com', '1q2w3e4r!')
  ```

- User 비밀번호 변경

  ```python
  user = User.objects.get(pk=2)
  User.set_password('new password')
  User.save()
  ```

- User 인증(비밀번호 확인)

  ```python
  from django.contrib.auth import authenticate
  user = authenticate(username='john', password='secret')
  ```



### signup

```python
#accounts/urls.py

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

```python
#accounts/views.py

from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

```html
<!--templtes/accounts/signup.html-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>회원가입</h1>
    {{ form.as_p }}
</body>
</html>
```

- 직접 생성한 모델로 변경

```python
#accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    #POST 요청 처리
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

```python
#accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm:

    class Meta:
        model = User
        fields = '__all__'
```

```python
#accounts/views.py

from .forms import CustomUserCreationForm

def signup(request):
    #POST 요청 처리
    if request.method == 'POST':
        #CustonUserCreationForm으로 변경
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        #CustonUserCreationForm으로 변경
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

