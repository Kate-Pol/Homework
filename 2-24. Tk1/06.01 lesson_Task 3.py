from tkinter import *

win= Tk()

#Get the current screen width and height
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

#Set the geometry of frame, including screen dimensions - Full screen 
win.geometry(f"{screen_width}x{screen_height}+0+0")

win.mainloop()
