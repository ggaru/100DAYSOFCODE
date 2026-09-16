from tkinter import *
import json
import pandas
import random

tk = Tk()

try:
    data = pandas.read_csv("Intermediate days\\day31\\data\\word_to_learn.csv")
except FileNotFoundError:
    original = pandas.read_csv("Intermediate days\\day31\\data\\palavras_japonesas.csv")
    to_learn = original.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
print(to_learn)

def randWords():
    global words
    n = random.randint(0,len(to_learn))
    new_word = to_learn[n]
    words = new_word
    return words

def getWord():
    global timer
    global translate
    tk.after_cancel(timer)    
    language.config(background="#ffffff", text="Japones", fg="#000000")
    canvas.itemconfig(img_background, image=img_cardfront)
    words = randWords()
    word.config(background="#ffffff",text= f"{words["japones"]}", fg="#000000")
    timer = tk.after(3000,showAnswer,words)

def learned():
    to_learn.remove(words)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Intermediate days\\day31\\data\\to_learn.csv", index = False)
    getWord()  

def showAnswer(words):
    canvas.itemconfig(img_background, image=img_cardback)
    language.config(background="#91c2af", text="Portugues", fg="#ffffff")
    word.config(background="#91c2af", text=f"{words["portugues"]}", fg="#ffffff")

BACKGROUND_COLOR = "#B4D8C5"
path="Intermediate days\\day31\\images\\"
img_cardback = PhotoImage(file=f"{path}card_back.png")
img_cardfront = PhotoImage(file=f"{path}card_front.png")
img_right = PhotoImage(file=f"{path}right.png")
img_wrong = PhotoImage(file=f"{path}wrong.png")
test = True

tk.config(background=BACKGROUND_COLOR, padx=50, pady=50)
tk.minsize(900,600)

words = randWords()
timer = tk.after(3000,showAnswer,words)

canvas = Canvas()
canvas.config(width=800,height=526, background=BACKGROUND_COLOR, highlightthickness=0)
img_background = canvas.create_image(402,265,image=img_cardfront)

canvas.grid(rowspan=3, columnspan=2)

language = Label(text="Japanese", font=("Arial italic",40,"italic"), background="#ffffff")
language.grid(row=0,columnspan=2)
word = Label(text="Watashi", font=("Arial", 60, "bold"), background="#ffffff")
word.grid(row=1, columnspan=2)
btn_right = Button(image=img_right, highlightthickness=0, command=learned).grid(row=3, column=1)
btn_wrong = Button(image=img_wrong, highlightthickness=0, command=getWord).grid(row=3,column=0)

getWord()

tk.mainloop()