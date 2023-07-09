from turtle import Turtle, Screen
from random import randint, choice
from string import hexdigits

# create turtle screen
screen = Screen()
screen.colormode(255)


# generate random_color
def gen_rand_color():
    color_string = []
    for _ in range(6):
        color_string.append(choice(hexdigits))
    return '#' + ''.join(color_string)


def get_position_string(position):
    position_string = ''
    if position == 1:
        position_string = 'First'
    elif position == 2:
        position_string = 'Second'
    elif position == 3:
        position_string = 'Third'
    elif position == 4:
        position_string = 'Fourth'
    elif position == 5:
        position_string = 'Fifth'
    elif position == 6:
        position_string = 'Sixth'
    return position_string


screen_width = 600
screen_height = 400
screen.setup(width=screen_width, height=screen_height)

initial_turtle_xcor = screen_width / 2
initial_turtle_ycor = screen_height / 2

turtles = []
for _ in range(6):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(gen_rand_color())
    new_turtle.hideturtle()
    # new_turtle.speed('fastest')
    new_turtle.penup()
    new_turtle.goto(-initial_turtle_xcor + 40, -initial_turtle_ycor + 40)
    new_turtle.showturtle()
    initial_turtle_ycor -= 60
    turtles.append(new_turtle)

# print(turtles)
is_game_on = True
while is_game_on:
    for turtle in turtles:
        r_distance = randint(0, 10)
        turtle.forward(r_distance)

    index = 0
    for turtle in turtles:
        if turtle.xcor() > (screen_width / 2 - 20):
            print(f'{get_position_string(index + 1)} turtle has won the race!')
            is_game_on = False
        index += 1

screen.exitonclick()
