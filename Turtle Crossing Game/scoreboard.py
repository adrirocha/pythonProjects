from turtle import Turtle

FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-285, 270)
        self.level = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", font=FONT)
