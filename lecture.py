import sys
rl = lambda: sys.stdin.readline()
for i in range(int(rl())):
    string = rl()
    arr = []
    for i in range(len(string)/2):
        arr.append(string[(2*i):((2*i)+2)])

    arr.sort()
    print ''.join(arr)

