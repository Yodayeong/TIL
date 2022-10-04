from django import forms
from .models import Article

#Article에 있는 필드들을 고대로 form으로 가져오기
class ArticleForm(forms.ModelForm):
    class Meta:
        #model은 Article의 것을 가져오고
        model = Article
        #모든 필드를 가져온다.
        fields = '__all__'