
afters = {}
befores = {}
updates = []

with open("data/day05.txt","r") as f:
    passed = False
    for line in f.readlines():
        if line.strip() == "":
            passed = True
            continue

        if not passed:
            data = [int(x) for x in line.strip().split("|")]
            x,y = data[0],data[1]

            a = afters.get(x,set())
            a.add(y)
            afters[x]=a

            b = befores.get(y,set())
            b.add(x)
            befores[y]=b

        else:
            updates.append([int(x) for x in line.strip().split(",")])



total = 0

def checkGood(row):
    pre = set()
    post = set()
    for x in row:
        if len(pre.intersection(afters.get(x,set())))>0:
            return False
        pre.add(x)
    return True
        

for row in updates:
    if checkGood(row):
        update = row[len(row)//2]
        total+=update
        print(update,total)

print(total)