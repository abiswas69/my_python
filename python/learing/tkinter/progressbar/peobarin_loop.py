from tkinter import *
from tkinter.ttk import *
import time
win=Tk()

def start():
    tss=10
    i=0
    while(i<tss):
        time.sleep(0.5)#dala one sceond
        proper["value"]+=10 #this value we inciriment
        i+=1
        percent.set(str(int((i/tss)*100))+"%")#we do is think i=1 than i/10*100= 10
        if (proper["value"]==100):
            win.destroy()
        else:
            win.update_idletasks()#this update the window per second

percent=StringVar()#this is allow us to update with new text
buton1=Button(win,text="press",command=start)
proper=Progressbar(win,length=300,orient=HORIZONTAL)
lae=Label(win,
          textvariable=percent#we cant update this textvariable with text
          )


lae.pack()
proper.pack()
buton1.pack()

win.mainloop()