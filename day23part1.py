with open("data/day23.txt","r")as f:
    connections = set([tuple(line.strip().split("-")) for line in f.readlines()])
    chief_connections = set([(a,b) for a,b in connections if a.startswith("t") or b.startswith("t")])

chiefs = dict()
for a,b in chief_connections:
    a_list = chiefs.get(a,set())
    b_list = chiefs.get(b,set())

    a_list.add(b)
    b_list.add(a)

    chiefs[a] = a_list
    chiefs[b] = b_list

for key in chiefs.keys():
    chiefs[key] = list(chiefs[key])

winners = set()
for chief, cons in chiefs.items():
    for i in range(len(cons)-1):
        a = cons[i]
        for j in range(i+1,len(cons)):
            b = cons[j]
            if (a,b) in connections or (b,a) in connections:
                winners.add(",".join(sorted([chief,a,b])))
print(winners)
print(len(winners))