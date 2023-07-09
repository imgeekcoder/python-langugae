from turtle import Turtle, Screen

jerry = Turtle()
jerry.speed("fastest")
jerry.hideturtle()


def draw_pattern(n_sides, number_of_times):
    for i in range(number_of_times):
        side_length = i + (i * 3) / n_sides
        jerry.forward(side_length)
        jerry.dot(15)
        jerry.left(((2 * number_of_times) / n_sides) + 1)

    # create a turtle screen
    screen = Screen()
    screen.exitonclick()


if __name__ == '__main__':
    draw_pattern(n_sides=4, number_of_times=100)
