#Bank class

#Stores data on the balance of the player adn house.

class Bank:
    def __init__(self, sum_player, sum_house):
        self.sum_player = sum_player
        self.sum_dealer = sum_house

    def bet_sum(self, bet_sum):

        while self.sum_player - bet_sum < 0:
            print("You don't have enough chips for that bet, your sum is {}".format(self.sum_player))
            bet_sum = int(input())
        self.sum_player -= bet_sum

    def if_win(self, amount):
        self.sum_player += amount