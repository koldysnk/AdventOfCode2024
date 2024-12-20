data = [(int(line.strip().split(",")[0]),int(line.strip().split(",")[1]))for line in open("data/day18.txt","r").readlines()]

data = data[:1024]

sX,sY = 0,0
eX,eY = 70,70
found = False
foundE = False


q = []
#x,y,direction,path,score
q.append((sX,sY,2,set(),0,0))
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

def validSpot(x,y):
    return x>=0 and y>=0 and x<=eX and y<=eY and (x,y) not in data

def displayPath(path):
    for y in range(eY+1):
        for x in range(eX+1):
            if (x,y) in path:
                print("O",end="")
            elif (x,y) in data:
                print("#",end="")
            else:
                print(".",end="")
        print()
    print()

scores = []
while len(q)>0:
    x,y,direction,path,score,prediction = q.pop(0)

    if (x,y) in path or not validSpot(x,y):
        continue

    path.add((x,y))
    #displayPath(path)

    if (x,y) == (eX,eY):
        scores.append(score)
        print(score)
        break

    score += 1
    
    

    e=score+abs(eX-x)+abs(eY-y+1)
    f=score+abs(eX-x-1)+abs(eY-y)
    g=score+abs(eX-x)+abs(eY-y-1)
    h=score+abs(eX-x+1)+abs(eY-y)
    steps = [
        (x,y-1,UP,path,   score,e),
        (x+1,y,RIGHT,path,score,f),
        (x,y+1,DOWN,path, score,g),
        (x-1,y,LEFT,path, score,h)
    ]

    for step in steps:
        pred = step[-1]
        added=False
        for i in range(len(q)):
            compare = q[i]
            if pred<q[i][-1]:
                q.insert(i, step)
                added = True
                break
        if not added:
            q.append(step)
        

    
print()
print(min(scores))