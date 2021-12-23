import turtle


FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.pencolor("black")
        self.goto(-200, 250)
        self.updated_scoreboard()

    def level_up(self):
        self.level += 1
        self.clear()
        self.updated_scoreboard()
        
    def updated_scoreboard(self):
        self.write(f"Level: {self.level}", align= ("center"), font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align= "center", font= FONT)
