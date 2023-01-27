from tkinter import *
import random
wind= Tk()
wind.title('Canvas')
canvas=Canvas(height=450,width=450,relief=SOLID, bd=1,bg='white')
canvas.pack()
for i in range(0,2000):
    wind.update()
    x=random.randint(0,450)
    y=random.randint(0,450)
    if x>y:o=random.randint(0,450-x)
    else:o=random.randint(0,450-y)
    color=f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'
    canvas.create_oval(x,y,x+o,y+o,fill=color,outline='black',width=3)
