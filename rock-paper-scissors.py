from tkinter import *
import random
wind= Tk()
wind.geometry('225x230')
wind.title('Rock-Paper-Scissors')
used=0
uwon=0
ulost=0
def count():
    global uwon
    global ulost
    uw.config(text=str(uwon))
    ul.config(text=str(ulost))
def rock():
    global used
    global uwon
    global ulost
    if used==0:
        i=0
        ty.config(text='Rock')
        i=random.randint(1,3)
        if i==1:
            ta.config(text='Rock')
            tb.config(text='    Draw!!!   ')
        elif i==2:
            ta.config(text='Paper')
            tb.config(text='    You lose!!!   ')
            ulost+=1
        else:
            ta.config(text='Scissors')
            tb.config(text='    You win!!!    ')
            uwon+=1
    used=1
    count()
def paper():
    global used
    global uwon
    global ulost
    if used==0:
        i=0
        ty.config(text='Paper')
        i=random.randint(1,3)
        if i==1:
            ta.config(text='Rock')
            tb.config(text='    You win!!!    ')
            uwon+=1
        elif i==2:
            ta.config(text='Paper')
            tb.config(text='    Draw!!!   ')
        else:
            ta.config(text='Scissors')
            tb.config(text='    You lose!!!   ')
            ulost+=1
    used=1
    count()
def scissors():
    global used
    global uwon
    global ulost
    if used==0:
        i=0
        ty.config(text='Scissors')
        i=random.randint(1,3)
        if i==1:
            ta.config(text='Rock')
            tb.config(text='    You lose!!!   ')
            ulost+=1
        elif i==2:
            ta.config(text='Paper')
            tb.config(text='    You win!!!    ')
            uwon+=1
        else:
            ta.config(text='Scissors')
            tb.config(text='    Draw!!!   ')
    used=1
    count()
def reset():
    global used
    used=0
    tt.config(text='You             -             AI')
    ty.config(text='Choose')
    tb.config(text='')
    ta.config(text='??????')
tt=Label(text='You             -             AI')
ty=Label(text='Choose')
tb=Label(text='')
ta=Label(text='??????')
uw=Label(text='0')
ul=Label(text='0')
sch=Label(text='-')
bt1=Button(text='Rock',width=10, command=rock)
bt2=Button(text='Paper',width=10, command=paper)
bt3=Button(text='Scissors',width=10, command=scissors)
btr=Button(text='Reset',width=30, command=reset)
tt.grid(column=0,row=0,columnspan=3)
ty.grid(column=0,row=1)
ta.grid(column=2,row=1)
tb.grid(column=1,row=1)
bt1.grid(column=0,row=2)
bt2.grid(column=1,row=2)
bt3.grid(column=2,row=2)
btr.grid(column=0,row=3,columnspan=3)
uw.grid(column=0,row=4)
ul.grid(column=2,row=4)
sch.grid(column=1,row=4)


