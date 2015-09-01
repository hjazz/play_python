import sys
from sets import Set

rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
    resultX = Set()
    resultY = Set()
    for i in range(3):
        line = rl()
        point = line.split()
        x = point[0]
        y = point[1]
        if x in resultX:
            resultX.remove(x)
        else:
            resultX.add(x)
        if y in resultY:
            resultY.remove(y)
        else:
            resultY.add(y)

    print resultX.pop() + ' ' + resultY.pop()


     
