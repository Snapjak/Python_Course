from turtle import Turtle, Screen

tim = Turtle()

# move around and stuff
def reset_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def rotate_right():
    tim.right(10)

def rotate_left():
    tim.left(10)

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

screen = Screen()
screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "d", fun = rotate_right)
screen.onkey(key = "a", fun = rotate_left)
screen.onkey(key = "c", fun = reset_clear)
screen.exitonclick()