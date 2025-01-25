"""
#LOCAL VARIABLES
#Local variables are used to store data, in this example, we created a
#variable called enemies
enemies = 1

def encrease_enenmies():
    #with the use of a function, we try to increase the value of the variable enemies
    enemies = 2
    #the output should be "2" here
    print (enemies)

encrease_enenmies()
#The output of this line it's 1. That happens because in the function encrease_enemies we are
#creating a new variable that's gonna be erased after it's use, instead of using the existent variable
print(enemies)

#example
def pot():
    potion = "Health"
    print(potion)

pot()
#another scope error
#print(potion)

#example
#global variables can be acessed by any function in the program. But not moddified
health = 10

def potion():
    print(health)

potion()

#EXERCICIO 1

def is_prime(num):
    if num == 1:
        return print(True)
    if num / num == 1 and num / 1 == num:
        if num % 2 != 0 and num % 3 != 0:
            return print(True)
        else:
            return print(False)



num = int(input("Digite um número:"))

is_prime(num)

#modifying global variables

#as we already learn, the difference between global and local variable is based on the scope
life = 1
def increase_life():
    #altough we CAN modify the global variables just by calling them in the function, isn't very recommended doing this way
    global life
    life += 1
    print(life)

#the good practices to change global variables is getting them as a return of a function. See the example below:
life = 0
def change_global_variables(life):
    return life + 3

#saving the output inside the global variable itself
life = change_global_variables(life)
print(life)

#global constants
#global constants are simply variables in your code that you dont plan to modify ever in your code
#the good practices to use it is by putting the name of the constant in uppercase to remind you not to change it
URL = "www.google.com.br"
"""

import random
from random import choice

"""
#FINAL CHALLENGE DAY 12 - GUESSING GAME (simply version with no func)
#todo 01 - tell the user to choose a number between 1 and 100 - DONE
    #todo 01.1 - randomly choose a number - DONE
#todo 02 - give the choice to user select a difficult - DONE
#todo 03 - based on the difficult, change the number of attempts - DONE
#todo 04 - after the user's guess, show if it's TOO HIGH or TOO LOW - DONE
#todo 05 - every attempt remove 1 value to user's attempts - DONE
#todo 06 - if user's run out of attempts or guess the number, end game - DONE

#global variable that's gonna store numbers
numbers = []
#global variable of attempts
attempts = 0

#adding the numbers with the use of a loop
for i in range(1,101):
    numbers.append(i)

#choosing and printing number to debug
num = choice(numbers)
print(num)

#asking the difficult to user
mode = input("I'm thinking of a number between 1 and 100! \n"
      "Wanna play on 'Easy' or 'Hard'?").lower()

#changing the attempt's based on difficult chosen
if mode == "easy":
    attempts = 10
else:
    attempts = 5

#showing the number of attempts to the user
print(f"You have {attempts} attempts! Try again.")

#asking for a number
guess = int(input("Guess a number: "))

#checking the distance between number and guess with a help of a while
while True:
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    elif guess == num:
        print("You got it!")
        break
    if attempts == 0:
        print("You have no attempts left, im very sorry!")
        break
    attempts -= 1
    print(f"You have {attempts} attempts! Try again.")
    guess = int(input("Guess a number: "))
print("Game end.")
"""


#FINAL CHALLENGE DAY 12 - GUESSING GAME (upgraded-code version with the use of functions)
def num():
    """FUNCTION THAT WILL CHOOSE THE NUMBER AND RETURN IT"""
    numbers = []
    for i in range(1,101):
        numbers.append(i)
    num = choice(numbers)
    return num

def mode():
    """FUNCTION TO CHOOSE THE DIFFICULT OF THE GAME"""
    difficult = input("I'm thinking of a number between 1 and 100! \n"
                 "Wanna play on 'Easy' or 'Hard'?").lower()
    return difficult

def attempts():
    """FUNCTION TO CALCULATE THE ATTEMPTS"""
    difficult = mode()
    attempts = 10
    if difficult != "easy":
        attempts = 5
    return attempts
playing = True

num = num()
attempts = attempts()

def guess():
    global playing
    guess = int(input("Guess a number: "))
    if guess < num:
        return print("Too Low. Try again.")
    elif guess > num:
        return print("Too high! Try again.")
    elif guess == num:
        print("You got it!")
        playing = False

while playing == True:
    if attempts > 0:
        print(f"You have {attempts} attempts!")
        guess()
        attempts -=1
    else:
        print("You ran out of attempts. I'm sorry.")
        playing = False

