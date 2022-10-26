from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)