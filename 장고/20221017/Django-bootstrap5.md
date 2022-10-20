## Django-bootstrap5



- bootstrap 설치

  ```bash
  pip install django-bootstrap5
  pip freeze > requirements.txt
  ```
  
- INSTALLED_APPS 에 등록

  ```python
  'django_bootstrap5'
  ```

- bootstrap을 적용하는 html에 load 해주기

  ```html
  {% extends 'base.html' %}
  
  <!-- load bootstrap -->
  {% load django_bootstrap5 %}
  
  {% block content %}
  
  <form action="" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
  
      {{ form.as_p }}
      <input type="submit" value="제출하기">
  
  </form>
  
  {% endblock %}
  ```

- bootstrap_form 적용해주기

  ```html
  {% extends 'base.html' %}
  
  <!-- load bootstrap -->
  {% load django_bootstrap5 %}
  
  {% block content %}
  
  <form action="" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
  
      <!-- bootstrap_form -->
      {% bootstrap_form form %}
      <!-- bootstrap_button -->
      {% bootstrap_button button_type="submit" content="제출하기" %}
  
  </form>
  
  {% endblock %}
  ```

- **django modelform custom**을 통해서 이쁘게 꾸밀 수도 있음!
