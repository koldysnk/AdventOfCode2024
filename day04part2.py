
data = [list(line.strip()) for line in open("data/day04.txt","r").readlines()]


total = 0

for y , row in enumerate(data):
    for x, spot in enumerate(row):
        if spot != "A" or not (x>0 and x+1<len(row) and y>0 and y+1<len(data)):
            continue

        topleft = data[y-1][x-1]
        topright = data[y-1][x+1]
        bottomleft = data[y+1][x-1]
        bottomright = data[y+1][x+1]

        if ((topleft=="M" and bottomright=="S")or(topleft=="S" and bottomright=="M")) and ((bottomleft=="M" and topright=="S")or(bottomleft=="S" and topright=="M")):
            total+=1
            print(total,x,y)
print(total)