
data = [list(line.strip()) for line in open("data/day04.txt","r").readlines()]


total = 0

for y , row in enumerate(data):
    for x, spot in enumerate(row):
        if spot != "X":
            continue

        #Going right
        if x+3<len(data[y]) and data[y][x+1] == "M" and data[y][x+2] == "A" and data[y][x+3] == "S":
            total+=1
        #Going left
        if x-3>=0 and data[y][x-1] == "M" and data[y][x-2] == "A" and data[y][x-3] == "S":
            total+=1

        #Going Down
        if y+3<len(data) and data[y+1][x] == "M" and data[y+2][x] == "A" and data[y+3][x] == "S":
            total+=1

        #Going Up
        if y-3>=0 and data[y-1][x] == "M" and data[y-2][x] == "A" and data[y-3][x] == "S":
            total+=1

        #Going Up Right
        if y-3>=0 and x+3<len(data[y]) and data[y-1][x+1] == "M" and data[y-2][x+2] == "A" and data[y-3][x+3] == "S":
            total+=1

        #Going down Right
        if y+3<len(data) and x+3<len(data[y]) and data[y+1][x+1] == "M" and data[y+2][x+2] == "A" and data[y+3][x+3] == "S":
            total+=1

        #Going down left
        if y+3<len(data) and x-3>=0 and data[y+1][x-1] == "M" and data[y+2][x-2] == "A" and data[y+3][x-3] == "S":
            total+=1

        #Going up left
        if y-3>=0 and x-3>=0 and data[y-1][x-1] == "M" and data[y-2][x-2] == "A" and data[y-3][x-3] == "S":
            total+=1

        print(total,x,y)

print(total)