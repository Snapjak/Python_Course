print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

t = lowercase_name1.count("t") + lowercase_name2.count("t")
r = lowercase_name1.count("r") + lowercase_name2.count("r")
u = lowercase_name1.count("u") + lowercase_name2.count("u")
e = lowercase_name1.count("e") + lowercase_name2.count("e")

l = lowercase_name1.count("l") + lowercase_name2.count("l")
o = lowercase_name1.count("o") + lowercase_name2.count("o")
v = lowercase_name1.count("v") + lowercase_name2.count("v")
e = lowercase_name1.count("e") + lowercase_name2.count("e")

TRUE = t + r + u + e
LOVE = l + o + v + e

Score = str(TRUE) + str(LOVE)
Score_int = int(Score)

if Score_int < 10 or Score_int > 90:
    print(f"Your score is {Score_int}, you go together like coke and mentos.")
elif Score_int >= 40 and Score_int <= 50:
    print(f"Your score is {Score_int}, you are alright together.")
else:
    print(f"Your score is {Score_int}.")



