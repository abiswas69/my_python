from tkinter import *
from tkinter import ttk
win=Tk()

notvoot=ttk.Notebook(win)#widegt that manage a collection of windows displays

tab1=Frame(notvoot)#new fram for tab
tab2=Frame(notvoot)

notvoot.add(tab1,text="tab 1")
notvoot.add(tab2,text="tab 2")
notvoot.pack()

Label(tab1,text="hi thus is just a text",width=50).pack()
Label(tab2,text="hi thus is tab 2",height=50).pack()

win.mainloop()