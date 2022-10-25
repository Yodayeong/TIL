## A one-to-many relationship



### RDB(관계형 데이터베이스) 복습

- 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
- RDB의 모든 테이블에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며, 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만드는 데 사용할 수 있음



### RDB에서의 관계

- **1:1**
  - one-to-one relationships
  - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
- **1:N**
  - one-to-many-relationships
  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
- **M:N**
  - many-to-many relationships
  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
  - 양쪽 모두에서 1:N 관계를 가짐



### Foreign Key

- 외래 키(외부 키)
- 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 키
- 참조되는 테이블의 기본 키(Primary Key)를 가리킴
- 키를 사용하여 부모 테이블의 유일한 값을 참조(참조 무결성)
- 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이어야 함



### 1:N (Article - Comment)

- 모델 관계 설정

  - 게시판의 게시글과 1:N 관계를 나타낼 수 있는 댓글 구현

  - 1:N 관계에서 댓글을 담당할 Article 모델은 1, Comment 모델은 N이 될 것

    - 게시글은 댓글을 0개 이상 가진다.
      - 게시글(1)은 여러 개의 댓글(N)을 가진다.
      - 게시글(1)은 댓글을 가지지 않을 수도 있다.
    - 댓글은 반드시 하나의 게시글에 속한다.

  - comment 테이블의 예시

    - | id   | content | created_at | updated_at | Article의 id |
      | ---- | ------- | ---------- | ---------- | ------------ |
      | 1    | 댓글1   | ...        | ...        | 1            |
      | 2    | 댓글2   | ...        | ...        | 3            |
      | 3    | 댓글3   | ...        | ...        | 3            |

      

### Django Relationship Fields 종류

- **OneToOneField()**
  - A one-to-one relationship
- **ForeignKey()**
  - A one-to-many relationship
- **ManyToManyField()**
  - A many-to-many relationship



### ForeignKey(to, on_delete, **options)

- A one-to-many relationship을 담당하는 Django의 모델 필드 클래스
- Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당
- 2개의 필수 위치 인자가 필요
  - 참조하는 model class
  - on_delete 옵션



### on_delete

- 외래 키가 참조하는 객체가 사라졌을 때, 외래 키가 가진 객체를 어떻게 처리할 지를 정의
- 데이터 무결성을 위해서 매우 중요한 설정
- on_delete 옵션 값
  - CASCADE : 부모 객체(참조된 객체)가 삭제 됐을 때, 이를 참조하는 객체도 삭제
  - PROJECT, SET_NULL, SET_DEFAULT ... 등 여러 옵션 값들이 존재
  - 수업에서는 CASCADE 값만 사용할 예정



### Comment 모델 정의

- 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작성됨
- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)로 작성하는 것을 권장



## 댓글 기능 구현



- comment 모델 정의

  ```python
  #articles/models.py
  
  class Comment(models.Model):
      comment = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
  ```

- 정의한 모델을 migrate 해주기

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- admin 사이트에서 모델들을 볼 수 있도록 하기

  ```python
  #articles/admin.py
  
  from django.contrib import admin
  from .models import Article, Comment
  
  class ArticleAdmin(admin.ModelAdmin):
      list_display = ('title', 'created_at', 'updated_at')
  
  class CommentAdmin(admin.ModelAdmin):
      list_display = ('content', 'created_at', 'article')
  
  # Register your models here.
  admin.site.register(Article, ArticleAdmin)
  admin.site.register(Comment, CommentAdmin)
  ```

- comments 출력 - views.py 수정

  ```python
  #articles/views.py
  
  def comment(request, pk):
      article = Article.objects.get(pk=pk)
      comments = article.comment_set.all()
      context = {
          'comments': comments
      }
      return render(request, 'articles/comment.html', context)
  ```

- comments 출력 - comment.html 생성

  ```html
  <!-- articles/comment.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  
  {% if comments %}
  	{% for comment in comments %}
  		{{ comment.content }} | {{ comment.created_at }}
  	{% endfor %}
  {% else %}
  	<p>no comments</p>
  {% endif %}
  
  {% endblock %}
  ```


- 댓글 작성을 위한 model form 생성

  ```python
  #articles/forms.py
  
  from .models import Comment
  from django import forms
  
  class CommentForm(forms.ModelForm):
      
      class Meta:
          model = Comment
          fields = ['content']
  ```

