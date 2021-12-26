from turtle import Turtle, onkey, position
import turtle


class Snake():

    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in self.starting_positions:
            tim = self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)    
    
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range (len(self.segments) -1, 0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != 0:
           self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
           self.head.setheading(0)
    
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    
    def up(self):
        if self.head.heading() != 270:
           self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
           self.head.setheading(270)

