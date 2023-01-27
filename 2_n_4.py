import random
class robot():
    def __init__(self,name,year,fsost,psost):
        self.name=name
        self.year=year
        self.__fsost=fsost
        self.__psost=psost
    def get_conditions(self):
        sost=self.__psost+self.__fsost
        if sost<-1:
            print('I feel really bad!')
        elif sost<=0 and sost>=-1:
            print('I feel pretty bad')
        elif sost<=0.5 and sost>=0:
            print('It could be worse')
        elif sost<=1 and sost>=0.5:
            print('It looks like everything if fine')
        elif sost>1:
            print('I am very good!!')
rb1=robot('Marvin',1979,0.2,0.4)
rb2=robot('Caliban',1993,-0.4,0.3)
rb1.get_conditions()
rb2.get_conditions()

class amogus():
    def __init__(self, name,colour,role):
        self.name=name
        self.colour=colour
        self.role=role
    def __call__(self, *args, **kwargs):
        print('Name: '+self.name)
        print('Colour: '+self.colour)
        print('Role: ' + str(self.role))
class among_us():
    def __init__(self, pl):
        if pl>9: pl=9
        if pl < 4: pl = 4
        self.players=[]
        self.colours=['red','green','blue','pink','orange','white','black','brown','yellow']
        x=random.randint(0,pl-1)
        y=x
        if pl>=7: y=random.randint(0,pl-1)
        for i in range(0,pl):
            if i==x or i==y:
                nam=input('Enter you nickname: ')
                print('Choose colours from: '+str(self.colours))
                col=''
                while col not in self.colours:
                    col=input('Enter you color: ')
                self.colours.remove(col)
                self.players.append(amogus(nam,col,0))
                print('You are imposter!')
                print('Shhhhhh!\n')
            else:
                nam = input('Enter you nickname: ')
                print('Choose colours from: ' + str(self.colours))
                col = ''
                while col not in self.colours:
                    col = input('Enter you color: ')
                print('\n')
                self.colours.remove(col)
                self.players.append(amogus(nam, col, 1))
a=among_us(4)


