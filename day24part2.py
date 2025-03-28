import itertools
original_wires = {}
original_instructions = []
with open("data/day24.txt","r") as f:
    line = f.readline()
    prep = True
    while line:
        if line =="\n":
            prep = False
        elif prep:
            wire = line[:3]
            value = int(line[-2])
            original_wires[wire] = value
        else:
            original_instructions.append(tuple([part for i, part in enumerate(line.strip().split(" ")) if i!=3]))
        line = f.readline()

operations = {
    'AND': lambda x,y: x & y,
    'XOR': lambda x,y: x ^ y,
    'OR': lambda x,y: x | y,
    'ADD': lambda x,y: x+y
}

def solve(instructions, wires):
    runs = 0
    status = len(instructions)
    while len(instructions)>0:
        if runs%300==0 and runs>0:
            if len(instructions)==status:
                return wires
            else:
                status = len(instructions)
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
        runs+=1
    return wires

def build(wires,color):
    result = ''
    count = 0
    building = True
    while building:
        wire = color+format(count,'02')
        value = wires.get(wire,None)
        if value is not None:
            result = f"{value}{result}"
        else:
            building = False
        count+=1
    if result == '':
        result = '0'
    return result, int(result,2)


def generate_sequence(start:list=[0,1,1,2],end_limit:int=5):
    current = start.copy()
    yield current
    while True:
        limit = end_limit
        pointer = len(current)-1
        finding = True
        rolled = False
        while finding:
            if pointer<0:
                current = start.copy()
                rolled = False
                break
            val = current[pointer] + 1
            if val > limit:
                rolled = True
                pointer -= 1
                limit = end_limit - (len(current)-pointer)//2 if pointer%2==0 else end_limit
            else:
                current[pointer] = val
                finding = False
        while rolled and pointer<len(current)-1:
            pointer+=1
            limit = end_limit - (len(current)-pointer)//2 if pointer%2==0 else end_limit
            if pointer%2==1:
                current[pointer] = current[pointer-1]+1
            else:
                current[pointer] = current[pointer-2]+1

        yield current




x = build(original_wires,'x')
print('x', x)
y = build(original_wires,'y')
print('y', y)

print(f"x AND y -> {operations['AND'](x[1],y[1])}")
print(f"x ADD y -> {operations['ADD'](x[1],y[1])}")
target = operations['ADD'](x[1],y[1])
binary, answer = build(solve(original_instructions.copy(),original_wires.copy()),'z')

print('\nOriginal: z',(binary,answer))
print(f'Target: {target}\n')
sub_count = 4
tested = 0
skipped = 0
print(f"Tries: {tested}")
current = []
for x in range(sub_count):
    current.append(x)
    current.append(x+1)
start = current.copy()
looped = False
sequence = generate_sequence(current,len(original_instructions)-1)

#f = open("day24part2output.txt","w")
#while answer != target:
for current in itertools.permutations(range(len(original_instructions)),2*sub_count):
    print(f"Tested: {tested} \tSkipped: {skipped}",end="\r")
    #current = next(sequence)
    if current == start:
        if looped:
            break
        else:
            looped = True
    if len(current)!=len(set(current)):
        skipped+=1
        #print(f"Skipped {current} (duplicate pair) Pairs: {current}")
        continue
    outputs = [original_instructions[i][-1] for i in current]
    if len(outputs)!=len(set(outputs)):
        skipped += 1
        #print(f"Skipped {current} (duplicate output) Outputs: {outputs}")
        continue
    gates = []
    [gates.extend([original_instructions[i][0],original_instructions[i][2]]) for i in current]
    if len(gates) != len(set(gates)):
        skipped += 1
        #print(f"Skipped {current} (duplicate gate) Gates: {gates}")
        continue

    tested += 1
    current_instructions = original_instructions.copy()
    for i in range(sub_count):
        a_pos = current[i*2]
        b_pos = current[i*2+1]

        current_instructions[a_pos] = (
            original_instructions[a_pos][0],
            original_instructions[a_pos][1],
            original_instructions[a_pos][2],
            original_instructions[b_pos][3],
        )
        current_instructions[b_pos] = (
            original_instructions[b_pos][0],
            original_instructions[b_pos][1],
            original_instructions[b_pos][2],
            original_instructions[a_pos][3],
        )
    current_wires = original_wires.copy()
    current_wires = solve(current_instructions,current_wires)
    binary, answer = build(current_wires,"z")
    if answer == target:
        break

print(f"Tested: {tested} \tSkipped: {skipped}")
print(",".join(sorted(outputs)))
#5,193,025,824,568,982,400 permutations
#reached (0, 1, 2, 3, 4, 151, 202, 131)