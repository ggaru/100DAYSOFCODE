from turtle import Turtle, Screen
import pandas as pd


screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
playing = True
states_corrects = []



doc = pd.read_csv("Intermediate days/day25/50_states.csv")
states_to_learn = []
for i in doc["state"]:
    states_to_learn.append(i)
img = "Intermediate days\\day25\\blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


def find_state(answer):
    
    if answer_state not in states_corrects:
        for i in doc['state']:
            if i == answer_state:
                states_corrects.append(i)
                states_to_learn.remove(i)
                for x in doc[doc['state'] ==i].x: getx = x
                for y in doc[doc['state'] ==i].y: gety = y
                show_state(answer_state, getx, gety)
    
            
            
def show_state(name, x,y):
    state = Turtle()
    state.hideturtle()
    state.penup()
    state.goto(x,y)
    state.write(name)
    

while playing:
    if len(states_corrects) != 50:
        score = len(states_corrects)
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another states name?")
        answer_state = answer_state.title()
        if answer_state == "Exit":
            file = open("Intermediate days/day25/states to learn.csv", "w")
            for i in states_to_learn: 
                file.write(f"{i}\n")
            file.close()
            playing = False
            break
        else:
            find_state(answer_state)
    else:
        print("Congratulations! You won!")

screen.mainloop()