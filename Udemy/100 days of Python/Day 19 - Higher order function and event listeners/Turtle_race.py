from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? enter a color: ")
print(user_bet)

is_race_on = False

if user_bet:
    is_race_on = True

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

def create_turtles(name):
    name = Turtle()
    return name

y = -100

for color in colors:
    x = -230    
    new_turtle = create_turtles(color)
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.goto(x,y)
    all_turtles.append(new_turtle)
    y += 50

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle won!")
            else:
                print(f"You've lost. The {winning_color} turtle won!")
        turtle.forward(randint(0,10))

screen.exitonclick()
