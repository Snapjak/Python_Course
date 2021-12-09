# Import data from backend
import Backend_data as b

drink_served = False
money = 0

#Extract resources to variables
resources = b.resources
print(resources)

#Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

choice = input("What would you like? (espresso/latte/cappuccino): ")
cost = 0

#Check the user’s input to decide what to do next.

def check_user_input():
    if choice == "off":
        exit
    elif choice == "report":
        for key in resources:
            if key == "coffee":
                print(f"{key.capitalize()}: {resources[key]}g")
            else:
                print(f"{key.capitalize()}: {resources[key]}ml")
        print (f"Money: ${money}")
            
check_user_input()

# Check if resources sufficient
for key in b.MENU:
    if choice == key:
        for key2 in resources:
            if key2 not in b.MENU[choice]["ingredients"]:
                continue
            ingredients = (b.MENU[choice]["ingredients"])
            if resources[key2] - ingredients[key2] <= 0:
                print(f"Sorry there is not enough {key2}")
            else:
                resources[key2] -= ingredients[key2]      
    cost = b.MENU[choice]["cost"]

# The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
