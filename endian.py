import sys

def conv(val):
    hexVal = int(val)
    converted = (hexVal & 0xff000000) >> 24
    converted += ((hexVal & 0x00ff0000) >> 16) << 8
    converted += ((hexVal & 0x0000ff00) >> 8) << 16
    converted += (hexVal & 0x000000ff) << 24

    return int(converted)

n = sys.stdin.readline()
for i in range(int(n)):
    val = sys.stdin.readline()
    print conv(val)

