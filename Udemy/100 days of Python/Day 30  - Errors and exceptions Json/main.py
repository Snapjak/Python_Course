
from turtle import mode


try:
    file =  open("a_file.txt")
except:
    open(file="a_file.txt", mode="w")