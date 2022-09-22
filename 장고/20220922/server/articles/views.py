from django.shortcuts import render
import random

# Create your views here.
def index(request):
    #환영하는 메인 페이지를 보여주자.

    names = ['주세환', '오진수', '임수경', '조병진', '차화영', '최근영', '김선교']

    name = random.choice(names)

    context = {
        'name': name,
        'img': 'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
    }
    return render(request, 'index.html', context)

def welcome(request, name):
    #사람들이 /welcome/본인이름 을 입력하면, 환영인사와 이름을 동시에 보여준다.
    context = {
        'name': name,
        'greetings': [
            '안녕하세요',
            'hello',
        ],
        'images': [
            'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
            'https://cdn.crowdpic.net/detail-thumb/thumb_d_9084D59564B7C339AB08A854E7EF6C18.jpg',
        ]
    }
    print(name)

    return render(request, 'welcome.html', context)