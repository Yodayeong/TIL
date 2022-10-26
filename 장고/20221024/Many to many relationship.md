## Many to many relationship



- 병원 예약 시스템 구축을 위한 데이터 베이스 모델링을 진행한다면?

  <hospitals_doctor>

  | id   | name  |
  | ---- | ----- |
  | 1    | alice |
  | 2    | bella |

  <hospitals_patient>

  | id   | name  | doctor_id |
  | ---- | ----- | --------- |
  | 1    | carol | 1         |
  | 2    | dane  | 2         |
  | 3    | carol | 2         |

  => 1번 환자 carol이 두 의사 모두에게 방문하려 함

  => **예약 테이블을 따로 하나 둠**

  <hospitals_patient>

  | id   | name  |
  | ---- | ----- |
  | 1    | carol |

  <hospitals_doctor>

  | id   | name   |
  | ---- | ------ |
  | 1    | 김철수 |
  | 2    | 이영희 |

  <reservation_table>

  | id   | patient_id | doctor_id |
  | ---- | ---------- | --------- |
  | 1    | 1          | 1         |
  | 2    | 1          | 2         |

  

- 글의 **좋아요 기능**도 마찬가지로 구현

  <Article_table>

  | id   | title  |
  | ---- | ------ |
  | 1    | 1번 글 |
  | 2    | 2번 글 |

  <User_table>

  | id   | name |
  | ---- | ---- |
  | 1    | tak  |

  <Like_table>

  | id   | article_id | user_id |
  | ---- | ---------- | ------- |
  | 1    | 1          | 1       |
  | 2    | 2          | 1       |

  

### 중개 모델

- 환자 모델의 외래 키를 삭제하고, 별도의 예약 모델을 새로 작성
- 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐

- (1) 의사와 환자 생성 후 예약 만들기

  ```python
  doctor1 = Doctor.objects.create(name='alice')
  patient1 = Patient.objects.create(name='carol')
  
  Reservation.objects.create(doctor=doctor1, patient=patient1)
  ```

- (2) 예약 정보 조회

  ```python
  #의사1 => 예약 정보 찾기
  doctor1.reservation_set.all()
  
  #환자1 => 예약 정보 찾기
  patient1.reservation_set.all()
  ```

- (3) 1번 의사에게 새로운 환자 예약이 생성 된다면,

  ```python
  patient2 = Patient.objects.create(name='dane')
  
  Reservation.objects.create(doctor=doctor1, patient=patient2)
  ```

- (4) 1번 의사의 예약 정보 조회

  ```python
  doctor1.reservation_set.all()
  ```

  

### Django ManyToManyField

- (1) 환자 모델에 Django ManyToManyField 작성

  ```python
  class Patient(models.Model):
      doctors = models.ManyToManyField(Doctor)
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
  ```

  => **생성된 중개 테이블 hospitals_patient_doctors** (id, patient_id, doctor_id)를 확인 가능

- 중개 테이블을 직접 작성하는 것과의 차이점

  ```python
  class Patient(models.Model):
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
      
  #중개 모델 작성
  class Reservation(models.Model):
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  ```

  => patient1의 예약들을 보려면 : **patient1.reservation_set.all()**

  ```python
  #ManyToManyField 활용
  class Patient(models.Model):
      doctors = models.ManyToManyField(Doctor)
      name = TextField()
      
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
  ```

  => patient이 만난 의사들을 보려면 : **patient1.doctors.all()**

- (2) 예약 생성(환자가 의사에게 예약)

  ```python
  #patient1이 doctor1에게 예약
  patient1.doctors.add(doctor1)
  
  #patient1 - 자신이 예약한 의사목록 확인
  patient1.doctors.all()
  <QuerySet [<Doctor: 1번 의사 alice>]>
  
  #doctor1 - 자신이 예약된 환자목록 확인
  doctor1.patient_set.all()
  <QuerySet [<Patient: 1번 환자 carol>]>
  ```

- (3) 예약 생성(의사가 환자를 예약)

  ```python
  #doctor1이 patient2를 예약
  doctor1.patient_set.add(patient2)
  
  #doctor1 - 자신의 예약 환자목록 확인
  doctor1.patient_set.all()
  <QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 dane>]>
  
  #patient1, 2 - 자신이 예약한 의사목록 확인
  patient1.doctors.all()
  <QuerySet [<Doctor: 1번 의사 alice>]>
  
  patient2.doctors.all()
  <QuerySet [<Doctor: 1번 의사 alice>]>
  ```

- (4) 예약 현황 확인

  | id   | patient_id | doctor_id |
  | ---- | ---------- | --------- |
  | 1    | 1          | 1         |
  | 2    | 2          | 1         |

- (5) 예약 취소하기(삭제)

  - 기존에는 해당하는 Reservation을 찾아서 지워야 했다면, 이제는 .remove()를 사용

  ```python
  #doctor1이 patient1 진료 예약 취소
  doctor1.patient_set.remove(patient1)
  
  doctor1.patient_set.all()
  <QuerySet [<Patient: 2번 환자 harry>]>
  
  patient1.doctors.all()
  <QuerySet []>
  
  #patient2가 doctor1 진료 예약 취소
  patient2.doctors.remove(doctor1)
  
  patient2.doctors.all()
  <QuerySet []>
  
  doctor1.patient_set.all()
  <QuerySet []>
  ```

- Django는 **ManyToManyField를 통해 중개 테이블을 자동으로 생성**함

- 그렇다면, **중개 모델**을 쓰는 경우는 언제일까?

  => 예약시간, 상담내용 등 다른 필드들을 덧붙일 때 중개 모델 설계

  => 중개 테이블을 수동으로 지정하려는 경우, **through 옵션**을 사용하여, 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음

  ```python
  class Patient(models.Model):
      doctors = models.ManyToManyField(Doctor, through='Reservation')
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
      
  class Reservation(models.Model):
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
      symptom = models.TextField()
      reserved_at = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
          return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
  ```

  => patient1이 예약들을 찾을 때 : **patient1.reservation_set.all()**

  => patient1이 의사들을 찾을 때 : **patient1.doctors.all()**

- **related_name** argmuent

  - target model이 source model을 참조할 때 사용할 manager name
  - ForeignKey()의 releated_name과 동일

  ```python
  class Patient(models.Model):
      #ManyToManyField의 related_name 작성
      doctors = ManyToManyField(Doctor, related_name='patients')
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
  ```

  