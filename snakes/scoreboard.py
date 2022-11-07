from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"score = {self.score}", align="center", font=("Arial", 24, "normal"))

    def update_scoreboard(self):
        self.write(f"score = {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
