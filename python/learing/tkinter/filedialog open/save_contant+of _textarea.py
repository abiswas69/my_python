from tkinter import *
from tkinter import  filedialog

win=Tk()

def awda():
    sabe=filedialog.asksaveasfile(
        initialdir="F:\\my code\\semple\\text",
        filetypes=[("all type","*.*")],
        defaultextension='.txt',#the defult file extation of file
    )
    daea=tearwe.get("1.0",END)
    sabe.write(daea)
    sabe.close

buttone=Button(win,text="get data",command=awda)
tearwe=Text(win)


buttone.pack()
tearwe.pack()
win.mainloop()