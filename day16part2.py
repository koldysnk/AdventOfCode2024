import bisect
import numpy as np

grid = [list(line.strip()) for line in open("data/day16sampleB.txt","r").readlines()]

sX,sY = 0,0
eX,eY = 0,0
found = False
foundE = False

for y,row in enumerate(grid):
    for x, spot in enumerate(row):
        if spot == "S":
            sX,sY = x,y
            found = True
            continue
        if spot == "E":
            eX,eY = x,y
            foundE = True
            

    if found and foundE: break

q = []
#x,y,direction,path,score
q.append((sX,sY,2,"",0,0))
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

def validSpot(x,y):
    return x>=0 and y>=0 and x<len(grid[0]) and y<len(grid) and grid[y][x] != "#"
def displayPath(path):
    if type(path) is str:
        path = [tuple([int(pos) for pos in spot.replace('.','').split(",")]) for spot in path.split("..")]

    for y,row in enumerate(grid):
        for x, spot in enumerate(row):
            if (x,y) in path:
                print("O",end="")
            else:
                print(spot,end="")
        print()
    print()

best_path = set()
scores = []
best_score =  11048#99448
count=0
best_spots = {}

while len(q)>0:
    count+=1
    x,y,direction,path,score,prediction = q.pop()
    str_spot = f".{x},{y}."

    if str_spot in path or not validSpot(x,y) or prediction>best_score:
        continue

    #if str_spot in best_spots:
    #    if score>best_spots[str_spot]:
    #        continue
    #    else:
    #        best_spots[str_spot] = score
    #else:
    #    best_spots[str_spot] = score


    path += f"{str_spot}"
    #displayPath(path)
    #input()

    if grid[y][x] == "E":
        if len(scores)>0 and score>scores[-1]:
            print(score)
            break
        scores.append(score)
        print(score)
        for element in [tuple([int(pos) for pos in spot.replace('.','').split(",")]) for spot in path.split("..")]:
            best_path.add(element)

        continue

    score += 1
    
    #go up
    #if direction != DOWN:
    a=score+1000*(direction!=UP)
    b=score+1000*(direction!=RIGHT)
    c=score+1000*(direction!=DOWN)
    d=score+1000*(direction!=LEFT)

    e=a+abs(eX-x)+abs(eY-(y-1))
    f=b+abs(eX-(x+1))+abs(eY-y)
    g=c+abs(eX-x)+abs(eY-(y+1))
    h=d+abs(eX-(x-1))+abs(eY-y)

    #e+=(min(abs(eX-x),abs(eY-(y-1))))*1000
    #f+=(min(abs(eX-(x+1)),abs(eY-y)))*1000
    #g+=(min(abs(eX-x),eY-(y+1)))*1000
    #h+=(min(abs(eX-(x-1)),eY-y))*1000
    steps = [
        (x,y-1,UP,path,   a,e),
        (x+1,y,RIGHT,path,b,f),
        (x,y+1,DOWN,path, c,g),
        (x-1,y,LEFT,path, d,h)
    ]

    for step in steps:
        if (step[2]+2)%4 == direction:
            continue
        pred = step[-1]
        added=False
        i=0
        while i<len(q) and pred<q[i][-1]:
            i+=1
        q.insert(i,step)
        #for i in range(len(q)):
        #    compare = q[i]
        #    if pred<q[i][-1]:
        #        q.insert(i, step)
        #        added = True
        #        break
        #if not added:
        #    q.append(step)
        

displayPath(best_path)
    
print()
print(min(scores))
print(len(best_path))
print(count)
#9837 is too high


'''
steps = [
        (x,y-1,UP,path,score+1000*(direction!=UP)),
        (x+1,y,RIGHT,path,score+1000*(direction!=RIGHT)),
        (x,y+1,DOWN,path,score+1000*(direction!=DOWN)),
        (x-1,y,LEFT,path,score+1000*(direction!=LEFT)),
    ]

    for step in steps:
        q.append(step)
'''