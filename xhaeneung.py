map = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10}
result = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
for i in range(int(raw_input())):
    s = raw_input().split()
    n = 0
    if s[1] == '+':
        n = map[s[0]] + map[s[2]]
    elif s[1] == '-':
        n = map[s[0]] - map[s[2]]
    elif s[1] == '*':
        n = map[s[0]] * map[s[2]]

    if (n < 0) | (n > 10):
        print "No"
    elif ''.join(sorted(s[4])) == ''.join(sorted(result[n])):
        print "Yes"
    else:
        print "No"


