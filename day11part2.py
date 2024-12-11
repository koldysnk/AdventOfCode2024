import time
def getDigits(stone):
    count = 0
    while stone!=0:
        stone//=10
        count+=1

    return count

data = [int(spot) for spot in open("data/day11.txt","r").read().strip().split()]


print(data)

start = time.time()
for _ in range(75):
    i = 0
    while i < len(data):
        stone = data[i]
        stone_digits = getDigits(stone)
        if stone == 0:
            data[i]=1
        elif stone_digits%2==0:
            data[i] = int(stone//10**(stone_digits/2))
            i+=1
            data.insert(i,int(stone%10**(stone_digits/2)))
        else:
            data[i] *= 2024

        i+=1
    print(_,":",len(data))

print(len(data))
end = time.time()
print(end-start)