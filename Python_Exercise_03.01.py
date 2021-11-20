#Chapter 3 - Exercise 1
xh = input('Enter hours: ')
xr = input('Enter rate: ')
fh = float(xh)
fr = float(xr)
ot = 1.5 * fr

if fh > 40 :
    print ("Overtime")
    Overtime = fh - 40
    xp = Overtime * ot + 40 * fr
else:
    xp = fr * fh
print(xp)