from tkinter import *
win=Tk()
win.geometry("420x420")
liste=["apple","banana","peinaple"]
xr=IntVar()
apple=PhotoImage(file="F:\\my code\\semple\\image\\apple.png")
banana=PhotoImage(file="F:\\my code\\semple\\image\\banana.png")
pinapple=PhotoImage(file="F:\\my code\\semple\\image\\pineapple.png")

def lei():
    if(xr.get()==0):
        print("you select apple")
    elif(xr.get()==1):
        print("you select BANANA")
    elif(xr.get()==2):
        print("you secleted PINAPPLE")
    else:
        print("idk...")

imagee=[apple,banana,pinapple]
for i in range(len(liste)):
    rediobutton=Radiobutton(win,text=liste[i]#this line add text to rediobutton
                            ,variable=xr #group together if shre the same vaeiable
                            ,value=i#this assigns each button a different value
                            ,image=imagee[i]
                            ,compound="left"
                            ,font=('impact',50)
                            ,command=lei
                            )
    

    rediobutton.pack()


win.mainloop()