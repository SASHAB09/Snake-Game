from turtle import *
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(.75, .75)
        self.color("red")
        self.speed(0)


    def reposition(self):
        r_x = random.randint(-280, 280)
        r_y = random.randint(-280, 280)
        self.goto(r_x, r_y)

    def end(self):
        self.hideturtle()