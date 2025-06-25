from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
make = CoffeeMaker()
money = MoneyMachine()
while True:
    print("\n")
    print(menu.get_items())
    item = input("Choose a coffe:")
    if item == 'report':
        make.report()
        money.report()
    else: 
        order = menu.find_drink(item)
        if make.is_resource_sufficient(order) == True:
            if money.make_payment(order.cost) == True:
            #Return if is possible to do the drink, passed by menu.find_drink
                make.make_coffee(order)
            else:break    
        else: break