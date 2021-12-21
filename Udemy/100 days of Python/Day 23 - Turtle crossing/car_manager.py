COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from random import randint, choice
from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(choice(COLORS))
        self.goto(300, randint(-300, 300))
        self.setheading(180)    
        
    def move(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())
