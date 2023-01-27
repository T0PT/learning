from tkinter import *
from tkinter import messagebox
wind= Tk()
wind.geometry('400x300')
wind.title('Calculator')
lb=Label(text='Enter a math expression, using \n + - * / ** // %')
lb2=Label(text='answer')
ent= Entry()
ent.focus()
def solve():
    sol=0
    try:
        sol=eval(ent.get())
    except SyntaxError:
        messagebox.showwarning('Attention!', 'You forgot something in yourepression, check it')
    except NameError:
        messagebox.showerror('Mistake!!', 'You wrote something incorrect, check it')       
    except ZeroDivisionError:
        messagebox.showwarning('Seriously?!?!', 'Dont you trying devide by 0?')
    lb2.config(text=str(sol))
        
but=Button(text='solve', command=solve)
lb.pack()
ent.pack()
but.pack()
lb2.pack()
