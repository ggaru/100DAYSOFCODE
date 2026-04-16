from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 100
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.left(90)
        self.showturtle()
       
    def move(self):
        self.forward(MOVE_DISTANCE)

    def win(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.reset()
            return True
    
    def reset(self):
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.showturtle()