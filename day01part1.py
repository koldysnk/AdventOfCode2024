import math

data = ""
with open("data/day01.txt","r") as f:
    data = f.readlines()

a = []
b=[]
for line in data:
    parts = line.split()
    a.append(int(parts[0]))
    b.append(int(parts[1]))

a.sort()
b.sort()

total = 0
for i, num1 in enumerate(a):
    total += abs(num1-b[i])

print(total)