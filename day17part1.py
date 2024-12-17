def parseFile():
    registers = [0,1,2,3]
    instructions = []

    with open("data/day17.txt","r") as f:
        line = f.readline()
        found = False
        while line:
            if line == "\n":
                found = True

            elif found:
                instructions = [int(num) for num in line.strip().split()[1].split(",")]
            else:
                registers.append(int(line.strip().split()[2]))
            
            line = f.readline()
    registers.append(7)

    return registers, instructions

def adv(num):
    global pointer
    registers[A] = registers[A]//2**registers[num]
    pointer += 2
    
def bxl(num):
    global pointer
    registers[B] = registers[B] ^ num
    pointer += 2

def bst(num):
    global pointer
    registers[B] = registers[num]%8
    pointer += 2

def jnz(num):
    global pointer
    if registers[A] != 0:
        pointer = num
    else:
        pointer += 2

def bxc(num):
    global pointer
    registers[B] = registers[B] ^ registers[C]
    pointer += 2

def out(num):
    global pointer
    output.append(registers[num]%8)
    pointer += 2

def bdv(num):
    global pointer
    registers[B] = registers[A]//2**registers[num]
    pointer += 2

def cdv(num):
    global pointer
    registers[C] = registers[A]//2**registers[num]
    pointer += 2



operations = [adv,bxl,bst,jnz,bxc,out,bdv,cdv]
A,B,C = 4,5,6
registers, instructions = parseFile()
pointer = 0
output = []



while pointer<len(instructions)-1:
    opcode = instructions[pointer]
    operand = instructions[pointer+1]
    operations[opcode](operand)
    #print(pointer)

print(f"Registers: {registers}")
print(output)
print(",".join([str(item) for item in output]))

