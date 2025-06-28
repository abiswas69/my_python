from tkinter import * 
 

win=Tk()
phot=PhotoImage(file="F:\\my code\\semple\\image\\data\\box.png")
#the arial is fpnt famliy and 40 is hight and style is bold
#fg stand for fourgrand clour of that text we can also use hex velu like #ff0000
#bg stamd for backgrand clor we can also use HEZ code jere 
labal=Label(win,text="Hi",
            font=('arial',40,'bold'),
            fg='blue',
            bg="#ff0000",
            relief=SUNKEN,#BODER STYEL
            bd=10,#bd is use for boder of the text 
            padx=20,
            pady=20,)
#add image here
l2=Label(win,text="Hi",
            font=('arial',40,'bold'),
            fg='blue',
            bg="#ff0000",
            relief=SUNKEN,#BODER STYEL
            bd=10,#bd is use for boder of the text 
            padx=20,
            pady=20,
            image=phot, compound='left')

labal.pack()
l2.pack()

win.mainloop()