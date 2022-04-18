import random

def dice():
	while True: 
		inp = input('Lete play the game? yes or no (y or n): ')
		if inp == 'y' or inp == 'Y':
			x = random.randint(1,6)
			print(x)
		elif inp == 'n' or inp == 'N':
			print('game is over')
			break

print(dice())
