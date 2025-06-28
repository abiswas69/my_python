from tkinter import *

win=Tk()

Scaleuptodown=Scale(win,from_=0,to=100)
scaldowntoup=Scale(win,from_=100,to=0)



Scaleuptodown.pack()
scaldowntoup.pack()

win.mainloop()