## QuerySet API



- gt (= greater than)

  ```bash
  Entry.objects.filter(id__gt=4)
  
  (==)
  SELECT ... WHERE id > 4;
  ```

- gte (= greater than equal)

  ```bash
  Entry.objects.filter(id__gte=4)
  
  (==)
  SELECT ... WHERE id >= 4;
  ```

- lt (= less than), lte (= less than equal)

  ```bash
  Entry.objects.filter(id__lt=4)
  Entry.objects.filter(id__lte=4)
  
  (==)
  SELECT ... WHERE id < 4;
  SELECT ... WHERE id <= 4;
  ```

- in

  ```bash
  Entry.objects.filter(id__in=[1, 3, 4])
  Entry.objects.filter(headline__in='abc')
  
  (==)
  SELECT ... WHERE id IN (1, 3, 4);
  SELECT ... WHERE headline IN ('a', 'b', 'c');
  ```

- startswith

  ```bash
  Entry.objects.filter(headline__startswith='Lennon')
  
  (==)
  SELECT ... WHERE headline LIKE 'Lennon%';
  ```

- istartswith (=insensitive startswith / 대소문자 구분 X) 

  ```bash
  Entry.objects.filter(headline__istartswith='Lennon')
  
  SELECT ... WHERE headline ILIKE 'Lennon%';
  ```

- contains

  ```bash
  Entry.objects.filter(headline__contains='Lennon')
  Entry.objects.filter(headline__icontains='Lennon')
  
  (==)
  SELECT ... WHERE headline LIKE '%Lennon%';
  SELECT ... WHERE headline ILIKE '%Lennon%';
  ```

- range

  ```bash
  import datetime
  start_date = datetime.date(2005, 1, 1)
  end_date = datetime.date(2005, 3, 31)
  Entry.objects.filter(pub_date__range=(start_date, end_date))
  
  (==)
  SELECT ... WHERE pub_date
  BETWEEN '2005-01-01' and '2005-03-31'
  ```

- 복합 활용

  ```bash
  inner_qs = Blog.objects.filter(name__contains='Cheddar')
  entries = Entry.objects.filter(blog__in=inner_qs)
  
  (==)
  SELECT ...
  WHERE blog.id IN (SELECT id FROM ... WHERE NAME 
  LIKE '%Cheddar%');
  ```

- 활용

  ```bash
  Entry.objects.all()[0]
  
  (==)
  SELECT ...
  LIMIT 1;
  ```

- 활용

  ```bash
  Entry.objects.order_by('id')
  
  (==)
  SELECT ...
  ORDER BY id;
  
  ======
  Entry.objects.order_by('-id')
  
  (==)
  SELECT ...
  ORDER BY id DESC;
  ```

  

### 실행

```bash
. venv/Scripts/activate

python manage.py shell_plus

#장르의 모든 값을 출력
Genre.objects.all()
#<QuerySet> : 개별 오브젝트의 모음
Genre.objects.all().query
print(Genre.objects.all().query)
```



## ORM 확장1

- 모델링 (ORM)

  ```bash
  class Genre(models.Model):
  	name = models.CharField(max_length=30)
  
  class Artist(models.Model):
  	name = models.CharField(max_length=30)
  	debut = models.DateField()
  
  class Album(models.Model):
  	name = models.CharField(max_length=30)
  	genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
  	artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
  ```

- models.ForeignKey 필드

  - 2개의 필수 위치 인자
    - Model class : 참조하는 모델
    - on_delete : 외래 키가 참조하는 객체가 삭제되었을 때 처리방식
      - CASCADE : 부모 객체가 삭제됐을 때 이를 참조하는 객체도 삭제
      - PROTECT : 삭제되지 않음
      - SET_NULL : NULL 설정
      - SET_DEFAULT : 기본 값 설정

- Foreign Key (외래키)

  - 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성)
    - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
  - 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함

- db 생성

  ```bash
  python manage.py shell_plus
  
  Genre.objects.create(name='발라드')
  
  artist = Artist()
  artist.name = '아이유'
  artist.debut = '2019-12-26'
  artist.save()
  
  #------
  album = Album()
  album.name = '꽃'
  genre = Genre.objects.get(id=1)
  album.genre = genre
  album.artist = Artist.objects.get(id=1)
  album.save()
  
  #------
  #or
  album = Album()
  album.genre_id = 1
  album.artist_id = 1
  album.name = '미아'
  album.save()
  
  #------
  #앨범의 id가 1인 것의
  album = Album.objects.get(id=1)
  #장르의 이름은?
  album.genre.name
  
  #------
  #id가 1인 장르의 모든 앨범은?
  g1 = Genre.objects.get(id=1)
  g1.album_set.all()
  ```