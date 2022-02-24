from asyncore import write
from ctypes import alignment
from curses import window
import email
from email import message
from statistics import mode
from tkinter import *
from venv import create
from matplotlib import image
from tkinter import messagebox
from matplotlib.pyplot import text


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()  
    
    if len(website) == 0 or len(password) == 0:
        is_empty = messagebox.showinfo(title=website, message=f"Please don't leave any empty fields !")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"These are your details \n Email: {email} \n Password: {password}\n Is it Ok to save?")

    if is_ok:
        with open(file="Data.txt", mode="a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

photo_img = PhotoImage(file="/home/jeremy/repos/Udemy/100 days of Python/Day 29 - Tkinter password manager/password-manager-start/logo.png")
canvas = Canvas(width=200,  height=200)
canvas.create_image(100, 100, image= photo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "jeremyabikhalil@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=16)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)












window.mainloop()