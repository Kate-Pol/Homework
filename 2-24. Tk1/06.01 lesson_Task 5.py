from tkinter import *

win = Tk()

#Get the current screen width and height
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

#Set the geometry of frame, including screen dimensions - Left Half screen
win.geometry(f"{int(screen_width/2)}x{screen_height}+0+0")

#Set the geometry of frame, including screen dimensions - Right Half screen
win1 = Tk()
win1.geometry(f"{int(screen_width/2)}x{screen_height}+{int(screen_width/2)}+0")

win.mainloop()
