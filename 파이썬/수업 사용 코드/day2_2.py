dust = int(input())

if (dust >= 0 and dust <= 30):
    print('좋음')
elif (dust > 30 and dust <= 80):
    print('보통')
elif (dust > 80 and dust <= 150):
    print('나쁨')
else:
    print('매우 나쁨')