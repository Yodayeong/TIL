from socket import fromshare
from django import forms
from .models import Articles

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = '__all__'