from tkinter import *


win=Tk()
def done():
    newwin=Toplevel()

def don():
    newwin=Tk()
    win.destroy()
    def don1():
        win=Tk()
    Button(newwin,text="new window",command=don1).pack()


Button(win,text="new window",command=done).pack()
Button(win,text="new window",command=don).pack()
win.mainloop()