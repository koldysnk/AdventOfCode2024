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

RIGHT = 0
UP = 1
DOWN = 
for y, row in enumerate(data):
    for x, spot in enumerate(row):
        if (x,y) in visited:
            continue

        fence_count = 0
        crop_count = 1
        next_plot = (x,y,RIGHT)
        exploring = True

        crop_type = data[y][x]

        while exploring:



        





print(total)