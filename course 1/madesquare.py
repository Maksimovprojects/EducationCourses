import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
for aColor in ["yellow", "red", "green", "blue"]:
    alex.color(aColor)
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
