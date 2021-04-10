##The player class

#The player is a human.

import Deck

class Player:
    def __init__(self):
        self.cards = []
        self.hand_value = 0
        self.aces = 0

    def draw_card(self, card):
        # card passed from Deck.deal_card()
        self.cards.append(card)
        self.hand_value += card.value

        if card.rank is 'Ace':
            self.aces += 1

    def change_ace(self):

        #if the hand is more than 21, it is logical to choose ace as 1.
        while self.hand_value > 21 and self.aces:
            self.hand_value -= 10
            self.aces -= 1

    def is_empty(self):
        if self.cards is []:
            return True
        else:
            return False



    #Shows the hand of the dealer.
    def __str__(self):
        for card in self.cards:
            print(card)