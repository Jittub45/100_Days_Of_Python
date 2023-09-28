import random
from turtle import Turtle, Screen

tim = Turtle()
tim.setheading(120)
tim.penup()
tim.forward(150)
tim.setheading(0)
tim.pendown()

colours = ["CornflowerBlue",  "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def shape(numbers_of_side):
    angle = 360 / numbers_of_side
    tim.color(random.choice(colours))
    for _ in range(numbers_of_side):
        tim.width(2)
        tim.speed(10)
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    shape(i)

my_screen = Screen()
# my_screen.exitonclick()
