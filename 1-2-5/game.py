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
IBlock = trtl.Turtle("I-Block.gif")
TBlock = trtl.Turtle("T-Block.gif")
ZBlock = trtl.Turtle("Z-Block.gif")
OBlock = trtl.Turtle("O-Block.gif")

#Create the on screen "Start Game" button

start.pencolor("Black")
start.write("Press SPACE to play", align='center', font=("Arial", 25, 'bold'))
start.hideturtle()

def change_background():
    wn.bgpic("tetris_mainUP2.gif")
    start.clear()

wn.onkeypress(change_background,"space")

Blocks = [IBlock, TBlock, ZBlock, OBlock]
index = rand.randint(0,len(Blocks)-1)
current_block = (Blocks[index])

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("tetris_backgroundUP.gif")
wn.mainloop()
