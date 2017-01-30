import turtle
sally = turtle.Turtle()

def NSides(y):
    x = 360 / y
    for i in range(y):
        sally.forward(35)
        sally.right(x)
    input()
NSides(10)
