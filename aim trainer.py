from tkinter import *
import random
import time

wind= Tk()
wind.title('Aim Trainer')
count=0
tm=0
cordinates1=0
cordinates2=0
initial=int(time.time())

def spawn():
    global cordinates1
    global cordinates2
    cordinates1=random.randint(0,470)
    cordinates2=random.randint(0,470)
    color=f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'
    canvas.create_oval(cordinates1,cordinates2,
                       cordinates1+30,cordinates2+30,fill=color,outline=color)
    f5()
def pop(event):
    global cordinates1
    global cordinates2
    global count
    if event.x>=cordinates1 and event.x<=cordinates1+30 and event.y>=cordinates2 and event.y<=cordinates2+30:
        canvas.create_rectangle(0,0,500,500,fill='white',outline='white')
        count+=1
        spawn()
    f5()
canvas=Canvas(width=500,height=500,bg='white')
cnt=Label(text=str(count))
cnt.pack()
canvas.pack()
canvas.bind('<Button-1>',pop)
def f5():
    global count
    global tm
    cnt.config(text=str(count-tm))
def tmm():
    global tm
    tm+=1
    f5()
    wind.after(1000, tmm)
spawn()
tmm()

