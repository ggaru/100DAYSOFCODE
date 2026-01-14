from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.tracer(0)

screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake")

turtle = Turtle()
snake = Snake()
<<<<<<< HEAD
food = Food()
=======
>>>>>>> 53e86e296198d438f58b301d74f190f9b700951f

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