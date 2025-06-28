from tkinter import *

win=Tk()
win.geometry("420x420")#optional i need this line 
ph=PhotoImage(file="F:\\my code\\semple\\image\\data\\ml.png")

def clki():
    print("button press") #and this is function of that command

buttone=Button(win,text="press"
               ,command=clki,# we add a command 
               font=("comic sans",20),
               fg="#00ff00",
               bg="black",
               activebackground="black",
               activeforeground="#00ff00",
               image=ph,#this line add a photo
               compound='center'#impotent this line show's the text
               
               
)#activebackground="black", this two lin
# activeforeground="#00ff00",)desvabel activ clour 
              


buttone.pack()

win.mainloop()