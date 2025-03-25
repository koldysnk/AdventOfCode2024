wires = {}
instructions = []
z = [None]*46
with open("data/day24.txt","r") as f:
    line = f.readline()
    prep = True
    while line:
        if line =="\n":
            prep = False
        elif prep:
            wire = line[:3]
            value = int(line[-2])
            wires[wire] = value
        else:
            instructions.append(tuple([part for i, part in enumerate(line.strip().split(" ")) if i!=3]))
        line = f.readline()

operations = {
    'AND': lambda x,y: x and y,
    'XOR': lambda x,y: x ^ y,
    'OR': lambda x,y: x or y
}


while len(instructions)>0:
    instruction = instructions.pop(0)
    a, operation, b, dest = instruction
    valA = wires.get(a,None)
    valB = wires.get(b,None)
    if valA != None and valB != None:
        valD = wires.get(dest,None)
        if valD is None:
            wires[dest] = operations[operation](valA,valB)
    else:
        instructions.append(instruction)

result = ''
count = 0
building = True
while building:
    wire = 'z'+format(count,'02')
    value = wires.get(wire,None)
    if value is not None:
        result = f"{value}{result}"
    else:
        building = False
    count+=1

print(result)
print(int(result,2))