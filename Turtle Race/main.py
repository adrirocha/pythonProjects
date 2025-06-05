from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", 
                 prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "blue", "yellow", "orange", "green", "purple"]
y_increment = -100
all_turtles = []
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_increment)
    y_increment += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} is the winner!")
            else:
                print(f"You've lost! the {winning_color} is the winner!")
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()
