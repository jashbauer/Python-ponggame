from turtle import Turtle

SHAPE = "square"
COLOR = "white"
Y_CHANGE = 80
WIDTH_STRETCH = 5
LEN_STRETCH = 1


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.segments = []
        self.create_paddle(x_pos)

    def create_paddle(self, x_pos):
        self.pu()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_wid=WIDTH_STRETCH, stretch_len=LEN_STRETCH)
        self.goto(x_pos, y=0)

    def move_up(self):
        new_y = self.ycor() + Y_CHANGE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - Y_CHANGE
        self.goto(self.xcor(), new_y)



