import itertools

def multiply(x,y):
    return x*y
def add(x,y):
    return x+y
def shift(x,y):
    return x*(10**len(list(str(y))))+y

operators  = [multiply, add, shift]
unoperators = [lambda x,y:x/y, lambda x,y:x-y, lambda x,y: (x-y)/(10**len(list(str(y))))]
data = []

with open("data/day07.txt","r") as f:
    data = f.readlines()


def validEquation(goal,numbers):
    '''
    total = numbers[0]
    for i, num in enumerate(numbers[1:]):
        for operator, unoperator in zip(operators,unoperators):
            total = operator(total,num)
            if i == len(numbers)-2 and total == goal:
                return True
        total = unoperator(total,num)
    '''
    if len(numbers) == 1:
        return goal == numbers[0]
    '''
    equations = [
        [operators[0]],
        [operators[1]],
        [operators[2]]
    ]

    for i in range(len(numbers)-2):
        double = [[e for e in eq] for eq in equations]
        triple = [[e for e in eq] for eq in equations]
        equations.extend(double)
        equations.extend(triple)
        for j,equation in enumerate(equations):
            equation.append(operators[((j)%3+j//3)%3])
    '''

    equations = list(itertools.product(operators,repeat=len(numbers)-1))

    if goal == 7290:
        pass
    for equation in equations:
        total = numbers[0]
        for i, number in enumerate(numbers[1:]):
            total = equation[i](total,number)
            if i==0 and total==48:
                pass

        if total == goal:
            print(f"{goal} is good")
            return True

    print(f"{goal} is bad")
    return False

total = 0
for line in data:
    sides = line.split(":")
    goal = int(sides[0])
    parts = [int(x) for x in sides[1].strip().split()]
    
    total += validEquation(goal,parts) * goal




print(total)

#646977953496 is wrong