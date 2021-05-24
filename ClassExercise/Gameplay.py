# The core game logic

import Bank
from Cards import Cards
import Dealer
from Deck import Deck
import Player
import random


def take_bet():
    try:
        bank.bet_sum(int(input("How much chips do you want to deposit? "
                               "you have {} chips".format(bank.sum_player))))
    except TypeError:
        print("You need to enter integers")


def hit(deck, player):
    single_card = deck.deal_card()
    player.draw_card(single_card)
    player.change_ace()


def hit_or_stand(deck, player):
    global game

    while True:
        choice = input("Do you want to hit or pass? Input H for 'hit' and P for 'pass'")
        choice.upper()
        if choice[0] == 'H':
            hit(deck, player)
        elif choice[0] == 'P':
            print("Player stands, dealer is playing")
            game = False
        else:
            print("Please enter 's' or 'p' only")
            continue
        break


def show_some(dealer, player):
    # Show only one card of the dealr's hand
    print("\n Dealer's Hand: frist card hidden!")
    print(dealer.cards[1])
    # Show all cards of the player's hand
    print("\nPlayer's hand: ")
    for card in player.cards:
        print(card)


def show_all(dealer, player):
    # show all dealer's cards
    print("\nDealer's hand: ", *dealer.cards, sep=' ')

    # calc value and display
    print(f"Value of dealer's hand is: {dealer.hand_value}")
    # show all the player's cards
    print("\nPlayer's hand: ", *player.cards, sep=' ')

    print(f"Value of player's hand is: {player.hand_value}")


def player_busts(player, dealer, bank):
    print('Bust Player!')


def player_wins(player, dealer, bank):
    print('Player Wins')


def dealer_busts(player, dealer, bank):
    print('Bust Dealer')


def dealer_wins(player, dealer, bank):
    print('Dealer Wins')


def push(player, dealer):
    print('Dealer and player tie! PUSH!')


while True:
    # Openning statement

    print("W E L C O M E  T O  B L A C K J A C K")
    deck = Deck()
    deck.shuffle_deck()
    player = Player.Player()
    dealer = Dealer.Dealer()
    bank = Bank.Bank(500, 500)
    # if the player or dealer have no cards, they will draw 2 cards each.
    if player.is_empty() == True:
        for i in range(2):
            player.draw_card(deck.deal_card())

    if dealer.is_empty() == True:
        for i in range(2):
            dealer.draw_card(deck.deal_card())
    while game:  # from hit_or_stand func
        # ask the player if he wants to hit or stand
        hit_or_stand(deck, player)

        # shows the cards.
        show_some(dealer, player)

        # if players hand exceeds 21, run player_bust and break
        if player.hand_value > 21:
            player_busts(player, dealer, bank.sum_player)
            break

    if player <= 21:
        while dealer.hand_value < 17:
            hit(deck, dealer_hand)
        show_all(dealer, player)
        if dealer.hand_value > 21:
            dealer_busts(player, dealer, bank.sum_player)
        elif dealer.hand_value > player.hand_value:
            dealer_wins(player, dealer, bank.sum_player)
        elif dealer.hand_value < player.hand_value:
            player_wins(player, dealer, bank.sum_player)
        else:
            push(player, dealer)

    print('\n Player total chips are at: {}'.format(bank.sum_player))

    new_game = input("Would you like another game?")

    if new_game.upper() == 'Y':
        game = True
        continue
    if new_game.upper() == 'N':
        print("Thank you for playing.")
        break
