from random import randint

def set_difficulty(difficulty):
    """Just set the difficulty using the user's input."""
    if difficulty == "easy":
        return 10
    if difficulty == "hard":
        return 5

def check_number(guess, secret_number):
    """Do the check between the guess and the secret number"""
    
    # Global variables should be defined inside the function like this
    # otherwise there will be errors.
    global is_game_over
    global attempts
    
    if guess == secret_number:
        print(f"You win! The secret number is {secret_number}")
        is_game_over = True
    else:
        attempts -= 1
        if not attempts:
            print("You've run out of guesses, you lose.")
            is_game_over = True
        if guess > secret_number:
            print(f"Too high.")
        else:
            print(f"Too low.")
        print("Guess again.")
        return attempts

is_game_over = False
attempts = -1

print(f"Welcome to the Number Guessing Game")
print(f"I'm thinking of a number between 1 and 100")
secret_number = randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = set_difficulty(difficulty)

while not is_game_over:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    check_number(guess, secret_number)





