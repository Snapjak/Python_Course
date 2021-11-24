
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest = -1

for i in student_scores:
    if highest < i:
        highest = i
print(f"The highest score in the class is : {highest}")



