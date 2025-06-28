from tkinter import *

win=Tk()
def desaw():
    lbox.delete(lbox.curselection())
    lbox.config(height=lbox.size())

lbox=Listbox(win,font=('arial',30))
delbu=Button(win,text="delet",command=desaw)

lbox.insert(1,"apple")
lbox.insert(2,"banana")
lbox.insert(3,"pinapple")
lbox.pack()
delbu.pack()

win.mainloop()