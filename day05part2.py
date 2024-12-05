
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

def reorder(row):
    new_row=[]

    for x in row:
        i = 0
        while i<len(new_row) and x in befores.get(new_row[i],set()):
            i+=1

        new_row.insert(i,x)


    return new_row

for row in updates:
    if not checkGood(row):
        row = reorder(row)
        update = row[len(row)//2]
        total+=update
        #print(update,total)

print(total)