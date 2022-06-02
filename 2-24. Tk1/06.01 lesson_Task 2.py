import tkinter as tk

root = tk.Tk()
root.title('I am a central platform')
root.geometry('300x300+500+200')

w = 200
h = 200

rt1 = tk.Tk()
rt1.geometry(f'{w}x{h}+0+0')

rt2 = tk.Tk()
rt2.geometry(f'{w}x{h}+0-0')

rt3 = tk.Tk()
rt3.geometry(f'{w}x{h}-0+0')

rt4 = tk.Tk()
rt4.geometry(f'{w}x{h}-0-0')

root.mainloop()
