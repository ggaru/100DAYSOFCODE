from turtle import Turtle
import random as rand

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
            self.all_cars = []
            self.spd = 5
            super().__init__()
    
    def create_car(self):
        random_chance = rand.randint(1,6)
        if random_chance == 6:
            newCar = Turtle()
            newCar.penup()
            newCar.shape('square')
            newCar.goto(rand.randrange(300, 350),rand.randrange(-250,250))
            newCar.left(180)
            newCar.color(rand.choice(COLORS))
            newCar.shapesize(1,2,0)
            self.all_cars.append(newCar)
       
    def move(self):
        for car in self.all_cars:
            car.forward(self.spd)
    
    def reset(self):
         self.all_cars == []
