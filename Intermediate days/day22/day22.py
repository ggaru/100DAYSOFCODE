from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#variables
turtle = Turtle()
screen = Screen()
screen.tracer(0)
playing = True
r_paddle = Paddle((-350))
l_paddle = Paddle((350))
ball = Ball()
score = Scoreboard()


#screen
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.listen()

#paddle1
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
#loop
while playing:
    time.sleep(0.05)
    ball.move()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(l_paddle) < 50 and ball.xcor() > 330 or ball.distance(r_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.spd += 0.2
    
    if ball.xcor() >400:
        ball.bounce_x()
        ball.reset()
        score.rpoint()
    elif ball.xcor() < -400:
        ball.bounce_x()
        ball.reset()
        score.lpoint()

    
        
screen.exitonclick()