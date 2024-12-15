
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
            row = ""
            for j, spot in enumerate(line.strip()):
                if spot==".":
                    row+=".."
                elif spot=="#":
                    row+="##"
                elif spot=="O":
                    row+="[]"    
                elif spot=="@":
                    row+="@."
                    y=i
                    x=j*2
            grid.append(list(row))

        i+=1
        line = f.readline()

def displayGrid(grid):
    xP,yP=0,0
    for y,row in enumerate(grid):
        for x,spot in enumerate(row):
            print(spot,end="")
            if spot=="@":
                xP,yP=x,y
        print()
    print(xP,yP)

def moveDir(pos,dir):
    return [sum(x) for x in zip(pos,dir)]

def calculateResult(grid):
    total = 0
    for y, row in enumerate(grid):
        for x, spot in enumerate(row):
            if spot == "[":
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
    #logic for left and right remains the same
    if dir in "><":
        valid = False

        nX,nY = x,y
        pX,pY = nX,nY
        while grid[nY][nX] not in ".#":
            nX,nY = moveDir((nX,nY),dirMap[dir])

        if grid[nY][nX] == "#":
            continue

        while (pX,pY) != (nX,nY):
            uX,uY = moveDir((nX,nY),unDirMap[dir])
            grid[nY][nX] = grid[uY][uX]
            nX, nY = uX,uY

        grid[nY][nX] = "."
        x,y = moveDir((nX,nY),dirMap[dir])

    #logic for up and down is more complcated
    else:
        nX,nY = x,y
        pX,pY = nX,nY
        _,dY = dirMap[dir]

        valid = True
        movers = set()
        movers.add((nX,nY))
        scanners = [(nX,nY)]

        while len(scanners)>0:
            nX,nY = scanners.pop()
            oX,oY = moveDir((nX,nY),dirMap[dir])
            spot = grid[oY][oX]

            if spot == "#":
                valid = False
                break
            if spot == "[":
                movers.add((oX,oY))
                scanners.append((oX,oY))
                side = tuple(moveDir((oX,oY),dirMap[">"]))
                if side not in movers:
                    movers.add(side)
                    scanners.append(side)
            elif spot == "]":
                movers.add((oX,oY))
                scanners.append((oX,oY))
                side = tuple(moveDir((oX,oY),dirMap["<"]))
                if side not in movers:
                    movers.add(side)
                    scanners.append(side)
        
        if valid:
            movers = list(movers)
            movers.sort()
            if dir=="v":
                movers.reverse()

            for mover in movers:
                nX,nY = moveDir(mover,dirMap[dir])
                grid[nY][nX] = grid[mover[1]][mover[0]]
                grid[mover[1]][mover[0]] = "."

            x,y = moveDir((pX,pY),dirMap[dir])



        pass

    if debug: displayGrid(grid)


result = calculateResult(grid)

print(result)