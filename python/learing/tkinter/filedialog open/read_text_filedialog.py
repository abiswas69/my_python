from tkinter import *
from tkinter import filedialog 


win=Tk()

def PATH():
    path=filedialog.askopenfilename(initialdir="E:\\document\\work",#this line goto file location to this path
        title="files",
        filetypes=(("text file","*.txt"),("all files","*.*"))#this line can select spcasipic file type
        )
    print(f"path od the file {path}")
    read=open(path,'r')
    print(f"this is contat od text file:-👉  {read.read()}  👈")
    read.close()

buton=Button(win,text="GET PATH",command=PATH)

buton.pack()
win.mainloop()