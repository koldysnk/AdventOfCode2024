UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4


def findGuard(data):
    for y, row in enumerate(data):
        for x, spot in enumerate(row):
            if spot == "^":
                return x,y,UP
            if spot == ">":
                return x,y,RIGHT
            if spot == "v":
                return x,y,DOWN
            if spot == "<":
                return x,y,LEFT

def move(data,cX,cY,direction):
    try:
        moved = False
        while not moved:
            if direction == UP:
                cY-=1
                if data[cY][cX] in ["#","O"]:
                    cY +=1
                    direction = RIGHT
                else:
                    moved = True
            elif direction == RIGHT:
                cX+=1
                if data[cY][cX] in ["#","O"]:
                    cX -=1
                    direction = DOWN
                else:
                    moved = True
            elif direction == DOWN:
                cY+=1
                if data[cY][cX] in ["#","O"]:
                    cY -=1
                    direction = LEFT
                else:
                    moved = True
            elif direction == LEFT:
                cX-=1
                if data[cY][cX] in ["#","O"]:
                    cX +=1
                    direction = UP
                else:
                    moved = True
    except:
        pass
    return cX,cY,direction

def findPath(data,start):
    cX, cY, direction = start
    history = set()
    other_history = set()

    while cX>=0 and cY >=0 and cY<len(data) and cX<len(data[cY]) and (cX,cY,direction) not in history:
        if (cX,cY) not in other_history:
            other_history.add((cX,cY))
        history.add((cX,cY,direction))

        cX,cY,direction = move(data,cX,cY,direction)
        
    return other_history

def display(data):
    print()
    for row in data:
        print(row)

def isInfinite(data,start):
    cX, cY, direction = start
    history = set()

    while cX>=0 and cY >=0 and cY<len(data) and cX<len(data[cY]):
        if (cX,cY,direction) in history:
            #display(data)
            return True

        history.add((cX,cY,direction))

        npos = move(data,cX,cY,direction)

        if npos == (cX,cY,direction):
            print("bad")
            return False
        cX,cY,direction = npos
        
    return False

def findLoops(data,start,path):
    total = 0
    for pos in path:
        if pos == (start[0],start[1]):
            continue

        temp = data[pos[1]][pos[0]]
        data[pos[1]][pos[0]] = "O"
        if temp != ".":
            print(temp)
        total += isInfinite(data,start)

        data[pos[1]][pos[0]] = temp
    return total


data = []

with open("data/day06.txt","r") as f:
    data = [list(line.strip()) for line in f.readlines()]

start = findGuard(data)
path = findPath(data,start)

total = findLoops(data,start,path)
print(total)

#1518 is incorrect and too high got after ~35 minutes
#62 is wrong
#1304 at 1.22 need to wait 3 minutes