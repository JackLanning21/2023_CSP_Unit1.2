import turtle as trtl
'''
Import turtle
x = starting distance
y = incremental distance

For loop
    1. Go forward x
    2. Go left (90)
    3. Go forward x + some value
    4. Go left (90)
    
Creating the Doors

'''
#New Turtle
maze_painter = trtl.Turtle()

#Create the Spiral
x = 12
y = 5
trtl.left(90)
trtl.width(6)
def maze():
    global x,y
    for maze in range(25):
        trtl.forward(x + y)
        trtl.left(90)
        y = y + 20
    trtl.hideturtle()
def door():
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(x * 2)
    maze_painter.pendown()
maze()




wn = trtl.Screen()
wn.mainloop()


