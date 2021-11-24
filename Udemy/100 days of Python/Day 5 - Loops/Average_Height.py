student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
count = 0

for i in student_heights:
    total += i
    count += 1
    average = round(total/count)

print(f"total height = {total}")
print(f"number of students = {count}")
print(average)



