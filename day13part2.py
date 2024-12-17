from sympy import symbols
from sympy.solvers.diophantine import diophantine

def getData():
    data=[]
    with open("data/day13.txt","r") as f:
        line = f.readline()
        i = 0
        while line:
            prize = {}
            if i%4==0:
                a = line.split(",")
                prize["aX"] = int(a[0].strip()[a[0].index("+")+1:])
                prize["aY"] = int(a[1].strip()[a[1].index("+"):])
                line = f.readline()
                b = line.split(",")
                prize["bX"] = int(b[0].strip()[b[0].index("+")+1:])
                prize["bY"] = int(b[1].strip()[b[1].index("+"):])
                line = f.readline()
                c = line.split(",")
                prize["xGoal"] = int(c[0].strip()[c[0].index("=")+1:])#+10000000000000
                prize["yGoal"] = int(c[1].strip()[c[1].index("="):])#+10000000000000

                data.append(prize)
                i+=3
                line = f.readline()
            else:
                line = f.readline()
                i+=1
    return data

data = getData()

            


a_cost = 3
b_cost = 1


total = 0

for prize in data:
    cost = 999999999999999999999999999999999999
    winnable = False
    aX = prize["aX"] 
    aY = prize["aY"]
    bX = prize["bX"] 
    bY = prize["bY"]
    xG = prize["xGoal"] 
    yG = prize["yGoal"]
    
    '''
    xG = a*aX + b*bX
    xG - b*bX = a*aX
    (xG - b*bX)/aX = a
    a = (xG - b*bX)/aX
    '''
    x, y = symbols('x y', integer=True)
    equation = x*aX + y*bX - xG
    solutions = diophantine(equation)
    print(solutions)
    
    total += cost*winnable

print(total)



'''
    for b in range(0,xG//bX+1):
        if b == 40:
            pass
        dX = b*bX
        diff = xG-dX
        aRem = diff%aX
        if aRem == 0:
            a = diff/aX
            if yG == a*aY + b*bY:
                cost = min(cost,a*a_cost+b*b_cost)
                winnable = True
    
    dividend = (change+xG)//xG
    sub_total += cost*(dividend)

    if not winnable:
        continue

    xG = (change+xG)%xG
    yG = (change+yG)%yG
    cost = 999999999999999999999999999999999999
    winnable = False

    for b in range(0,xG//bX+1):
        if b == 40:
            pass
        dX = b*bX
        diff = xG-dX
        aRem = diff%aX
        if aRem == 0:
            a = diff/aX
            if yG == a*aY + b*bY:
                cost = min(cost,a*a_cost+b*b_cost)
                winnable = True

    total += winnable*(cost+sub_total)'''