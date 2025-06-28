from tkinter import *

def sunew():
    asd=lbox.get(lbox.curselection())
    print(asd)
win=Tk()
lbox=Listbox(win,
             width=10,
             font=("constantia",30),
             fg="#aff803",
             bg="#3b13ca"
             )

sune=Button(win,text="press",command=sunew)
lbox.insert(1,"apple")
lbox.insert(2,"banna")
lbox.insert(3,"pinapple")

lbox.pack()
sune.pack()
lbox.config(height=lbox.size())

win.mainloop()