# snake2D.py

from turtle import *
from keyboard import *

t = Turtle()
t.up()
t.speed(0)
screen = Screen()
_objects = {}

def window(x, y, title, bgColor):
    screen.title(title)
    screen.setup(x, y)
    screen.bgcolor(bgColor)

def triangle(x1, y1, x2, y2, x3, y3, objColor, objName):
    global _objects
    _objects[objName] = [[x1, y1], [x2, y2], [x3, y3], objColor]
    t.color(objColor)
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    t.up()
    t.color("black")

def square(x1, y1, x2, y2, objColor, objName):
    global _objects
    _objects[objName] = [[x1, y1,], [x2, y2], objColor]
    t.color(objColor)
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.up()
    t.color("black")

def render_done():
    done()

def key(k):
    if is_pressed(k):
        return True
    else:
        return False

def cube(x1, y1, z1, x2, y2, z2, objColor, objName):
    global _objects
    
    _objects[objName] = [[x1, y1, z1]]
    t.goto(x1, y1)
