import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
tim.hideturtle()
color_list = [(251, 238, 16), (205, 11, 34), (237, 226, 6), (47, 78, 177), (29, 39, 154), (215, 75, 12), (15, 220, 95), (15, 154, 15), (208, 13, 9), (243, 34, 167), (230, 17, 125), (70, 10, 31), (59, 15, 8), (243, 161, 27), (11, 97, 62), (48, 214, 230), (18, 19, 43), (11, 227, 239), (236, 172, 7), (78, 209, 160), (113, 71, 197), (85, 233, 199), (217, 129, 157), (58, 233, 242), (4, 68, 42), (243, 159, 189)]
y_dot = 0
y_coordinate = 30
count = True
while count:
    for _ in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot(15)
        tim.penup()
        tim.forward(30)

    tim.goto(0, y_coordinate)
    y_coordinate += 30
    y_dot += 1
    if y_dot == 10:
        count = False








screen = Screen()
screen.exitonclick()