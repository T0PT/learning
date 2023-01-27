class warrior():
    def __init__(self, health,stamina):
        self.__health=health
        self.__stamina=stamina

    @property
    def stamina(self):
        return self.__stamina
    @stamina.setter
    def stamina(self, x):
        self.__stamina=x
        print(self.__stamina)

    @property
    def health(self):
        return self.__health
    @stamina.setter
    def health(self, x):
        self.__health = x
        print(self.__health)
    def shoot(self,target):
        target.health-=10
        print('target health = '+target.health)

class archer(warrior):
    def snipershot(self,target):
        target.health -= 15
        print('target health = ' + str(target.health))
        self.stamina-=30

war = warrior(100,100)
arch = archer(100,100)