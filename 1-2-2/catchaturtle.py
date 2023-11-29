# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import turtle as score_writer
import turtle as counter
import leaderboard as lb

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
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("Please enter your name")

#-----initialize turtle-----
jack = trtl.Turtle()
jack.speed(100)
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
    manage_leaderboard()

  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
def manage_leaderboard():

  global score
  global jack

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list)) < 5 or score >= (leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, jack, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, jack, score)

#-----events----------------
wn = trtl.Screen()
wn.bgcolor("Yellow")
jack.onclick(turtle_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()