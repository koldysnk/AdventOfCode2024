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
    registers.append("a")

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

    if not goal.startswith(",".join([str(item) for item in output])):
        return True

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
goal = ",".join([str(item) for item in instructions])


i = 1
while True:
    pointer=0
    registers[A] = i
    registers[B] = 0
    registers[C] = 0
    output = []
    while pointer<len(instructions)-1:
        opcode = instructions[pointer]
        operand = instructions[pointer+1]
        try:
            if operations[opcode](operand):
                break
        except:
            print("invalid")
            break
    
    if i%1000 == 0: print(f"Reviewed {i} programs")
    #print(f"Reviewed {i} ")

    if goal == ",".join([str(item) for item in output]):
        break
    else:
        i+=1
    

print()      
print(i)
print(f"Registers: {registers}")
print(output)
print(",".join([str(item) for item in output]))

#6945558000 too low