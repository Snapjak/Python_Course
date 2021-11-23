print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcome to treasure hunt. Your Mission is to find the treasure")
decision = input('You\'re at a crossroad, where do you want to go? Type "Left" or "Right".').lower()

if decision == "right":
    decision2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or "swim" to swim accross').lower()
    if decision2 == "wait":
        decision3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?').lower()
        if decision3 == "yellow":
            print("You found the treasure. You win !")
        elif decision3 == "red":
            print("It's a room full of fire. Game over.")
        elif decision3 == "blue":
            print("You entered a room full of beasts. Game over.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fell into a whole. Game over.")
