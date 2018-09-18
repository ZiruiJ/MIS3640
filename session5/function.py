import turtle
import math

# def square(t,length):
#     for i in range (4):
#         t.fd(length)
#         t.lt(90)

def polygon(t,length,n):
    for i in range (n):
        t.fd(length)
        t.lt (360/n)


def circle(t,r):
    circumference= 2* math.pi * r
    n-50
    length= circumference / n
    polygon (t,length, n)

jack = turtle.Turtle()

# polygon(jack, 80,10)
circle(jack,150)
turtle.mainloop()




