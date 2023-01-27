class rectangle():
    def __init__(self, width=10,height=5):
        self.width=width
        self.height=height
    def calc_area(self):
        print('area = '+str(self.height*self.width))
    def draw(self):
        for i in range(0,self.height):
            x=''
            for i in range(0,self.width):
                x+='* '
            print(x)
rect=rectangle(5,3)

class square(rectangle):
    def __init__(self, width=10):
        self.width=width
        self.height=width
sq=square(5)

class elevator():
    def __init__(self, house=5, floor=3):
        self.house=house
        self.floor=floor
    def up(self):
        if self.house>self.floor:
            self.floor+=1
            print('elevator is on the ' + str(self.floor) + ' floor')
        else:print('already on the top floor')
    def down(self):
        if self.floor!=1:
            self.floor-=1
            print('elevator is on the '+ str(self.floor)+ ' floor')
        else:print('already on the first floor')
elev=elevator()

class good_elevator(elevator):
    def move(self,x):
        if x<=self.house and x>0:
            if self.floor!=x:
                print('elevator is moving from '+ str(self.floor)+' to '+str(x)+' floor')
                self.floor=x
            else:
                print('already on '+str(self.floor)+' floor')
        else:
            print('wrong floor, try agian')
g_elev=good_elevator()