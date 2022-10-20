from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)

def show(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }

    return render(request, 'articles/show.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, '글 수정이 완료되었습니다.')
            return redirect('articles:show')
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)