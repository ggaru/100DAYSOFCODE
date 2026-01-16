from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, turtlex):
        super().__init__()
        self.turtleSpd = 20
        self.penup()
        self.goto(turtlex,0)
        self.setheading(90)
        self.shapesize(1,5)
        self.color("White")
        self.shape("square")

    def up(self):
        self.forward(self.turtleSpd)

    def down(self):
        self.forward(-self.turtleSpd)


