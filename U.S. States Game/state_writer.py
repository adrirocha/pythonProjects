from turtle import Turtle

class StateWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, x, y, state_name):
        self.goto(x, y)
        self.write(f"{state_name}")
