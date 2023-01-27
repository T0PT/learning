import time
initial=0.0
lst=[]
def counttime(x):
    global initial
    initial = round(float(time.time()), 2)
    x()
    print(round(float(time.time()), 2) - initial)

def wrapper(x):
    def ex():
        print('ex')
        x()
    return ex

@wrapper
def ask():
    y=input('Enter something: ')
    #print(y)
    return y

def controller(x):
    global lst
    def check(d):
        if d in lst:
            print('already used this')
        else:
            lst.append(d)
            x(d)
    return check
@controller
def hello(x):
    print('Hi, '+x+'!')
