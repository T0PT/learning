class Warrior:
    def __init__(self, health=100, stamina=100):
        self.health = health
        self.stamina = stamina

    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nStamina: {self.stamina}')
        print('---------------')

    def heals(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} накладывает повязку из',
              f'целебных трав {target.__class__.__name__}')
        self.stamina -= 20
        target.health += 10
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
              f'\nУ {self.__class__.__name__} осталось {self.stamina} единиц запаса сил')
        print('---------------')

    def attacks(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} наносит урон мечом {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
        print('---------------')
    def __str__(self):
        s1='----------\n'
        s2='Class: '+self.__class__.__name__+'\n'
        s3='Health: '+str(self.health)+'\n'
        s4='Stamina: '+str(self.stamina)+'\n'
        return s1+s2+s3+s4+s1
    def __call__(self, *args, **kwargs):
        s1 = '----------\n'
        s2 = 'Class: ' + self.__class__.__name__ + '\n'
        s3 = 'Health: ' + str(self.health) + '\n'
        s4 = 'Stamina: ' + str(self.stamina) + '\n'
        print(self)
        return s1 + s2 + s3 + s4 + s1
    def __add__(self, other):
        if isinstance(other,int):
            self.health+=other
        elif isinstance(other,list):
            other.append(self.__class__.__name__)
        elif isinstance(other, object):
            other.health+=10

    def __sub__(self, other):
        if isinstance(other,int):
            self.health-=other
        elif isinstance(other,list):
            other.append(self.__class__.__name__)
        elif isinstance(other, object):
            other.health-=10

class Mage(Warrior):

    def __init__(self, health=60, mana=120):
        self.health = health
        self.mana = mana

    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nMana: {self.mana}')
        print('---------------')

    def heals(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} применяет заклинание лечения',
              f'к {target.__class__.__name__}')
        target.health += 10
        self.mana -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
              f'\nУ {self.__class__.__name__} осталось {self.mana} единиц магии')
        print('---------------')

    def attacks(self, target):
        print(f'{self.__class__.__name__} наносит урон магией {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
        print('---------------')
    def __setattr__(self, key, value):
        if value<0:
            self.__dict__[key]=0
        elif key=='health':
            self.__dict__[key] = value
            if value>60:
                self.__dict__[key] = 60
        elif key=='mana':
            self.__dict__[key] = value
            if value > 120:
                self.__dict__[key] = 120

    def __len__(self):
        return len(self.__dict__)

war=Warrior()
mag=Mage()
