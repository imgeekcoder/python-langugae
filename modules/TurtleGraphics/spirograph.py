from turtle import Turtle, Screen
from random import choice
from string import hexdigits

# create turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()

jerry.speed('fastest')


def random_color():
    color_array = []
    for _ in range(6):
        color_array.append(choice(hexdigits))
    return "#" + "".join(color_array)


def draw_spirograph(radius, size_of_gap):
    for _ in range(360 // size_of_gap):
        jerry.color(random_color())
        jerry.circle(radius)
        jerry.setheading(jerry.heading() + size_of_gap)


draw_spirograph(radius=100, size_of_gap=5)
screen.exitonclick()
