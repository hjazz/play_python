import sys
from sets import Set

rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
    points = []
    for i in range(3):
        line = rl()
        points.append(line.split())

    resultX = Set()
    resultY = Set()
    for point in points:
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


     
