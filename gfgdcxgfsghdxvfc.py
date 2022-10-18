import turtle as t
import random 

t.speed(0)
t.colormode(255)

while True :
	x = random.randint(-200, 200)
	y = random.randint(-100, 100)
	circles = random.randint(3, 6)
	radius = random.randint(30, 50)
	red = random.randint(0, 255)
	green = random.randint(0, 255)
	blue = random.randint(0, 255)

	t.penup()
	t.setposition(x, y)

	for i in range(circles):
		t.pendown()
		t.fillcolor(red, green, blue)
		t.begin_fill()
		t.circle(radius)
		t.end_fill()
		t.penup()
		t.setheading(90)
		t.fd(radius * 2)
		t.setheading(0)	
		radius /= 2
		

t.done()
