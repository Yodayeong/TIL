#우리편 피카츄
pikka_1_hp = 100
#상대편 피카츄
pikka_2_hp = 100

#이것을 클래스로 정의하면
class pikka:

    def __init__(self):
        self.health = 100
        self.energy = 0

pikka1 = pikka()
pikka2 = pikka()

pikka1.health = pikka1.health - 20

print(pikka1.health, pikka2.health)