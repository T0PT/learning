from tkinter import *
import time
import random

Wind = Tk()
Wind.geometry("300x300")
Initial=0.0
Initial=round(float(time.time()-Initial),2)
ideal=0.0
paused=False
rounds=0
ls=list()

def clck(event):
    global Initial
    global ideal
    global rounds
    if rounds<6 and paused==False:
        if ideal>time.time():
            Canvas.create_rectangle(0,0,300,300,fill='black',outline='black')
            Text.insert(END,'Too early!\n')
            rounds+=1
        else:
            Text.insert(END,str(round(float(time.time()-ideal),2))+'\n')
            ls.append(round(float(time.time()-ideal)))
            Initial=round(float(time.time()-Initial),2)
            x=random.randint(0,999)/100
            ideal=x+time.time()
            Canvas.create_rectangle(0,0,300,300,fill='red',outline='red')
            Wind.after(int(x*1000),green)
            rounds+=1
    elif rounds==6:
        Text.insert(END,str(sum(ls)/len(ls))+'-average\n')
def green():
    Canvas.create_rectangle(0,0,300,300,fill='green',outline='green')
def start():
    ls.clear()
    paused=False
    global Initial
    global ideal
    global rounds
    rounds=0
    Text.delete(0.0,END)
    Initial=round(float(time.time()-Initial),2)
    x=random.randint(0,999)/100
    ideal=x+time.time()
    print(ideal)
    print(time.time())
    Canvas.create_rectangle(0,0,300,300,fill='red',outline='red')
    Wind.after(int(x*1000),green)
    rounds+=1
def stop():
    paused=True
StartButton=Button(width=10,height=5,text='START', command=start)
StopButton=Button(width=10,height=5,text='STOP', command=stop)
Text=Text(width=11,height=12)
Text.insert(END,'Waiting\nfor click\non start\nbutton\n\nRED-wait\nfor green\nGREEN-click\nBLACK-you\nclicked too\nearly')
Canvas=Canvas(width=200,height=200,bg='white')
StartButton.grid(column=0,row=0)
StopButton.grid(column=1,row=0)
Text.grid(column=0,row=1,padx=10)
Canvas.grid(column=1,row=1,columnspan=2)
Canvas.bind('<Button-1>',clck)
    
Wind.mainloop()
