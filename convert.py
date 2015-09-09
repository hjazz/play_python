for i in range(int(raw_input())):
    n, unit = raw_input().split()
    n = float(n)
    if unit == "kg":
        print "%d %.4f %s" % (i + 1, n * 2.2046, "lb")
    elif unit == "l":
        print "%d %.4f %s" % (i + 1, n * 0.2642, "g")
    elif unit == "lb":
        print "%d %.4f %s" % (i + 1, n * 0.4536, "kg")
    elif unit == "g":
        print "%d %.4f %s" % (i + 1, n * 3.7854, "l")

