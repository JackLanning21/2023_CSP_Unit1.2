#   a123_apple_1.py
import turtle as trtl
import random as rand
# -----setup-----
apple_image = "apple.gif"  # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
List = []
Letters = []
for i in range(5):
  apple2 = trtl.Turtle()
  List.append(apple2)
  Letters.append(rand.choice(alphabet))
# -----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(index):
  List[index].penup()
  List[index].shape(apple_image)
  wn.tracer(False)
  List[index].setx(rand.randint(-150, 150))
  List[index].sety(rand.randint(-40, 150))
  List[index].sety(List[index].ycor() - 37)
  List[index].color("white")
  List[index].write(Letters[index], align='center', font=("Arial", 30, "bold"))
  List[index].sety(List[index].ycor() + 37)
  List[index].showturtle()
  wn.tracer(True)
  wn.update()
def falling(index):
  List[index].penup()
  List[index].clear()
  List[index].goto(0, -150)
  List[index].hideturtle()
  draw_apple(index)

def checkA():
  for i in range(5):
    if Letters[i] == "a":
      falling(i)
def checkS():
  for i in range(5):
    if Letters[i] == "s":
      falling(i)
def checkD():
  for i in range(5):
    if Letters[i] == "d":
      falling(i)
def checkF():
  for i in range(5):
    if Letters[i] == "f":
      falling(i)
def checkG():
  for i in range(5):
    if Letters[i] == "g":
      falling(i)
def checkH():
  for i in range(5):
    if Letters[i] == "h":
      falling(i)
def checkJ():
  for i in range(5):
    if Letters[i] == "j":
      falling(i)
def checkK():
  for i in range(5):
    if Letters[i] == "k":
      falling(i)
def checkL():
  for i in range(5):
    if Letters[i] == "l":
      falling(i)

def checkQ():
  for i in range(5):
    if Letters[i] == "q":
      falling(i)

def checkW():
  for i in range(5):
    if Letters[i] == "w":
      falling(i)

def checkE():
  for i in range(5):
    if Letters[i] == "e":
      falling(i)

def checkR():
  for i in range(5):
    if Letters[i] == "r":
      falling(i)

def checkT():
  for i in range(5):
    if Letters[i] == "t":
      falling(i)

def checkY():
  for i in range(5):
    if Letters[i] == "y":
      falling(i)

def checkU():
  for i in range(5):
    if Letters[i] == "u":
      falling(i)

def checkI():
  for i in range(5):
    if Letters[i] == "i":
      falling(i)

def checkO():
  for i in range(5):
    if Letters[i] == "o":
      falling(i)

def checkP():
  for i in range(5):
    if Letters[i] == "p":
      falling(i)

def checkZ():
  for i in range(5):
    if Letters[i] == "z":
      falling(i)

def checkX():
  for i in range(5):
    if Letters[i] == "x":
      falling(i)

def checkC():
  for i in range(5):
    if Letters[i] == "c":
      falling(i)

def checkV():
  for i in range(5):
    if Letters[i] == "v":
      falling(i)

def checkB():
  for i in range(5):
    if Letters[i] == "b":
      falling(i)

def checkN():
  for i in range(5):
    if Letters[i] == "n":
      falling(i)

def checkM():
  for i in range(5):
    if Letters[i] == "m":
      falling(i)

# -----function calls-----
for i in range(5):
  draw_apple(i)
wn.onkeypress(checkA, "a")
wn.onkeypress(checkS, "s")
wn.onkeypress(checkD, "d")
wn.onkeypress(checkF, "f")
wn.onkeypress(checkG, "g")
wn.onkeypress(checkH, "h")
wn.onkeypress(checkJ, "j")
wn.onkeypress(checkK, "k")
wn.onkeypress(checkL, "l")
wn.onkeypress(checkQ, "q")
wn.onkeypress(checkW, "w")
wn.onkeypress(checkE, "e")
wn.onkeypress(checkR, "r")
wn.onkeypress(checkT, "t")
wn.onkeypress(checkY, "y")
wn.onkeypress(checkU, "u")
wn.onkeypress(checkI, "i")
wn.onkeypress(checkO, "o")
wn.onkeypress(checkP, "p")
wn.onkeypress(checkZ, "z")
wn.onkeypress(checkX, "x")
wn.onkeypress(checkC, "c")
wn.onkeypress(checkV, "v")
wn.onkeypress(checkB, "b")
wn.onkeypress(checkN, "n")
wn.onkeypress(checkM, "m")

wn.listen()
wn.bgpic("background.gif")
wn.mainloop()