from tkinter import*

win=Tk()
win.geometry("420x420")#optionlan
def sun():
    fdg=inputes.get() #this will get the data
    print(fdg)

def backspece():
    inputes.delete(len(inputes.get())-1,END) # this delte last chr

def delte():
    inputes.delete(0,END) #this delte all 

inputes=Entry(win,font=("arial",10))
sumbu=Button(win,text="SUBMIT",command=sun)
delteA=Button(win,text="delte",command=delte)
backspecee=Button(win,text="backspece",command=backspece)

inputes.pack()
sumbu.pack()
delteA.pack()
backspecee.pack()

win.mainloop()