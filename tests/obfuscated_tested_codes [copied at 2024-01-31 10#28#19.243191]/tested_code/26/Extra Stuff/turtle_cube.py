import turtle

jimothy = turtle.Turtle()
jimothy.shape(name="turtle")
jimothy.setheading(90)
jimothy.pencolor("green")


for i in range(6):
    jimothy.forward(180)
    jimothy.right(60)

jimothy.penup()
jimothy.forward(180)
jimothy.right(120)
jimothy.pendown()
jimothy.forward(180)
jimothy.left(60)
jimothy.forward(180)
jimothy.penup()
jimothy.left(180)
jimothy.forward(180)
jimothy.left(60)
jimothy.pendown()
jimothy.forward(180)

