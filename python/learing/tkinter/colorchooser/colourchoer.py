from tkinter import *
from tkinter import colorchooser


Win=Tk()
Win.geometry("400x400")
def asw():
    aswe=colorchooser.askcolor()
    print(aswe)

butom=Button(Win,text="press",font=("arial",30),command=asw)


butom.pack()
Win.mainloop()