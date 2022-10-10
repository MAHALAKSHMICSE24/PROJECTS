import turtle
import random
from alphabet import alphabet

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(5)
window = turtle.Screen()
window.bgcolor("black")
myPen.pensize(2)

def displayMessage(message,fontSize,color,x,y):
  myPen.color(color)
  message=message.upper()
  
  for character in message:
    if character in alphabet:
      letter=alphabet[character]
      myPen.penup()
      for dot in letter:
        myPen.goto(x + dot[0]*fontSize, y + dot[1]*fontSize)
        myPen.pendown()
        
      x += fontSize
      
    if character == " ":
      x += fontSize
    x += characterSpacing 

#Main Program Starts Here
fontSize = 30
characterSpacing = 5
fontColor = "white"
print("ENTER THE TEXT YOU WANT TO PRINT")
message = str(input())
displayMessage(message,fontSize,fontColor,0,0)
turtle.done()
