from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('', views.users, name='users'),
]