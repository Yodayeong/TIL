#django에 내장된 UserCreationForm 과 accounts의 모델에서 정의한 User를 가져옴
from django.contrib.auth.forms import UserCreationForm
#from .models import User
from django.contrib.auth.forms import get_user_model

#CustomUserCreationForm은 UserCreationForm을 상속받음
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        #User의 model을 활용
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']