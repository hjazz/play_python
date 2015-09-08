for i in range(int(raw_input())):
    line = raw_input()
    n, s = line.split()
    n = int(n)
    print i+1, s[0:n-1] + s[n:]
    
