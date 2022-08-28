#함수 내부에서 값을 쓰고 싶으면 어떻게 해야하죠?
#정의할 때 이름을 지어놓고, 호출할 때 값을 넘겨줘요!

class MyClass:
    class_variable = '클래스 변수'

    #메서드들을 정의
    def __init__(self):
        self.instance_variable = '인스턴스 변수'
    #인스턴스 메서드 정의
    def instance_method(self):
        return self, self.instance_variable
    #클래스 메서드 정의
    @classmethod
    def class_method(cls):
        return cls, cls.class_variable
    #스태틱 메서드 정의
    @staticmethod
    def static_method():
        return '스태틱'

c1 = MyClass()
print('인스턴스 변수 호출', c1.instance_variable)
print('인스턴스 메서드 호출', c1.instance_method()) #(<__main__.MyClass object at 0x00000174A67BFAC0>, '인스턴스 변수'): 인스턴스 그자체
print('클래스 메서드 호출', c1.class_method()) #(<class '__main__.MyClass'>, '클래스 변수'): 클래스 그자체
print('스태틱 메서드 호출', c1.static_method()) #스태틱 메서드 호출 스태틱 : 스태틱 메서드에서는 클래스나 인스턴스를 넘겨주지 않음
                                                #그래서 스태틱 메서드 안에서는 클래스나 인스턴스를 쓸 수 없음