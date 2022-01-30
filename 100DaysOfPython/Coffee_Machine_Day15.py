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
}

money_earned_so_far = 0
coffee_price = 0.0


# def check_resources_for_coffee(type_of_coffee):
#     if type_of_coffee == "espresso":
#         if resources["water"] >= 50:
#             if resources["coffee"] >= 18:
#                 buy_coffee(type_of_coffee)
#             else:
#                 print("Sorry there is not enough 'coffee'")
#         else:
#             print("Sorry there is not enough 'water'")
#     elif type_of_coffee == "latte":
#         if resources["water"] >= 200:
#             if resources["milk"] >= 150:
#                 if resources["coffee"] >= 24:
#                     buy_coffee(type_of_coffee)
#                 else:
#                     print("Sorry there is not enough 'coffee'")
#             else:
#                 print("Sorry there is not enough 'milk'")
#         else:
#             print("Sorry there is not enough 'water'")
#     elif type_of_coffee == "cappuccino":
#         if resources["water"] >= 250:
#             if resources["milk"] >= 100:
#                 if resources["coffee"] >= 24:
#                     buy_coffee(type_of_coffee)
#                 else:
#                     print("Sorry there is not enough 'coffee'")
#             else:
#                 print("Sorry there is not enough 'milk'")
#         else:
#             print("Sorry there is not enough 'water'")


def check_resources_for_coffee(type_of_coffee):
    for item in resources:
        if item in MENU[type_of_coffee]['ingredients']:
            if MENU[type_of_coffee]['ingredients'][item] > resources[item]:
                print(f"Sorry there is not enough '{item}' ")
                return
    buy_coffee(type_of_coffee)


def buy_coffee(type_of_coffee):
    global coffee_price
    global money_earned_so_far
    coffee_price = MENU[type_of_coffee]['cost']
    print(" Please insert coins ")
    quarters = (float(input("how many quarters?: ")) / 4)
    dimes = (float(input("how many dimes?: ")) / 10)
    nickles = (float(input("how many nickles?: ")) / 20)
    pennies = (float(input("how many pennies?: ")) / 100)
    sum_of_inserted_money = quarters + dimes + nickles + pennies
    if (sum_of_inserted_money - coffee_price) >= 0:
        print(f"Here is your {type_of_coffee} ☕️ enjoy ")
        print(f"Here is ${sum_of_inserted_money - coffee_price} in change ")
        money_earned_so_far += coffee_price
        for item in resources:
            if item in MENU[type_of_coffee]['ingredients']:
                resources[item] = resources[item] - MENU[type_of_coffee]['ingredients'][item]
            # print(f"{item} ==> {resources[item]}")
        # print(f" total_money {money_earned_so_far}")
        # resource_report["money_earned"] = resource_report["money_earned"] + coffee_price
        # print(f"left over resources from report are {resource_report}")
    elif (sum_of_inserted_money - coffee_price) < 0:
        print(f"Sorry that's not enough money. Money refunded.")


turn_on_machine = True

while turn_on_machine:
    choice = input("Select a Drink : 'espresso' ,'latte', 'cappuccino' :").lower()
    # quarter (.25), dime (.10), nickle (0.05), penny (0.01)
    # espresso 1.5, latte 2.5, cappuccino 3
    if choice == "report":
        print(f" Milk = {resources['milk']}ml \n Water = {resources['water']}ml \n Coffee = {resources['coffee']}gm ")
        print(f" Money = {money_earned_so_far}$ \n")
    elif choice in MENU:
        check_resources_for_coffee(choice)
    elif choice == "off":
        turn_on_machine = False
    else:
        print("Invalid selection, Please try again 🥺")
