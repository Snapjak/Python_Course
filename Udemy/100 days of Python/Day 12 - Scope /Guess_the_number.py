#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)

print("Welcome to the number guessing game !")
print("I'm thinking of a number between 1 and 100")

number = random.choice(range(1,100))
print(number)

difficulty = input("Choose a difficulity level. Type 'easy' or 'hard': ").lower()

easy = 10
hard = 5

def too_low_too_high(l_guess):
    global easy
    global hard
    global number
    if l_guess < number:
        if difficulty == "easy":
            easy -= 1
        elif difficulty == "hard":
            hard -= 1
        print ("Too low")
    elif l_guess > number:
        if difficulty == "easy":
            easy -= 1
        elif difficulty == "hard":
            hard -= 1
        print ("Too high")

    print("Guess again")
    print(f"You have {easy} attempts remaining to guess the number.")


if difficulty == "easy":
    print(f"You have {easy} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
elif difficulty == "hard":
    print(f"You have {hard} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
while guess != number:
    too_low_too_high(guess)
    guess = int(input("Make a guess: "))
    if guess == number:
        print (f"You got it! the answer was {number}") 

