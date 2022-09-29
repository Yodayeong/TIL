from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    Post.objects.create(title=title, content=content)

    context = {
        'title': title,
        'content': content
    }

    return redirect('posts:index')

def delete(request, pk):
    Post.objects.get(id=pk).delete()

    return redirect('posts:index')