print("Welcome to the tip calculator")
total = input("What was the total bill?")
people = input("How many people to split the bill?")
perc = input("What percentage tip would you like to give? 10, 12 or 15?")

amount = (float(total) / float(people)) * (1 + (float(perc)/100))
print("Each person should pay ", "$", amount)