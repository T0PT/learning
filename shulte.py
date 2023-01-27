from tkinter import *
import random
import datetime
import threading
x=datetime.datetime.now()
print(x.second)
lis=[]
butts=[]
onnum=1
col=0
rw=0
wind= Tk()
wind.geometry('300x250')
wind.title('Shulte')
gf=Frame()
lbt=Label()
xi=0
lb=Label(gf,text='Шульте — это простая игра, которая развивает\n периферическое зрение, скорость чтения и реакцию!\nПравила игры:\n1. Игрок должен быстрее всех выбрать все числа по порядку от 1 до 9. \n2. Если игрок ошибается – игра начинается заново.\n3. Побеждает тот, кто быстрее всех справится с задачей.')
def updatetimer():
    global xi
    print(str(datetime.datetime.now().second-xi.second)+'.'+str(datetime.datetime.now().microsecond-xi.microsecond))
    lbt.config(text=str(datetime.datetime.now().second-xi.second)+'.'+str(datetime.datetime.now().microsecond-xi.microsecond))
def start():
    global xi
    xi=datetime.datetime.now()
    global col
    global rw
    gf.forget()
    updatetimer()
    while len(lis)<9:
        x=random.randint(1,9)
        if not x in lis:
            lis.append(x)
    for i in range(0,9):
        butts.append(Button(height=5,width=10,text=lis[i]))
        butts[i].grid(column=col, row=rw) #prodolzhai ot suda
        col+=1
        if col==3:
            rw+=1
            col=0
    lbt=Label(text='----')
    lbt.grid(column=3,row=1)
    timer = threading.Timer(1, updatetimer)
    timer.start()
butt=Button(gf,text='Start game!',command=start)
gf.pack()
lb.pack()
butt.pack()
wind.mainloop()
