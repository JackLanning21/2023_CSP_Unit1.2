import turtle as trtl

test = trtl.Turtle()
def drawTriangle():
    test.pendown()
    test.fd(100)
    test.right(120)
    test.fd(100)
    test.right(120)
    test.fd(100)

def drawTriangle(long, x ,y):
    test.penup()
    test.goto(x, y)
    test.pendown()
    test.fd(long)
    test.right(120)
    test.fd(long)
    test.right(120)
    test.fd(long)

path_width = 100
wall_length = 100
length = 43
for tri in range(100):
    drawTriangle(length, path_width, wall_length)
    path_width += length * 1.25
    wall_length += length * 1.25
    length += 1
wn = trtl.Screen()
wn.mainloop()