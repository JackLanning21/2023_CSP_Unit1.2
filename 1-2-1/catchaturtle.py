# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand


#-----game configuration----
turtle_color = "Blue"
turtle_size = 3
turtle_shape = "turtle"

#-----initialize turtle-----
jack = trtl.Turtle()
jack.fillcolor(turtle_color)
jack.shapesize(turtle_size)
jack.shape(turtle_shape)

#-----game functions--------
def turtle_clicked(x, y):
    print("Jack was clicked!")
def change_position():
    rand.randint(0,400)
    new_xpos = rand.randint
    new_ypos = rand.randint
    jack.goto(new_xpos, new_ypos)

#-----events----------------
wn = trtl.Screen()
jack.onclick(turtle_clicked)
wn.mainloop()