MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


on = True


def checkResources(flavor):
    global on
    #checking first if all ingredients are enough
    for i in MENU[flavor]["ingredients"]:
        if resources[i] < MENU[flavor]["ingredients"][i]:
            print("not enough resourcers")
            on = False
    #then subtracting 
    for i in MENU[flavor]["ingredients"]:        
        resources[i] -= MENU[flavor]["ingredients"][i]
    #DEBUG


def makingCoffe(flavor):
    global on

    checkResources(flavor)
    #adding and giving back the coins 
    coin = 0
    coin += int(input("How many quarters?")) * 0.25
    coin += int(input("How many dimes?")) * 0.10
    coin += int(input("How many nickels?")) * 0.05
    coin += int(input("How many pennies?")) * 0.01
    print(f"Total inserted: {coin}")
    if coin >= int(MENU[flavor]["cost"]):
        print("Here is your change: ", round(coin - MENU[flavor]["cost"]))
        resources["money"]+= MENU[flavor]["cost"]
    else:
        print(f"You did'nt put money enough. Here's your money back: {coin}")
        on = False
    print("Making coffe . . . . ")
    print(f"Here's your {flavor}!")

while on:
    flavor = input("What would you like? (espresso/latte/cappuccino): ").lower()
    match flavor:
        case "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: {resources['money']}")
        case "espresso":
            makingCoffe(flavor)
        case "latte":
            makingCoffe(flavor)
        case "cappuccino":
            makingCoffe(flavor)