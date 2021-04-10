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
        self.hand_value += card.value

    def is_empty(self):
        if self.cards is []:
            return True
        else:
            return False

    #Shows the hand of the dealer.
    def __str__(self):
        for card in self.cards:
            print(card)