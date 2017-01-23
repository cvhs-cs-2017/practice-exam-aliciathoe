"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""

import turtle
sven = turtle.Turtle()
sven.speed(0)
sven.pu()
sven.goto(-100,150)
sven.pd()
for i in range(100):
    sven.forward(100)
    sven.right(43)
input()
