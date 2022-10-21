import turtle as t
import math
t.speed(0)


def drow_house(walls_x, walls_y, walls_width, walls_height, walls_color):

    """
    walls_x - левый нижний угол стены
    walls_y - левый нижний угол стены
    walls_width - ширина стен
    walls_height - высота стен
    walls_color - hex цвет заливки стен
    door_width - ширина двери
    door_height - высота двери
    door_color - red цвет заливки двери
    door_x
    door_y
    """

    door_x = walls_x
    door_y = walls_y

    drow_walls(walls_x, walls_y, walls_width, walls_height, walls_color)
    drow_door(door_x, door_y, door_width, door_height, door_color)
    drow_roof()


def drow_walls(walls_x, walls_y, walls_width, walls_height, walls_color):
    t.penup()
    t.goto(walls_x, walls_y)
    t.pendown()
    t.fillcolor(walls_color)
    t.begin_fill()
    for i in range(2):
        t.fd(walls_width)
        t.left(90)
        t.fd(walls_height)
        t.left(90)
    t.end_fill()


def drow_door(door_x, door_y, door_width, door_height, door_color):
    t.fd(walls_width / 2 - door_width / 2)
    t.fillcolor(door_color)
    t.begin_fill()
for i in range(2):
    t.fd(door_width)
    t.left(90)
    t.fd(door_height)
    t.left(90)
t.end_fill()

def drow_roof():
    t.right(180)
t.fd(walls_width / 2 - door_width / 2)
t.right(90)
t.fd(walls_height)
t.fillcolor(roof_color)
t.begin_fill()
t.right(90)
t.left(roof_angle)
t.fd(roof_side)
t.right(roof_angle * 2)
t.fd(roof_side)
t.setheading(180)
t.fd(walls_width)
t.end_fill()

drow_house(-100, 0, 200, 150, "#ff0000")
drow_house(70, 90, "#00ff00")

t.done()
