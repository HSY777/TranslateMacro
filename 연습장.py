class Character:
    def __init__(self):
        self.life = 1000
    
    def attacked(self):
        self.life -= 10
        print('공격받음! 생명력 = ', self.life)

class Warrior(Character):
    def __init__(self):
        super(Warrior, self).__init__() # 부모클래스의 초기화 생성자 호출
        self.strength = 15              # 생성한 자식 클래스에 __init__초기화 생성자가 없으면 super()를 하지 않아도 알아서 부모클래스의 초기화 생성자를 호출해줌
        self.intelligence = 5
        
    def asdf(self):
        print('asdf')

class Wizard(Character):
    def __init__(self):
        super(Wizard, self).__init__()
        self.strength = 5
        self.intelligence = 15
    
a = Warrior()
print(a.life)