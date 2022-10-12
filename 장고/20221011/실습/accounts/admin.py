from django.contrib import admin
#현재 django.contrib.auth의 model을 가져옴
from django.contrib.auth import get_user_model
#django.contrib.auth.admin에서 UserAdmin을 가져옴
from django.contrib.auth.admin import UserAdmin

admin.site.register(get_user_model(), UserAdmin)