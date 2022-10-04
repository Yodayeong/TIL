from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)

def new(request):
    #ArticleForm의 모델을 article_form 변수에 담아줌
    article_form = ArticleForm()
    context = {
        'article_form': article_form
    }

    return render(request, 'articles/new.html', context)

def create(request):
    #ArticleForm형식에 POST 형식으로 받은 요청을 넣어준 것을, 
    #articles 변수에 담아줌
    articles = ArticleForm(request.POST)

    #만약 articles가 유효하다면,
    if articles.is_valid():
        articles.save()
        return redirect('articles:index')
    #만약 articles가 유효하지 않다면,
    else:
        context = {
            'article_form': articles
        }
        return render(request, 'articles/new.html', context=context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }

    return render(request, 'articles/detail.html', context)

#update함수는 두가지를 생각해야 한다.
#1. detail page에서 update 함수로 넘어오는 경우 => method가 GET 방식
#2. update page에서 update 함수로 넘어오는 경우 => method가 POST 방식
def update(request, pk):
    #일단 pk 값에 해당하는 객체를 article에 저장
    article = Article.objects.get(pk=pk)

    #만약 POST 방식으로 값이 들어왔다면,
    if request.method == 'POST':
        #article인 객체의 ArticleForm을,
        #POST로 들어온 요청을 담아서,
        #article_form 변수에 담아준다.
        article_form = ArticleForm(request.POST, instance=article)
        #그리고 article_form의 유효성 검사를 해준다.
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')

    #만약 GET 방식으로 값이 들어왔다면,
    else:
        #현재 pk 값에 해당하는 글(위에서 정의한 article)을 불러와야한다.
        article_form = ArticleForm(instance=article)
        context = {
            'article_form': article_form
        }
        return render(request, 'articles/update.html', context=context)
