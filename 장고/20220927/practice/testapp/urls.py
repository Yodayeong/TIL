from django.urls import path
from . import views

app_name = 'testapp'

urlpatterns = [
    path('index/', views.index, name="index"),
    path('ping/', views.ping, name="ping"),
    path('pong/', views.pong, name="pong"),
]