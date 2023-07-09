from turtle import Turtle, Screen

# create turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()


# screen.title("Python Turtle Graphics")
def move_forward():
    jerry.forward(10)


def move_backward():
    jerry.backward(10)


def turn_left_direction():
    new_heading = jerry.heading() + 10
    jerry.setheading(new_heading)


def turn_right_direction():
    new_heading = jerry.heading() - 10
    jerry.setheading(new_heading)


def clear_screen():
    jerry.clear()
    jerry.penup()
    jerry.home()
    jerry.pendown()


screen.listen()
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=turn_left_direction, key="a")
screen.onkey(fun=turn_right_direction, key="d")
screen.onkey(fun=clear_screen, key="c")
screen.exitonclick()
