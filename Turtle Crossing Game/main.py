from turtle import Turtle, Screen
from time import sleep
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)

    car_manager.generate_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    
    # Detect win
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.update_score()
        car_manager.car_move_increment()








screen.exitonclick()
