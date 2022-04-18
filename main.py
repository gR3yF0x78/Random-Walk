from turtle import Turtle, Screen
import random
from random import randint

t = Turtle()
t.shape("arrow")
t.color("green")
t.pensize(12)
t.speed("fast")

screen = Screen()
screen.bgcolor("#0a0a0a")

# Generate random custom colours --start
color = []
n = 10
for i in range(n):
    color.append('#%06X' % randint(0, 0xFFFFFF))
# Generate random custom colours --end

direction = [0, 90, 180, 270]

for number in range(200):
    t.color(random.choice(color))
    t.width(4)
    t.forward(30)
    t.setheading(random.choice(direction))

screen.exitonclick()