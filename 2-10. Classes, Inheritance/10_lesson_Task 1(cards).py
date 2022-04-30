import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        self.deck_cards = [] #list of dictionaries
    
    def deck_build(self):
        suit_lst = ['Heart', 'Club', 'Spade', 'Diamond']
        rank_lst = ['A','K','Q','J','2','3','4','5','6','7','8','9','10']
        for suit in range(len(suit_lst)):
            for rank in range(len(rank_lst)):
                self.cards.append(Card[suit, rank])  #have in total 4 suites(hearts, clubs, spades, diamonds), 
                                            # and thirteen values(A, K, Q, J, 2, 3, 4, 5, 6, 7, 8, 9, 10)
                                             
    def get_deck_of_cards(self):
        for crd in self.deck_cards:
            if crd['suit'] in self.deck_cards and crd['value'] in self.deck_cards:
                return crd
        else:
            raise ValueError('do not have this card in the deck')
        
    def shuffle_deck(self):
        for i in range(len(self.deck_cards)):
            c = random.randint(0, i)
            self.cards[i], self.cards[c] = self.cards[c], self.cards[i]
    
    def del_card(self, card):
        for i in enumerate(self.deck_cards):
            self.deck_cards.pop(i)
            break
        else: 
            raise ValueError('do not have this card in the deck')
                       
    def show_how_many_cards(self):
        for i in self.deck_cards:
            for j in self.deck_cards:
                print(i, j)
        return self.deck_cards
                                                            
c = Card('Heard', 'A')
d = Deck()

d.deck_build()                                                       
                                                       
                                                        