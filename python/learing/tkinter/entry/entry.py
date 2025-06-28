from tkinter import *

win=Tk()

def sim():
    dara=entryu.get()#we can get the value by get method Entry,get()
    print(dara)

entryu=Entry(win,font=("arial",10))
bu=Button(win,text="press",command=sim)#if press this we get the value

entryu.pack()
bu.pack()

win.mainloop()