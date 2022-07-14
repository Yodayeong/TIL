#소리 파일 저장용량 계산하기

#h, b, c, s 가 공백을 두고 입력된다.
#h는 48,000이하, b는 32이하(단, 8의배수), c는 5이하, s는 6,000이하의 자연수이다.

#필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
#단, 소수점 첫째 자리까지의 정확도로 출력하고 MB를 공백을 두고 출력한다.

#h: 1초 동안 마이크로 소리강약을 체크하는 횟수
#b: 한 번 체크한 값을 저장할 때 사용하는 비트수
#c: 좌우 등 소리를 저장할 트랙 개수인 채널 개수
#s: 녹음할 시간(초)

#44100*16*2*1/8/1024/1024 

h, b, c, s = map(int, input().split())

mb = float(h * b * c * s / 8 / 1024 / 1024)

print('%.1f' %mb, 'MB')