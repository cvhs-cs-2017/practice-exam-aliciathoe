""" Create a Turtle, name it, make it BLUE and draw a Smiley Face"""
import turtle

smiley = turtle.Turtle()
smiley.color("Blue")
smiley.pu()
smiley.goto(-100,100)
smiley.pd()
for i in range(30):
    smiley.forward(1)
    smiley.right(12)
smiley.pu()
smiley.goto(0,100)
smiley.pd()
for i in range(30):
    smiley.forward(1)
    smiley.right(12)
smiley.pu()
smiley.goto(67,75)
smiley.pd()
def smile(x):
    smiley.right(90)
    for i in range(37):
        smiley.forward(10)
        smiley.right(5)
smile(4)
input()
