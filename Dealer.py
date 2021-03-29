#The dealer class

#The dealer is a computer.

#Dealer deals the cards and plays along with the player.

import Deck

class Dealer:
    def __init__(self):
        self.cards = []
        self.hand_value = 0

    def draw_card(self, card):
        self.cards.append(card)

    def hand(self):