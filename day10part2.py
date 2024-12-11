
def getScore(data,x,y,spot=0, visited:set = set()):
    if x<0 or y<0 or y>=len(data) or x>=len(data[y])  or (x,y) in visited or data[y][x]!=spot:
        return 0
    
    if spot == 9:
        return 1

    total = 0
    visited.add((x,y))

    total += getScore(data,x-1,y,spot+1,visited.copy())
    total += getScore(data,x,y-1,spot+1,visited.copy())
    total += getScore(data,x+1,y,spot+1,visited.copy())
    total += getScore(data,x,y+1,spot+1,visited.copy())

    return total



data = [[int(spot)for spot in row.strip()] for row in open("data/day10.txt","r").readlines()]

total = 0

for y, row in enumerate(data):
    for x, spot in enumerate(row):
        if spot == 0:
            score = getScore(data, x,y)
            print((x,y), score)
            total+=score

print(total)