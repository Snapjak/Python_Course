number = int(input("Which number do you want to check? "))

mod = number % 2

if mod == 0:
    print("This is an even number")
else:
    print("This is an odd number")