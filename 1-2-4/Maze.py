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
path_width = 12
wall_length = 5
i = 0
maze_painter.left(90)
maze_painter.width(6)
maze_painter.speed(200)

def door():
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(path_width * 3)
    maze_painter.pendown()

def barrier():
    maze_painter.forward(50)
    maze_painter.left(90)
    maze_painter.forward(path_width * 3)
    maze_painter.back(path_width * 3)
    maze_painter.right(90)

def maze():
    global path_width,wall_length,i
    for maze in range(25):
        if i < 3:
            maze_painter.penup()
        random_num = rand.randint(0, 3)
        if random_num <= 1:
            door()
            barrier()
        else:
            barrier()
            door()
        maze_painter.forward(path_width + wall_length)
        maze_painter.left(90)
        wall_length = wall_length + 20
        i = i + 1
    maze_painter.hideturtle()
maze()

wn = trtl.Screen()
wn.mainloop()





