from turtle import Turtle, Screen
from random import choice, randint

# create a turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()

# change color_mode
screen.colormode(255)

jerry.speed(0)
jerry.pensize(10)
jerry.hideturtle()


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return red, green, blue


direction = ['left', 'right', 'forward', 'backward']
# color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
#          "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for _ in range(360):
    move_in_direction = choice(direction)
    if move_in_direction == 'left':
        jerry.setheading(90)
    elif move_in_direction == 'right':
        jerry.setheading(270)
    elif move_in_direction == 'forward':
        jerry.setheading(0)
    elif move_in_direction == 'backward':
        jerry.setheading(180)
    jerry.color(random_color())
    jerry.forward(20)

screen.exitonclick()
