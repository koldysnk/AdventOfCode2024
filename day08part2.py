
def parseAntennas(data):
    antennas = {}

    for y, row in enumerate(data):
        for x, node in enumerate(row):
            if node.isalnum():
                spot = antennas.get(node,[])
                spot.append((x,y))
                antennas[node] = spot

    return antennas

data = [list(line.strip()) for line in open("data/day08.txt","r").readlines()]

antennas = parseAntennas(data)

antinodes = set()
for key,values in antennas.items():
    for i, node in enumerate(values[:-1]):
        for nodeb in values[i+1:]:
            dX = nodeb[0]-node[0]
            dY = nodeb[1]-node[1]

            x,y=(nodeb[0],nodeb[1])
            while x>=0 and x<len(data[0]) and y>=0 and y<len(data):
                antinodes.add((x,y))
                x,y=(x+dX,y+dY)

            x,y = (node[0],node[1])
            while x>=0 and x<len(data[0]) and y>=0 and y<len(data):
                antinodes.add((x,y))
                x,y=(x-dX,y-dY)


print(len(antinodes))