from tkinter import *

window = Tk()
window.title("My First Program")
width =900
height =600 
window.minsize(width,height)
window.config(padx=50, pady=50)

def convert():
    km = int(input.get())
    km = km*1.6
    km_label["text"] = km
    

my_label = Label(text="is equal to", font=("Arial", 10))
my_label.grid(column=0, row=1)

my_label = Label(text="Miles", font=("Arial", 10))
my_label.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=1, row=0)

km_label = Label(text=0)
km_label.grid(column=1, row=1)

my_label = Label(text="Kilometers", font=("Arial", 10))
my_label.grid(column=2, row=1)

button = Button(text="Convert", command=convert)
button.grid(column=1, row=2)

window.mainloop()