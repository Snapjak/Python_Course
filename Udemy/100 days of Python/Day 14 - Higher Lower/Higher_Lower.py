import art
import random as r
import data as d

print (art.logo)

A = 0
B = 0
follower_A = 0
follower_B = 0
score = 0
end_game = False

def pick_from_dic(a):
    key_1 = r.choice(d.data)
    a = (f"{key_1['name']}, a {key_1['description']}, from {key_1['country']}")
    follower = key_1["follower_count"]
    details = [a, follower]
    return details

def compare_followers(G, S):
    global B
    global A
    global follower_A
    global follower_B
    global end_game
    if follower_A > follower_B and G == "B":
        print(f"Sorry that's wrong. Final score: {S}")
        end_game = True
    elif follower_B > follower_A and G == "A":
        print(f"Sorry that's wrong. Final score: {S}")
        end_game = True
    elif follower_A > follower_B and G == "A":
        S += 1
        print(f"You are right! Current score: {S}")
        A = B
        follower_A = follower_B
        B = pick_from_dic(B)[0]
        follower_B = pick_from_dic(B)[1]
    elif follower_B > follower_A and G == "B":
        S += 1
        print(f"You are right! Current score: {S}")
        A = B
        follower_A = follower_B
        B = pick_from_dic(B)[0]
        follower_B = pick_from_dic(B)[1]

def comparator(a, b):
    a = pick_from_dic(a)[0]
    follower_A = pick_from_dic(a)[1]
    print(f"Compare A: {a}")

    print (art.vs)

    b = pick_from_dic(b)[0]
    follower_B = pick_from_dic(b)[1]
    print (f"Against B: {b}")

while end_game == False:
    comparator(A, B)
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    compare_followers (guess, score)

