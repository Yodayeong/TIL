from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }

    return render(request, 'todos/index.html', context)

def create(request):
    content = request.GET.get('content__')
    Todo.objects.create(content=content)

    return redirect('todos:index')

def delete(request, pk):
    todos = Todo.objects.get(pk = pk)
    todos.delete()
    return redirect('todo:index')
