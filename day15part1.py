
grid = []
moves = []
x,y = 0,0

with open("data/day15.txt","r") as f:
    second = False
    line = f.readline()

    i=0
    while line:
        if second:
            moves.extend(list(line.strip()))
        elif line == "\n":
            second = True
        else:
            grid.append(list(line.strip()))
            if "@" in line:
                y=i
                x=line.find("@")

        i+=1
        line = f.readline()

def displayGrid(grid):
    for row in grid:
        for spot in row:
            print(spot,end="")
        print()

def moveDir(pos,dir):
    return [sum(x) for x in zip(pos,dir)]

def calculateResult(grid):
    total = 0
    for y, row in enumerate(grid):
        for x, spot in enumerate(row):
            if spot=="O":
                total += 100*y + x
    return total


dirMap = {
    "^":(0,-1),
    ">":(1,0),
    "v":(0,1),
    "<":(-1,0),
}
unDirMap = {
    "^":(0,1),
    ">":(-1,0),
    "v":(0,-1),
    "<":(1,0),
}


debug = False
if debug: displayGrid(grid)


for dir in moves:
    valid = False
    
    nX,nY = x,y
    pX,pY = nX,nY
    while grid[nY][nX] not in [".","#"]:
        nX,nY = moveDir((nX,nY),dirMap[dir])

    if grid[nY][nX] == "#":
        continue

    while (pX,pY) != (nX,nY):
        uX,uY = moveDir((nX,nY),unDirMap[dir])
        grid[nY][nX] = grid[uY][uX]
        nX, nY = uX,uY
    
    grid[nY][nX] = "."
    x,y = moveDir((nX,nY),dirMap[dir])

    if debug: displayGrid(grid)


result = calculateResult(grid)

print(result)