
def makeShort(drive):
    newDrive = []
    for row in drive:
        for x in row:
            newDrive.append(x)

    return newDrive

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
    drive.append([val for _ in range(num)])

print(f"Dots: {drive.count('.')}")
print(f"Numbers: {len(drive)-drive.count('.')}")
print(f"Total: {len(drive)}")


attempted = set()
i=len(drive)-1
while i>0:
    section = drive[i]
    if len(section)>0 and section[0] != '.' and section[0] not in attempted:
        attempted.add(section[0])
        for j, newSection in enumerate(drive[:i]):
            if len(newSection)>=len(section) and newSection[0] == '.':
                diff = len(newSection)-len(section)
                drive[j] = section.copy()
                drive[i] = ['.' for _ in range(len(section))]
                drive.insert(j+1,['.' for _ in range(diff)])
                i+=1
                #displayDrive(makeShort(drive))
                break
    i-=1            

drive = makeShort(drive)

print(f"Dots: {drive.count('.')}")
print(f"Numbers: {len(drive)-drive.count('.')}")
print(f"Total: {len(drive)}")

total = 0
for i,x in enumerate(drive):
    if x!='.':
        total += i*int(x)
print(total)

#4839040325682 is wrong