import tkinter
import random

#number dice
def dice():
	while True: 
		inp = input('Lete play the game? yes or no (y or n): ')
		if inp == 'y' or inp == 'Y':
			x = random.randint(1,6)
			print(x)
		elif inp == 'n' or inp == 'N':
			print('game is over')
			break

# graph dice
def roll():
	root = tkinter.Tk()
	root.geometry('400x400')

	lable = tkinter.Label(root,font=("Helvetica",260))

	def roll_dice():
		dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
		result = random.choice(dice)
		lable.configure(text=result)
		lable.pack()
		
	button=tkinter.Button(root,text="Roll the Dice!",foreground='blue',command=roll_dice)
	button.pack()

	root.mainloop()
