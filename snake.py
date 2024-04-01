import turtle
import time
from score import Score


screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Classic snake game")
screen.tracer(0)



class Snake:
    def __init__(self):
        self.starting_pos = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []



    def create_snake(self):
        for pos in self.starting_pos:
            self.add_segment(pos)

    def move_forward(self):
            for segment_number in range(len(self.segments)-1, 0, -1):
                next_x = self.segments[segment_number - 1].xcor()
                next_y = self.segments[segment_number - 1].ycor()
                self.segments[segment_number].goto(next_x, next_y)
            self.segments[0].forward(20)
            screen.update()
            time.sleep(.1)

    def dir_right(self):
         
        if (self.segments[0].heading() != 180):
            self.segments[0].seth(0)
        else:
             pass

        #  self.segments[0].forward(20)

    def dir_left(self):
        if (self.segments[0].heading() != 0):
            self.segments[0].seth(180)
        else:
            pass
        #  self.segments[0].forward(20)


    def dir_up(self):
        if (self.segments[0].heading() != 270):
            self.segments[0].seth(90)
        else:
            pass
        # self.segments[0].forward(20)


    def dir_down(self):
        if (self.segments[0].heading() != 90):
            self.segments[0].seth(270)
        else:
            pass
        #  self.segments[0].forward(20)

    def add_segment(self, pos):
        segment = turtle.Turtle("square")
        segment.penup()
        segment.color("green")
        segment.goto(pos)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def end(self):
        for segment in self.segments:
            segment.hideturtle()

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
