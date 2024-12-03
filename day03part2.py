import math


data = []
with open("data/day03.txt","r") as f:
    data = f.read().split("do()")


total = 0

for line in data:
    if line.startswith("don't()"):
        continue
    lines = line.split("don't()")
    data2 = lines[0].split("mul(")

    for line2 in data2:
        sub = line2.split(",")
        try:
            x = int(sub[0])
            y = int(sub[1].split(")")[0])
            total += x*y
        except:
            pass


print(total)