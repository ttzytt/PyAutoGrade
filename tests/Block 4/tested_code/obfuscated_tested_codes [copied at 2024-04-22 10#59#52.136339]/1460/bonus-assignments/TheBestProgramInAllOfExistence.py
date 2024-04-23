import turtle

timothy = turtle.Turtle()
timothy.shape(name='turtle')
def turn(x):
    timothy._rotate(x)
    return
def draw(x):
    timothy.forward(x)
    return
for i in range(12):
    turn(30)
    draw(10)
turn(180)
for i in range(19):
    turn(30)
    draw(30)
turn(180)
turn(90)
draw(70)
turn(-90)
draw(30)
turn(-90)
draw(70)
