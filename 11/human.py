class Human:
    def __init__(self, name = 'Акакий Акакиевич Башмачкин'):
        self.name = name
        print(f'Родился человек с именем {self.name}')

    def set_name(self, name):
        self.name = name
    
    def growing(self):
        print(f'{self.name} отмечает день рождения')
    
    def get_name(self):
        print(self.name)

    def eating(self):
        print(f'{self.name} ест')
    
    def sleeping(self):
        print(f'{self.name} спит')

    def working(self):
        print(f'{self.name} работает')

    def relaxing(self):
        print(f'{self.name} отдыхает')

class Life():
    def life(self, human, years = 70):
        year = 0
        while year < 18:
            human.growing()
            human.eating()
            human.sleeping()
            human.relaxing()
            year += 1
        print(f'{human.name} отмечает 18-ти летие и начинает работать.')
        while year < 65:
            human.growing()
            human.eating()
            human.sleeping()
            human.working()
            human.relaxing()
            year += 1
        print(f'{human.name} отмечает 65-ти летие и выходит на пенсию.')
        while year <= years:
            human.growing()
            human.eating()
            human.sleeping()
            human.relaxing()
            year += 1

rakhman = Human('Рахман')
my_life = Life()
my_life.life(rakhman, 80)
