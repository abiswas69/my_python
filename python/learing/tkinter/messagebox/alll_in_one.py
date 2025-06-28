from tkinter import *
from tkinter import messagebox

win=Tk()
win.geometry("400x200")
def clicke():
    messagebox.showinfo(title="this is mbox of showinfo "
                        ,message="this showinfo messagebox")
def clicke1():
    messagebox.showwarning(title="WARNING",message="this is warning messagebox")

def clicke2():
    messagebox.showerror(title="ERROR",message="this is error messbox")
    
def clicke3():
    if messagebox.askokcancel(title="askingokcancel",message="enter okay or cancel"):
        print("enter okay")
    else:
        print("enter cancel")

def clicke4():
    ASE= messagebox.askquestion(title="askingokcancel",message="enter okay or cancel")
    if(ASE=="yes"):
        print("you select yes")
    else:
        print("you enter no")
    

def clicke5():
    aes=messagebox.askretrycancel(title="this askretrycancel box",message="seclacted retry or cancel")
    if(aes==True):
        print("you enter retry")
    else:
        print("you enterr cancel")

def clicke6():
    wssd=messagebox.askyesnocancel(title="this is askyesnocancel ",message="seclected yes no cancel")
    if(wssd== True):
        print("you seclectd yes")
    elif(wssd==False):
        print("you seclectd no")
    elif(wssd==None):
        print("you seclectd cancel")
    else:
        print("idk know..")

def clicke7():
    wssd=messagebox.askyesnocancel(title="this is askyesnocancel "
                                   ,message="seclected yes no cancel"
                                   ,icon="info" #this line change the icon
                                   )
    if(wssd== True):
        print("you seclectd yes")
    elif(wssd==False):
        print("you seclectd no")
    elif(wssd==None):
        print("you seclectd cancel")
    else:
        print("idk know..")


buton=Button(win,text="showinfow",command= clicke)
buton1=Button(win,text="showwarning",command= clicke1)
buton2=Button(win,text="showerror",command= clicke2)
buton3=Button(win,text="ok-or-cancel",command= clicke3)
buton4=Button(win,text="askquestion",command= clicke4)
buton5=Button(win,text="askretrycancel",command= clicke5)
buton6=Button(win,text=" askyesnocancel",command= clicke6)
buton7=Button(win,text=" askyesnocancel",command= clicke7)




buton.grid(row=0,column=1)
buton1.grid(row=0,column=2)
buton2.grid(row=0,column=3)
buton3.grid(row=0,column=4)
buton4.grid(row=0,column=5)
buton5.grid(row=1,column=1)
buton6.grid(row=1,column=2)
buton7.grid(row=1,column=3)




win.mainloop()