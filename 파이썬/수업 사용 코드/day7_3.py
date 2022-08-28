#Class는 Person
#instance는 사례 - ex)홍길동

class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        return(self.name, self.age, self.gender)

hong = Person('홍길동', 100, 'M')
ko = Person('고길동', 40, 'M')

print(hong.info())
print(hong.name)
print(hong.age)
print(type(hong))