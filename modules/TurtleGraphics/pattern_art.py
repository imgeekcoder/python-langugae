from turtle import Turtle, Screen

# create a turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()
screen.bgcolor('#C4DFDF')
jerry.pencolor('#F24C3D')


# draw polygon shape
def draw_polygon_shape(number_of_sides, length_of_shape):
    for _ in range(number_of_sides):
        jerry.forward(length_of_shape)
        jerry.left(360 // number_of_sides)


# draw polygon pattern
def draw_pattern(number_of_sides, length_of_shape, tilt_angle=15):
    for _ in range(360 // tilt_angle):
        draw_polygon_shape(number_of_sides=number_of_sides, length_of_shape=length_of_shape)
        jerry.left(tilt_angle)


# generate polygon pattern
draw_pattern(number_of_sides=5, length_of_shape=100, tilt_angle=180)
screen.exitonclick()
