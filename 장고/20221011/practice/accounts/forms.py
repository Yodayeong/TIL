from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm:

    class Meta:
        model = User
        fields = '__all__'