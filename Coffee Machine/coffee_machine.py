from data import MENU, resources, coins

def processCoins(coins):
    """Get the total value from the coins."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    quarters *= coins["quarters"]
    dimes = int(input("How many dimes?: "))
    dimes *= coins["dimes"]
    nickles = int(input("How many nickles?: "))
    nickles *= coins["nickles"]
    pennies = int(input("How many pennies?: "))
    pennies *= coins["pennies"]
    total = quarters+dimes+nickles+pennies
    return total

def checkExchange(coinsValue, choice):
    """Check if a exchange is needed"""
    if coinsValue > MENU[choice]["cost"]:
        exchange = coinsValue - MENU[choice]["cost"]
        print(f"Here is ${round(exchange, 2)} in change.")

def doReport(resources):
    print("Water: {}ml" .format(resources["water"]))
    print("Milk: {}ml" .format(resources["milk"]))
    print("Coffee: {}g" .format(resources["coffee"]))
    print("Money: ${}" .format(resources["money"]))

def whatIsMissing(choice, resources):
    """Check the resource that is missing to make the item."""

    item = MENU[choice]
    itemWater, itemCoffee, itemMilk = getItemIngredients(item)

    if resources["water"] < itemWater:
        return "water"
    if resources["coffee"] < itemCoffee:
        return "coffee"
    if resources["milk"] < itemMilk:
        return "milk"


def getItemIngredients(item):
    """Get the ingredients from the specified item."""
    
    return item["ingredients"].get("water"), item["ingredients"].get("coffee"), \
    item["ingredients"].get("milk", 0)

def updateResources(item, resources):
    """Update the resources of the coffee machine."""
    
    itemWater, itemCoffee, itemMilk = getItemIngredients(item)
    resources["water"] -= itemWater
    resources["coffee"] -= itemCoffee
    resources["milk"] -= itemMilk

def checkCoffee(choice, resources):
    """Check if the coffee machine has the available resources
    to do the chosen coffee."""

    if choice not in MENU:
        raise Exception("This coffee is not in the menu.")
    
    item = MENU[choice]
    
    itemWater, itemCoffee, itemMilk = getItemIngredients(item)

    
    if resources["water"] >= itemWater \
    and resources["coffee"] >= itemCoffee \
    and resources["milk"] >= itemMilk:
        updateResources(item, resources)
        return True
    else:
        return False

while True:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if choice == "off":
        break
    
    if choice == "report":
        doReport(resources)
        continue

    canDoCoffee = checkCoffee(choice, resources)

    if not canDoCoffee:
        missingResource = whatIsMissing(choice, resources)
        print("Sorry. There is no available resources.")
        print(f"There is not enough {missingResource}.")
        break

    coinsValue = processCoins(coins)
    if coinsValue >= MENU[choice]["cost"]:
        checkExchange(coinsValue, choice)
        resources["money"] += MENU[choice]["cost"]
        print(f"Here is your {choice}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
        continue




