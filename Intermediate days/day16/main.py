from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#starting objects
menu = Menu()
make = CoffeeMaker()
money = MoneyMachine()


while True:
    print("\n")
    print(menu.get_items()) #print all the items of the menu
    item = input("Choose a coffe:") 
    if item == 'report': #condition to print all the reports 
        make.report() 
        money.report()
    else: 
        order = menu.find_drink(item) #find the drink choosed in the menu
        if make.is_resource_sufficient(order) == True and money.make_payment(order.cost) == True: #if are resourcers, keep makeing
                make.make_coffee(order)
        else:break    
        