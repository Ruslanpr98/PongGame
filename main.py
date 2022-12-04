from turtle import Screen, Turtle
import time
from Paddle import Paddle
from Ball import Ball

from Score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PongGame")
screen.tracer(0)

score = Score()
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball((0,0))

screen.listen()

screen.onkeypress(paddle1.go_up, "Up")
screen.onkeypress(paddle1.go_down, "Down")
screen.onkeypress(paddle2.go_up, "w")
screen.onkeypress(paddle2.go_down, "s")

game_is_on = True

while game_is_on:
    #time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if ball.distance(paddle1) < 30 and ball.xcor() > 320 or ball.distance(paddle2) < 30 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 420:
        score.right_score()
        ball.goto(0,0)
        ball.bounce_x()
    
    if ball.xcor() < -420:
        score.left_score()
        ball.goto(0,0)
        ball.bounce_x()

screen.exitonclick()


