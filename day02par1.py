import math

def testSafe(row, dir = 0):
    for i, x in enumerate(row[:-1]):
        y = row[i+1]

        diff = x - y

        absDiff = abs(diff)
        
        if absDiff < 1 or absDiff > 3:
            return False

        if dir == 0:
            dir = diff//absDiff
        elif dir != diff//absDiff:
            return False     

    return True

data = []
with open("data/day02.txt","r") as f:
    data = [[int(x) for x in line.strip().split(" ")] for line in f.readlines()]


total = 0

for row in data:
    total += testSafe(row)

print(total)