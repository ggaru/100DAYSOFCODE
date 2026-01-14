from turtle import Turtle

class Scoreboard(Turtle):

    def __init__ (self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.points = -1
        self.goto(0,200)
        self.refreshScore()

    def refreshScore(self):
        self.clear()
        self.points+=1
        self.write("Points:" + str(self.points), False, align="center", font=("Arial", 32, "normal"))

    def gameover(self):
        self.home()
        self.write("GAME OVER", False, align="center", font=("Arial", 32, "normal") )