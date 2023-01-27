from tkinter import *

brushsize=5
lastcolor=f'#{0:02x}{0:02x}{0:02x}'
color=f'#{0:02x}{0:02x}{0:02x}'
brush=True

wind= Tk()
wind.title('PAINt')
cn=Canvas(width=700,height=500,bg='white')
def changescale(size):
    global brushsize
    brushsize=int(size)
def changecolor(red):
    global color
    global brush
    global lastcolor
    r=int(scr.get())    
    g=int(scg.get())
    b=int(scb.get())
    scr.config(troughcolor=f'#{r:02x}{0:02x}{0:02x}')
    scg.config(troughcolor=f'#{0:02x}{g:02x}{0:02x}')
    scb.config(troughcolor=f'#{0:02x}{0:02x}{b:02x}')
    color=f'#{r:02x}{g:02x}{b:02x}'
    col.config(bg=color)
    if brush==True:
        lastcolor=color
def clear():
    cn.delete("all")
def rubber():
    global brush
    global lastcolor    
    brush=False    
    if brush==False:
        lastcolor=f'#{255:02x}{255:02x}{255:02x}'
        rubberbutt.config(relief=SUNKEN)
        brushbutt.config(relief=RAISED)
    else:
        lastcolor=color
        rubberbutt.config(relief=RAISED)
        brushbutt.config(relief=SUNKEN)        
def brush():
    global brush
    global lastcolor
    global color
    brush=True    
    if brush==False:
        lastcolor=f'#{0:02x}{0:02x}{0:02x}'
        rubberbutt.config(relief=SUNKEN)
        brushbutt.config(relief=RAISED)
    else:
        lastcolor=color
        rubberbutt.config(relief=RAISED)
        brushbutt.config(relief=SUNKEN)
        
sc=Scale(command=changescale, label='Brush\nscale')
scr=Scale(command=changecolor, label='Red',from_=0,to=255,troughcolor='red')
scg=Scale(command=changecolor, label='Green',from_=0,to=255,troughcolor='green')
scb=Scale(command=changecolor, label='Blue',from_=0,to=255,troughcolor='blue')
col=Label(text='Your\ncolor',width=10,height=5,bg=color,fg='white')
delbutt=Button(text='DELETE\nALL',command=clear,height=5,width=10)
rubberbutt=Button(text='Rubber',command=rubber,height=5,width=5,relief=RAISED)
brushbutt=Button(text='Brush',command=brush,height=5,width=5,relief=SUNKEN)
def draw(event):
    global brushsize
    global lastcolor
    global color
    cn.create_oval(event.x-brushsize,
                   event.y-brushsize,
                   event.x+brushsize,
                   event.y+brushsize, fill=lastcolor, outline=lastcolor)
    
cn.bind('<B1-Motion>',draw)
sc.grid(column=0,row=0)
scr.grid(column=1,row=0)
scg.grid(column=2,row=0)
scb.grid(column=3,row=0)
col.grid(column=4,row=0)
delbutt.grid(column=7,row=0)
rubberbutt.grid(column=5,row=0)
brushbutt.grid(column=6,row=0)
cn.pack() #.grid(column=0,row=2,columnspan=8)
brush()
wind.mainloop()
