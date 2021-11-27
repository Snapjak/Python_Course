def prime_checker(number):
    x = ""
    prime = True
    for x in range(2, number):
        result = number % x
        if result == 0:
            prime = False
    if prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
