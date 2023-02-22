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