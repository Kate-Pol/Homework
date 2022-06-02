import tkinter as tk

w = 200
h = 200

rt1 = tk.Tk()
rt1.geometry(f'{w}x{h}+0+0')

rt2 = tk.Tk()
rt2.geometry(f'{w+30}x{h+30}+0-0')

rt3 = tk.Tk()
rt3.geometry(f'{w+50}x{h+50}-0+0')

rt4 = tk.Tk()
rt4.geometry(f'{w+70}x{h+70}-0-0')

rt1.mainloop()
