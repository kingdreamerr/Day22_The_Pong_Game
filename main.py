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