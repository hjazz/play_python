for i in range(int(raw_input())):
    s = raw_input()
    s = s.replace("%20", " ")
    s = s.replace("%21", "!")
    s = s.replace("%24", "$")
    s = s.replace("%28", "(")
    s = s.replace("%29", ")")
    s = s.replace("%2a", "*")
    s = s.replace("%25", "%")
    print s 



