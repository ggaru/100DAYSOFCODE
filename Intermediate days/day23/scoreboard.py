from turtle import Turtle

FONT = ("Courier", 24, "normal")
STARTING_POSITION = (-280,250)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.hideturtle()
        

    def board(self, level):
        self.clear()
        self.write(f"LEVEL:{level}",False,"left",FONT)

  