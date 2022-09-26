from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    return render(request, 'pong.html', {'name': request.GET.get('ball')})