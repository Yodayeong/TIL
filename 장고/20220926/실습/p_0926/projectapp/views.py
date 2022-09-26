from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def isOddEven(request, number):
    if number % 2 == 0:
        type = '짝수'
    if number % 2 == 1:
        type = '홀수'
    if number == '0':
        type = '0'

    return render(request, 'isOddEven.html', {'number': number, 'type': type})

def calculate(request, num1, num2):
    plus = int(num1)+int(num2)
    minus = int(num1)-int(num2)
    times = int(num1)*int(num2)
    divide = int(num1)//int(num2)
    return render(request, 'calculate.html', {'num1': num1, 'num2': num2, 'plus': plus, 'minus': minus, 'times': times, 'divide': divide})

def input(request):
    return render(request, 'input.html' )

def output(request):
    name = request.GET.get('name')
    acts = ['고양이', '돼지', '왕자님', '돌맹이', '공주님', '사자']
    act = random.random(acts)
    print(act)

    return render(request, 'ouput.html', {'name': name, 'past': act})