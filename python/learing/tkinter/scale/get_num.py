from tkinter import *

win=Tk()

def sumbit():
    print(f"number:-{scal.get()}")

scal=Scale(win,from_=100,to=0)
buttonsumet=Button(win,text="SUMBIT",command=sumbit)

scal.pack()
buttonsumet.pack()

win.mainloop()