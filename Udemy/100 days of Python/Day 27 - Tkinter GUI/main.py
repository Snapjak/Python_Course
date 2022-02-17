from tkinter import *

window = Tk()
window.minsize(width=300, height=100)
window.title("Mile to KM converter")
window.config(padx=20, pady=20)

def converter():
    miles = entry.get()
    if include_decimals.get() == 1:
        km = float(miles) * 1.609
    else:
        km = round(int(miles) * 1.609)
    label4.config(text= km)

button = Button(text="Calculate", command=converter)
button.grid(row=2, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="Km")
label3.grid(row=1, column=2)

label4 = Label(text= "0")
label4.grid(row=1,column=1)

entry = Entry(textvariable=0, width=5)
entry.grid(row=0, column=1)

def is_decimals_included():
    print(include_decimals.get())

include_decimals = IntVar()
check = Checkbutton(text="Include decimals", variable=include_decimals, command=is_decimals_included)
check.grid(row=2, column=2)












window.mainloop()
