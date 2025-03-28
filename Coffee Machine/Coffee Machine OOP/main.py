from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while True:
    choice = input("What would you like? (espresso/latte/cappuccino/):").lower()
    if choice == "off":
        break
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        if menu.find_drink(choice):
            item = menu.find_drink(choice)
            if coffeeMaker.is_resource_sufficient(item):
                if moneyMachine.make_payment(item.cost):
                    coffeeMaker.make_coffee(item)
                else:
                    continue
            else:
                break

        else:
            print("This drink doesnt exists.")
            continue
