from tkinter import *
import random
chisl=20
wind= Tk()
wind.geometry('400x300')
wind.title('Palki')
tl=Label(text='Enter number from 1 to 3',font=('Arial', 15, 'bold'))
ent = Entry(font=('Arial', 15, 'bold'),justify=CENTER)
tl2=Label(text='||||||||||||||||||||',font=('Arial', 30, 'bold'))
tl3=Label(text=str(chisl),font=('Arial', 30, 'bold'))
def take():
    global chisl
    butt.config(state=DISABLED)
    nm=int(ent.get())
    chisl-=nm
    tl3.config(text=str(chisl))
    txt=''
    for i in range(0,chisl):txt+='|'
    tl2.config(text=txt)
    if chisl==1 :
        tl.config(text='You WON!!!')
    else:
        tl.config(text='wait for computer')
        def opa():
            global chisl
            if chisl==4:
                z=3
            elif chisl==3:
                z=2
            elif chisl==2:
                z=1
            else:
                z = random.randint(1,3)
            chisl-=z        
            tl3.config(text=str(chisl))
            txt=''
            for i in range(0,chisl):txt+='|'
            tl2.config(text=txt)
            if chisl==1:
                tl.config(text='You LOST!!!')
            else:
                tl.config(text='computer took '+str(z)+' stics, your turn')
                ent.delete(0, 'end')
                butt.config(state=NORMAL)
        wind.after(2000, opa)    
butt=Button(text='Take a stick',command=take)
tl.grid(column=0,row=0)
ent.grid(column=0,row=1)
tl2.grid(column=0,row=2)
tl3.grid(column=0,row=3)
butt.grid(column=0,row=4)
