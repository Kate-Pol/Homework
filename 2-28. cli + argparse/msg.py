import tkinter as tk
import sys


args = sys.argv

def user_input():
    global user
    user = input('Please enter sentences: ')
user_input()

def kill():
    root.destroy()
    
root = tk.Tk()

if '-t' in args: 
    user_time = int(input('Change time to (ms): '))
    root.after(f'{user_time}', kill)
else: 
    root.after(5000, kill)
    
lb = tk.Label(text = f'{user}', font = ('Courier', '22'))
lb.pack()
root.mainloop()
