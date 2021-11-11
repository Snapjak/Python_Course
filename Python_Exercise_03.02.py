#Chapter 3 - Exercise 2
xh = input('Enter hours: ')
xr = input('Enter rate: ')
try:
    fh = float(xh)
    fr = float(xr)
except:
    print("Please enter numeric value")
    quit()
ot = 1.5 * fr

if fh > 40 :
    print ("Overtime")
    Overtime = fh - 40
    xp = Overtime * ot + 40 * fr
else:
    xp = fr * fh
print(xp)