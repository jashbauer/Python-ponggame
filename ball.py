from turtle import Turtle
from random import choice

SHAPE = "circle"
COLOR = "white"
WALL_X = 400
WALL_Y = 280
Y_CHANGES = [-4, -2, 2, 4]
X_CHANGES = [-6, -3, 3, 6]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape(SHAPE)
        self.color(COLOR)
        self.DX = choice(X_CHANGES)
        self.DY = choice(Y_CHANGES)

    def move(self):
        new_x = self.xcor() + self.DX
        new_y = self.ycor() + self.DY
        self.goto(new_x, new_y)

    def change_dir(self):
        self.DY = choice(Y_CHANGES)
        self.DX = choice(X_CHANGES)

    def wall_collision(self):
        if self.ycor() == WALL_Y or self.ycor() == -WALL_Y:
            self.DY *= -1

    def paddle_collision(self, paddle):
        if paddle.xcor() > 0:
            if self.distance(paddle) < 50 and self.xcor() > 320:
                self.DX *= -1.20
        elif paddle.xcor() < 0:
            if self.distance(paddle) < 50 and self.xcor() < 330:
                self.DX *= -1.20

    def ball_reset(self):
        if self.xcor() > WALL_X or self.xcor() < -WALL_X:
            self.goto(0, 0)
            self.change_dir()
