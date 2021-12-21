from turtle import Turtle, xcor

class Paddle(Turtle):
    def __init__(self, initial_position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len = 1, stretch_wid=5)
        self.penup()
        self.goto(initial_position)

    def move_up(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(),new_y)
    
    def move_down(self):
        new_y = self.ycor() -20
        self.goto(self.xcor(), new_y)