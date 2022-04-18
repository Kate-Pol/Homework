def season(x):
	if x in range(1,3) or x == 12:
		return('it is winter season')
	elif x in range(3,6):
		return('it is spring season')
	elif x in range(6,9):
		return('it is summer season')
	elif x in range(9,12):
		return('it is autumn season')
		
x = int(input('enter number: '))

print(season(x))
