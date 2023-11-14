# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import turtle as score_writer
import turtle as counter

#-----game configuration----
turtle_color = "Blue"
turtle_size = 3
turtle_shape = "turtle"
score = 0
colors = ["Blue, Yellow, Red, Green, Gray, Black"]

score_writer.penup()
score_writer.goto(300, 300)
score_writer.pendown()
score_writer.hideturtle()

font_setup = ("Arial", 20, "normal")

counter = trtl.Turtle()
counter.penup()
counter.goto(-380, 300)
counter.pendown()
counter.hideturtle()

font_setup = ("Arial", 20, "normal")
timer = 3
counter_interval = 1000   #1000 represents 1 second
timer_up = False

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
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    if timer_up == True:
        jack.hideturtle()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)



#-----events----------------
wn = trtl.Screen()
wn.bgcolor("Yellow")
jack.onclick(turtle_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()