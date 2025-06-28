from tkinter import * 

win=Tk()

def sumbit():
    inpu=area.get("1.0",END)#1.0 is startinf indux and end is last word
    print(inpu)

area=Text(win)
butas=Button(win,text="sumbit",command=sumbit)



area.pack()
butas.pack()
win.mainloop()