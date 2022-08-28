class Person:
    pass

#Person 클래스의 인스턴스 iu
iu = Person()
#iu의 인스턴스 변수 할당
iu.name = '아이유'
iu.age = 28
iu.gender = 'F'
#인스턴스 변수 접근
print(iu)
print(iu.name)


#처음 만들 때 부터 모든 것을 해주자!
#=> 생성자!

class Person:

    #생성자! 인스턴스가 생성될 때 어떠한 작업!
    def __init__(self, name):
        print('응애!')
        #그 인스턴스의 이름을 name으로 해주세요.
        self.name = name

#Person 클래스의 인스턴스인 iu를 생성
iu = Person('아이유')
print(iu.name)
jimin = Person('지민')
print(jimin.name)