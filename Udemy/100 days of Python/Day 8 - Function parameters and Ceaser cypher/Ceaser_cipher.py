alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(direction, text, shift):
    cypher_text = ""
    if direction == "encode":
        for letter in text:
            new_index = ""
            old_index = alphabet.index(letter)
            new_index = (old_index + shift) % len(alphabet)
            new_letter = alphabet[new_index]
            cypher_text += new_letter
        print(f"Your message is {cypher_text}")
    elif direction == "decode":
        for letter in text:
            old_index = ""
            position = alphabet.index(letter)
            old_index = (position - shift) % len(alphabet)
            new_letter = alphabet[old_index]
            cypher_text += new_letter 
        print(f"Your message is {cypher_text}")

ceaser(direction, text, shift)
