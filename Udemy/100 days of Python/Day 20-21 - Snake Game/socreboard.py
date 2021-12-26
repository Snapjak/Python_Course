from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.pencolor("white")
        self.hideturtle()
        with open("/home/jeremy/repos/Udemy/100 days of Python/Day 20-21 - Snake Game/data.txt", "r") as data:
            self.highscore = int(data.read())
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, Highscore: {self.highscore}", align= "center", font= ("Arial", 12, "bold"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("/home/jeremy/repos/Udemy/100 days of Python/Day 20-21 - Snake Game/data.txt", "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align= "center", font= ("Arial", 12, "bold"))
