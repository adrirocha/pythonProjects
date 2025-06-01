import turtle as t
from random import choice

# import colorgram

# rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colorgram.extract('image.jpg', 20)]

color_list = [(140, 22, 67), (77, 107, 190), (142, 151, 43), 
 (235, 211, 82), (218, 164, 56), (110, 151, 220), 
 (232, 205, 218), (60, 128, 64), (178, 68, 142), 
 (3, 67, 152), (207, 105, 56), (152, 99, 66), 
 (149, 37, 36), (230, 177, 202), (45, 81, 166), 
 (183, 79, 145), (193, 141, 169)]

t.colormode(255)
singleton = t.Turtle()
singleton.speed("fastest")
singleton.penup()
singleton.hideturtle()
x=-220
y=-220
singleton.setposition(x, y)
for i in range(10):
    for j in range(10):
        singleton.dot(20, choice(color_list))
        singleton.forward(50)
    y+=50
    singleton.setposition(x, y)


screen = t.Screen()
screen.exitonclick()
