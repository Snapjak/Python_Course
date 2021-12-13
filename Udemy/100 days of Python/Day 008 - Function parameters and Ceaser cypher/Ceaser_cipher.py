alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)
continue_game = True

def ceaser(direction, text, shift):
    cypher_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            new_index = ""
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % len(alphabet)
            cypher_text += alphabet[new_index]
        else:  
            cypher_text += char
 
    print(f"Your message is {cypher_text}")

while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(direction, text, shift)
    stop_game = input("Do you want to try again? 'Yes' or 'No': ").lower()
    if stop_game == "no":
        continue_game = False
        print("Goodbye")
