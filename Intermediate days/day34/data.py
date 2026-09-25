import requests



def getQuests():
    response = requests.get(url="https://opentdb.com/api.php?amount=10&category=15&type=boolean")
    data = response.json()
    return data["results"]

question_data = getQuests()