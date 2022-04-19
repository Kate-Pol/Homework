def forward(n):
	i = 0
	while i < n: 
		i += 1
		print(i, '!!!', i, '!!!')
	
def backward(n):
	i = n
	while i <= n and i > 0:
		i -= 1
		print(i, '///', i, '///')
	
def voice(say):
	print(say, '!!!', say, '!!!')
