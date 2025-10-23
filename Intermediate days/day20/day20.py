from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.tracer(0)

screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake")

turtle = Turtle()
snake = Snake()

playing = True

snake.createTurtle()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while playing:
    screen.update()
    time.sleep(0.1)
    snake.move()
    print(snake.blocks[0].heading())
screen.exitonclick()