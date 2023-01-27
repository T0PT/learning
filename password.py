from tkinter import *
white=True
wind= Tk()
wind.geometry("400x300")
lf=LabelFrame(text="password",width=200,height=200)
lf.pack()
lb1=Label(lf,text="Enter password")
lb2=Label(lf,text="")
inpt=Entry(lf,width=10,show="~",justify=CENTER,bg='black',fg='pink')
def show():
    first=False
    second=False
    third=False
   
    password=inpt.get()
    for i in password:
        if i.islower()==True: first=True
        if i.islower()!=True: second=True
        if i.isdigit()==True: third=True
    if first==second==third==True:
        lb2.config(text="password is good!",fg='green')
    else:
        txt=''
        lb2.config(text="password is not good!",fg='red')
        if first==False: txt+='There is no lowercase letters!\n'
        if second==False: txt+='There is no capital letters!\n'
        if third==False: txt+='There is no digits!\n'
        lb2.config(text=txt,fg='red')
def theme():
    global white
    if white==True:
        white=False
        lf.config(bg='grey',fg='white')
        lb1.config(bg='grey',fg='white')
        lb2.config(bg='grey',fg='white')
        butt.config(bg='grey',fg='white')
        butt2.config(bg='grey',fg='white')
        wind.config(bg='grey')
    else:
        white=True
        lf.config(bg='grey90',fg='black')
        lb1.config(bg='grey90',fg='black')
        lb2.config(bg='grey90',fg='black')
        butt.config(bg='grey90',fg='black')
        butt2.config(bg='grey90',fg='black')
        wind.config(bg='grey90')
butt=Button(lf,text="Show", command=show)
butt2=Button(lf,text="Change theme", command=theme)
lb1.grid(column=0, row=0)
lb2.grid(column=0, row=2)
butt.grid(column=0, row=3)
inpt.grid(column=0, row=1)
butt2.grid(column=0, row=4)


    
