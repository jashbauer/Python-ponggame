from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 12, "normal")
END_FONT = ("courier", 20, "normal")


class Scorer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.r_score = 0
        self.l_score = 0

    def score_board(self, side):
        self.pu()
        self.hideturtle()
        if side == "r":
            self.goto(150, 250)
            self.write_score(side)
        elif side == "l":
            self.goto(-200, 250)
            self.write_score(side)

    def increase_l_score(self, ball):
        if ball.xcor() > 400:
            self.clear()
            self.l_score += 1

    def increase_r_score(self, ball):
        if ball.xcor() < -400:
            self.clear()
            self.r_score += 1

    def write_score(self, side):
        if side == "l":
            self.write(f"SCORE: {self.l_score}", font=FONT)
        elif side == "r":
            self.write(f"SCORE: {self.r_score}", font=FONT)

    def winner(self):
        self.clear()
        self.goto(0, 0)
        if self.r_score > self.l_score:
            self.write(f"RIGHT WINS! R:{self.r_score}, L:{self.l_score}", font=END_FONT, align=ALIGN)
        elif self.l_score > self.r_score:
            self.write(f"LEFT WINS!  R:{self.r_score}, L:{self.l_score}", font=END_FONT, align=ALIGN)
        else:
            self.write(f"IT'S A DRAW!  R:{self.r_score}, L:{self.l_score}", font=END_FONT, align=ALIGN)


