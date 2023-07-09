from turtle import Turtle, Screen

# create a turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()


# draw a square logic
def draw_circle(radius):
    jerry.circle(radius=radius)


# draw a pattern
def draw_pattern(radius, movement_angle, color):
    angle = 0
    jerry.color(color)
    while angle <= 360:
        jerry.begin_fill()
        draw_circle(radius=radius)
        jerry.left(movement_angle)
        angle += movement_angle
        jerry.end_fill()


def draw_icecream_top():
    radius, movement_angle = 100, 25
    color = ['coral', 'yellow', 'orange', 'red']
    for i in range(4):
        draw_pattern(
            radius=radius,
            movement_angle=movement_angle,
            color=color[i]
        )
        radius -= 25
        movement_angle -= 5


# call draw_pattern function
jerry.speed(0)
draw_icecream_top()
screen.exitonclick()
