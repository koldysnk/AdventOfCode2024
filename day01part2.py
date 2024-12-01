import math

data = ""
with open("data/day01.txt","r") as f:
    data = f.readlines()

a = []
b=[]
count = {}
for line in data:
    parts = line.split()
    num1 = int(parts[0])
    num2 = int(parts[1])
    a.append(num1)
    b.append(num2)

    if num1 not in count:
        count[num1] = 0

    if num2 in count:
        count[num2]+=1
    else:
        count[num2] = 1



total = 0
for num1 in a:
    total += count[num1]*num1

print(total)