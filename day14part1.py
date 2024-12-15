import math

def createOutput(x,y):
    output = []
    for _ in range(y):
        output.append([0]*x)

    return output

def displayOutput(output):
    for y, row in enumerate(output):
        for x, spot in enumerate(row):
            print(spot,end="") if spot  else print(".",end="")

        print()

data = []

with open("data/day14.txt","r") as f:
    for line in f.readlines():
        line = line.strip().split()
        p = (int(num) for num in line[0].split("=")[1].split(","))
        v = (int(num) for num in line[1].split("=")[1].split(","))

        data.append({"p":p,"v":v})

steps = 63*82*166
xBound = 101#11
yBound = 103#7
xMiddle = xBound//2
yMiddle = yBound//2

quads = [0,0,0,0]

debug = True
if debug: output = createOutput(xBound,yBound)

for robot in data:
    pX,pY = robot["p"]
    vX,vY = robot["v"]
    
    nX = (pX + vX*steps)%xBound
    nY = (pY + vY*steps)%yBound
    nP = (nX,nY)

    if debug: output[nY][nX] += 1

    if nX == xMiddle or nY == yMiddle:
        continue

    quadNum = 0

    quadNum += nX>xMiddle
    quadNum += (nY>yMiddle)*2

    quads[quadNum] += 1

if debug: displayOutput(output)

print(math.prod(quads))
