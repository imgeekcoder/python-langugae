from turtle import Turtle, Screen
import random

# create a turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()

screen.title('Scribble Art')
screen.bgcolor('#606C5D')

jerry.speed(0)
screen_width = screen.window_width()
screen_height = screen.window_height()

number_of_scribble_dot = 100
for _ in range(number_of_scribble_dot):
    # generate random position
    x_coordinate_position = random.randint(-screen_width // 2, screen_width // 2)
    y_coordinate_position = random.randint(-screen_height // 2, screen_height // 2)

    # move turtle to random position
    jerry.goto(x_coordinate_position, y_coordinate_position)

    # make a dot at that random position
    jerry.dot(20, '#F1C376')

screen.exitonclick()
