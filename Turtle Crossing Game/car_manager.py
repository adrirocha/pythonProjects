from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_move_speed = STARTING_MOVE_DISTANCE
    
    def generate_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.goto(295, randint(-249, 249))
            self.cars.append(new_car)
    
    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_move_speed)
    
    def car_move_increment(self):
        self.car_move_speed += MOVE_INCREMENT
