from tkinter import *

win=Tk()

canva=Canvas(win,height=420,width=420)
canva.create_line(0,0# straing point
                  ,420,420#ending point
                  ,fill="red"#this line colour to line
                  ,width=5
                  )#this line create a line
canva.create_line(0,420,420,0,fill="blue",width=5)

canva.create_rectangle(50,50,208,208,fill="red")

canva.create_polygon( 209,0,#first(top)
                      400,400,#second(right)
                      0,400#third(left)
                      ,fill="blue"

)
point=[0,0,420,420]
canva.create_arc(point,fill="green")
canva.create_arc(point,fill="green",start=180#this line reouted 180 drgree
                 )

canva.pack()
win.mainloop()