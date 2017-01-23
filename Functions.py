"""1. Write a function that will double any integer (n) and return the result"""

def Double(x):
    x = x * 2
    return x

print(Double(4))



"""2.  Write a program that will (1) ask the user for an input value, (2) take
that and double it and  (3) print the result.
Include necessary print statements and address whitespace issues."""

print ("Enter any value to double it.")
x = int(input())

def DoubleUser(x):
    y = x * 2
    print (y)

DoubleUser(x)
