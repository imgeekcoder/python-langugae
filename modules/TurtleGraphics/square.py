from turtle import Turtle, Screen

# create a turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()


# draw a square logic
def draw_square():
    for i in range(4):
        jerry.forward(100)
        jerry.left(90)


# draw a pattern
def draw_pattern():
    angle = 0
    while angle <= 360:
        draw_square()
        jerry.left(10)
        angle += 10


# call draw_pattern function
jerry.speed(0)
draw_pattern()
screen.exitonclick()
