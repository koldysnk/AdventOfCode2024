import time
def getDigits(stone):
    count = 0
    while stone!=0:
        stone//=10
        count+=1

    return count

def dataToString(data):
    return ', '.join([str(num) for num in data])

data = {int(spot):1 for spot in open("data/day11.txt","r").read().strip().split()}


print(data)

start = time.time()
for _ in range(75):
    new_data = {}
    for stone, count in data.items():
        stone_digits = getDigits(stone)
        if stone == 0:
            new_data[1] = new_data.get(1,0) + count
        elif stone_digits%2==0:
            new_stone_a = int(stone//10**(stone_digits/2))
            new_stone_b = int(stone%10**(stone_digits/2))
            new_data[new_stone_a] = new_data.get(new_stone_a,0) + count
            new_data[new_stone_b] = new_data.get(new_stone_b,0) + count
        else:
            new_stone = stone * 2024
            new_data[new_stone] = new_data.get(new_stone,0) + count

        #print(dataToString(data))
    data = new_data.copy()
    print(_,":",sum([value for key,value in data.items()]))
    pass

#print(len(data))
end = time.time()
print(end-start)