- 댓글 작성 폼을 comment.html에 넘겨주기

  ```python
  #articles/views.py
  from .forms import CommentForm
  
  def comment(request, pk):
      article = Article.objects.get(pk=pk)
      #CommentForm도 함께 넘겨주기
      comment_form = CommentForm()
      comments = article.comment_set.all()
      context = {
          'comments': comments,
          'comment_form': comment_form
      }
      return render(request, 'articles/comment.html', context)
  ```

  ```html
  <!-- articles/comment.html -->
  
  {% extends 'base.html' %}
  {% load django_bootstrap5 %}
  
  {% block content %}
  
  <!-- django_bootstrap5를 활용해서 댓글 폼 출력 -->
  <p>댓글 작성하기</p>
  <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form comment_form layout='inline' %}
      {% bootstrap_button button_type="submit" content="댓글 작성하기"%}
  </form>
  
  <p style="margin:0; margin-top:1rem;">댓글 목록</p>
  <p style="margin:0;">총 댓글 개수 : {{ comment_num }}</p>
  <hr style="margin:0;">
  {% if comments %}
      {% for comment in comments %}
          {{ comment.content }} | {{ comment.created_at }}
          <br>
      {% endfor %}
  {% else %}
      <p>no comments</p>
  {% endif %}
  
  <a href="{% url 'articles:show' %}">게시판 돌아가기</a>
  
  {% endblock %}
  ```

- 댓글 views.py를 POST 방식일 때도 추가해주기

  ```python
  #articles/views.py
  
  def comment(request, pk):
      article = Article.objects.get(pk=pk)
      #POST 방식일 때,
      if request.method == 'POST':
          comment_form = CommentForm(request.POST)
          if comment_form.is_valid():
              #comment_form에서는 article 값을 입력 받지 않으므로, 이대로 저장하면 오류가 뜬다. 그러므로 commit=False로 바로 저장되는 것을 멈추고, comment에 article을 추가 후, 직접 save 한다.
              comment = comment_form.save(commit=False)
              comment.article = article
              comment.save()
              return redirect('articles:comment', article.pk)
      #GET 방식일 때,
      else:
          comment_form = CommentForm()
      comments = article.comment_set.order_by('-pk')
      comment_num = article.comment_set.count()
      context = {
          'comments': comments,
          'comment_form': comment_form,
          'comment_num': comment_num
      }
      return render(request, 'articles/comment.html', context)
  ```

- 댓글 삭제하기

  ```python
  #articles/urls.py
  
  app_name = 'articles'
  
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('show/', views.show, name='show'),
      path('update/<int:pk>/', views.update, name='update'),
      path('delete/<int:pk>/', views.delete, name='delete'),
      path('comment-page/<int:pk>', views.comment, name='comment'),
      #경로를 넘겨줄 때, article_pk값과 comment_pk값을 모두 넘겨줌
      path('comment-delete/<int:article_pk>/<int:comment_pk>', views.comment_delete, name='comment_delete'),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

  ```python
  #articles/views.py
  
  def comment_delete(request, article_pk, comment_pk):
      article = Article.objects.get(pk=article_pk)
      comment = Comment.objects.get(pk=comment_pk)
      #넘겨받은 comment_pk에 해당하는 댓글을 삭제하고
      comment.delete()
      #article_pk 값의 댓글로 redirect
      return redirect('articles:comment', article.pk)
  ```

  ```html
  <!-- articles/comment.html -->
  
  {% extends 'base.html' %}
  {% load django_bootstrap5 %}
  
  {% block content %}
  
  <p>댓글 작성하기</p>
  <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form comment_form layout='inline' %}
      {% bootstrap_button button_type="submit" content="댓글 작성하기"%}
  </form>
  
  <p style="margin:0; margin-top:1rem;">댓글 목록</p>
  <p style="margin:0;">총 댓글 개수 : {{ comment_num }}</p>
  <hr style="margin:0;">
  {% if comments %}
      {% for comment in comments %}
  		<!-- 삭제하기를 눌렀을때 comment_delete로 넘겨주기. comment의 article_id값과 comment의 id값을 함께 넘겨줌. -->
          {{ comment.content }} | {{ comment.created_at }} | <a href="{% url 'articles:comment_delete' comment.article_id comment.id %}">삭제하기</a>
          <br>
      {% endfor %}
  {% else %}
      <p>no comments</p>
  {% endif %}
  
  <a href="{% url 'articles:show' %}">게시판 돌아가기</a>
  
  {% endblock %}
  ```

  

## 다른 수정 사항들



**user가 작성한 모든 글!**

: user.article_set.all

=> user 프로필에서 user가 작성한 글들을 볼 수 있게

```html
<h3>작성한 글</h3>
<!-- 작성한 글의 개수 -->
<p class="text-muted">{{ user.article_set.count }}개를 작성하였습니다.</p>
<!-- user가 작성한 글들을 돌면서 -->
{% for article in user.article_set.all %}
	<!-- 숫자를 점점 증가하고 -->
	{{ forloop.counter }}
	<!-- article title을 출력하고, 이를 클릭하면 detail로 -->
	<a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a>
{% endfor %}
```



내가 작성한 글만 수정 할 수 있도록! (html/views 모두에서 막아주기)

```html
<!-- html -->

