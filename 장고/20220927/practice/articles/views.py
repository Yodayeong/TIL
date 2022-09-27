from django.shortcuts import render
from testpjt.settings import BASE_DIR
from .models import Article

guestbook = []

# Create your views here.
def index(request):
    guestbook = Article.objects.all()
    return render(request, 'index.html', {'guestbook': guestbook})

def create(request):
    content = request.GET.get('content')
    Article.objects.create(content=content)
    return render(request, 'create.html', {'content': content})