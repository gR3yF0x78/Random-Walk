import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("arrow")
tim.color("green")
tim.pensize(12)
tim.speed("fast")

screen = Screen()
screen.colormode(0)
screen.bgcolor("#0a0a0a")

# Generate random custom colours --start
# color = []
# n = 10
# for i in range(n):
#     color.append('#%06X' % randint(0, 0xFFFFFF))
# Generate random custom colours --end

# Generate random RGB --start
def random_rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
# Generate random RGB --end

direction = [0, 90, 180, 270]

for number in range(200):
    tim.color(random_rgb_color())
    tim.width(4)
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen.exitonclick()