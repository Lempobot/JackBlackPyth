#Deck class.

import Cards
from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck:


    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.new_card = Cards(suit, rank)
                self.deck.append(self.new_card)

    def shuffle(self):
       shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()