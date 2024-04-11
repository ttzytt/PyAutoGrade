import turtle
import random


turtle.screensize(1000, 1000)

sheldon = turtle.Turtle()
sheldon.shape(name="square")
sheldon.setheading(90)
turtle.colormode(255)
sheldon.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
sheldon.pensize(10)
sheldon.speed("fastest")

while True:
    sheldon.setheading(random.randint(0, 360))
    sheldon.forward(180)
    position = sheldon.pos()
    if position[0] > 500 or position[0] < -500 or position[1] > 500 or position[1] < -500:
        sheldon.penup()
        sheldon.goto(0, 0)
        sheldon.pendown()
    rand_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    sheldon.pencolor(rand_color)
    if rand_color == (255,255,255):
        sheldon.clear()
    print("AAAAAAAAAAA I MOVED!!!")

