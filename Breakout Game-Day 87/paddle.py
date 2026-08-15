from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.penup()
        self.speed("fastest")
        self.goto(x=0,y=-280)
        self.start = False


    def right(self, screen):
        if self.xcor() < 230:
            x_cor = self.xcor() + 20
            self.goto(x_cor, self.ycor())
            screen.update()

    def left(self, screen):
        if self.xcor() > -230:
            x_cor = self.xcor() - 20
            self.goto(x_cor, self.ycor())
            screen.update()

    def launch(self):
        self.start = True
