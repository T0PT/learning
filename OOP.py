import random

class warrior():
    def __init__(self, health=100, stamina=100):
        self.__health=health
        self.__stamina=stamina
    def get_health(self):
        return self.__health
    def set_health(self,x):
        if x<=100 and x>=0:
            self.__health=x
    def get_stamina(self):
        return self.__stamina
    def set_stamina(self,x):
        if x<=100 and x>=0:
            self.__stamina=x
    def intro(self):
        print(__class__.__name__)
        print(self.__health)
        print(self.__stamina)
    def heal(self,target):
        if self.get_stamina() >= 10:
            print(self.__class__.__name__ + ' healed ' + target.__class__.__name__)
            self.set_stamina(self.get_stamina()-10)
            target.set_health(target.get_health()+10)
            self.status()
            target.status()
        else:
            print('Not enough stamina to do this')
    def status(self):
        print(__class__.__name__)
        print('health = '+str(self.__health))
        print('stamina = '+str(self.__stamina))
    def attack(self,target):
        if self.get_stamina() >=10:
            print(self.__class__.__name__ + ' attacked ' + target.__class__.__name__)
            self.__stamina-=10
            target.set_health(target.get_health()-10)
            self.status()
            target.status()
        else: print('Not enough stamina to do this')
        if target.get_health()<=0:
            print(self.__class__.__name__ + ' just killed ' + target.__class__.__name__+'\n'+'R.I.P, '+target.__class__.__name__)
            del(target)

class mage():
    def __init__(self, health=60, stamina=60):
        self.__health=health
        self.__stamina=stamina
    def get_health(self):
        return self.__health
    def set_health(self,x):
        if x<=100 and x>=0:
            self.__health=x
    def get_stamina(self):
        return self.__stamina
    def set_stamina(self,x):
        if x<=100 and x>=0:
            self.__stamina=x
    def intro(self):
        print(__class__.__name__)
        print(self.health)
        print(self.stamina)
    def status(self):
        print(__class__.__name__)
        print('health = '+str(self.__health))
        print('stamina = '+str(self.__stamina) +'\n')
    def heal(self, target):
        if self.get_stamina() >= 10:
            print(self.__class__.__name__+' healed '+ target.__class__.__name__ )
            self.set_stamina(self.get_stamina() - 10)
            target.set_health(target.get_health() + 10)
            self.status()
            target.status()
        else: print('Not enough stamina to do this')
    def attack(self,target):
        if self.get_stamina() >= 10:
            print(self.__class__.__name__ + ' attacked ' + target.__class__.__name__)
            self.__stamina -= 10
            target.set_health(target.get_health() - 10)
            self.status()
            target.status()
        else: print('Not enough stamina to do this')
        if target.get_health()<=0:
            print(self.__class__.__name__ + ' just killed ' + target.__class__.__name__+'\n'+'R.I.P, '+target.__class__.__name__)
            del(target)
class archer(warrior):
    def __init__(self, arrow=20, health=100, stamina=100):
        super().__init__(health,stamina)
        self.__arrows=arrow
    def attack(self,target):
        if self.get_stamina() >= 10:
            print(self.__class__.__name__ + ' attacked with a bow ' + target.__class__.__name__)
            self.__arrows -= 1
            self.set_stamina(self.get_stamina()-10)
            target.set_health(target.get_health() - 10)
            self.status()
            target.status()
        else: print('Not enough stamina to do this')
        if target.get_health()<=0:
            print(self.__class__.__name__ + ' just killed ' + target.__class__.__name__+'\n'+'R.I.P, '+target.__class__.__name__)
            del(target)
    def status(self):
        print(__class__.__name__)
        print('health = '+str(self.get_health()))
        print('stamina = '+str(self.get_stamina()))
        print('arrows = ' + str(self.__arrows) +'\n')
class alchemist(mage):
    def __init__(self,health=100,stamina=100,flasks=10):
        super().__init__(health,stamina)
        self.__flasks=flasks
    def attack(self,target):
        if self.get_stamina() >= 10:
            print(self.__class__.__name__ + ' attacked with a potion ' + target.__class__.__name__+'\n')
            self.__flasks -= 1
            self.set_stamina(self.get_stamina() - 10)
            target.set_health(target.get_health()-10)
            self.status()
            target.status()
        else: print('Not enough stamina to do this')
        if target.get_health()<=0:
            print(self.__class__.__name__ + ' just killed ' + target.__class__.__name__+'\n'+'R.I.P, '+target.__class__.__name__)
            del(target)

    def status(self):
        print(__class__.__name__)
        print('health = '+str(self.get_health()))
        print('stamina = '+str(self.get_stamina()))
        print('flasks = ' + str(self.__flasks) +'\n')

class knight(warrior):
    def __init__(self,health=100,armor=100,stamina=100):
        super().__init__(health,stamina)
        self.__armor=armor
    def get_armor(self):
        return self.__armor
    def set_armor(self,x):
        self.__armor+=x
    def status(self):
        super().status()
        print('armor = '+str(self.get_armor()))
    def __critical_hit(self,target):
        if self.get_stamina() >= 10:
            print(self.__class__.__name__ + ' attacked with a sword ' + target.__class__.__name__+'\n')
            self.set_stamina(self.get_stamina() - 10)
            target.set_health(target.get_health()-30)
            self.status()
            target.status()
        else: print('Not enough stamina to do this')
        if target.get_health()<=0:
            print(self.__class__.__name__ + ' just killed ' + target.__class__.__name__+'\n'+'R.I.P, '+target.__class__.__name__)
            del(target)
    def attack(self,target):
        j = random.randint(0,100)
        if j<41:
            self.__critical_hit(target)
        else:
            super().attack(target)
class wizard(mage):
    def __init__(self,health=100,armor=30,stamina=100):
        super().__init__(health,stamina)
        self.__armor = armor
    def fireball(self,target):
        if self.get_stamina() >= 10:
            print(self.__class__.__name__ + ' attacked with a sword ' + target.__class__.__name__+'\n')
            self.set_stamina(self.get_stamina() - 10)
            target.set_health(target.get_health()-40)
            self.status()
            target.status()
        else: print('Not enough stamina to do this')
        if target.get_health()<=0:
            print(self.__class__.__name__ + ' just killed ' + target.__class__.__name__+'\n'+'R.I.P, '+target.__class__.__name__)
            del(target)
    def attack(self,target):
        j = random.randint(0, 100)
        if j < 41:
            self.__critical_hit(target)
        else:
            super().attack(target)
        j = random.randint(0, 100)
        if j < 21:
            self.fireball(target)

unit3=knight()
unit1=archer()
unit2=alchemist()