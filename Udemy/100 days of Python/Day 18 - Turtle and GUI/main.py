from turtle import Screen, Turtle
import random
import turtle

tim = Turtle()
tim.shape("turtle")
tim.color("red")


# Draw a square
# for x in range(0,4):
#     tim.forward(100)
#     tim.right(90)

# Draw dashed line
# for x in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Draw the shapes
# sides = [3,4,5,6,7,8,9,10]
# colors = ["red", "blue", "green", "black", "grey", "yellow", "green"]
# for side in sides:
#     tim.pencolor(random.choice(colors))
#     for x in range(side):
#         tim.forward(100)
#         tim.right(360/side)

# # Draw random path with random colors and thickness and faster
# directions = [0, 90 , 180, 270]

# for _ in range(200):
#     tim.pencolor(random.choice(colors))
#     tim.pensize(5)
#     tim.speed(10)
#     tim.forward(25)
#     tim.setheading(random.choice(directions))

# # Create random color for turtle
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

# directions = [0, 90 , 180, 270]

# for _ in range(200):
#     tim.color(random_color())
#     tim.pensize(5)
#     tim.speed(5)
#     tim.forward(25)
#     tim.setheading(random.choice(directions))

# Drawing spirograph

tim.speed("fastest")
def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading +gap_size)


draw_spirograph(5)



















screen = Screen()
screen.exitonclick()