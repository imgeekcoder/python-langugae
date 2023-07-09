import turtle

# create a turtle screen
screen = turtle.Screen()

# create a turtle on screen
jerry = turtle.Turtle()

screen.bgcolor('white')
jerry.pencolor('black')

jerry.hideturtle()
jerry.speed(0)
# tracer to draw
turtle.tracer(n=2, delay=10)


def shift_turtle_position(x_position, y_position):
    jerry.penup()
    # print(x_position, y_position)
    jerry.goto(x_position, y_position)
    jerry.pendown()


def draw_square(width, fill_color):
    jerry.fillcolor(fill_color)
    jerry.begin_fill()
    for _ in range(4):
        jerry.forward(width)
        jerry.left(90)
    jerry.end_fill()


def draw_single_chess_row(width, number_of_columns, direction):
    # draw square for each column
    for i in range(number_of_columns):
        if i % 2 == 0:
            draw_square(width, 'white')
        else:
            draw_square(width, 'black')

        # move turtle to draw next square
        jerry.penup()
        if direction == 'forward':
            jerry.forward(width)
        else:
            jerry.backward(width)
        jerry.pendown()


def draw_chessboard(number_of_rows, number_of_columns, width):
    # position turtle to make centered-chessboard
    x_position = (number_of_rows // 2) * width
    y_position = (number_of_columns // 2) * width

    for i in range(number_of_rows):
        if i % 2 == 0:
            # for drawing even chessboard rows
            shift_turtle_position(-x_position, -y_position)
            draw_single_chess_row(width=width, number_of_columns=number_of_columns, direction='forward')
        else:
            # for drawing odd chessboard rows
            shift_turtle_position(-x_position + (number_of_rows - 1) * width, -y_position)
            draw_single_chess_row(width=width, number_of_columns=number_of_columns, direction='backward')

        # update to draw next row of chessboard
        y_position -= width


if __name__ == '__main__':
    draw_chessboard(number_of_rows=8, number_of_columns=8, width=79)

screen.exitonclick()
