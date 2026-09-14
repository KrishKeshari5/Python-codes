import turtle
import colorsys

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.width(2)
h = 0
n = 200
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    t.color(c)
    h += 1 / n

    t.circle(150)   
    t.left(1)



