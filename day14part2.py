import math

def createOutput(x,y):
    output = []
    for _ in range(y):
        output.append([0]*x)

    return output

def displayOutput(output,i=-1,data=[],f=None):
    if i ==0:
        for robot in data:
            output[robot["p"][1]][robot["p"][0]] += 1
    for y, row in enumerate(output):
        for x, spot in enumerate(row):
            if f is None:
                print(spot,end="") if spot  else print(".",end="")
            else:
                f.write(f"{spot if spot else "."}")

        if f is None:
            print()
        else:
            f.write("\n")
    if i ==0:
        for robot in data:
            output[robot["p"][1]][robot["p"][0]] -= 1

def moveRobots(data,steps,output,xBound=101,yBound=103,dir=1):
    for robot in data:
        pX,pY = robot["p"]
        vX,vY = robot["v"]

        nX = (pX + vX*steps)%xBound
        nY = (pY + vY*steps)%yBound
        nP = (nX,nY)

        output[nY][nX] += dir

def stepThroughTime(data,xBound,yBound,output):
    i = -1

    while True:
        i+=1
        moveRobots(data,i,output,xBound,yBound)
        displayOutput(output,i)
        print(f"Seconds: {i}")
        moveRobots(data,i,output,xBound,yBound,dir=-1)
        
        if "k" in input(""):
            break

def stepThroughTimeFile(data,xBound,yBound,output):
    i = 0
    f= open("data/day14output.txt","w")
    while i<10000:
        i+=1
        moveRobots(data,i,output,xBound,yBound)
        displayOutput(output,i,f=f)
        f.write(f"Seconds: {i}\n")
        moveRobots(data,i,output,xBound,yBound,dir=-1)
        
        

        

        

def buildTree(xBound=101,yBound=103):
    data = createOutput(xBound,yBound)
    center = round(xBound/2)
    i=0
    while i<yBound:
        x = i//2
        if center-x>=0:
            data[i][center-x] +=1
        if center+x<xBound:
            data[i][center+x] +=1
        i+=1
    return data


def getData():
    data = []
    with open("data/day14.txt","r") as f:
        for line in f.readlines():
            line = line.strip().split()
            p = [int(num) for num in line[0].split("=")[1].split(",")]
            v = [int(num) for num in line[1].split("=")[1].split(",")]

            data.append({"p":p,"v":v})
    return data

data = getData()

#this is the wrong tree
tree = buildTree()
displayOutput(tree)


xBound = 101#11
yBound = 103#7
xMiddle = xBound//2
yMiddle = yBound//2

auto = True
output = createOutput(xBound,yBound)

if auto:
    stepThroughTimeFile(data,xBound,yBound,output)
else:
    stepThroughTime(data,xBound,yBound,output)
