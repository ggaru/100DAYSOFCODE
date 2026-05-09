from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

import time

level = 1
screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
carManager = CarManager()
game_is_on = True



while game_is_on:
    
    screen.onkey(player.move,'w')
    score.board(level)
    if player.win():
        level+=1
        carManager.spd += 10

    time.sleep(0.1)
    screen.update()
    carManager.create_car()
    carManager.move()
    
    for car in carManager.all_cars:
        if car.distance(player) < 20:
            score.gameOver()
            game_is_on = False

screen.exitonclick()