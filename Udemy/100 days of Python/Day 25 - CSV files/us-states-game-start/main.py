import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "/home/jeremy/repos/Udemy/100 days of Python/Day 25 - CSV files/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("/home/jeremy/repos/Udemy/100 days of Python/Day 25 - CSV files/us-states-game-start/50_states.csv")

guessed_states = []
correct_guess = 0

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{correct_guess}/50 States Correct", prompt= "What's another state's name?").title()
    states = data.state.to_list()

    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        break

    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
        correct_guess += 1

states_to_learn = pandas.DataFrame(missing_states)
states_to_learn.to_csv("/home/jeremy/repos/Udemy/100 days of Python/Day 25 - CSV files/states_to_learn.csv")











screen.exitonclick()