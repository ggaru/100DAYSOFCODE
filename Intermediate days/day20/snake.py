from turtle import Turtle

class Snake():

    def __init__(self):
        self.blocks = []
    

    def createTurtle(self, blocks):
        x = 0
        for i in range(3):
            i = Turtle()
            i.penup()
            i.color("white")
            i.shape("square")
            i.goto(x,0)
            x = x - 20
            blocks.append(i)

    def move(self):
        