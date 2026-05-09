from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.reset()
       
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

    