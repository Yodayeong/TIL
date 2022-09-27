from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'practices/index.html')

def ping(request):
    return render(request, 'practices/ping.html')

def pong(request):
    return render(request, 'practices/pong.html', {'name': request.GET.get('ball')})