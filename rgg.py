import turtle as t


start_radius = -50
for i in range(3):
    t.circle(start_radius)

    start_radius = start_radius / 2
start_radius = 25
for i in range(2):
    t.circle(start_radius)

    start_radius = start_radius / 2
    input("+++++++++++++")

t.done()
