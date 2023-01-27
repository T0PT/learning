from tkinter import *

num=1
wind = Tk()
wind.geometry("300x500")
fr = LabelFrame(text='add',width=600,height=200)
fr.pack(padx=3, pady=3)
lb1=Label(fr,text='What thing')
lb2=Label(fr,text='When')
what= Entry(fr)
when=Entry(fr)
def write():
    global num
    x=what.get()
    y=when.get()
    txt.insert(END,str(num)+'. '+x+'\t\t\t'+y+'\n')
    when.delete(0,END)
    what.delete(0,END)
    num+=1
butt=Button(fr,text='Write to the list',width=15,command=write)
lb1.grid(column=0,row=0,padx=5,pady=5)
lb2.grid(column=1,row=0,padx=5,pady=5)
what.grid(column=0,row=1,padx=5,pady=5)
when.grid(column=1,row=1,padx=5,pady=5)
butt.grid(column=0,row=2,columnspan=2,padx=5,pady=5)
txt = Text(width=35, height=20)
txt.pack()
def dell():
    txt.delete(0.0,END)
btt=Button(text='delete all', command=dell)
btt.pack()
