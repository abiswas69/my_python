from tkinter import *

win = Tk()

def allkey(event):
    if event.char:
        print(f"Character pressed: {event.char}")
    else:
        # This branch handles special keys that don't have a printable character
        print(f"Special key pressed: {event.keysym}")

win.bind("<Key>", allkey)
win.mainloop()