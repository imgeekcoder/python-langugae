from turtle import Turtle, Screen

# create a turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()
jerry.speed(0)
jerry.hideturtle()


# shift turtle's origin
def shift_origin_turtle(xcor, ycor):
    jerry.penup()
    jerry.goto(xcor, ycor)
    jerry.pendown()


shift_origin_turtle(-150, 0)
for _ in range(15):
    jerry.forward(10)
    jerry.penup()
    jerry.forward(10)
    jerry.pendown()

screen.exitonclick()
