from turtle import *
# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colrs = ['yellow', 'white', 'orange', 'cyan', 'pink', 'red']
tur = turtle.Turtle()
turtle.bgcolor('black')
for i in range(360):
    tur.pencolor(colrs[i%6])
    tur.width(i//100 + 1)
    tur.forward(i)
    tur.left(59)