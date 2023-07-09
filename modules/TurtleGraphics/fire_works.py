from turtle import Turtle, Screen
from string import hexdigits
from random import randint, choice

# create a turtle screen
screen = Screen()

# create a turtle on screen
jerry = Turtle()

screen.title('Fire Works')
screen.bgcolor('#222222')

# hide drawing turtle
jerry.hideturtle()
jerry.speed(0)


def draw_star(x_pos, y_pos, size_of_star):
    # goto specified position
    jerry.penup()
    jerry.goto(x_pos, y_pos)
    jerry.pendown()

    # draw 5-sided-star at current_position
    jerry.color('#ffffff')
    for _ in range(5):
        jerry.forward(size_of_star)
        jerry.backward(size_of_star)
        jerry.right(72)


# generate random_color
def gen_rand_color():
    color_string = []
    for _ in range(6):
        color_string.append(choice(hexdigits))
    return '#' + ''.join(color_string)


# draw a firework
def draw_fire_work(x_pos, y_pos, intensity_of_firework):
    # goto specified position
    jerry.penup()
    jerry.goto(x_pos, y_pos)
    jerry.pendown()

    # draw a firework at current_position
    for _ in range(36):
        jerry.forward(intensity_of_firework)
        jerry.backward(intensity_of_firework)
        jerry.right(10)


def draw_fireworks_in_night(number_of_stars, number_of_fireworks):
    # generate random stars
    for _ in range(number_of_stars):
        size_of_star = randint(2, 8)

        # get random position
        x = randint(-screen.window_width() // 2 + size_of_star, screen.window_width() // 2 - size_of_star)
        y = randint(-screen.window_height() // 2 + size_of_star, screen.window_height() // 2 - size_of_star)

        draw_star(x, y, size_of_star)

    # generate random-colored fireworks
    for _ in range(number_of_fireworks):
        size_of_firework = randint(20, 150)
        # get random position
        x = randint(-screen.window_width() // 2 + size_of_firework,
                    screen.window_width() // 2 - size_of_firework)
        y = randint(-screen.window_height() // 2 + size_of_firework,
                    screen.window_height() // 2 - size_of_firework)
        jerry.color(gen_rand_color())
        # jerry.color(random.choice(['red', 'green', 'yellow', 'pink']))
        draw_fire_work(x, y, size_of_firework)


draw_fireworks_in_night(number_of_fireworks=17, number_of_stars=23)
screen.exitonclick()
