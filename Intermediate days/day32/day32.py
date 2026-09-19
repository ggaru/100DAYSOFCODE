import smtplib
import datetime as dt
import random
import pandas as pd

GGARU_MAIL = "ggaru.dev@gmail.com"
PASSWORD = "xbvu xmxz lpcz yovp"


##################### Extra Hard Starting Project ######################

# 2. Check if today matches a birthday in the birthdays.csv
df = pd.read_csv("100DAYSOFCODE\\Intermediate days\\day32\\birthdays.csv")
now = dt.datetime.now()

def sendmail(mail, message):
    print(message)
    with smtplib.SMTP("smtp.gmail.com") as connection:
         connection.starttls()
         connection.login(user=GGARU_MAIL, password=PASSWORD)
         connection.sendmail(from_addr=GGARU_MAIL, to_addrs=mail, msg=f"Subject:Happy Bday!\n\n{message}")
 

def createLetter(mail, name):
   
    letters = [1,2,3]
    n = random.choice(letters)
    with open(f"100DAYSOFCODE\\Intermediate days\\day32\\letter_templates\\letter_{n}.txt", "r") as file:
        letter = file.read()
        new_letter = letter.replace("[NAME]", name)
        sendmail(mail, new_letter)
        


hoje = df[(df["day"] == now.day) & (df["month"] == now.month) & (df["year"] == now.year)]
print(hoje)
for _, linha in hoje.iterrows():
    print(linha["name"], linha["email"])
    createLetter(linha["email"], linha["name"])
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




