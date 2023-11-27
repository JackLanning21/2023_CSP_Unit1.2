#Stage 1
x = ""
space = str("xxxxxx")
x = 5

def rightPyramid():
   for lines in range(6):
      global space
      space = space[0:-1]
      print(space)

rightPyramid()

spacer = str("xxxxxx")
for line in range(6):
   spacer = spacer[0:-5]
   print(spacer)














