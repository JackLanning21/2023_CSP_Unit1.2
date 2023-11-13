# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import turtle as score_writer

#-----game configuration----
turtle_color = "Blue"
turtle_size = 3
turtle_shape = "turtle"
score = 0

score_writer.penup()
score_writer.goto(300, 300)
score_writer.pendown()
score_writer.hideturtle()

font_setup = ("Arial", 20, "normal")

#-----initialize turtle-----
jack = trtl.Turtle()
jack.fillcolor(turtle_color)
jack.shapesize(turtle_size)
jack.shape(turtle_shape)

#-----game functions--------
def turtle_clicked(x, y):
    jack.penup()
    change_position()
    jack.pendown()
    jack.showturtle()
    update_score()
def change_position():
    rand.randint(-400,400)
    new_xpos = rand.randint(-400,400)
    new_ypos = rand.randint(-400,400)
    jack.goto(new_xpos, new_ypos)
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

#-----events----------------
wn = trtl.Screen()
jack.onclick(turtle_clicked)
wn.mainloop()