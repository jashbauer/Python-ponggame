from turtle import Turtle


class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, -300)
        self.setheading(90)
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.draw_net()

    def draw_net(self):
        while self.ycor() < 300:
            self.pd()
            self.forward(10)
            self.pu()
            self.forward(10)