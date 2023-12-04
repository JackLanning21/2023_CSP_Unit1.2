csv ="FourKnights,KingsIndian,QueensGambit,TheColle,TheFrench,TheFriedLiver,TheFourKnights"

value =""
index = 0
myValues = []
#Do Part 1 of the challenge below here
for index in range(len(csv)):
    if index == len(csv):
        myValues.append(value)
    else:
        if(csv[index] != ","):
            value += csv[index]
        else:
            myValues.append(value)
            value = ""

#Do part 2 of the challenge below here
for index in range(len(myValues)):
    print(str(index) + " - " + myValues[index])
