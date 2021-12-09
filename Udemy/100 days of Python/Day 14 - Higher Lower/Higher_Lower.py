import art
import random as r
import data as d

A = 0
B = 0
follower_A = 0
follower_B = 0
score = 0
end_game = False

def pick_from_dic():
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
        return S
    elif follower_B > follower_A and G == "B":
        S += 1
        print(f"You are right! Current score: {S}")
        return S

def comparator():
    global follower_B
    global A
    global B
    global follower_A
    global score
    if score == 0:
        C = pick_from_dic()
        A = C[0] 
        follower_A = C[1]
    else:
        A = B
        follower_A = follower_B

    print(f"Compare A: {A}")

    print (art.vs)

    C = pick_from_dic()
    B = C[0]
    follower_B = C[1]
    print (f"Against B: {B}")

while end_game == False:
    print (art.logo)
    comparator()
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    score = compare_followers (guess, score)
    
        
    

