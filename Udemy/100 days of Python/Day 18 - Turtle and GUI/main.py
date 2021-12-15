from turtle import Screen, Turtle, setposition, st
import random
import turtle

tim = Turtle()
tim.shape("turtle")
tim.color("red")

colors = [(40, 98, 148), (178, 46, 78), (205, 160, 93), (224, 210, 102), (137, 89, 63), (178, 165, 36), (110, 175, 208), (213, 130, 174), (228, 72, 48), (201, 74, 117), (92, 103, 188), (22, 154, 87), (122, 217, 208), (126, 41, 70), (95, 158, 62), (45, 190, 204), (226, 171, 187), (130, 189, 161), (213, 206, 38), (232, 171, 163), (172, 186, 222), (153, 208, 218), (104, 50, 38), (45, 62, 101), (44, 75, 80), (51, 61, 71)]
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
# turtle.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r,g,b)
#     return random_color

# directions = [0, 90 , 180, 270]

# for _ in range(200):
#     tim.color(random_color())
#     tim.pensize(5)
#     tim.speed(5)
#     tim.forward(25)
#     tim.setheading(random.choice(directions))

# Drawing spirograph

# tim.speed("fastest")
# def draw_spirograph(gap_size):
#     for _ in range(int(360/gap_size)):
#         tim.color(random_color())
#         tim.circle(100)
#         current_heading = tim.heading()
#         tim.setheading(current_heading +gap_size)


# draw_spirograph(5)

turtle.colormode(255)
tim.speed("fastest")
def hirst_painting():
    for x in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

def starting_position():
    tim.hideturtle()
    tim.penup()
    tim.setposition(-450, -450)

def draw_random_circle():
    tim.pendown()
    chosen_color = random.choice(colors)
    tim.color(chosen_color)
    tim.pencolor(chosen_color)
    tim.fillcolor(chosen_color)
    tim.begin_fill()
    tim.circle(20)
    tim.end_fill()

def move_forward_invis():
    tim.penup()
    tim.hideturtle()
    tim.forward(100)

def reset_position(y):
    tim.setposition(-450, -450 + y)

starting_position()
y = 100

for f in range (10):
    for x in range (10):
        draw_random_circle()
        move_forward_invis()
    reset_position(y)
    y += 100

screen = Screen()
screen.screensize(750,750)
screen.exitonclick()