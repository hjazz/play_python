for i in range(int(raw_input())):
    line = raw_input()
    info = line.split()
    in_str = info[1]
    in_idx = int(info[0])
    print i+1, in_str[0:in_idx-1] + in_str[in_idx:]
    
