from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExczkxc2dhanQzcWM4a2txZzk4bmNvbXgzZTBoa2E3aXR0Nzg0YWF4diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Q7M2NziacKnSiSYHIt/giphy.gif">'

number_to_be_guessed = randint(0, 9)

@app.route("/<int:guess>")
def guessing_number(guess):
    if guess==number_to_be_guessed:
        return '<h1 style="color:green">You found me</h1>' \
               '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXB4Ymxqa2FpM3plZXJnNWpxdGRpZDJmaDI5bmZjMXd3ZGI5bWY3ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/e7Y2mRgPS7afrnoWz2/giphy.gif">'
    else:
        if guess > number_to_be_guessed:
            return '<h1 style="color:purple">Too high, try again!</h1>' \
                   '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaW1yYmJqcGp4bHZwaGZ5NnlndWd5b2Y5dmV2ZXg4dDdibjd2OXdyYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cPg419Or9TaglvbTAu/giphy.gif">'
        else:
            return '<h1 style="color:red">Too low, try again!</h1>' \
                   '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYW91M3R0cGY1azF0ZnM2cndhYW5qYWF2Mmo3enpvcWgyOWxoNXV0aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Pk8pcKvPrOkzA5rbQw/giphy.gif">'

if __name__ == "__main__":
    app.run(debug=True)
