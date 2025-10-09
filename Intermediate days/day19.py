from turtle import Turtle, Screen
from random import *
screen = Screen()

"""
def forward():
    turtle.forward(20)
def backward():
    turtle.forward(-20)
def counterClockwise():
    turtle.left(15)
def clockwise():
    turtle.right(15)
def clear():
    turtle.goto(0,0)
    turtle.clear()
    

screen.onkey(forward, "w")
screen.onkey(backward,"s")
screen.onkey(counterClockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")

screen.listen()
"""

"""Project day 19"""
screen.setup(500,400)
colors = ["red", "yellow", "purple", "pink", "orange", "green", "blue"]
bet = screen.textinput("Bet", "Choose a color: ")
y = 130
turtles = []
play = True

for i in colors:
    turtle = i
    turtle = Turtle("turtle")
    turtle.color(i)
    y = y-30
    turtle.penup()
    turtle.goto( -230,y)
    turtles.append(turtle)

print(turtles[0])


while play:
    for turtle in turtles:
        distance = randint(0,100)
        turtle.forward(distance)
        if turtle.pos() > (205,0):
            color = turtle.pencolor()
            if color == bet: 
                print("you won!")
                play = False
            else: 
                print ("you lose")
                play = False
            
    

screen.exitonclick()
