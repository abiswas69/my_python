from tkinter import * 

win=Tk()

win.geometry("420x420")

def s():
    asd=box.get()
    print(asd)
def enaval():
    box.config(show="*")
def desaval():
    box.config(state=DISABLED)

box=Entry(win,font=('arial',10),)
box.insert(0,"hello")
bount=Button(win,text="press",command=s)
at=Button(win,text="*",command=enaval)
dest=Button(win,text="DISABLED",command=desaval)

box.pack()
bount.pack()
at.pack()
dest.pack()

win.mainloop()