
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Password = ""

# for x in range(0, nr_letters):
#     index_letters = random.randint(0, len(letters) -1)
#     letter = letters[index_letters]
#     Password += letter

# for x in range(0, nr_symbols):
#     index_symbols = random.randint(0, len(symbols) -1)
#     symbol = symbols[index_symbols]
#     Password += symbol
    
# for x in range(0, nr_numbers):
#     index_numbers = random.randint(0, len(numbers) -1)
#     number = numbers[index_numbers]
#     Password += number

# print(Password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

Password = ""
characters = []
total_charachters = nr_symbols + nr_letters + nr_numbers

for x in range(0, nr_letters):
    index_letters = random.randint(0, len(letters) -1)
    letter = letters[index_letters]
    characters += letter

for x in range(0, nr_symbols):
    index_symbols = random.randint(0, len(symbols) -1)
    symbol = symbols[index_symbols]
    characters += symbol
    
for x in range(0, nr_numbers):
    index_numbers = random.randint(0, len(numbers) -1)
    number = numbers[index_numbers]
    characters += number

for x in range(0,total_charachters):
    print(characters)
    x = random.choice(characters)
    Password += x
    characters.remove(x)

print(characters)
print(Password)    