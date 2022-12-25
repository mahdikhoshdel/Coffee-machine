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
            "water": 50,
            "coffee": 22,
            "milk": 15
        },
        "cost": 2.3,
    },
    "cappuccino": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 10
        },
        "cost": 2.1,
    }
}

resource = {
    "water": 1000,
    "milk": 1000,
    "coffee": 100,
    "money": 0,
}


def resource_calculate(choice, money):
    milk = 0
    water = MENU[choice]['ingredients']['water']
    coffee = MENU[choice]['ingredients']['coffee']
    if choice == "latte" or order == "cappuccino":
        milk = MENU[order]['ingredients']['milk']

    resource['water'] -= water
    resource['coffee'] -= coffee
    resource['milk'] -= milk
    resource['money'] += money

    source_lack = [key for key, val in resource.items() if val < 0]
    if source_lack:
        print(f"Not enough {source_lack} for ordering {choice}")
    else:
        print(f"Here is your {choice}. Enjoy!")


ordering = True

while ordering:
    order = input("What would you like? (espresso/latte/cappuccino):")

    if order in MENU.keys():
        cost = MENU[order]['cost']
        payment = input(f"Ordering {order} cost you {cost}\nPay please(eg. 3.2):")

        if float(cost) == float(payment):
            print("Payed successfully!")
            resource_calculate(order, cost)
        else:
            print("Failed to pay, Try again please.")

    elif order == 'off':
        print("\nGoodbye, Have a nice day !!")
        ordering = False

    elif order == 'report':
        for key, value in resource.items():
            print(f'{key}: {value}')

    else:
        print("Wrong order item!")

