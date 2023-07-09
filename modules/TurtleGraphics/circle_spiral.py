from turtle import Turtle, Screen

# create a turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()
jerry.speed(0)
jerry.color('green')


def draw_spirograph(radius, size_of_gap):
    for _ in range(360 // size_of_gap):
        jerry.circle(radius)
        jerry.setheading(jerry.heading() + size_of_gap)


def draw_pattern():
    radius = 0
    for _ in range(7):
        radius += 20
        draw_spirograph(radius=radius, size_of_gap=10)
    jerry.hideturtle()


draw_pattern()
screen.exitonclick()
