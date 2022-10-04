from django.shortcuts import render, redirect

import articles
from .models import Articles
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Articles.objects.order_by('-pk')
    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)

def new(request):
    article_form  = ArticleForm()
    context = {
        'article_form': article_form
    }

    return render(request, 'articles/new.html', context=context)

def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Articles.objects.create(title=title, content=content)

    article_form = ArticleForm(request.POST)
    if article_form.is_valid():
        article_form.save()
        return redirect('articles:index')
    else:
        context = {
            'article_form': article_form
        }
    return render(request, 'articles/new.html', context=context)

def detail(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'article': article
    }

    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Articles.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)