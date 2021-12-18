from turtle import Turtle, onkey
import turtle


class Snake():

    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        def create_turtle(new_turtle):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            return new_turtle

        for x in self.starting_positions:
            tim = create_turtle(x)
            tim.penup()
            tim.goto(x)
            self.segments.append(tim)
        self.head = self.segments[0]
    
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
    
    def up(self):
        if self.head.heading() != 270:
           self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
           self.head.setheading(270)

