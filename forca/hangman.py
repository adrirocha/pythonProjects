import random

word_list = ['text', 'panther', 'airplane']

lives = 6

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += '_'

print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    
    print(f'You have {lives} lives')
    
    guess = input("\nGuess a later: ").lower()
    print(guess)

    if guess in correct_letters:
        print(f'You\'ve already guessed {guess}')
    
    display = ''

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    
    print('Word to guess: ' + display)


    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed {guess}, that\'s not in the word. You lose a life.\n')
        
        if lives == 0:
            game_over = True
            print('You lose.')
            print(f'It was {chosen_word}')

    if '_' not in display:
        game_over = True
        print('You win.')
    





