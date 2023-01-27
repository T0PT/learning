from tkinter import *
import math
wind= Tk()
wind.geometry('300x250')
wind.title('Quad equation calc')
fr=LabelFrame(text='Enter data: ')
fr2=LabelFrame(text='Solving: ')
a=0
b=0
c=0
ent1=Entry(fr, width=5)
lb1=Label(fr, text='x**2 + ')
ent2=Entry(fr, width=5)
lb2=Label(fr, text='x + ')
ent3=Entry(fr, width=5)
txt=Text(fr2, height=10)
def solve(event):   
    txt.delete(0.0,END)
    global a
    global b
    global c
    try:
        a=int(ent1.get())
        b=int(ent2.get())
        c=int(ent3.get())
        d=b**2-4*a*c
        x1=0
        x2=0
        txt.insert(END,'Discriminant D = '+str(d)+'\n')
        if d>=0:
            x1=(-b+math.sqrt(d))/2*a
            x2=(-b-math.sqrt(d))/2*a
            if x1==x2:
                txt.insert(END,'Answer: x = '+str(x1)+'\n')
            else:
                txt.insert(END,'Answer:\nx1 = '+str(x1)+'\nx2 = '+str(x2))
        else:
            txt.insert(END,'There is no answer,\nbecause D < 0')
    except ValueError:
        print('Check your numbers')
wind.bind('<Return>',solve)
def autoclear(event):
    try:
        event.widget.delete(0,END)
    except:
        pass
wind.bind('<FocusIn>',autoclear)
#butt=Button(text='solve',command=solve)
def focus1(event):
    ent1.focus_set()
def focus2(event):
    ent2.focus_set()
def focus3(event):
    ent3.focus_set()
wind.bind('<Control-Key-1>',focus1)
wind.bind('<Control-Key-2>',focus2)
wind.bind('<Control-Key-3>',focus3)
fr.pack()
fr2.pack()
ent1.grid(column=0,row=0)
lb1.grid(column=1,row=0)
ent2.grid(column=2,row=0)
lb2.grid(column=3,row=0)
ent3.grid(column=4,row=0)
txt.pack()
#butt.pack()
