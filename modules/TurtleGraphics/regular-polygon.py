from string import hexdigits
from turtle import Turtle, Screen
from random import choice

# create a turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()


# generate random_color_string
def get_random_color():
    color_string = ['#']
    for _ in range(6):
        color_string.append(choice(hexdigits))
    return "".join(color_string)


def draw_regular_polygon(num_sides):
    jerry.color(get_random_color())
    angle = 360 / num_sides
    for _ in range(num_sides):
        jerry.forward(100)
        jerry.right(angle)


def move_turtle_position(xcor, ycor):
    jerry.hideturtle()
    jerry.penup()
    jerry.goto(xcor, ycor)
    jerry.pendown()
    jerry.showturtle()


def draw_pattern():
    move_turtle_position(-100, 200)
    jerry.speed(0)
    for polygon_side in range(12, 5, -1):
        jerry.begin_fill()
        draw_regular_polygon(polygon_side)
        jerry.end_fill()
    jerry.hideturtle()


draw_pattern()
screen.exitonclick()
