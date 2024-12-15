#Find outer perimiter and keep track of edges
#check if object outside is an edge
#Try to count that too

data = [[item for item in row.strip()] for row in open("data/day12.txt","r").readlines()]
col_len = len(data)
row_len = len(data[0])

def isValid(x,y):
    return x>=0 and y>=0 and y<col_len and x<row_len

total = 0
visited = set()
for y, row in enumerate(data):
    for x, spot in enumerate(row):
        if (x,y) in visited:
            continue

        fence_count = 0
        crop_count = 0
        need_to_visit = [(x,y)]
        crop_type = data[y][x]

        while len(need_to_visit)>0:
            nX,nY = need_to_visit.pop()
            if (nX,nY) in visited:
                continue
            visited.add((nX,nY))

            fence_count+=4
            crop_count+=1
            #(0,-1),(-1,0),
            for dX,dY in [(0,-1),(-1,0),(0,1),(1,0)]:
                fX,fY = nX+dX,nY+dY
                if isValid(fX,fY) and data[fY][fX] == crop_type:
                    fence_count -= 1
                    need_to_visit.append((fX,fY))

        print(f"Fences: {fence_count} Crops: {crop_count}")
        total +=fence_count*crop_count





print(total)