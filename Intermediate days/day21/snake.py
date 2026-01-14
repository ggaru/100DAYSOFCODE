from turtle import Turtle
from random import randint

class Snake():

    def __init__(self):
       self.blocks = []
       self.createTurtle()
       pass    

    def createTurtle(self):
       
        for i in range(3):
          self.add_segment(i)

    def add_segment(self,position):
            
            i = Turtle()
            i.penup()
            i.color("white")
            i.shape("square")
            x = 0
            i.goto(x,0)
            x = x - 20
            self.blocks.append(i)

    def extend(self):
        self.add_segment(self.blocks[-1].position())


    def move(self):
        for i in range(len(self.blocks)-1,0,-1):
            x = self.blocks[i -1].xcor()
            y = self.blocks[i -1].ycor()
            self.blocks[i].goto(x,y)
        self.blocks[0].forward(20)
    
    def up(self): 
        if  self.blocks[0].heading() != 270:
            self.blocks[0].setheading(90)
           

    def down(self):
        if  self.blocks[0].heading() != 90:
             self.blocks[0].setheading(270)
           
    def right(self):
        if  self.blocks[0].heading() != 180:
            self.blocks[0].setheading(0)

    def left(self):
        if  self.blocks[0].heading() != 0:
            self.blocks[0].setheading(180)

    
