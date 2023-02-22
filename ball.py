import time
from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.Turtle()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move_ball(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.x_move *= -1
        self.move_ball()
