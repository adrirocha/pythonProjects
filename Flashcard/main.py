BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
from random import choice

#-----------------FUNCTIONALITIES------------------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/korean_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

current_card = {}

# Flashcards Mechanism
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    
    current_card = choice(to_learn)
    flashcard.itemconfig(canvas_image, image=card_front_image)
    flashcard.itemconfig(lang_text, text="Korean", fill="black")
    flashcard.itemconfig(word_text, text=current_card['Korean'], fill="black")
    
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_card
    flashcard.itemconfig(canvas_image, image=card_back_image)
    flashcard.itemconfig(lang_text, text="English", fill="white")
    flashcard.itemconfig(word_text, text=current_card["English"], fill="white")


# Save Progress
def is_known():
    global current_card
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()


#---------------------------UI------------------------------

# Create Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas Flashcard
flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
canvas_image = flashcard.create_image(400, 263, image=card_front_image)
lang_text = flashcard.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = flashcard.create_text(400, 263, text="", font=("Arial", 60, "bold"))
flashcard.grid(row=0, column=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()


window.mainloop()
