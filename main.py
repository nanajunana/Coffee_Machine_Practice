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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

coins = {
    "penny": 0.01,
    "dime": 0.1,
    "Nickel": 0.05,
    "Quarter": 0.25
}

def process_transaction(order):
    if order == 'espresso':
        if (MENU[order]['ingredients']['water'] <= resources['water'] and
                MENU[order]['ingredients']['coffee'] <= resources['coffee']):

            print("Insert your coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total_pay = quarters + dimes + nickles + pennies
            if total_pay >= MENU[order]['cost']:
                change = total_pay - MENU[order]['cost']
                if change != 0:
                    print(f"Here is your change ${change}")
                    resources['water'] -= MENU[order]['ingredients']['water']
                    resources['coffee'] -= MENU[order]['ingredients']['coffee']
                    resources['money'] += MENU[order]['cost']
                print(f"Here is your {order}. Enjoy!")
            else:
                print(f"That's not enough money. Money refunded")
        elif (MENU[order]['ingredients']['water'] <= resources['water'] and
                MENU[order]['ingredients']['coffee'] > resources['coffee']):
            print("Not enough coffee")
        elif (MENU[order]['ingredients']['water'] > resources['water'] and
                MENU[order]['ingredients']['coffee'] <= resources['coffee']):
            print("Not enough water")
        else:
            print("Not enough ingredients")

    elif (MENU[order]['ingredients']['water'] <= resources['water'] and
            MENU[order]['ingredients']['coffee'] <= resources['coffee'] and
            MENU[order]['ingredients']['milk'] <= resources['milk']):

        print("Insert your coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total_pay = quarters + dimes + nickles + pennies
        if total_pay >= MENU[order]['cost']:
            change = total_pay - MENU[order]['cost']
            if change != 0:
                print(f"Here is your change ${change}")
                resources['water'] -= MENU[order]['ingredients']['water']
                resources['milk'] -= MENU[order]['ingredients']['milk']
                resources['coffee'] -= MENU[order]['ingredients']['coffee']
                resources['money'] += MENU[order]['cost']
            print(f"Here is your {order}. Enjoy!")
        else:
            print(f"That's not enough money. Money refunded")
    elif MENU[order]['ingredients']['water'] <= resources['water'] and MENU[order]['ingredients']['coffee'] <= resources['coffee'] and MENU[order]['ingredients']['milk'] > resources['milk']:
        print("Sorry, there is not enough milk")
    elif MENU[order]['ingredients']['water'] <= resources['water'] and MENU[order]['ingredients']['coffee'] > resources['coffee'] and MENU[order]['ingredients']['milk'] <= resources['milk']:
        print("Sorry, there is not enough coffee")
    elif MENU[order]['ingredients']['water'] > resources['water'] and MENU[order]['ingredients']['coffee'] <= resources['coffee'] and MENU[order]['ingredients']['milk'] <= resources['milk']:
        print("Sorry, there is not enough water")
    elif MENU[order]['ingredients']['coffee'] > resources['coffee'] and MENU[order]['ingredients']['milk'] > resources['milk']:
        print("Sorry, there is not enough milk and coffee")
    elif MENU[order]['ingredients']['water'] > resources['water'] and MENU[order]['ingredients']['milk'] > resources['milk']:
        print("Sorry, there is not enough milk and water")
    elif MENU[order]['ingredients']['water'] > resources['water'] and MENU[order]['ingredients']['coffee'] > resources['coffee']:
        print("Sorry, there is not enough water and coffee")
    else:
        print("Sorry, not enough ingredients")

machine = True

while machine:
    user_input = input("What do you like? espresso/latte/cappuccino: ").lower()

    if user_input == 'report':
        print(resources)
    elif user_input in ['espresso', 'latte', 'cappuccino']:
        process_transaction(user_input)
    elif user_input == 'off':
        exit()
    else:
        print("Wrong input")