import random
x=0
y=0
num=0
did=False
while did==False:
    try:
        x=int(input('minimum value: '))
        did=True
    except:
        print('i do not understand, try agian')
did=False
while did==False:
    try:
        y=int(input('maximum value: '))
        did=True
    except:
        print('i do not understand, try agian')
did=False
num=random.randint(x,y)
dog=y+1
while dog!=num:
    try:
        dog=int(input('guess the number: '))
        if dog ==num:print('You got this!!')
        else:print('Wrong!')
    except:
        print('i do not understand, try agian')
    
