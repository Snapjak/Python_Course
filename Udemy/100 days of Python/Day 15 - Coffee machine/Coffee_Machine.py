# Import data from backend
import Backend_data as b

turn_off = False
money = 0
total_paid = 0
choices = ["espresso", "latte", "cappuccino", "off", "report"]

#Extract resources to variables

resources = b.resources
print(resources)
cost = 0

def check_user_input():
    success = True

    if choice == "off":
        turn_off = True
    elif choice == "report":
        for key in resources:
            if key == "coffee":
                print(f"{key.capitalize()}: {resources[key]}g")
            else:
                print(f"{key.capitalize()}: {resources[key]}ml")
        print (f"Money: ${money}")
    elif choice not in choices:
        print("Please insert valid choice.")
        success = False

    return success
        

#Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while turn_off == False:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    #Check the user’s input to decide what to do next.

    success = check_user_input()
    if not success:
        continue

    proceedToPayment = True
    # Check if resources sufficient
    for key in b.MENU:
        if key != choice:
            continue
        else:
            for key2 in resources:
                if key2 not in b.MENU[choice]["ingredients"]:
                    continue
                ingredients = (b.MENU[choice]["ingredients"])
                if resources[key2] - ingredients[key2] <= 0:
                    print(f"Sorry there is not enough {key2}")
                    proceedToPayment = False
                    continue
                else:
                    resources[key2] -= ingredients[key2]      
        cost = b.MENU[choice]["cost"]

    if not proceedToPayment:
        continue
    
    # The prompt should show every time action has completed, e.g. once the drink is
    # dispensed. The prompt should show again to serve the next customer.

    # Process coins

    coins = {
        "quarters" : 0.25,
        "dimes" : 0.1,
        "nickles" : 0.05,
        "pennies" : 0.01,
        }

    print("Please insert coins.")
    def process_coins(coins):
        money = int(input(f"how many {coins}: "))
        return money

    for key in coins:
        total_paid += process_coins(key)*coins[key]

    
    if total_paid < cost:
        total_paid = 0
        print("Sorry that's not enough money. Money refunded.")
    elif total_paid > cost:
        change = round((total_paid - cost),2)
        money += cost
        print(f"Here is ${change} in change.")

    print(f"Here is you {choice}. Enjoy!")
