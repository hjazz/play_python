for i in range(int(raw_input())):
    w = int(raw_input())
    a = raw_input().split()
    t = 0
    for j in range(len(a)):
        t += int(a[j])
    if t <= w:
        print "YES"
    else:
        print "NO"

        
