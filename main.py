from turtle import Turtle, Screen
import random
from random import randint

t = Turtle()
t.shape("arrow")
t.color("green")
t.width(2)

screen = Screen()
screen.bgcolor("#F2EFDE")

# Generate random custom colours --start
color = []
n = 10
for i in range(n):
    color.append('#%06X' % randint(0, 0xFFFFFF))
# Generate random custom colours --end

direction = [0, 90, 180, 270]
turtle_movement = random.randint(0, 100)
turtle_angle = random.randint(0, 360)

for number in range(200):
    t.color(random.choice(color))
    t.width(4)
    t.forward(30)
    t.setheading(random.choice(direction))

screen.exitonclick()