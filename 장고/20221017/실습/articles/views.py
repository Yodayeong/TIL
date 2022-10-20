from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'articles/index.html')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }

    return render(request, 'articles/create.html', context)

def show(request):
    forms = Article.objects.all()
    context = {
        'forms': forms
    }
    return render(request, 'articles/show.html', context)