for i in range(int(raw_input())):
    s = raw_input()
    print s.replace("%20", " ").replace("%21", "!").replace("%24", "$").replace("%28", "(").replace("%29", ")").replace("%2a", "*").replace("%25", "%")
