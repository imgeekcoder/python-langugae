from turtle import Turtle, Screen

# create a turtle screen
screen = Screen()
# create a turtle on the screen
jerry = Turtle()

jerry.speed(speed=0)

jerry.color('red', 'yellow')
jerry.begin_fill()
while True:
    jerry.forward(250)
    jerry.left(170)
    if abs(jerry.pos()) < 1:
        break
jerry.end_fill()
jerry.hideturtle()
screen.exitonclick()
