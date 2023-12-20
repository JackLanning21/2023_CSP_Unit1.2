import turtle as trtl
import random as rand
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
i = 0
door_random = rand.randint(0, 200)
barrier_random = rand.randint(0, 200)
maze_painter.left(90)
maze_painter.width(6)
maze_painter.speed(200)

def door():
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(x * 3)
    maze_painter.pendown()

def barrier():
    maze_painter.forward(50)
    maze_painter.left(90)
    maze_painter.forward(x * 3)
    maze_painter.back(x * 3)
    maze_painter.right(90)

def maze():
    global x,y,i, door_random, barrier_random
    door_random = rand.randint(x * 2, (y - x * 2))
    barrier_random = rand.randint(x * 2, (y - x * 2))
    for maze in range(25):
        if i < 3:
            maze_painter.penup()
        door()
        barrier()
        maze_painter.forward(x + y)
        maze_painter.left(90)
        y = y + 20
        i = i + 1
    maze_painter.hideturtle()
maze()

wn = trtl.Screen()
wn.mainloop()




