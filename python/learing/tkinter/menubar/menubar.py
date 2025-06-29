from tkinter import *

win=Tk()

# 3. Create the main menu bar. This will sit at the very
#  top of our window.
# It's a 'Menu' object associated with our 'win' window.
manyu=Menu(win)#
# 4. Tell our window to use 'manyu' as its official menu bar.
# This makes the menu bar visible in the window.
win.config(menu=manyu)
# 5. Create the first dropdown menu, typically named 'File'.
# 'tearoff=0' is a small setting that removes a dashed line that would
# otherwise appear at the top of the dropdown, making it look cleaner.
filw=Menu(manyu)
filwe=Menu(manyu)
# 7. Add the 'file' dropdown menu to our main menu bar ('manyu').
# 'label="file"' is the text that appears on the main menu bar.
# 'menu=filw' means when you click 'file', the 'filw' dropdown
#  will open.
manyu.add_cascade(label="file",menu=filw)
manyu.add_cascade(label="files",menu=filwe)
# --- Add items to the 'file' dropdown menu ---

# Add a 'save' item to the 'filw' dropdown menu.
# 'command=save_file' means when this item is
#  clicked, the 'save_file' function runs.
filw.add_command(label="save")
filw.add_command(label="open")
filw.add_command(label="exit")



win.mainloop()