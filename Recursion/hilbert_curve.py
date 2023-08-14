import matplotlib.pyplot as plt

import turtle


def hilbert_curve(t, n, length, angle):
    if n == 0:
        return
    t.right(angle)
    hilbert_curve(t, n-1, length, -angle)
    t.forward(length)
    t.left(angle)
    hilbert_curve(t, n-1, length, angle)
    t.forward(length)
    hilbert_curve(t, n-1, length, angle)
    t.left(angle)
    t.forward(length)
    hilbert_curve(t, n-1, length, -angle)
    t.right(angle)


t = turtle.Turtle()
t.speed(10)

length = 5
angle = 90

hilbert_curve(t, 3, length, -angle)

turtle.done()
