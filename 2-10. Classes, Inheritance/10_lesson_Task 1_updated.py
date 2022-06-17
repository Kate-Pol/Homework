import random

nominal = ['A','K','Q','J', 2,3,4,5,6,7,8,9,10]
suite = ['Heart', 'Club', 'Spade', 'Diamond']

class Card:
    def __init__(self, nominal, suite):
        self.nominal = nominal
        self.suite = suite
        
    def __str__(self):
        return f'[{nominal[self.nominal]}:{suite[self.suite]}]'
        
    def __repr__(self):
        return f'({nominal[self.nominal]}:{suite[self.suite]})'
        
    def nice(self):
        return nominal[self.nominal], suite[self.suite]
        
class Hand:
    def __init__(self):
        self.hand = []
        self.set()
        
    def set(self):
        for i in range(len(suite)):
            for j in range(len(nominal)):
                self.hand.append(Card(j,i))
                
    
    def show(self):
        print(len(self.hand))
        for i in self.hand:
            print(i, end = ' ')
            
    def shuffle(self):
        random.shuffle(self.hand)
        
    def get_card(self):
        k = self.hand.pop()
        return k
    
    def __len__(self):
        n = len(self.hand)
        return n
        
    def __str__(self):
        f = 'cards: '
        for i in self.hand:
            f += str(i) + ' '
            f += '\n'
        return f
            
        
        
h = Hand()
print(h)

print('----')
h.shuffle()

print(h)

player = []
for i in range(10): 
    player.append(h.get_card())
print('\n\n')
print(player)
for card in player:
    print(card.nice())
h.show()

