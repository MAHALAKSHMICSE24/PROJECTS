import turtle
def draw(rad):
  for i in range(2):
    turtle.circle(rad,90)
    turtle.circle(rad//2,90)
turtle.seth(-45)
draw(150)
turtle.clear()
turtle.done()