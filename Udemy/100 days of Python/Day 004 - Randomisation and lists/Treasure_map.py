# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

Vertical = int(position[0]) #2 column
Horizontal = int(position[1])   #3 row

# select_row = map[Horizontal-1]
# select_row[Vertical-1] = "X" 

#or use this line of code

map[Horizontal-1][Vertical-1] = "X"

print(f"{row1}\n{row2}\n{row3}")