import tkinter as tk
import tkinter.font as font


root = tk.Tk()
root.title('Password')
root.geometry('500x400+100+100')

def root_close():
    root.destroy()

lb = tk.Label(root, text = 'Enter the Password', font = ('', 15)).pack(pady = 20)

password = tk.Entry(root, show = '*', width = 20)
password.pack()

myFont = font.Font(size = 15)

bt = tk.Button(root, text = 'Close', font = myFont, background = '#BFF3A5', command = root_close).pack(pady = 20)

root.mainloop()
