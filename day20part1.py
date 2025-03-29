import time
import json

original_grid = []
start = ()
end = ()
with open("data/day20.txt","r") as f:
    for y, line in enumerate(f.readlines()):
        original_grid.append(list(line.strip()))
        x = line.find('S')
        if x>0:
            start = (x,y)
        x = line.find('E')
        if x > 0:
            end = (x,y)

def printSeconds(diff):
    minutes = int(diff//60)
    seconds = diff%60
    return f"{f'{minutes} minutes and ' if minutes > 0 else ''}{seconds} seconds"

def solve(grid,timed = False,limit=10000):
    start_time = time.time()
    
    searching = True
    #steps, x, y, history
    queue = [(0,start[0],start[1],set())]
    while searching and len(queue)>0:
        steps, x, y, history = queue.pop(0)

        if grid[y][x]=='E':
            searching = False
            break
        
        steps += 1
        if steps >= limit:
            continue

        history.add((x,y))
        #UP, RIGHT, DOWN, LEFT
        for dir in [(-1,0),(0,1),(1,0),(0,-1)]:
            nX = x + dir[1]
            nY = y + dir[0]

            if grid[nY][nX] != "#" and (nX,nY) not in history:
                queue.append((steps,nX,nY,history.copy()))

    if searching:
        steps = -1
    end_time = time.time()
    
    if timed:
        return steps, (end_time-start_time)
    return steps

def buildGridList(grid:list):
    grid_list = []
    for y, row in enumerate(grid):
        for x, spot in enumerate(row):
            if spot == "#" and x!=0 and x!=len(row)-1 and y!=0 and y!=len(grid)-1:
                new_grid = grid.copy()
                new_grid[y] = ["." if i==x else j for i, j in enumerate(row)]
                grid_list.append(new_grid)
    return grid_list

baseline  = solve(original_grid,True)
print(f"Baseline {baseline} took {printSeconds(baseline[1])}")

grid_list = buildGridList(original_grid)

print(f"{len(grid_list)} iterations should take {printSeconds(baseline[1]*len(grid_list))}")

global_start = time.time()
total_count = 0
cheats = {}
for iteration, grid in enumerate(grid_list):
    steps = solve(grid,limit=baseline[0]-99)

    if iteration%100 == 0:
        global_current = time.time()
        diff = global_current - global_start
        print(f"Progress: {iteration}/{len(grid_list)} \tTime Taken: {printSeconds(diff)} \tEstimated Time Left: {printSeconds(diff*(len(grid_list)-iteration)/max(1,iteration))} \tEstimated Total Time: {printSeconds(diff*len(grid_list)/max(1,iteration))}",end=f"{'\n'if iteration%1000==0 else '\r'}")

    if steps==-1:
        continue
    savings = baseline[0]-steps
    count = cheats.get(savings,0) + 1
    cheats[savings] = count
    if savings >= 100:
        total_count += 1

print(f"Progress: {iteration}/{len(grid_list)} \tTime Taken: {printSeconds(diff)} \tEstimated Time Left: {printSeconds(diff*(len(grid_list)-iteration)/iteration)} \tEstimated Total Time: {printSeconds(diff*len(grid_list)/iteration)}")
print(json.dumps(cheats,indent=4))
print(f"Total valid savings: {total_count}")