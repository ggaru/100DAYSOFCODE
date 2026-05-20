from turtle import Turtle

class Scoreboard(Turtle):

    def __init__ (self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.points = 0
        with open("Intermediate days\day24 copy\data.txt") as file:
             self.highscore = int(file.read())
        self.goto(0,200)
        self.write("HighScore:"  + str(self.highscore), False, align="left", font=("Arial", 32, "normal"))
        self.write("Points:" + str(self.points), False, align="right", font=("Arial", 32, "normal"))


    def refreshScore(self):
        self.clear()
        self.write("HighScore:"  + str(self.highscore), False, align="left", font=("Arial", 32, "normal"))
        self.write("Points:" + str(self.points), False, align="right", font=("Arial", 32, "normal"))

    def reset(self):
        if self.points > self.highscore:
            self.highscore = self.points
        with open("Intermediate days\day24 copy\data.txt", "w") as file:
            file.write(str(self.highscore))
        self.points = 0
        self.refreshScore()

    # def gameover(self):
    #    
    #     self.refreshScore()
    #     self.home()
    #     self.write("GAME OVER", False, align="center", font=("Arial", 32, "normal") )