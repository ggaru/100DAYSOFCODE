import requests
from datetime import datetime
import random
import smtplib
import time

GGARU_MAIL = "ggaru.dev@gmail.com"
PASSWORD = "xbvu xmxz lpcz yovp"
MY_LAT = -3.718460 # Your latitude
MY_LONG = -38.541672 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()

print("iss:", iss_latitude, iss_longitude)
print("mine:",MY_LAT, MY_LONG)

while True:
    if iss_latitude in range (int(MY_LAT-5.0), int(MY_LAT+5.0)) and iss_longitude in range (int(MY_LONG-5.0), int(MY_LONG+5.0)) :
        if time_now.hour in range(sunrise, sunset):
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=GGARU_MAIL, password=PASSWORD)
                connection.sendmail("ggaru.dev@gmail.com", "ggaru.dev@gmail.com", "Subject:Hey!\n\nLook up lil bro")
        else: 
            print("ISS is above your head! But it's too damn bright.")
    else:
        print("Nah no iss bro")
    time.sleep(60)