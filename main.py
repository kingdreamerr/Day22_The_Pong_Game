from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)
screen.tracer(0)
screen.title("Pong")
board = Scoreboard()

ball = Ball()
# paddle 1
paddle = Paddle((450, 0))

# paddle 2
paddle2 = Paddle((-450, 0))

game_on = True

screen.listen()

screen.onkeypress(paddle.go_up, "Up")
screen.onkeypress(paddle.go_down, "Down")

screen.onkeypress(paddle2.go_up, "w")
screen.onkeypress(paddle2.go_down, "s")

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 365 or ball.ycor() < -365:
        ball.bounce_y()

#     collision with the paddle
    if ball.distance(paddle) < 50 and ball.xcor() > 420 or ball.distance(paddle2) < 50 and ball.xcor() < -420:
        ball.bounce_x()

#     detect score
    if ball.xcor() > 460:
        ball.refresh()
        board.l_score()

    if ball.xcor() < -460:
        ball.refresh()
        board.r_score()


screen.exitonclick()
