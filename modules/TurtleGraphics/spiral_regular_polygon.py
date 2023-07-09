from turtle import Turtle, Screen
from string import hexdigits
from random import choice


def draw_pattern(n_sides):
    jerry = Turtle()
    jerry.speed("fastest")

    # generate random_color_string
    def get_random_color():
        color_string = []
        for _ in range(6):
            color_string.append(choice(hexdigits))
        return "#" + "".join(color_string)

    # get random_colors for regular polygon of n_sides
    colors = [get_random_color() for _ in range(n_sides)]
    angle = (360 / n_sides) + 1
    jerry.hideturtle()

    draw_number_of_times = 180
    # print(jerry.width())
    for i in range(draw_number_of_times):
        pen_width = (i * n_sides) / (2 * draw_number_of_times)
        side_length = i + (i * 3) / n_sides
        jerry.pencolor(colors[i % n_sides])
        jerry.forward(side_length)
        jerry.left(angle)
        jerry.width(pen_width)
        # print(jerry.width())

    # create a turtle screen
    screen = Screen()
    screen.exitonclick()


if __name__ == '__main__':
    draw_pattern(n_sides=3)