<!-- 요청한 사용자와 글의 작성자가 같다면, -->
{% if request.user == article.user %}
<a href="{% url 'articles:update' article.pk %}">수정하기</a>
{% endif %}
```

```python
#views.py

def update(request, pk):
    article = Article.objects.get(pk=pk)
    #요청한 사용자와 글의 작성자가 같다면,
    if request.user == article.user:
        if request.method == 'POST':
            ...
    #요청한 사용자가 글의 작성자가 아닐때,
    else:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()
```



## 1:N (User - Comment)



- Article모델과 Comment 모델에 작성자를 추가해준다.

  ```python
  class Article(models.Model):
      title = models.CharField(max_length=20)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      image = ProcessedImageField(upload_to='images/', blank=True, processors=[ResizeToFill(400, 300)], format='JPEG', options={'quality': 60})
      #글 작성자를 AUTH_USER_MODEL로 들고옴
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  
  class Comment(models.Model):
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      #댓글 작성자를 AUTH_USER_MODEL로 들고옴
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  ```

- 유저 정보는 어떻게 넣을까?

  ```python
  #articles/views.py
  
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST, request.FILES)
          if form.is_valid():
              #바로 저장되는 것을 막고, article 변수에 담아준 뒤,
              article = form.save(commit=False)
              #유저 정보를 입력받고
              article.user = request.user
              #저장한다.
              article.save()
              messages.success(request, '글 작성이 완료되었습니다.')
              return redirect('articles:index')
      else:
          form = ArticleForm()
      context = {
          'form': form
      }
      return render(request, 'articles/create.html', context)
  
  def comment(request, pk):
      article = Article.objects.get(pk=pk)
      if request.method == 'POST':
          comment_form = CommentForm(request.POST)
          if comment_form.is_valid():
              comment = comment_form.save(commit=False)
              comment.article = article
              #comment의 user도 request를 보낸 user로 저장
              comment.user = request.user
              comment.save()
              return redirect('articles:comment', article.pk)
      else:
          comment_form = CommentForm()
      comments = article.comment_set.order_by('-pk')
      comment_num = article.comment_set.count()
      context = {
          'comments': comments,
          'comment_form': comment_form,
          'comment_num': comment_num
      }
      return render(request, 'articles/comment.html', context)
  ```

- 로그인 한 경우에만, 댓글을 쓸 수 있도록

  ```html
  <!-- articles/comment.html -->
  
  {% extends 'base.html' %}
  {% load django_bootstrap5 %}
  
  {% block content %}
  
  <!-- 로그인을 해야 댓글 창이 보임 -->
  {% if request.user.is_authenticated %}
  <p>댓글 작성하기</p>
  <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form comment_form layout='inline' %}
      {% bootstrap_button button_type="submit" content="댓글 작성하기"%}
  </form>
  {% endif %}
  
  <p style="margin:0; margin-top:1rem;">댓글 목록</p>
  <p style="margin:0;">총 댓글 개수 : {{ comment_num }}</p>
  <hr style="margin:0;">
  {% if comments %}
      {% for comment in comments %}
          {{ comment.content }} | {{ comment.created_at }} | <a href="{% url 'articles:comment_delete' comment.article_id comment.id %}">삭제하기</a>
          <br>
      {% endfor %}
  {% else %}
      <p>no comments</p>
  {% endif %}
  
  <a href="{% url 'articles:show' %}">게시판 돌아가기</a>
  
  {% endblock %}
  ```

  ```python
  #articles/views.py
  
  from django.contrib.auth.decorators import login_required
  
  @login_required
  def comment_create(request, pk):
      ...
  ```



### 퀴즈) user가 작성한 글 중, 첫번째 글의 댓글 중에 첫번째의 user

- user.article_set.all()	#article로 이뤄진 QuerySet => user의 글들
- user.article_set.all()[0]   #article 인스턴스(첫번째 글)
- user.article_set.all()[0].comment_set.all()   #article 인스턴스의 comment로 이뤄진 QuerySet => article 인스턴스(첫번째 글)의 댓글들
- user.article_set.all()[0].comment_set.all()[0] #그 댓글들 중 첫번째
- user.article_set.all()[0].comment_set.all()[0].user #그 첫번째 댓글의 유저
