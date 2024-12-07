operators  = [lambda x,y:x*y, lambda x,y:x+y]
unoperators = [lambda x,y:x/y, lambda x,y:x-y]
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

    equations = [
        [operators[0]],
        [operators[1]]
    ]

    for i in range(len(numbers)-2):
        double = [[e for e in eq] for eq in equations]
        double.reverse()
        equations.extend(double)
        for j,equation in enumerate(equations):
            equation.append(operators[j%2])

    for equation in equations:
        total = numbers[0]
        for i, number in enumerate(numbers[1:]):
            total = equation[i](total,number)

        if total == goal:
            return True

    return False

total = 0
for line in data:
    sides = line.split(":")
    goal = int(sides[0])
    parts = [int(x) for x in sides[1].strip().split()]
    
    total += validEquation(goal,parts) * goal




print(total)