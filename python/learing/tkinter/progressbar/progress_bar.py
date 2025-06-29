from tkinter import *
from tkinter.ttk import*


win=Tk()

def start():
    progressbar2["value"] +=10 #😁so this the value if we called start progressbar 
    #well iness by 10

progressbar2=Progressbar(win,
orient=HORIZONTAL,#this line of make the bar HORIZONTAL or vertical
length=300)#this is length of progressbar now it 300

progressbar2.pack()

buton=Button(win,text="download",command=start).pack()



win.mainloop()