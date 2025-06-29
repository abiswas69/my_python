from tkinter import *

win=Tk()
def fub(event):
    print("w")

def fubA(event):
    print("A")

def fubW(event):
    print("S")

def fubE(event):
    print("D")




win.bind("<w>",fub)
win.bind("<a>",fubA)
win.bind("<S>",fubW)
win.bind("<d>",fubE)

win.mainloop()