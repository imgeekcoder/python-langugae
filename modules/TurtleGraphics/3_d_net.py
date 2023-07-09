from turtle import Turtle, Screen

# create a turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()

screen.title('3D Art')

jerry.speed(0)
jerry.color('#F24C3D')

number_of_lines_to_draw = 35
interval_between_lines = 10


# draw a straight line
def draw_line(x_from, y_from, x_to, y_to):
    jerry.penup()
    jerry.goto(x_from, y_from)
    jerry.pendown()
    jerry.goto(x_to, y_to)


def draw_in_quadrant(quadrant):
    if quadrant == 1:
        # start position of line
        x_from = 0
        y_from = number_of_lines_to_draw * interval_between_lines

        # end position of line
        y_to = 0
        x_to = 0

        for _ in range(number_of_lines_to_draw):
            draw_line(x_from=x_from, y_from=y_from, x_to=x_to, y_to=y_to)
            x_to += interval_between_lines
            y_from -= interval_between_lines
    elif quadrant == 4:
        # start position of line
        x_from = number_of_lines_to_draw * interval_between_lines
        y_from = 0

        # end position of line
        x_to = 0
        y_to = 0

        for _ in range(number_of_lines_to_draw):
            draw_line(x_from=x_from, y_from=y_from, x_to=x_to, y_to=y_to)
            x_from -= interval_between_lines
            y_to -= interval_between_lines
    elif quadrant == 3:
        # start position of line
        x_from = 0
        y_from = -number_of_lines_to_draw * interval_between_lines

        # end position of line
        x_to = 0
        y_to = 0

        for _ in range(number_of_lines_to_draw):
            draw_line(x_from=x_from, y_from=y_from, x_to=x_to, y_to=y_to)
            x_to -= interval_between_lines
            y_from += interval_between_lines
    else:
        # start position of line
        x_from = -number_of_lines_to_draw * interval_between_lines
        y_from = 0

        # end position of line
        x_to = 0
        y_to = 0
        for _ in range(number_of_lines_to_draw):
            draw_line(x_from=x_from, y_from=y_from, x_to=x_to, y_to=y_to)
            x_from += interval_between_lines
            y_to += interval_between_lines


if __name__ == '__main__':
    for _ in range(4):
        draw_in_quadrant(_ + 1)
    jerry.hideturtle()
screen.exitonclick()
