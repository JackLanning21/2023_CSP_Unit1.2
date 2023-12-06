# Import Turtle
import turtle as trtl

# Declare Turtles.
# ONLY USE THE lines TURTLE!!!!
box = trtl.Turtle()
lines = trtl.Turtle()
wn = trtl.Screen()
Startx = -490
Starty = -300
Endx = 540
Endy = -300
lines.speed(200)

# Setup Screen
def setupScreen():
    global wn
    wn.setup(1000, 700)

# Create the box on the screen
def setupBox():
    box.speed(0)
    box.penup()
    box.goto(-490, -300)
    box.pendown()
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.left(90)
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.hideturtle()


# Code for 80 point version goes here
def v80():
    global Startx
    global Starty
    global Endx
    global Endy
    lines.penup()
    lines.goto(Startx,Starty)
    lines.pendown()
    for x in range(100):
        lines.goto(Endx, Endy)
        lines.goto(Startx, Starty)
        Startx += 9.999
        Endy += 9.85

# Code for the 90 point version goes here
def v90():
    # Calling the 80 point function - don't copy-paste from earlier method!!
    v80()
    global Startx
    global Starty
    global Endx
    global Endy
    lines.penup()
    lines.goto(Endx, Endy)
    lines.pendown()
    for x in range(100):
        lines.goto(Startx, Starty)
        lines.goto(Endx, Endy)
        Startx += 9.999
        Endy += 9.85




# Code for the 100 point version here
def v100():
    # Calling the 90 point function - don't copy-paste from earlier method!!
    v90()




# Code for the 110 point version here
def v110():
    # Calling the 100 point function - don't copy-paste from earlier method!!
    v100()


setupScreen()
setupBox()
v110()





wn.mainloop()
