from turtle import Turtle, Screen, left
import turtle
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmandar"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)


# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()