## importing module
from turtle import *
import random

## creating new turtle instance
turtle = Turtle()

## making a square with turtle
"""
raphael.forward(100)
raphael.left(90)
raphael.forward(100)
raphael.left(90)
raphael.forward(100)
raphael.left(90)
raphael.forward(100)
raphael.left(90)
"""

# making the turtle makes a dashed line.
"""
turtle.teleport(-400,0)
lineLen = 5

for _ in range (50):
    turtle.forward(lineLen)
    turtle.penup()
    turtle.forward(lineLen)
    turtle.pendown()
    lines += 1
"""

#making the turtle draw's geometry 
"""
turtle.teleport(-300, 300)
angle = 360
line = 3
size = 100
rand = Random()
colors = ["red", "green", "blue", "yellow", "orange", "violet", "magenta", "brown", "gray", "cyan",]

while line <= 10:

    #changing the turtle colors
   
    randColor = rand.randint(0, len(colors)-1)
    turtleColor = colors[randColor]
    turtle.color(turtleColor)
    colors.remove(turtleColor)
    print(f"dps do código: line: {line} Index da cor:  {randColor}, Cor:  {turtleColor}, array:  {colors}")
  
    

    #making the geometry shape based on how many lines it has
    for i in range(line):
        turtle.right(angle/line)
        turtle.forward(size)
    
    #adding one more line to make another shape
    line += 1
"""

## making a random route
"""
turtle.pensize(15);
turtle.speed(20);

def chooseDir():
    ang = choice([90, 180, 270, 360])
    dir = choice(["left", "right"])
    match dir:
        case "left":
            turtle.left(ang);
        case "right":
            turtle.right(ang);
        case other:
            breakpoint();
    changeColor();
    turtle.forward(30);

def changeColor():
    c = choice(["darkred", "darkblue", "orange", "violet", "magenta", "gray", "darkgreen"])
    turtle.color(c)

for i in range(100):
    chooseDir();
"""

## making a esphirograph
"""
turtle.speed(20)
turtle.screen.colormode(255)
gap = 6

def change_Color():
    r = random.randint(0,255)
    g =random.randint(0,255)
    b = random.randint(0,255)    
    randColor = (r,g,b)
    return randColor

for i in range(0, 360, gap):
    turtle.setheading(i);
    turtle.circle(120);
    turtle.pencolor(change_Color())
"""

## ending loop
turtle.screen.mainloop()