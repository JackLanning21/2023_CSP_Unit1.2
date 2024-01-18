import turtle as trtl
import random as rand

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape("I-Block.gif")
wn.addshape("O-Block.gif")
wn.addshape("T-Block.gif")
wn.addshape("Z-Block.gif")

start = trtl.Turtle()
drawer = trtl.Turtle()
drawer.speed(200)
drawer.hideturtle()
IBlock = trtl.Turtle("I-Block.gif")
TBlock = trtl.Turtle("T-Block.gif")
ZBlock = trtl.Turtle("Z-Block.gif")
OBlock = trtl.Turtle("O-Block.gif")
IBlock.hideturtle()
TBlock.hideturtle()
ZBlock.hideturtle()
OBlock.hideturtle()
start.hideturtle()
IBlock.goto(0,100)
TBlock.goto(0,100)
ZBlock.goto(0, 100)
OBlock.goto(0, 100)
IBlock.penup()
TBlock.penup()
ZBlock.penup()
OBlock.penup()

#Create the on screen "Start Game" button

start.pencolor("Black")
start.write("Press SPACE to play", align='center', font=("Arial", 25, 'bold'))
Blocks = [IBlock, TBlock, ZBlock, OBlock]
x = 0
y = 100
i = 1
def cb():
    global current_block, x, y, i, Blocks
    index = rand.randint(0, len(Blocks) - 1)
    current_block = (Blocks[index])
    current_block.showturtle()
    current_block.speed(2)

score = 0

def drop():
    global x, score
    current_block.goto(x, -400)
    if current_block == OBlock:
        if x >= -200 and x <= -90:
            score += 1
        current_block.hideturtle()
        cb()

    if current_block == IBlock:
        if x >= -90 and x <= 20:
            score += 1
        current_block.hideturtle()
        cb()

    if current_block == TBlock:
        if x >= 20 and x <= 130:
            score += 1
        current_block.hideturtle()
        cb()
    if current_block == ZBlock:
        if x >= 130 and x <= 250:
            score += 1
        current_block.hideturtle()
        cb()

def change_background():
    wn.bgpic("tetris_mainUP2.gif")
    start.clear()
    IBlock.hideturtle()
    TBlock.hideturtle()
    ZBlock.hideturtle()
    OBlock.hideturtle()
    drawer.showturtle()
    drawer.color("red")
    drawer.width(3)
    drawer.penup()
    drawer.goto(-200,-435)
    drawer.pendown()
    for lines in range(3):
        drawer.forward(110)
        drawer.left(90)
        drawer.forward(100)
        drawer.right(180)
        drawer.forward(100)
        drawer.left(90)
    drawer.forward(110)
    drawer.penup()
    drawer.goto(-200, -475)
    drawer.pendown()
    drawer.forward(55)
    drawer.begin_fill()
    drawer.fillcolor("Yellow")
    drawer.circle(20)
    drawer.end_fill()
    drawer.forward(55)
    drawer.forward(55)
    drawer.begin_fill()
    drawer.fillcolor("Aqua")
    drawer.circle(20)
    drawer.end_fill()
    drawer.forward(55)
    drawer.forward(55)
    drawer.begin_fill()
    drawer.fillcolor("Purple")
    drawer.circle(20)
    drawer.end_fill()
    drawer.forward(55)
    drawer.forward(55)
    drawer.begin_fill()
    drawer.fillcolor("Red")
    drawer.circle(20)
    drawer.end_fill()
    drawer.forward(55)
    cb()

wn.onkeypress(change_background,"space")




def move_left():
    global x
    x -= 10
    current_block.goto(x,y)

def move_right():
    global x
    x += 10
    current_block.goto(x,y)

wn.onkeypress(move_left,"a")
wn.onkeypress(move_right,"d")
wn.onkeypress(drop, "s")
wn.listen()
wn.mainloop()
