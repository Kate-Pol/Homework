import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import random


def throw():
    num_lst = []
    for i in range(3):
        num = random.randint(0, 10)
        num_lst.append(str(num))

    lb['text'] = ' '.join(num_lst)


root = tk.Tk()
root.title('I am one-armed bandit')
root.geometry('500x400+100+100')

myFont = font.Font(size = 15)

fr = ttk.Frame(root, width = 100, height = 100, border = 5, relief = 'ridge')
fr.grid(column = 0, columnspan = 3, row = 0, sticky = 'WE') 

lb = ttk.Label(fr, text = "Let's start", font = ('', 35))
lb.grid()

bt = tk.Button(root, text = 'Press the Button', font = myFont, background = '#2626E6', comman = throw)
bt.grid()


root.mainloop()
