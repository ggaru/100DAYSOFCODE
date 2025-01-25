##DAY 13 - Debbuging previous days
#Debbuging odd or even
def odd_or_even(number):
    #The problem was that this line below only had one equal sign.
    if (number%2) == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

#debugging = print(odd_or_even(int(input("Put an number: "))))

#debbuging leap year
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            #The problem was that year was dividing by 4000
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#debugging = print(is_leap(int(input("number:"))))

#debuggin fizzbuzz
def fizz_buzz(target):
    for number in range(1, target):
        #The problem was a OR operator, instead of AND, plus several if statements, where should be elif's, and also two [] in the print number
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number )


print(fizz_buzz(int(input("number:"))))