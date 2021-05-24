#Bank class

#Stores data on the balance of the player adn house.

class Bank:
    def __init__(self, sum_player=100, sum_house=100):
        self.sum_player = sum_player
        self.sum_dealer = sum_house

    def bet_sum(self, bet_sum):

        while self.sum_player - bet_sum < 0:
            try:
                bet_sum = int(input("You don't have enough chips for that bet, your sum is {}".format(self.sum_player)))
            except TypeError:
                print("You need to enter integers")
        self.sum_player -= bet_sum

    def if_win(self, amount):
        self.sum_player += amount