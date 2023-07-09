from turtle import Turtle, Screen

# create a turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()


# draw a square logic
def draw_circle():
    jerry.circle(radius=75)


# draw a pattern
def draw_pattern():
    angle, movement_angle = 0, 10
    while angle <= 360:
        draw_circle()
        jerry.left(movement_angle)
        angle += movement_angle


# call draw_pattern function
jerry.speed(0)
draw_pattern()
screen.exitonclick()
