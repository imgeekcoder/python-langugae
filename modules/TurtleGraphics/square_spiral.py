from turtle import Turtle, Screen

# create a turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()
screen.bgcolor('#A6D0DD')
jerry.pencolor('#FF6969')
jerry.pensize(2)
jerry.hideturtle()

side = 1
for _ in range(37):
    jerry.forward(side)
    jerry.right(90)
    side += 10
screen.exitonclick()
