from tkinter import *

win= Tk()

def sion():
    lbox.insert(lbox.size(),inpu.get())
    lbox.config(height=lbox.size())

lbox=Listbox(win,font=("arial",30))
inpu=Entry(win)
sume=Button(win,text="SUMBIT",command=sion)


lbox.pack()
inpu.pack()
sume.pack()
win.mainloop()