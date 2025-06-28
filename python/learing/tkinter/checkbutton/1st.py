from tkinter import *


def sia():
    if(a.get()==1):
        print("you agrre")
    else:
        print("you don't agrre")
win=Tk()
a=IntVar()
cheak_button=Checkbutton(win,text="i agrre",
                         variable=a,
                         offvalue=0,
                         onvalue=1,
                         command=sia)

cheak_button.pack()

win.mainloop()