from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.order_by('priority')
    return render(request, 'todo/index.html', {'todos': todos})

def create(request):
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')

    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    return redirect('todo:index')

def delete(request, id):
    todo = Todo.objects.get(pk=id)
    todo.delete()

    return redirect('todo:index')

def update(request, id):
    todo = Todo.objects.get(pk=id)
    
    if todo.completed == False:
        todo.completed = True
    else:
        todo.completed = False

    todo.save()

    return redirect('todo:index')