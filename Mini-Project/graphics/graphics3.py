import turtle
turtle.showturtle()
turtle.shape("turtle")
turtle.pencolor('red')
for i in range(180):
    turtle.forward(100)
    turtle.right(30)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(50)
    turtle.right(30)
    turtle.penup()
    turtle.setposition(0, 0)
    turtle.pendown()
    turtle.right(2)