from tkinter import *

win= Tk()
wes=Frame(win)
wes.pack()

Button(wes,text="W").pack(side="top")
Button(wes,text="A").pack(side="left")
Button(wes,text="S").pack(side="left")
Button(wes,text="D").pack(side="left")

win.mainloop()