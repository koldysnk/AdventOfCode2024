import numpy as np

data = np.array([int(line) for line in open("data/day22.txt","r").readlines()])

for i in range(2000):
    data = data*64 ^ data
    data = data%16777216
    data = data//32 ^ data
    data = data%16777216
    data = data*2048 ^ data
    data = data%16777216
print(sum(data))
print()

count = float(0)
for num in data:
    count+=float(num)
print(count)

#1737647416 is too low