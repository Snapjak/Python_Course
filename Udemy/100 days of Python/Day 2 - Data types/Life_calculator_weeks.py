# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated number

age = input("What is your current age?")
print(age)
max_age = 90
age_int = int(age)

years = max_age - age_int

months = years * 12

weeks = years * 52

days = years * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")



