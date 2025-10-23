from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.tracer(0)

screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake")


playing = True


createTurtle()
print(blocks)

while playing:
    screen.update()
    time.sleep(0.1)

    for i in range(len(blocks)-1,0,-1):
        x = blocks[i -1].xcor()
        y = blocks[i -1].ycor()
        blocks[i].goto(x,y)
    blocks[0].forward(20)
   
            

screen.exitonclick()