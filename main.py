MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """returns true when order can be made,false if ingredients not enough."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough{item}.")
            return False
    return True


def process_coins():
    """"returns the total calculated from coins inserted"""
    print("please insert coins: ")
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.1
    total += int(input("how many nickles: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total


def is_transcation_success(money_received, drink_cost):
    """return true when the payment is accepted ,or false if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is your change{change}$.thankyou")
        global profit
        profit += drink_cost
        return True
    else:
        print("not enough money.money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """deduct the requirements from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name} ")

# todo:prompt user input choice and other than the user prompt should be changing state of the machine(on/off).


is_on = True
while is_on:
    choice = input('what would you like? (expresso/latte/cappuccino): ')
    if choice == "menu":
        coffee_types = MENU.keys()
        print(list(coffee_types))

    elif choice.lower() == "off":
        is_on = False
    elif choice.lower() == "report":
        print(f"water:{resources['water']} ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}ml")
        print(f"money:{profit}ml")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transcation_success(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
