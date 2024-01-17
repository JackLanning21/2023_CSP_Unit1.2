import turtle as trtl
import random as rand

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape("I-Block.gif")
wn.addshape("O-Block.gif")
wn.addshape("T-Block.gif")
wn.addshape("Z-Block.gif")

start = trtl.Turtle()
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

x = 0
y = 100
i = 1
def cb():
    global current_block, x, y, i
    current_block.showturtle()
    current_block.speed(2)

def drop():
    current_block.goto(0, -400)


def change_background():
    wn.bgpic("tetris_mainUP2.gif")
    start.clear()
    IBlock.hideturtle()
    TBlock.hideturtle()
    ZBlock.hideturtle()
    OBlock.hideturtle()
    cb()


wn.onkeypress(change_background,"space")


Blocks = [IBlock, TBlock, ZBlock, OBlock]
index = rand.randint(0,len(Blocks)-1)
current_block = (Blocks[index])

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

wn.listen()
wn.mainloop()
