from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.pencolor("white")
        self.hideturtle()
        self.score = 0
        self.track_score()

    def track_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align= "center", font= ("Arial", 12, "bold"))
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= "center", font= ("Arial", 12, "bold"))
