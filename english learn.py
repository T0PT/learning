from tkinter import *
from tkinter import messagebox
words={'you':'ты', 'i':'я','we':'мы','are':'являемся','champions':'чемпионы'}
import random
n='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n2='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
word='nah'
transcription=''
onletter=0
transto='rus'
ewords=dict([[v, k] for k,v in words.items()])
wind= Tk()
wind.geometry('225x260')
wind.title('Learning English')
answr=Label(text='')
itog=Label(text='==')
#wind.resizable(False,False)
def forbutts(button):
    global answr
    global itog
    global word
    #global transcription
    global onletter
    letter=button.cget('text')
    letter=letter.lower()   
    if transcription[onletter]== letter:        
        button.config(bg='green')
        onletter+=1
        txt=''
        for i in range(0,onletter):
            txt+=transcription[i]
        answr.config(text=txt)
    else:        
        button.config(bg='red')
    print(onletter)
    print(len(transcription))
    if onletter == len(transcription):
        messagebox.showinfo("Поздравляю" , 'You won!!!')
def opengame():
    global word
    global transto
    global transcription
    global answr
    global itog
    alf=n
    if transto=='rus':        
        m=random.randint(0,4)
        wordss=list(words.keys())
        word=wordss[m]
        transcriptionss=list(ewords.keys())
        transcription=transcriptionss[m]
        alf=n2
    else:        
        m=random.randint(0,4)
        wordss=list(ewords.keys())
        word=wordss[m]
        transcriptionss=list(words.keys())
        transcription=transcriptionss[m]
        alf=n    
    butt=[]
    column=0
    row=2      
    lb=Label(text=word)    
    lb.grid(column=0,row=0,columnspan=5)
    answr.grid(column=0,row=1,columnspan=5)
    itog.grid(column=0,row=row+1,columnspan=5)
    for i in range(0,len(alf)):
        butt.append(Button(text=alf[i],width=5))
        butt[i].config(command=lambda button=butt[i]: forbutts(button))
        butt[i].grid(column=column,row=row)
        column+=1
        if column>4:
            column=0
            row+=1
    
def rus():
    global transto
    transto='rus'
    bt1.grid_forget()
    bt2.grid_forget()
    opengame()
def eng():
    global transto
    transto='eng'
    bt1.grid_forget()
    bt2.grid_forget()
    opengame()
bt1=Button(text="Can you translate?\nENG->RUS",width=30,command=rus)
bt2=Button(text="Can you translate?\nRUS->ENG",width=30,command=eng)
def choose():
    bt1.grid(column=0,row=1)
    bt2.grid(column=0,row=2)
    print(words)
    
choose()
wind.mainloop()

