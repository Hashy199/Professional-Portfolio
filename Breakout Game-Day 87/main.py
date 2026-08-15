from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from wall import Wall
from scoreboard import Scoreboard
# from game_over import GameOver
from ball import Ball

import time

#Main Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)
#All objects fromm their classes
paddle = Paddle()
ball = Ball()
wall = Wall()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(lambda: paddle.right(screen), key="Right")
screen.onkeypress(lambda: paddle.left(screen), key="Left")
screen.onkeypress(paddle.launch, key="Up")

game_is_on = True

#MainLoop

lives = 3
while game_is_on:


    time.sleep(0.1)
    screen.update()
    if paddle.start:
        ball.move()


    if ball.ycor() > 280:
        ball.bounce_y()
    if ball.distance(paddle) < 40 and ball.ycor() > -250 and ball.can_bounce or ball.ycor() > 250:
        ball.bounce_y()
        ball.can_bounce = False
    if ball.distance(paddle) > 60:
        ball.can_bounce = True
    if ball.xcor() > 295:
        ball.bounce_x()
    if ball.xcor() < -295:
        ball.bounce_x()


    bounced = False
    for i in range(6):
        brick_row = wall.bricks[i]
        bricks = brick_row["bricks"]
        bricks_to_remove = []
        for brick in bricks:
            if ball.distance(brick) <= 20:
                brick.hideturtle()
                bricks_to_remove.append(brick)
                if not bounced:
                    ball.bounce_y()
                bounced = True

                score_board.score += brick_row["points"]

        for brick in bricks_to_remove:
            bricks.remove(brick)


        brick_row["bricks"] = bricks
        wall.bricks[i] = brick_row

    if ball.ycor() < -280:

        score_board.lives -= 1
        for row in wall.bricks:
            for brick in row["bricks"]:
                brick.hideturtle()
        wall = Wall()
        paddle.hideturtle()
        paddle = Paddle()

        ball.hideturtle()
        ball = Ball()

        screen.listen()
        screen.onkeypress(lambda: paddle.right(screen), key="Right")
        screen.onkeypress(lambda: paddle.left(screen), key="Left")
        screen.onkeypress(paddle.launch, key="Up")


    if score_board.lives < 1:
        game_is_on = False
        score_board.game_over()

    score_board.update_scoreboard()


screen.exitonclick()

