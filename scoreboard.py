from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left = 0
        self.right = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.left, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.right, align='center', font=('Courier', 80, 'normal'))

    def l_score(self):
        self.left += 1
        self.clear()
        self.update_score()

    def r_score(self):
        self.right += 1
        self.clear()
        self.update_score()