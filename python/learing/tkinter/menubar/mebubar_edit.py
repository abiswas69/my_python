from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser

def open():
    prie=filedialog.askopenfilename()
    print(prie)

def bgr():
    storetheclore=colorchooser.askcolor()
    win.config(bg=storetheclore[1])

win=Tk()

openw=PhotoImage(file="F:\\my code\\semple\\image\\icon\\file1.png")
savew=PhotoImage(file="F:\\my code\\semple\\image\\icon\\save1.png")
editw=PhotoImage(file="F:\\my code\\semple\\image\\icon\\edit1.png")
exitw=PhotoImage(file="F:\\my code\\semple\\image\\icon\\exit1.png")

meau=Menu(win)
win.config(menu=meau) #so we crated it here 

fielemenu=Menu(meau,#this crated a menu to manu bar
               tearoff=0 #thus is off the teaf of me off fluting menu
               ) 
edite=Menu(meau,tearoff=0)
meau.add_cascade(label="file",menu=fielemenu)#this add option to the meanu menu 
meau.add_cascade(label="edit",menu=edite)

fielemenu.add_command(label="open",command=open,image=openw,compound="left")#this command we can modify
fielemenu.add_command(label="save",image=savew,compound="left")#this is command buttoon add to file menu
fielemenu.add_separator()#this add a separat line 
fielemenu.add_command(label="exit",command=exit,image=exitw,compound="left")

edite.add_command(label="peak color",command=bgr,image=editw,compound="left")

win.mainloop()