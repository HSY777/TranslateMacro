class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print('안녕 나는' + to_name + '나는' + self.name)
    def introduce(self):
        print('내이름은' + self.name + '나는' + self.name)

class Police(Person):
    def arrest(self, to_arrest):
        print('넌 체포됬다, ', + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print('다음엔 뭘 만들지? 아 이걸' + to_program)

wonie = Person('워니' 20)
jenny = Police('제니', 21)
michael = Programmer('마이클', 22)



'''wonie = Person('워니', 20)
micheal = Person('마이클', 30)
jenny = Person('제니', 13)

wonie.say_hello('철수')
micheal.say_hello('미지')
jenny.say_hello('영희')

wonie.introduce()
'''
