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


easy = 10
hard = 5

turns = 0

def too_low_too_high(l_guess, l_number, l_turns):
    if l_guess < l_number:
        print ("Too low")
        return l_turns - 1
    elif l_guess > l_number:
        print ("Too high")
        return l_turns - 1
    else: 
        print (f"You got it! the answer was {l_number}") 
        return
    print("Guess again")
    print(f"You have {l_turns} attempts remaining to guess the number.")

def set_difficulity():  
    difficulty = input("Choose a difficulity level. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        turns = easy
        return turns
    else:
        turns = hard
        return turns   

def game():

    print(logo)
    print("Welcome to the number guessing game !")
    print("I'm thinking of a number between 1 and 100")
    number = random.choice(range(1,100))
    print(number)

    turns = set_difficulity()
    guess = 0

    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = too_low_too_high(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != guess:
            print("Guess again.")
            
game() 
