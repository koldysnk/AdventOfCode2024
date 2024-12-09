
def displayDrive(drive):
    if len(drive)>200:
        with open("data/day09out.txt",'a') as f:
            f.write("\n")
            line = ''
            for x in drive:
                line += x
            f.write(line)
    else:
        for x in drive:
            print(x,end="")
        print()

data = [int(num) for num in list(open("data/day09.txt",'r').read().strip())]

drive = []

for i, num in enumerate(data):
    val = '.' if i%2==1 else str(i//2)
    for _ in range(num):
        drive.append(val)

print(f"Dots: {drive.count('.')}")
print(f"Numbers: {len(drive)-drive.count('.')}")
print(f"Total: {len(drive)}")


#displayDrive(drive)
for i,val in enumerate(drive):
    if val == '.':
        newVal = drive.pop()
        while len(drive)-1>i and newVal == '.':
            newVal = drive.pop()
        drive[i] = newVal
        #displayDrive(drive)

print(f"Dots: {drive.count('.')}")
print(f"Numbers: {len(drive)-drive.count('.')}")
print(f"Total: {len(drive)}")

total = 0
for i,x in enumerate(drive):
    if x!='.':
        total += i*int(x)
    else:
        print(x)
print(total)

#4839040325682 is wrong