import math


data = []
with open("data/day03.txt","r") as f:
    data = f.read().split("mul(")


total = 0

for line in data:
    sub = line.split(",")
    try:
        x = int(sub[0])
        y = int(sub[1].split(")")[0])
        total += x*y
    except:
        pass


print(total)