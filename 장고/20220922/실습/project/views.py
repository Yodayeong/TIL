from django.shortcuts import render
import random

# Create your views here.
def dinner(request):
    menu = ['삼겹살', '떡볶이', '돈까스']
    menu_img = [
    'https://cdn.mindgil.com/news/photo/202103/70839_7148_1250.jpg',
    'https://doewxs707ovkc.cloudfront.net/v3/prod/image/item/mainpage/907/ad4474bef39c4167b84477eaa7a5052f20210708171733.',
    'http://image.g9.co.kr/g/1832366398/n?ts=1634380390000',
    ]

    num = random.randrange(0,3)

    return render(request, 'dinner.html', {'menu':menu[num], 'menu_img':menu_img[num]})

def lotto(request):

    lotto = [3, 11, 15, 29, 35, 44]
    #nums
    nums = [[random.randrange(1,46) for i in range(5)] for j in range(5)]

    idx = 0
    for num in nums:
        cnt = 0

        for i in range(5):
            if num[i] == lotto[i]:
                cnt += 1
        
        if cnt < 1:
            nums[idx].append('꽝')
        if 1 <= cnt and cnt < 2:
            nums[idx].append('5등')
        if 2 <= cnt and cnt < 3:
            nums[idx].append('4등')
        if 3 <= cnt and cnt < 4:
            nums[idx].append('3등')
        if 4 <= cnt and cnt < 5:
            nums[idx].append('2등')
        if cnt == 5:
            nums[idx].append('1등')
        
        idx += 1

    return render(request, 'lotto.html', {'nums': nums})