from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.goto(-100, 200)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"Score: {self.score}", align="center", font= ("Courier", 30, "normal"))
        self.goto(100, 260)
        self.write(f"Lives: {self.lives}", align="center", font =("Courier", 30, "normal") )

    def game_over(self):
        self.goto(-0, 0)
        self.write("Game Over", align="center", font=("Courier", 50, "normal"))