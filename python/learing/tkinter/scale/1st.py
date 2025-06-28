from tkinter import *

win=Tk()

def sume():
    print(f"num:-{sacl.get()}")
sacl=Scale(win,from_=100,to=0,
           length=400,#this hight of scale
            orient=HORIZONTAL #this can be  VERTICAL or HORIZONTAL
            ,tickinterval=10#this is the step of number
            ,showvalue=0#this line hide current value
            ,troughcolor="#69eaff"
            ,fg='red',
            bg='black'

            )
buton=Button(win,text="press",command=sume)
exitw=Button(win,text="exit",command=exit)

sacl.set(50)#this line cheange the scale postion to 50
sacl.pack()
buton.pack() 
exitw.pack()
win.mainloop()