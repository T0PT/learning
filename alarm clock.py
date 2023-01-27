from tkinter import *
import random
clocks={}
wind=Tk()
wind.iconbitmap('alarm.ico')
lbl=Label(text='Alarm clocks: 0')
lstbox=Listbox(width=30,height=10, justify=CENTER, selectmode=MULTIPLE)
def obnov():
    lbl.config(text='Alarm clocks: '+str(len(clocks)))
def create():
    global clocks
    for i in range(0,10):
        if i >1:
            clocks[i]='07:'+str(random.randint(i*5, i*5+5))
        else:
            clocks[i]='07:0'+str(random.randint(i*5, i*5+4))
    for i in range(0,11):
        lstbox.insert(END, clocks.get(i))
    obnov()
btt=Button(text='random', command=create)
def dell():
    for i in range(10,1, -1):
        if i in lstbox.curselection():
            lstbox.delete(i)
            clocks.pop(i)
    obnov()
def delle():
    lstbox.delete(0,END)
    #lstbox.delete(ACTIVE)
    clocks.clear()
    obnov()
def change():
    x=lstbox.curselection()
    nwind=Toplevel()
    llb=Label(nwind,text='Enter new value')
    ent=Entry(nwind)
    def save():
        lstbox.insert(ACTIVE, ent.get())
        lstbox.delete(ACTIVE)
        nwind.destroy()
    but=Button(nwind,text='Save', command=save)
    llb.pack()
    ent.pack()
    but.pack()    
butt=Button(text='delete active',command= dell)
butt2=Button(text='delete all',command= delle)
butt3=Button(text='change',command= change)
lbl.pack()
lstbox.pack()
btt.pack()
butt.pack()
butt2.pack()
butt3.pack()
        
