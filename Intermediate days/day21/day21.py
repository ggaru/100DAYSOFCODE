from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)

screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake")

turtle = Turtle()
snake = Snake()
food = Food()
score = Scoreboard()

playing = True

snake.createTurtle()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while playing:
    screen.update()
    time.sleep(0.05)
    snake.move()
    
    if snake.blocks[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.refreshScore()

    if snake.blocks[0].xcor() > 300 or snake.blocks[0].xcor() < -300 or snake.blocks[0].ycor() > 300 or snake.blocks[0].ycor() < -300:
            playing = False
            score.gameover()

    for block in snake.blocks[1:]:
        if snake.blocks[0].distance(block) < 10:
                playing = False
                score.gameover()

screen.exitonclick()