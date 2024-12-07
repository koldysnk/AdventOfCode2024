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
        if direction == UP:
            cY-=1
            if data[cY][cX] == "#":
                cY +=1
                cX +=1
                direction = RIGHT
        elif direction == RIGHT:
            cX+=1
            if data[cY][cX] == "#":
                cY +=1
                cX -=1
                direction = DOWN
        elif direction == DOWN:
            cY+=1
            if data[cY][cX] == "#":
                cY -=1
                cX -=1
                direction = LEFT
        elif direction == LEFT:
            cX-=1
            if data[cY][cX] == "#":
                cY -=1
                cX +=1
                direction = UP
    except:
        pass
    return cX,cY,direction

def findPath(data):
    total =0
    cX, cY, direction = findGuard(data)
    history = set()
    other_history = set()

    while cX>=0 and cY >=0 and cY<len(data) and cX<len(data[cY]) and (cX,cY,direction) not in history:
        if (cX,cY) not in other_history:
            total+=1
            other_history.add((cX,cY))
        history.add((cX,cY,direction))

        cX,cY,direction = move(data,cX,cY,direction)
        
    return total

data = []

with open("data/day06.txt","r") as f:
    data = [list(line.strip()) for line in f.readlines()]

total = findPath(data)
print(total)