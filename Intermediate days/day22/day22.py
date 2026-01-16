from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

#variables
turtle = Turtle()
screen = Screen()
screen.tracer(0)
playing = True
r_paddle = Paddle((-350))
l_paddle = Paddle((350))
ball = Ball()

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
    ball.move()
    ball.colision()
    screen.update()
screen.exitonclick()