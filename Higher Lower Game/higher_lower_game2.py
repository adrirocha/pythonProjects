from random import choice
from game_data import profiles
"""This is a mini version of the higher_lower_game.py"""

def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score = 0
game = True

account_b = choice(profiles)

while game:
    
    account_a = account_b
    account_b = choice(profiles)
    if account_a == account_b:
        while account_a == account_b:
            account_b = choice(profiles)

    print(f"Compare A: {format_data(account_a)}")
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["level"]
    b_follower_count = account_b["level"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game = False



