from turtle import *
import colorgram
import random

### making a hirst painting
# 10 dot's per line and collumn. Each dot has a size of 20px. And a pace of 50px from each other. 

turtle = Turtle();

# Extract colors from an image.


colors = [(202, 186, 138), (204, 160, 186), (222, 205, 104), (190, 201, 213)]
"""
colors = colorgram.extract('Intermediate days\day18\image.jpg', 6)
c = []
for i in range(6):
    c.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))
"""
turtle.screen.colormode(255)
turtle.speed(10)
turtle.penup()
turtle.teleport(-200,-200)
dots = 4

def teleportTurtle():
    x = -200
    y = -200
    for i in range(dots):
        turtle.teleport(x, y)
        paintDots(dots)
        y = y+50
        
def color():
    c = random.choice(colors)
    return turtle.color(c)

def paintDots(dots):
    for i in range(dots):
        color()
        turtle.dot(20)
        turtle.forward(50)
        
      

teleportTurtle()
turtle.screen.mainloop();
