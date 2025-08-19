from turtle import *
import colorgram

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
turtle.teleport(-400,-300)
turtle.speed(20)
turtle.circle(20)

turtle.screen.mainloop();