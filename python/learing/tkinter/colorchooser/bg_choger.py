from tkinter import *
from tkinter import colorchooser

win=Tk()
win.geometry("420x420")

def dede():
    vare=colorchooser.askcolor()
    print(vare)
    print(vare[1])
    win.config(bg=vare[1])

buton=Button(win,text="press",command=dede)


buton.pack()

win.mainloop()