import time

data = [int(spot) for spot in open("data/day11.txt","r").read().strip().split()]


print(data)

start = time.time()
for _ in range(25):
    i = 0
    while i < len(data):
        stone = data[i]
        stone_list = list(str(stone))
        if stone == 0:
            data[i]=1
        elif len(stone_list)%2==0:
            data[i] = int(''.join(stone_list[:len(stone_list)//2]))
            i+=1
            data.insert(i,int(''.join(stone_list[len(stone_list)//2:])))
        else:
            data[i] *= 2024

        i+=1
    print(_,":",len(data))

print(len(data))

print(len(data))
end = time.time()
print(end-start)