from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.move()

    def move(self):
        self.setheading(37)
        self.forward(0.3)
    
    def collision(self):
        self.distance()