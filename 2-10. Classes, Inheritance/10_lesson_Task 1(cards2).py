import random

nominal = ['A','K','Q','J','2','3','4','5','6','7','8','9','10']
suite = ['Heart', 'Club', 'Spade', 'Diamond']


class Card:
    def __init__(self, nominal, suite):
        self.nominal = nominal
        self.suite = suite
        
    def nice(self):
		return nominal[self.nominal], suite[self.suite]
		
class Hand:
	def __init__(self):
		self.hand = []
		self.set()
		
	def set(self):
		for i in range(len(suite)):
			for j in range(len(nominal)):
				self.hand.append(Card[i, j])
				
	
	def show(self):
		print(len(self.hand))
		for i in self.hand:
			print(i.nice(), end = ' ')
			
	def shuffle(self):
		random.shuffle(self.hand)
		
	def get_card(self):
		k = self.hand.pop()
		print k
		
		
h = Hand()
h.show()
print('----')
h.shuffle()
h.show()
player = []
for i in range(10) 
	player.append(h.get_card())
print('\n\n')
for card in player:
	print(card.nice())
h.show()
