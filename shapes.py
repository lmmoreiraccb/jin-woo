import turtle 
t = turtle.Turtle()
t.speed(1)
t.penup()
t.goto(-50, 0)
t.pendown()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.penup()
t.goto(-200, 0)
t.pendown()
for _ in range(3):
    t.forward(100)
    t.right(120)
t.penup()
t.goto(200, 0)
t.pendown()
for _ in range(2):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
r=50
t.circle(r)