from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
machine = CoffeeMaker()
money = 0
turn_off = False

choice = input(f"What would you like? {menu.get_items()}: ")

drink = menu.find_drink(choice)
choice_cost = drink.cost

def check_user_input():
    success = True

    if choice == "off":
        exit
        turn_off = True
    elif choice == "report":
        machine.report()
        print (f"Money: ${money}")
    elif drink != None:
        print(f"You ordered {choice}")

check_user_input()
#         print("Please insert valid choice.")
#         success = False

#     return success
        

# #Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# while turn_off == False:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")

#     #Check the user’s input to decide what to do next.

#     success = check_user_input()
#     if not success:
#         continue

#     proceedToPayment = True
#     # Check if resources sufficient
#     for key in b.MENU:
#         if key != choice:
#             continue
#         else:
#             for key2 in resources:
#                 if key2 not in b.MENU[choice]["ingredients"]:
#                     continue
#                 ingredients = (b.MENU[choice]["ingredients"])
#                 if resources[key2] - ingredients[key2] <= 0:
#                     print(f"Sorry there is not enough {key2}")
#                     proceedToPayment = False
#                     continue
#                 else:
#                     resources[key2] -= ingredients[key2]      
#         cost = b.MENU[choice]["cost"]

#     if not proceedToPayment:
#         continue
    
#     # The prompt should show every time action has completed, e.g. once the drink is
#     # dispensed. The prompt should show again to serve the next customer.

#     # Process coins

#     coins = {
#         "quarters" : 0.25,
#         "dimes" : 0.1,
#         "nickles" : 0.05,
#         "pennies" : 0.01,
#         }

#     print("Please insert coins.")
#     def process_coins(coins):
#         money = int(input(f"how many {coins}: "))
#         return money

#     for key in coins:
#         total_paid += process_coins(key)*coins[key]

    
#     if total_paid < cost:
#         total_paid = 0
#         print("Sorry that's not enough money. Money refunded.")
#     elif total_paid > cost:
#         change = round((total_paid - cost),2)
#         money += cost
#         print(f"Here is ${change} in change.")

#     print(f"Here is you {choice}. Enjoy!")
