
with open("/home/jeremy/repos/Udemy/100 days of Python/Day 26 - list comprehension/file1.txt") as f1:
    numbers_1 = f1.readlines()
    result1 = [x.strip() for x in numbers_1]
    print (result1)

with open("/home/jeremy/repos/Udemy/100 days of Python/Day 26 - list comprehension/file2.txt") as f2:
    numbers_2 = f2.readlines()
    result2 = [x.strip() for x in numbers_2]
    print (result2)

result = [int(x) for x in result2 if x in result1]

# Write your code above 👆

print(result)


