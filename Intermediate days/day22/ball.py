from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.spd = 1
        self.xmove = 10 
        self.ymove = 10
       

    def move(self):
        x = self.xcor() + self.xmove *self.spd
        y = self.ycor() + self.ymove *self.spd
        self.goto(x,y) 

    def bounce_y(self):
        self.ymove *= -1
    
    def bounce_x(self):
        self.xmove *= -1
        
    def reset(self):
        self.spd = 1
        self.goto(0,0)