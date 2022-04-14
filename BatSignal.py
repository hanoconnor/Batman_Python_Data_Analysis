import turtle
import math

turtle.title('Bat Signal with Turtle')
print('Holy Bat Signal Batman!')
batpen = turtle.Turtle()
batpen.speed(2)

window = turtle.Screen()
window.bgcolor("#000000")
batpen.color("gold")

size = 60

batpen.left(90)
batpen.penup()
batpen.goto(-7 * size, 0)
batpen.pendown()

for a in range(-7 * size, -3 * size, 1):
    x = a / size
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    batpen.goto(a, y * size)

for a in range(-3 * size, -1 * size - 1, 1):
    x = a / size
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    batpen.goto(a, y * size)

batpen.goto(-1 * size, 3 * size)
batpen.goto(int(-0.5 * size), int(2.2 * size))
batpen.goto(int(0.5 * size), int(2.2 * size))
batpen.goto(1 * size, 3 * size)

print('Hurry! Gotham needs a Hero!')
for a in range(1 * size + 1, 3 * size + 1, 1):
    x = a / size
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    batpen.goto(a, y * size)

for a in range(3 * size + 1, 7 * size + 1, 1):
    x = a / size
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    batpen.goto(a, y * size)

for a in range(7 * size, 4 * size, -1):
    x = a / size
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    batpen.goto(a, y * size)

for a in range(4 * size, -4 * size, -1):
    x = a / size
    rel = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
    batpen.goto(a, y * size)

for a in range(-4 * size - 1, -7 * size - 1, -1):
    x = a / size
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    batpen.goto(a, y * size)

batpen.penup()
batpen.goto(-500, -500)
turtle.done()
print('Batman is on his way! Thanks for watching')
