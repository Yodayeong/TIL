## base.html 생성

- 가장 최상단에 templates/base.html 생성

  ```html
  <!-- templates/base.html -->
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
      <!-- css 들어갈부분 -->
      {% block css %}
      {% endblock css %}
      <title>Document</title>
  </head>
  <body>
      
      <!-- content 들어갈부분 -->
      {% block content %}
      {% endblock content %}
  
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

- 프로젝트의 settings.py에 DIRS 바꿔주기

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          #DIRS를 BASE_DIR/'templates'로 바꿔준다.
          'DIRS': [BASE_DIR / 'templates'],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

- base.html을, 확장하고자 하는 html에 연결해주기

  ```html
  <!-- articles/index.html -->
  
  {% extneds 'base.html' %}
  {% block content %}
  {% endblock content %}
  ```

  