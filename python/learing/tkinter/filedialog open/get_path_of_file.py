from tkinter import *
from tkinter import filedialog

win= Tk()

def path():
    filepath=filedialog.askopenfilename()
    print(filepath)

butopm=Button(win,text="get path",command=path)
butopm.pack()
win.mainloop()