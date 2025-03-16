import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
limit = 21

"""
This was my first blackjack that i ever made, so it doesnt has some features that are in the 'pro_blackjack.py'
like computer's playing after the user, the compare() function and other stuffs.
"""

def calculation(my_cards, computer_cards):
    print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}\n")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n")
    if sum(my_cards) > limit:
        print('You lose')

def keep(my_cards, computer_cards):
    print(f"Your cards: {my_cards}, current score: {sum(my_cards)}\n")
    print(f"Computer's first card: {computer_cards[0]}\n")

def blackjack():
    while True:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play == 'y':
            my_cards = [random.choice(cards), random.choice(cards)]
            computer_cards = [random.choice(cards), random.choice(cards)]
            keep(my_cards=my_cards, computer_cards=computer_cards)
            while True:
                if sum(my_cards) == 21:
                    calculation(my_cards=my_cards, computer_cards=computer_cards)
                    print('You won!')
                    break
                elif sum(my_cards) > 21:
                    calculation(my_cards=my_cards, computer_cards=computer_cards)
                    break
                choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if choice == 'y':
                    my_cards.append(random.choice(cards))
                    computer_cards.append(random.choice(cards))
                    keep(my_cards=my_cards, computer_cards=computer_cards)
                else:
                    calculation(my_cards=my_cards, computer_cards=computer_cards)
                    if sum(my_cards) == sum(computer_cards):
                        print('Draw!')
                    break
        else:
            break
blackjack()


