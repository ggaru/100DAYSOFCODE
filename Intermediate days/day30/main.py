from tkinter import *
from tkinter import messagebox
import random
import json

tk = Tk()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passwordGenerator():
    if password_box != '':
        password_box.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    let = random.randint(4,8)
    num = random.randint(2,4)
    sym = random.randint(2,4)
    password = []

    list_letters = [password.append(letters[random.randint(0,len(letters)-1)]) for n in range(0,let)]
    list_numbers = [password.append(numbers[random.randint(0,len(numbers)-1)]) for n in range(0,let)]
    list_symbols = [password.append(symbols[random.randint(0,len(symbols)-1)]) for n in range(0,let)]

    passw = ""

    for char in password:
        passw += char
    password_box.insert(0,f"{passw}")
  

def load_password():
    website = website_box.get()
    try:
        with open("Intermediate days\\day30\\senhas.json", "r") as file:   
            data = json.load(file)
            data = data[website]  
    except KeyError:
         messagebox.showerror(title="Missing Website", message="That website isn't saved")    
         
    else:      
        messagebox.showinfo(title="Password", message=f"Your {website} email and password are: \n Email:{data['email']} \n password:{data["password"]}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_box.get()
    password = password_box.get()
    email = email_box.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}
    
    if website == "" or password == "" or email == "":
        messagebox.showerror(title="Missing Infos", message="Empty spaces? Not cool")
    else:
        try:
            with open("Intermediate days\\day30\\senhas.json", "r") as file:   
                data = json.load(file)
                data.update(new_data)
            
            with open("Intermediate days\\day30\\senhas.json", "w") as file:
                json.dump(data,file, indent=4)      
        except:
            with open("Intermediate days\\day30\\senhas.json", "w") as file:
                            json.dump(new_data,file, indent=4)   

        
        website_box.delete(first=0, last=len(website))
        password_box.delete(first=0, last=(len(password)))
        email_box.delete(first=0, last=len(email))
        email_box.insert(0, "@gmail.com")
# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas()
logo_png = PhotoImage(file="Intermediate days\\day29\\logo.png")

tk.config(padx=50, pady=50)
canvas.config(width=200,height=200)
canvas.create_image(100,100, image=logo_png)
canvas.grid(column=1, row=0)

website_title = Label(text="Website:", font=("bold"))
website_title.grid(column=0, row=1)
website_box = Entry(width=32)
website_box.focus()
website_box.grid(column=1, row=1)

email_title = Label(text="Email/Username:", font=("bold"))
email_title.grid(column=0, row=2)
email_box = Entry(width=50)
email_box.insert(0, "@gmail.com")
email_box.grid(column=1, row=2,columnspan=2)

password_title = Label(text="Password:", font=("bold"))
password_button = Button(text="Generate Password", command=passwordGenerator)
password_box = Entry(width=32)
password_title.grid(column=0, row=3)
password_box.grid(column=1, row=3,)
password_button.grid(column=2,row=3)

search_button = Button(text="Search", width=12, command=load_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, columnspan=2, row=4)


tk.mainloop()