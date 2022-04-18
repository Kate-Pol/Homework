import math

x = int(input('please enter square side: '))

def square(x):
	per = x * 4
	area = x ** 2
	diag = math.sqrt(2) * x
	square_dim = (per, area, diag)
	return square_dim
	
print(square(x))
	
