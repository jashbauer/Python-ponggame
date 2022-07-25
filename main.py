from turtle import Screen
from paddle import Paddle
from ball import Ball
from net import Net
from scorer import Scorer
import time

# TODO 1) Create Scoreboard
# TODO 2) Create condition to quit game

WIDTH = 800
HEIGHT = 600
SCREEN_COLOR = "black"
R_X = 350
L_X = -350
REFRESH_TIME = 0.001

screen = Screen()
screen.title("pong")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.tracer(0)


r_paddle = Paddle(x_pos=R_X)
l_paddle = Paddle(x_pos=L_X)
ball = Ball()

net = Net()
scorer = Scorer()

game_on = True
while game_on:
    screen.update()
    time.sleep(REFRESH_TIME)

    r_scoreboard = scorer.score_board(side="r")
    l_scoreboard = scorer.score_board(side="l")

    ball.ball_reset()
    ball.wall_collision()
    ball.move()

    ball.paddle_collision(r_paddle)
    ball.paddle_collision(l_paddle)

    scorer.increase_r_score(ball)
    scorer.increase_l_score(ball)

    screen.listen()
    screen.onkey(fun=r_paddle.move_up, key="Up")
    screen.onkey(fun=r_paddle.move_down, key="Down")
    screen.onkey(fun=l_paddle.move_up, key="w")
    screen.onkey(fun=l_paddle.move_down, key="s")

    sum_score = scorer.r_score + scorer.l_score
    if sum_score == 10:
        game_on = False


scorer.winner()
screen.exitonclick()

