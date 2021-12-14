from turtle import Screen, Turtle

tim = Turtle()
tim.shape("turtle")
tim.color("red")


# Draw a square
for x in range(0,4):
    tim.forward(100)
    tim.right(90)


import heroes
print(heroes.gen())
































screen = Screen()
screen.exitonclick()


