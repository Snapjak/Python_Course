from cgi import test
from glob import glob
from itertools import count
from tabnanny import check
from tkinter import *
from tkinter import font
from tracemalloc import start
from click import command

from matplotlib.pyplot import pink, text
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = []
my_timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(my_timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text= "00:00")
    checkmark_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1   
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60    

    if reps % 2 != 0 and reps < 8:
        timer_label.config(text="Work",fg=GREEN)
        countdown(work_sec)
    elif reps == 8:
        timer_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0 and reps > 0:
        timer_label.config(text= "Break", fg=PINK)
        countdown(short_break_sec)

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global my_timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ""
        for x in range (math.floor(reps/2)):
            mark += "✔"
            checkmark_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

canvas = Canvas(width= 200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Udemy/100 days of Python/Day 28 - Tkinter dynamic typing and pomodoro/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command= reset_timer)
reset_button.grid(row=2, column=2)

checkmark_label = Label(bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3,column=1)












window.mainloop()