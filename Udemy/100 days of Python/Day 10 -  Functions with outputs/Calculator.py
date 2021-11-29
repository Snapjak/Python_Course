import art
import os
os.system('clear')

#Add
def addition(first_number, second_number):
    result = first_number + second_number
    return result

#Substract
def substratcion(first_number, second_number):
    result = first_number - second_number
    return result


#Multiply
def multiplication(first_number, second_number):
    result = first_number * second_number
    return result


#Divide
def division(first_number, second_number):
    result = first_number / second_number
    return result

operations = {
    "+": addition,
    "-": substratcion,
    "*": multiplication,
    "/": division,
    }
def calculator():
    print(art.logo)
    first_number = float(input("Insert first number:"))
    for key in operations:
        print(key)
    continue_calc = True

    while continue_calc:
        operator = input("Pick an operation: ")
        second_number = float(input("Insert another number: "))
        calculation_function = operations[operator]
        #calculation function will take the form of the whichever function is above based on the key
        result = calculation_function(first_number, second_number) #here is takes the arguments also to plug them in the relative function

        print(f"{first_number} {operator} {second_number} = {result}")
        again = input(f"Type 'Y' if you want to doanother operation on {result}, or 'N' to start a new operation: ").lower()
        if again == "y":
            first_number = result
        elif again == "n":
            clear = lambda: os.system('clear')
            clear()
            continue_calc = False
            calculator()
        else:
            print("I dont know what you mean... let's start again anw")
            again = input(f"Type 'Y' if you want to doanother operation on {result}, or 'N' to start a new operation: ").lower()

calculator()