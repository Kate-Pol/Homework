import tkinter as tk
import pult


root = tk.Tk()
root. title('TV Controller')
root.geometry('500x500')

    

fr = tk.Frame(root, width = 1200, height = 1200, border = 5, relief = 'raised')
fr.grid()

bt_start = tk.Button(fr, text = '  START  ', background = '#C7C7C7')
bt_start.grid(column = 3, row = 1)

bt_menu = tk.Button(fr, text = '  MENU  ', background = '#C7C7C7', command = lambda: pult.controller.print_menu())
bt_menu.grid(column = 3, row = 3)

bt_1 = tk.Button(fr, text = 'FIRST CHANNEL', background = '#C7C7C7', command = lambda: pult.controller.first_channel())
bt_1.grid(column = 1, row = 5)
bt_3 = tk.Button(fr, text = 'LAST CHANNEL', background = '#C7C7C7', command = lambda: pult.controller.last_channel())
bt_3.grid(column = 5, row = 5)

bt_prev = tk.Button(fr, text = '  <--  ', background = '#C7C7C7', command = lambda: pult.controller.previous_channel())
bt_prev.grid(column = 1, row = 7)
bt_cur = tk.Button(fr, text = 'CURRENT CHANNEL', background = '#C7C7C7', command = lambda: pult.controller.current_channel())
bt_cur.grid(column = 3, row = 7)
bt_next = tk.Button(fr, text = '  -->  ', background = '#C7C7C7', command = lambda: pult.controller.next_channel())
bt_next.grid(column = 5, row = 7)

bt_search = tk.Button(fr, text = 'SEARCH', background = '#C7C7C7', command = lambda: pult.controller.turn_channel())
bt_search.grid(column = 3, row = 11)


root.mainloop()
