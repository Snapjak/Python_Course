
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

number_of_names = len(names)

index = random.randint(0,number_of_names-1)
pay = names[index]

print(f"{pay} is going to buy the meal today!")

#we can also use the random.choice(names) instead of all that code
