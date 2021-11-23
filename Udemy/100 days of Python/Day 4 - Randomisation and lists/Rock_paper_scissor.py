import random
try: 
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
except:
    print("You typed the wrong value. You lost!")
computer_choice = random.randint(0,2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]
try:
    choice_str = rps[choice]
    computer_choice_str = rps[computer_choice]

    if computer_choice_str == rock and choice_str == paper:
        print(f"you chose Paper {choice_str}")
        print(f"computer chose Rock {computer_choice_str}")
        print("Paper beats rock. You win!")
    elif computer_choice_str == scissors and choice_str == paper:
        print(f"you chose Paper {choice_str}")
        print(f"computer chose Scissors {computer_choice_str}")
        print("Scissors beats Paper. Computer wins!")
    elif computer_choice_str == paper and choice_str == rock:
        print(f"you chose Rock {choice_str}")
        print(f"computer chose Paper {computer_choice_str}")
        print("Paper beats Rock. Computer wins!")
    elif computer_choice_str == paper and choice_str == scissors:
        print(f"you chose Scissors {choice_str}")
        print(f"computer chose Paper {computer_choice_str}")
        print("Scissors beats Paper. You win!")
    elif computer_choice_str == rock and choice_str == scissors:
        print(f"you chose Scissors {choice_str}")
        print(f"computer chose Rock {computer_choice_str}")
        print("Rock beats Scissors. Computer wins!")
    elif computer_choice_str == scissors and choice_str == rock:
        print(f"you chose Rock {choice_str}")
        print(f"computer chose Scissors {computer_choice_str}")
        print("Rock beats Scissors. You win!")
    else:
        print(f"you chose {choice_str}")
        print(f"computer chose  {computer_choice_str}")
        print("Its a draw")
except:
    print("You chose the wrong value. You lost!")
    exit
