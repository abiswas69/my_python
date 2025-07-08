from tkinter import *
from pymem import Pymem
 #so the 0x is hex value adn the address


def start():
    pm=Pymem("ac_client.exe")
    addres=0x0074FD74 
    data=entey.get()
    data=int(data)
    pm.write_int(addres,data)
   
    

win=Tk()
win.geometry("432x420")
entey=Entry(win)
b1=Button(win,text="start",command=start)

entey.pack()
b1.pack()

win.mainloop()
#if you have any problem commant down